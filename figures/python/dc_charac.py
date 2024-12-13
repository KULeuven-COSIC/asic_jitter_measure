"""Generate measured stage delay distributions figure."""
import argparse
import sys
from os import getcwd, listdir
from os.path import join, isfile, basename
from typing import List, Tuple, cast
import numpy as np
sys.path.append(getcwd())
from lib import graph_maker as g_m # pylint: disable=wrong-import-position
from lib import store_data as s_d # pylint: disable=wrong-import-position
from measurements import file_manager as f_m # pylint: disable=wrong-import-position

TEMP = 15
SUP = 1.2
NB_CHIPS = 5

RAW_DATA_FOLDER = join('measurements', 'm1')

parser = argparse.ArgumentParser()
parser.add_argument('-v', help='Print process', action='store_true')
parser.add_argument('-d', help='Collect data', action='store_true')
parser.add_argument('-q', help='Quit after data collect', action='store_true')
args = parser.parse_args()

chips: List[int] = []
delays_p_0: List[List[float]] = []
delays_n_0: List[List[float]] = []
delays_p_1: List[List[float]] = []
delays_n_1: List[List[float]] = []

store_data = s_d.StoreData(name='dc_charac')

if args.d:

    def check_cond(file_name_: str) -> bool:
        """Check if the given file_name is valid."""
        parsed = parse_m1_file_name(file_name_)
        return (parsed[2] == TEMP) & (parsed[3] == SUP)

    def parse_m1_file_name(file_name_: str) -> Tuple[int, int, float, float, float, int, List[int]]:
        """Parse the given filename."""
        parts = file_name_.split('_')
        m = int(parts[0][1:])
        c_ = int(parts[1][4:])
        t = float(parts[2][4:])
        s = float(parts[3][3:])
        a = float(parts[4][3:])
        n = int(parts[5][3:])
        c_parts = parts[6][4:].split('-')
        c_parts[-1] = c_parts[-1].split('.')[0]
        co = [int(p) for p in c_parts]
        return (m, c_, t, s, a, n, co)

    data_files = [f for f in listdir(RAW_DATA_FOLDER)
                  if isfile(join(RAW_DATA_FOLDER, f))]
    m1_files = [f for f in data_files if f[:2] == 'm1']
    cond_files = [join(RAW_DATA_FOLDER, f) for f in m1_files if check_cond(f)]
    chip_files: List[List[str]] = [[] for _ in range(NB_CHIPS)]
    for f in cond_files:
        c = parse_m1_file_name(basename(f))[1]
        chip_files[c] += [f]

    nb_chips = 0 # pylint: disable=invalid-name
    for chip in range(NB_CHIPS):
        if not chip_files[chip]:
            continue
        nb_chips += 1
    if args.v:
        print(f'Number chips: {nb_chips}')

    data_to_write: List[List[float]] = []
    for chip in range(NB_CHIPS):
        if not chip_files[chip]:
            continue
        dp0_m = [0.0]*128
        dn0_m = [0.0]*128
        dp1_m = [0.0]*128
        dn1_m = [0.0]*128
        nb_good = 0 # pylint: disable=invalid-name
        for file_index, file_name in enumerate(chip_files[chip]):
            file_manager = f_m.FileManager(file_name) # type: ignore
            data = file_manager.read_file(col_arrays=(False, False, False, False, False), # type: ignore # pylint: disable=line-too-long
                                         col_ints=[True, False, False, False, False])
            dp0s = cast(List[float], data[1]) # type: ignore
            dn0s = cast(List[float], data[2]) # type: ignore
            dp1s = cast(List[float], data[3]) # type: ignore
            dn1s = cast(List[float], data[4]) # type: ignore
            if len(dn1s) < 128:
                continue
            for i in range(128):
                dp0_m[i] += dp0s[i]
                dn0_m[i] += dn0s[i]
                dp1_m[i] += dp1s[i]
                dn1_m[i] += dn1s[i]
            nb_good += 1
        dp0_m = [d / nb_good for d in dp0_m]
        dn0_m = [d / nb_good for d in dn0_m]
        dp1_m = [d / nb_good for d in dp1_m]
        dn1_m = [d / nb_good for d in dn1_m]

        if args.v:
            print(f'CHIP {chip}')
            print(f'dp0 mean: {np.mean(dp0_m)}, max: {max(dp0_m)}')
            print(f'dn0 mean: {np.mean(dn0_m)}, max: {max(dn0_m)}')
            print(f'dp1 mean: {np.mean(dp1_m)}, max: {max(dp1_m)}')
            print(f'dn1 mean: {np.mean(dn1_m)}, max: {max(dn1_m)}')

        data_to_write.append([chip])
        data_to_write.append(dp0_m)
        data_to_write.append(dn0_m)
        data_to_write.append(dp1_m)
        data_to_write.append(dn1_m)
        chips.append(chip)
        delays_p_0.append(dp0_m)
        delays_n_0.append(dn0_m)
        delays_p_1.append(dp1_m)
        delays_n_1.append(dn1_m)

    store_data.write_data(data_to_write, over_write=True)
    if args.q:
        sys.exit()
else:
    if not store_data.file_exist:
        if args.v:
            print(f'File: {store_data.file_path} does not exist!')
        sys.exit()
    data = store_data.read_data() # type: ignore
    if data is None:
        if args.v:
            print(f'Error in data: {store_data.file_path}!')
            sys.exit()
    nb_data = int(len(data) / 5) # type: ignore
    for chip_i in range(nb_data):
        chips.append(int(data[chip_i * 5][0])) # type: ignore
        delays_p_0.append(data[chip_i * 5 + 1]) # type: ignore
        delays_n_0.append(data[chip_i * 5 + 2]) # type: ignore
        delays_p_1.append(data[chip_i * 5 + 3]) # type: ignore
        delays_n_1.append(data[chip_i * 5 + 4]) # type: ignore

graph_maker = g_m.GraphMaker('dc_charac.svg', figure_size=(1, 1), folder_name='figures')
graph_maker.create_grid(size=(1, 1))

ax = graph_maker.create_ax(0, 0, # pylint: disable=invalid-name
                           title='DC stage delay distribution',
                           x_label='DC edge type',
                           y_label='DC stage delay',
                           x_unit = '-',
                           y_unit=r's',
                           x_scale='fix',
                           y_grid=True,
                           show_legend=True,
                           legend_loc='upper right',
                           fixed_locs_x=[1, 2, 3, 4, 5, 6],
                           fixed_labels_x=['C0, DC0', 'C0, DC1', 'C1, DC0',
                                           'C1, DC1', 'C2, DC0', 'C2, DC1'],
                           x_lim=(0.5, 2 * len(chips) + 0.5)) # Fix graph width for boxplot transform. # pylint: disable=line-too-long

# Plot data:
for chip, (d_p_0, d_n_0, d_p_1, d_n_1) in enumerate(zip(delays_p_0, delays_n_0,
                                                        delays_p_1, delays_n_1)):
    graph_maker.violin(ax, d_p_0, color=0, position=1 + chip*2,
                       show_box=True, side='low', marker='cross')
    graph_maker.violin(ax, d_n_0, color=1, position=1 + chip*2,
                       show_box=True, side='high', marker='plus')
    graph_maker.violin(ax, d_p_1, color=0, position=2 + chip*2,
                       show_box=True, side='low', marker='cross')
    graph_maker.violin(ax, d_n_1, color=1, position=2 + chip*2,
                       show_box=True, side='high', marker='plus')

# Create legend entries:
graph_maker.plot(ax, xs=[], ys=[], color=0, marker='cross', label='P',
                 visible=False, line_style='none')
graph_maker.plot(ax, xs=[], ys=[], color=1, marker='plus', label='N',
                 visible=False, line_style='none')

# Generate SVG:
graph_maker.write_svg()
