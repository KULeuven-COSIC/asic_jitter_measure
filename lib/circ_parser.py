"""Parse the netlist files."""
from typing import Dict, List, Optional, Any, Union, Tuple
import argparse
import json
from os.path import join
from functools import reduce
from PySpice.Spice import Parser # type: ignore

TREE_TYPE = Dict[str, Tuple[int, 'TREE_TYPE']]

TOP_MODULE = 'top_level'

class CircParser:
    """A Spice circuit parser."""

    _HW_FOLDER = 'hardware'
    _MAP_FILE = join('lib', 'params', 'model_name_map.json')
    _MAX_LINE_LEN = 100

    def __init__(self, module_name: str, hw_folder: Optional[str]=None,
                 model_map: Optional[str]=None,
                 verbose: bool=False):
        self._module_name = module_name
        if hw_folder is None:
            self._hw_folder = self._HW_FOLDER
        else:
            self._hw_folder = hw_folder
        self._model_map: Dict[str, Dict[str, str]] = {}
        model_map_file = model_map
        if model_map_file is None:
            model_map_file = self._MAP_FILE
        with open (model_map_file, 'r', encoding='utf-8') as map_file:
            self._model_map = json.load(map_file)
        self._sub_circuits: Optional[List[Parser.SubCircuit]] = None
        self._verbose = verbose

    def parse(self) -> None:
        """Parse the circuit."""
        c_parser = Parser.SpiceParser(self._rcir_file)
        c_parser.build_circuit()
        self._sub_circuits = c_parser.subcircuits

    def write(self) -> None:
        """Write the parsed circuit to the target circuit file."""
        if not self._sub_circuits:
            self._print('First parse the circuit.')
            return
        with open(self._cir_file, 'w', encoding='utf-8') as cir_file:
            cir_file.write(f'* Top cell name: {self._module_name}\n')
            for sub_circ in self._sub_circuits:
                cir_file.write('\n')
                cir_file.write(self._get_circ_lines(sub_circ))

    def append_readme(self) -> None:
        """Append the cell hierarchy and netlist to the readme file."""
        if not self._sub_circuits:
            self._print('First parse the circuit.')
            return
        cells_flat = self._extract_cells_flat()
        if self._module_name not in cells_flat:
            self._print(f'Could not find top cell: {self._module_name}')
            return
        tree = CircParser._get_node_tree(self._module_name, cells_flat)
        with open(self._md_file, 'a', encoding='utf-8') as md_file:
            md_file.write(CircParser._cell_hierarchy_txt(tree, self._module_name))
            md_file.write('\n')
            md_file.write(self._cell_netlist_txt())

    @staticmethod
    def append_hierarchy(module: str=TOP_MODULE) -> None:
        """Append the hierarchy to the readme."""
        circ_parser = CircParser(m_name)
        circ_parser.parse()
        cells_flat = circ_parser._extract_cells_flat()
        tree = circ_parser._get_node_tree(module, cells_flat)
        mos_pairs = CircParser._get_primitive_cnt(tree, 'n_mos')
        # mos_pairs = CircParser._get_primitives(tree)['n_mos']
        hier_txt = CircParser._get_hierarchy_tree(tree, module, mos_pairs, -1)
        with open(join(circ_parser._HW_FOLDER, 'readme.md'), 'a', encoding='utf-8') as md_file:
            md_file.write('## ASIC Hierarchy\n\n')
            md_file.write('The following hierarchy is used in the ASIC '
                          '(each cell can be expanded to show its components):\n\n')
            md_file.write(hier_txt)
            md_file.write('\n')

    @staticmethod
    def _get_hierarchy_tree(tree: TREE_TYPE, cell_name: str, mos_pairs: int, nb_repeats: int) -> str:
        """Get the hierarchy for the given tree."""
        repeat_str = f'x{nb_repeats}' if nb_repeats > 1 else ''
        if not tree:
            return f'<li><code>{cell_name}</code> <b>{mos_pairs:d}</b> <i>{repeat_str}</i></li>\n'
        result = f'<details>\n<summary><code>{cell_name}</code> <b>{mos_pairs:d}</b> <i>{repeat_str}</i></summary>\n<blockquote>\n'
        has_child_leafs = False
        for child, (nb_child, child_tree) in tree.items():
            if not child_tree:
                has_child_leafs = True
                continue
            mos_pairs = CircParser._get_primitive_cnt(child_tree, 'n_mos')
            result += CircParser._get_hierarchy_tree(child_tree, child, mos_pairs, nb_child)
        if has_child_leafs:
            result += '<ul>\n'
            for child, (nb_child, child_tree) in tree.items():
                if child_tree:
                    continue
                mos_pairs = CircParser._get_primitive_cnt(child_tree, 'n_mos')
                result += CircParser._get_hierarchy_tree(child_tree, child, mos_pairs, nb_child)
            result += '</ul>\n'
        result += '</blockquote>\n</details>\n'
        return result

    def _get_circ_lines(self, circ: Parser.SubCircuit) -> str:
        """Get the line for the given circuit."""
        result = ''
        name = self._get_module_name(circ.name)
        result += f'.SUBCKT {name}'
        start_nodes = len(result) + 1
        for node in circ.nodes:
            result = CircParser._add_to_line(result, f' {node.lower()}',
                                             self._MAX_LINE_LEN, start_nodes)
        result += '\n'
        for sub_circ in circ:
            if not isinstance(sub_circ, Parser.Element):
                continue
            result += self._get_sub_circ_line(sub_circ)
        result += '.ENDS\n'
        return result

    def _get_sub_circ_line(self, circ: Parser.Element) -> str:
        """Get the line for the given sub sicruit."""
        result = ''
        name = self._get_circ_name(circ)
        result += f'    {circ._prefix}{circ.name.lower()}' # pylint: disable=protected-access
        start_nodes = len(result) + 1
        nodes: List[str] = [n for n in circ._nodes if n != '/'] # pylint: disable=protected-access
        for node in nodes:
            result = CircParser._add_to_line(result, f' {node.lower()}',
                                             self._MAX_LINE_LEN, start_nodes)
        result = CircParser._add_to_line(result, f' {name}',
                                         self._MAX_LINE_LEN, start_nodes)
        for k, v in circ._dict_parameters.items(): # pylint: disable=protected-access
            if k == 'model':
                continue
            result = CircParser._add_to_line(result, f' {k}={v}',
                                             self._MAX_LINE_LEN, start_nodes)
        result += '\n'
        return result

    def _cell_netlist_txt(self) -> str:
        """Generate the cell netlist for the readme."""
        result = '## Netlist\n\n'
        if not self._sub_circuits:
            self._print('First parse the circuit.')
            return result + 'No netlist found.\n'
        for sub_circ in self._sub_circuits:
            circ_name = self._get_module_name(sub_circ.name)
            if circ_name == self._module_name:
                result += '```\n'
                result += self._get_circ_lines(sub_circ)
                result += '```\n'
                return result
        return result + 'No netlist found.\n'
    
    @staticmethod
    def _get_primitive_cnt(tree: TREE_TYPE, prim_name: str) -> int:
        """Get the number of primitive in the given tree."""
        primitives = CircParser._get_primitives(tree)
        if prim_name not in primitives:
            return 0
        return primitives[prim_name]

    @staticmethod
    def _cell_hierarchy_txt(tree: TREE_TYPE, module: str) -> str:
        """Generate the cell hierarchy for the readme."""
        nb_top_pairs = CircParser._get_primitive_cnt(tree, 'n_mos')
        result = ('## Cell Hierarchy\n\n'
                  f'`{module}` **{nb_top_pairs:d}** (number MOS pairs)\n')
        for child, (nb_child, child_tree) in tree.items():
            nb_child_pairs = CircParser._get_primitive_cnt(child_tree, 'n_mos')
            nb_str = f' *x{nb_child:d}*' if nb_child > 1 else ''
            result += (f'- `{child}` **{nb_child_pairs:d}**{nb_str}\n')
        return result

    @staticmethod
    def _get_primitives(tree: TREE_TYPE) -> Dict[str, int]:
        """Get the primitves in the given tree."""
        result: Dict[str, int] = {}
        for child, (nb_child, child_tree) in tree.items():
            if not child_tree:
                if child in result:
                    result[child] += nb_child
                else:
                    result[child] = nb_child
            else:
                result_child = CircParser._get_primitives(child_tree)
                for r_child, r_nb in result_child.items():
                    if r_child in result:
                        result[r_child] += nb_child * r_nb
                    else:
                        result[r_child] = nb_child * r_nb
        return result

    def _extract_cells_flat(self) -> Dict[str, List[str]]:
        """Extract the raw cells."""
        cells_flat: Dict[str, List[str]] = {}
        if not self._sub_circuits:
            return cells_flat
        for sub_circ in self._sub_circuits:
            circ_name = self._get_module_name(sub_circ.name)
            children: List[str] = []
            for sub_sub_circ in sub_circ:
                if not isinstance(sub_sub_circ, Parser.Element):
                    continue
                name = self._get_circ_name(sub_sub_circ)
                children.append(name)
            cells_flat[circ_name] = children
        return cells_flat

    @staticmethod
    def _get_node_tree(node_name: str, cells_flat: Dict[str, List[str]]) -> TREE_TYPE:
        """Get the given node tree recursively."""
        result: TREE_TYPE = {}
        if node_name not in cells_flat:
            return result
        children = cells_flat[node_name]
        for child in children:
            if child in result:
                result[child] = (result[child][0] + 1, result[child][1])
            else:
                child_tree = CircParser._get_node_tree(child, cells_flat)
                result[child] = (1, child_tree)
        return result
    
    @staticmethod
    def _add_to_line(line: str, add_str: str,
                     max_len: int, start: int=0) -> str:
        """Add to the given line, without exceeding the line length."""
        result = '' + line
        last_line = len(line.split('\n')[-1])
        if last_line + len(add_str) > max_len:
            result += '\n' + ' ' * start + '+'
        return result + add_str

    @property
    def _module_folder(self) -> str:
        """The module source folder."""
        return join(self._hw_folder, self._module_name)

    @property
    def _cir_file(self) -> str:
        """The target CIR file."""
        return join(self._module_folder, f'{self._module_name}.cir')

    @property
    def _rcir_file(self) -> str:
        """The source CIR file."""
        return join(self._module_folder, f'{self._module_name}.rcir')

    @property
    def _md_file(self) -> str:
        """The readme file."""
        return join(self._module_folder, 'readme.md')

    def _get_module_name(self, name: str) -> str:
        """Convert the module name."""
        name = name.lower()
        if name in self._model_map['modules']:
            name = self._model_map['modules'][name]
        return name

    def _get_model_name(self, name: str) -> str:
        """Convert the model name."""
        name = name.lower()
        if name in self._model_map['models']:
            name = self._model_map['models'][name]
        return name

    def _get_circ_name(self, sub_sub_circ: Parser.Element) -> str:
        if sub_sub_circ._parameters: # pylint: disable=protected-access
            name = sub_sub_circ._parameters[0] # pylint: disable=protected-access
            name = self._get_module_name(name)
        else:
            name = sub_sub_circ._dict_parameters['model'] # pylint: disable=protected-access
            name = self._get_model_name(name)
        return name

    def _print(self, txt: str) -> None:
        """Print the given text."""
        if self._verbose:
            print(txt)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', help='Enable verbose output', action='store_true')
    parser.add_argument('-a', help='Append to readme', action='store_true')
    parser.add_argument('-t', help='Append to hierarchy to top readme', action='store_true')
    parser.add_argument('-c', help='Generate CIR netlist', action='store_true')
    parser.add_argument('-m', help='Hardware module name')
    args = parser.parse_args()

    if not args.m:
        m_name = TOP_MODULE # pylint: disable=invalid-name
        print(f'No module chosen, selected top module: {TOP_MODULE}')
    else:
        m_name = args.m

    circ_parser = CircParser(m_name)
    circ_parser.parse()
    if args.c:
        circ_parser.write()
    if args.a:
        circ_parser.append_readme()
    if args.t:
        CircParser.append_hierarchy()
