"""Merge generated SVG layer files."""
from typing import Dict, List, Tuple, Optional, Any, Callable
import argparse
import sys
import json
from os import listdir, remove, getcwd
from os.path import isfile, join, isdir
import copy
import xml.etree.ElementTree as et
import numpy as np
import gdspy # type: ignore
from shapely.geometry import Polygon # type: ignore
from shapely import transform # type: ignore
sys.path.append(getcwd())
from lib import time_logger as t_l # pylint: disable=wrong-import-position

TOP_MODULE = 'core_top'

class GdsToSvg:
    """This class converts GDS files to SVG."""

    _SVG_NS = 'http://www.w3.org/2000/svg'
    _SVG_LINK = 'http://www.w3.org/1999/xlink'
    _HW_FOLDER = 'hardware'
    _LAYER_DATA_FILE = join('lib', 'params', 'gds_to_svg_layers.json')

    def __init__(self, module_name: str, hw_folder: Optional[str]=None,
                 layer_data: Optional[str]=None, background_col: str='#ffffff',
                 padding: int=5,
                 verbose: bool=False, time_log: bool=False,
                 intermediate_write: bool=False) -> None:
        self._module_name = module_name
        if hw_folder is None:
            self._hw_folder = self._HW_FOLDER
        else:
            self._hw_folder = hw_folder
        self._layer_data = {}
        layer_data_file = layer_data
        if layer_data_file is None:
            layer_data_file = self._LAYER_DATA_FILE
        with open (layer_data_file, 'r', encoding='utf-8') as layer_file:
            self._layer_data = json.load(layer_file)
        self._background_col = background_col
        self._padding = padding
        self._verbose = verbose
        self._time_log = time_log
        if self._time_log:
            self._logger = t_l.TimeLogger(0)
        self._intermediate_write = intermediate_write
        self._merged_svg: Optional[et.Element] = None

    def merge(self, output_name: Optional[str]=None,
              keep_temp_svg: bool=False) -> None:
        """Merge the input SVGs."""
        if not isdir(self._module_folder):
            self._print(f'Module {self._module_name} does not exist.')
            return
        if output_name is None:
            output_name = self._module_name + '.svg'
        self._gen_svg_layers()
        svg_files, layer_names = self._find_svgs()
        parsed_svgs = self._parse_svgs(svg_files)
        viewbox = self._get_viewbox(parsed_svgs)
        self._merged_svg = self._init_merged_svg(viewbox)
        defs = self._init_defs(parsed_svgs)
        self._merged_svg.append(defs)
        module_group = self._construct_svg(parsed_svgs, layer_names)
        self._merged_svg.append(module_group)
        if not keep_temp_svg:
            self._clean_svg()
        et.ElementTree(element=self._merged_svg).write(self._svg_file, encoding='utf-8')

    @property
    def _module_folder(self) -> str:
        """The module source folder."""
        return join(self._hw_folder, self._module_name)

    @property
    def _gds_file(self) -> str:
        """The source GDS file."""
        return join(self._module_folder, f'{self._module_name}.gds')

    @property
    def _svg_file(self) -> str:
        """The target SVG file."""
        return join(self._module_folder, f'{self._module_name}.svg')

    @property
    def _temp_svg_file(self) -> str:
        """Temporary SVG output file."""
        return join(self._module_folder, f'{self._module_name}_temp.svg')

    def _svg_layer_file(self, layer: int) -> str:
        """The base SVG file name."""
        return join(self._module_folder, f'{self._module_name}-{layer}.svg')

    def _print(self, txt: str, cr: bool=False) -> None:
        """Print text."""
        kwargs = {}
        if cr:
            kwargs['end'] = '\r'
        if self._verbose:
            if self._time_log & (self._logger is not None):
                self._logger.log(txt, **kwargs)
            else:
                print(txt, **kwargs) # type: ignore

    def _gen_svg_layers(self) -> None:
        """Generate the SVG layer temp files."""
        self._print(f'Generate SVG layers for {self._module_name}')
        lib = gdspy.GdsLibrary(infile=self._gds_file)
        all_layers = set()
        for cell in lib.top_level():
            all_layers.update(cell.get_layers())
        for keep in all_layers:
            lib_copy = copy.deepcopy(lib)
            for cell in lib_copy.cells.values():
                cell.remove_polygons(lambda _, layer, __: layer != keep) # pylint: disable=cell-var-from-loop
                cell.remove_paths(lambda path: path.layers[0] != keep) # pylint: disable=cell-var-from-loop
                cell.remove_labels(lambda label: label.layer != keep) # pylint: disable=cell-var-from-loop
            for cell in lib_copy.top_level():
                cell.write_svg(self._svg_layer_file(keep), scaling=1000,
                               style=self._layer_style, background=self._background_col,
                               pad=self._padding)

    @property
    def _layer_style(self) -> Dict[Tuple[int, int], Dict[str, Any]]:
        """Generate the layer style dict."""
        result: Dict[Tuple[int, int], Dict[str, Any]] = {}
        for layer_s, layer_d in self._layer_data['layers'].items():
            for data_type_s, data_type_d in layer_d['data_types'].items():
                result[(int(layer_s), int(data_type_s))] = data_type_d['style']
        return result

    def _find_svgs(self) -> Tuple[List[str], List[str]]:
        """Find SVG files."""
        svg_files: List[str] = []
        layer_names: List[str] = []
        for layer_nb_s, layer_data_s in self._layer_data['layers'].items():
            svg_file_name = self._svg_layer_file(int(layer_nb_s))
            if isfile(svg_file_name):
                svg_files.append(svg_file_name)
                layer_names.append(layer_data_s['name'])
        return svg_files, layer_names

    def _parse_svgs(self, svg_files: List[str]) -> List[et.Element]:
        """Parse the given SVG layer files."""
        result: List[et.Element] = []
        for f in svg_files:
            result.append(et.parse(f).getroot())
        return result

    def _get_viewbox(self, parsed_svgs: List[et.Element]) -> Dict[str, int]:
        """Get the max viewbox."""
        viewboxes: List[Tuple[int, int, int, int]] = [] # (min_x, min_y, max_x, max_y)
        for p_svg in parsed_svgs:
            viewbox_s = p_svg.attrib.get('viewBox')
            assert viewbox_s is not None
            parsed_viewbox = [int(np.round(float(v))) for v in viewbox_s.split(' ')]
            viewboxes.append(tuple(parsed_viewbox)) # type: ignore
        min_x = min((vb[0] for vb in viewboxes))
        max_x = max((vb[2] + vb[0] for vb in viewboxes))
        min_y = min((vb[1] for vb in viewboxes))
        max_y = max((vb[3] + vb[1] for vb in viewboxes))
        return {'min_x': min_x, 'min_y': min_y, 'max_x': max_x, 'max_y': max_y}

    def _init_merged_svg(self, viewbox: Dict[str, int]) -> et.Element:
        """Initialize the merged SVG."""
        merged_attr: Dict[str, str] = {
            'width': f'{viewbox["max_x"] - viewbox["min_x"]:d}',
            'height': f'{viewbox["max_y"] - viewbox["min_y"]:d}',
            'viewBox': (f'{viewbox["min_x"]:d} {viewbox["min_y"]:d} '
                        f'{viewbox["max_x"] - viewbox["min_x"]:d} '
                        f'{viewbox["max_y"] - viewbox["min_y"]:d}'),
            'xmlns': self._SVG_NS,
            'xmlns:xlink': self._SVG_LINK
        }
        return et.Element('svg', attrib=merged_attr)

    def _init_defs(self, parsed_svgs: List[et.Element]) -> et.Element:
        """Construct style."""
        merged_style_text: str = ''
        for p_svg in parsed_svgs:
            def_el = p_svg.find('ns:defs', namespaces={'ns': self._SVG_NS})
            assert def_el is not None
            style_el = def_el.find('ns:style', namespaces={'ns': self._SVG_NS})
            assert style_el is not None
            assert style_el.text is not None
            merged_style_text = merged_style_text + style_el.text.replace('\n', '')
        merged_style_text = merged_style_text + 'path {fill-rule: evenodd;}'
        merged_style = et.Element('style', attrib={'type': 'text/css'})
        merged_style.text = merged_style_text
        merged_defs = et.Element('defs')
        merged_defs.append(merged_style)
        return merged_defs

    def _clean_svg(self) -> None:
        """Remove all SVG files in module folder."""
        for f in listdir(self._module_folder):
            if f.endswith('.svg'):
                remove(join(self._module_folder, f))

    def _construct_svg(self, parsed_svgs: List[et.Element], layer_names: List[str]) -> et.Element:
        """Collect all layers and merge to single SVG file."""
        top_group = et.Element('g', attrib={'transform': 'scale(1 -1)'})
        for p_svg, l_name in zip(parsed_svgs, layer_names):
            self._print(f'Processing layer: {l_name}')
            g_el = p_svg.find('ns:g', namespaces={'ns': self._SVG_NS})
            assert g_el is not None
            layer_g = et.Element('g', attrib={'id': l_name})
            polys_per_cls, classes = self._generate_poly(g_el)
            defs_el = p_svg.find('ns:defs', namespaces={'ns': self._SVG_NS})
            assert defs_el is not None
            polys_per_cls_u, classes_u = self._generate_use(g_el, defs_el)
            # Merge and check for overlaps:
            for polys, cls in zip(polys_per_cls_u, classes_u):
                if cls not in classes:
                    classes.append(cls)
                    polys_per_cls.append([])
                cls_index = classes.index(cls)
                for p in polys:
                    polys_per_cls[cls_index].append(p)
                polys_per_cls[cls_index] = self._remove_overlap(polys_per_cls[cls_index],
                                                                self._time_log)
            # Convert to XML elements:
            for polys, cls in zip(polys_per_cls, classes):
                cls_g = et.Element('g', attrib={'class': cls})
                for p in polys:
                    p_el = self._poly_to_svg_path(p)
                    cls_g.append(p_el)
                layer_g.append(cls_g)
            top_group.append(layer_g)
            if self._intermediate_write:
                assert self._merged_svg is not None
                top_group.attrib['id'] = 'top_group'
                self._merged_svg.append(top_group)
                et.ElementTree(element=self._merged_svg)\
                    .write(self._temp_svg_file, encoding='utf-8')
                self._merged_svg.remove(top_group)
                del top_group.attrib['id']
        return top_group

    def _generate_poly(self, parent_group: et.Element) \
        -> Tuple[List[List[Polygon]], List[str]]:
        """Construct simplified plygon set without overlaps"""
        poly_iter = parent_group.findall('ns:polygon', namespaces={'ns': self._SVG_NS})
        polys_per_cls: List[List[Polygon]] = []
        classes: List[str] = []
        for poly in poly_iter:
            cls = poly.attrib['class']
            assert cls is not None
            if cls not in classes:
                classes.append(cls)
                polys_per_cls.append([])
            cls_index = classes.index(cls)
            parsed_points = self._parse_poly_points(poly.attrib['points'])
            geo_poly = Polygon(parsed_points)
            intersect = True
            while intersect:
                intersect = False
                for test_i, test_poly in enumerate(polys_per_cls[cls_index]):
                    if test_poly.intersects(geo_poly):
                        intersect = True
                        geo_poly = test_poly.union(geo_poly)
                        del polys_per_cls[cls_index][test_i]
                        break
            polys_per_cls[cls_index].append(geo_poly)
        return polys_per_cls, classes

    def _generate_use(self, parent_group: et.Element, defs: et.Element) \
        -> Tuple[List[List[Polygon]], List[str]]:
        """Construct polygon set from use elements, without overlaps."""
        g_iter = defs.findall('ns:g', namespaces={'ns': self._SVG_NS})
        g_ids: List[str] = []
        g_polys: List[List[List[Polygon]]] = []
        g_classes: List[List[str]] = []
        stuck_cnt = len(g_iter)
        while g_iter:
            self._print(f'   Assembling uses, remaining: {len(g_iter)}',
                        cr=True)
            g = g_iter.pop(0)
            # Check if all required uses are available:
            req_uses = g.findall('ns:use', namespaces={'ns': self._SVG_NS})
            all_available = True
            for u in req_uses:
                if u.attrib[f'{{{self._SVG_LINK}}}href'][1:] not in g_ids:
                    all_available = False
                    break
            if not all_available:
                g_iter.append(g)
                stuck_cnt -= 1
                if stuck_cnt <= 0:
                    self._print('Could not find all uses, stopping conversion.')
                    break
                continue
            stuck_cnt = len(g_iter)
            # We know the group is available:
            polys_per_cls, classes = self._generate_poly(g)
            g_id = g.attrib['id']
            if g_id in g_ids:
                self._print(f'Found double ID: {g_id}')
                continue
            # Convert uses to polygons:
            for u in req_uses:
                u_classes, u_polys = self._use_to_poly(u, g_ids, g_classes, g_polys)
                for cls, polys in zip(u_classes, u_polys):
                    if cls not in classes:
                        classes.append(cls)
                        polys_per_cls.append([])
                    cls_index = classes.index(cls)
                    for p in polys:
                        polys_per_cls[cls_index].append(p)
                    # polys_per_cls[cls_index] \
                    #     = self._remove_overlap(polys_per_cls[cls_index],
                    #                            self._time_log)
            # Maybe this is better?
            for cls_i, polys in enumerate(polys_per_cls):
                polys_per_cls[cls_i] = self._remove_overlap(polys, self._time_log)
            g_ids.append(g_id)
            g_polys.append(polys_per_cls)
            g_classes.append(classes)
        # Iterate over all use:
        use_iter = parent_group.findall('ns:use', namespaces={'ns': self._SVG_NS})
        poly_classes: List[str] = []
        polys_in_class: List[List[Polygon]] = []
        for u in use_iter:
            transf = u.attrib['transform']
            tran_fun = self._parse_transform(transf)
            id_ = u.attrib[f'{{{self._SVG_LINK}}}href'][1:]
            if id_ not in g_ids:
                self._print(f'ID: {id_} not in defs!')
                continue
            id_index = g_ids.index(id_)
            id_poly_classes = g_classes[id_index]
            id_polys_per_cls = g_polys[id_index]
            for cls, poly_lst in zip(id_poly_classes, id_polys_per_cls):
                if cls not in poly_classes:
                    poly_classes.append(cls)
                    polys_in_class.append([])
                cls_index = poly_classes.index(cls)
                for p in poly_lst:
                    transformed_p = transform(p, tran_fun)
                    polys_in_class[cls_index].append(transformed_p)
        for cls_i, p_per_cls in enumerate(polys_in_class):
            ps_simpl = self._remove_overlap(p_per_cls, self._time_log)
            polys_in_class[cls_i] = ps_simpl
        return polys_in_class, poly_classes

    def _use_to_poly(self, use_el: et.Element, ids: List[str], classes: List[List[str]],
                     polys: List[List[List[Polygon]]]) \
        -> Tuple[List[str], List[List[Polygon]]]:
        """Convert the use reference to a poly list."""
        transf = use_el.attrib['transform']
        tran_fun = self._parse_transform(transf)
        id_ = use_el.attrib[f'{{{self._SVG_LINK}}}href'][1:]
        if id_ not in ids:
            return [], []
        id_index = ids.index(id_)
        result_classes = classes[id_index]
        result_polys = [[transform(poly, tran_fun) for poly in polys_per_cls]
                        for polys_per_cls in polys[id_index]]
        return result_classes, result_polys

    def _parse_transform(self, transform_: str) -> Callable[[Any], Any]:
        """Parse the given transform string."""
        t_x, t_y = 0, 0
        translate = transform_.find('translate')
        if translate >= 0:
            translate_s = transform_[translate + 10:].split(')')[0]
            t_x, t_y = [int(float(s)) for s in translate_s.split(' ')]
        s_x, s_y = 1, 1
        scale = transform_.find('scale')
        if scale >= 0:
            scale_s = transform_[scale + 6:].split(')')[0]
            s_x, s_y = [int(float(s)) for s in scale_s.split(' ')]
        rot = 1
        rotate = transform_.find('rotate')
        if rotate >= 0:
            rotate_s = transform_[rotate + 7:].split(')')[0]
            alpha = int(float(rotate_s))
            if alpha == 180:
                s_x, s_y = -s_x, -s_y
            elif alpha == 90:
                rot, s_y = -1, -s_y
            elif alpha == 270:
                rot, s_x = -1, -s_x
            else:
                self._print(f'Unsuported rotation angle found: {alpha}!')
        return lambda c: c[:,::rot] * [s_x, s_y] + [t_x, t_y]

    def _remove_overlap(self, polys: List[Polygon], log: bool=False) -> List[Polygon]:
        """Remove all overlap in given poly list."""
        result_poly: List[Polygon] = []
        if log & self._time_log:
            self._logger = t_l.TimeLogger(len(polys))
            self._print('   Removing overlap...')
            self._logger.start()
        for p in polys:
            intersect = True
            while intersect:
                intersect = False
                for test_i, test_poly in enumerate(result_poly):
                    if test_poly.intersects(p):
                        intersect = True
                        p = test_poly.union(p)
                        del result_poly[test_i]
                        break
            result_poly.append(p)
            if log & self._time_log:
                self._logger.iterate()
        if log & self._time_log:
            self._logger.clear()
        return result_poly

    def _parse_poly_points(self, points_str: str) -> List[Tuple[int, int]]:
        """Parse the poly points list."""
        result: List[Tuple[int, int]] = []
        pairs = points_str.split(' ')
        for p in pairs:
            x, y = p.split(',')
            result.append((int(float(x)), int(float(y))))
        return result

    def _poly_to_svg_path(self, poly: Polygon) -> et.Element:
        """Convert the given polygon to an SVG path element."""
        c = poly.exterior.coords
        result_d = f'M {int(c[0][0]):d},{int(c[0][1]):d} '
        for x, y in c[1:-1]:
            result_d = result_d + f'L {int(x):d},{int(y):d} '
        result_d = result_d + 'Z'
        for interior in poly.interiors:
            c = interior.coords
            result_d = result_d + f' M {int(c[0][0]):d},{int(c[0][1]):d} '
            for x, y in c[1:-1]:
                result_d = result_d + f'L {int(x):d},{int(y):d} '
            result_d = result_d + 'Z'
        result = et.Element('path', attrib={'d': result_d})
        return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', help='Enable verbose output', action='store_true')
    parser.add_argument('-l', help='Enable time log output', action='store_true')
    parser.add_argument('-i', help='Enable intermediate SVG output', action='store_true')
    parser.add_argument('-m', help='Hardware module name')
    parser.add_argument('-k', help='Keep temp SVG files', action='store_true')
    args = parser.parse_args()

    if not args.m:
        m_name = TOP_MODULE # pylint: disable=invalid-name
        print(f'No module chosen, selected top module: {TOP_MODULE}')
    else:
        m_name = args.m
    g2s = GdsToSvg(m_name, verbose=args.v, time_log=args.l,
                   intermediate_write=args.i)
    g2s.merge(keep_temp_svg=args.k)
