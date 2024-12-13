"""Generate sample variance versus sample Allan variance figure."""
import argparse
import sys
from os import getcwd, listdir
from os.path import join, isfile, basename
from typing import List, Callable, Tuple
import numpy as np
from scipy.optimize import minimize # type: ignore
import matplotlib.pyplot as plt
sys.path.append(getcwd())
from lib import graph_maker as g_m # pylint: disable=wrong-import-position
from lib import store_data as s_d # pylint: disable=wrong-import-position
from measurements import file_manager as f_m # type: ignore # pylint: disable=wrong-import-position

TEMP = 15
SUP = 1.2
NB_CHIPS = 5
CONF = (0, 0, 0, 0)
N = 100

RAW_DATA_FOLDER = join('measurements', 'm3')

X_MIN = 5e-9
X_MAX = 5e0
Y_MIN = 1e-3
Y_MAX = 1e13

parser = argparse.ArgumentParser()
parser.add_argument('-v', help='Print process', action='store_true')
parser.add_argument('-d', help='Collect data', action='store_true')
parser.add_argument('-q', help='Quit after data collect', action='store_true')
args = parser.parse_args()

chips: List[int] = []
c_accs: List[List[float]]= []
c_vars: List[List[float]] = []
c_avars: List[List[float]] = []

store_data = s_d.StoreData(name='allan_var')

if args.d:

    def check_cond(file_name_: str) -> bool:
        """Check if the given file_name is valid."""
        parsed = parse_m3_file_name(file_name_)
        return ((parsed[2] == TEMP) & (parsed[3] == SUP) & (parsed[5][0] == CONF[0]) \
            & (parsed[5][1] == CONF[1]) & (parsed[5][2] == CONF[2]) \
            & (parsed[5][3] == CONF[3]) & (parsed[4] == N))

    def parse_m3_file_name(file_name_: str) -> Tuple[int, int, float, float, int, List[int]]:
        """Parse the given file name."""
        parts = file_name_.split('_')
        m = int(parts[0][1:])
        c_ = int(parts[1][4:])
        t = float(parts[2][4:])
        s = float(parts[3][3:])
        n = int(parts[4][3:])
        c_parts = parts[5][4:].split('-')
        c_parts[-1] = c_parts[-1].split('.')[0]
        co = [int(p) for p in c_parts]
        return (m, c_, t, s, n, co)

    data_files = [f for f in listdir(RAW_DATA_FOLDER) if isfile(join(RAW_DATA_FOLDER, f))]
    m3_files = [f for f in data_files if f[:2] == 'm3']
    cond_files = [join(RAW_DATA_FOLDER, f) for f in m3_files if check_cond(f)]
    chip_files: List[List[str]] = [[] for _ in range(NB_CHIPS)]
    for f in cond_files:
        c = parse_m3_file_name(basename(f))[1]
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
        if args.v:
            print(f'Chip: {chip}')
        n_s = [parse_m3_file_name(basename(chip_file_i))[4] for chip_file_i in chip_files[chip]]
        for file_index, chip_file_i in enumerate(chip_files[chip]):
            parsed_file_name = parse_m3_file_name(basename(chip_file_i))
            if parsed_file_name[4] != max(n_s):
                continue
            file_manager = f_m.FileManager(chip_file_i)
            data = file_manager.read_file(col_arrays=[False, False, False, False,
                                                      True, True, True, True],
                                          col_ints=[True, False, False, False,
                                                    False, False, False, False])
            assert data is not None
            exp = data[0]
            acc_len: List[float] = data[1] # type: ignore
            ro_per_0: List[float] = data[2] # type: ignore
            ro_per_1: List[float] = data[3] # type: ignore
            phase_0_new: List[List[float]] = [list(d_i) for d_i in data[4]] # type: ignore
            phase_1_new: List[List[float]] = [list(d_i) for d_i in data[5]] # type: ignore
            phase_0_old: List[List[float]] = [list(d_i) for d_i in data[6]] # type: ignore
            phase_1_old: List[List[float]] = [list(d_i) for d_i in data[7]] # type: ignore

            #Construct Allan vars:
            avs_o = [sum(((po_0ij - po_0ijm)**2
                          for po_0ij, po_0ijm in zip(po_0i[1:], po_0i))) * 0.5 / (len(po_0i) - 1)
                     for po_0i in phase_0_old]
            avs_n = [sum(((pn_0ij - pn_0ijm)**2
                          for pn_0ij, pn_0ijm in zip(pn_0i[1:], pn_0i))) * 0.5 / (len(pn_0i) - 1)
                     for pn_0i in phase_0_new]

            # Construct normal vars:
            old_vars = [np.var([po_0ij - po_1ij for po_0ij, po_1ij in zip(po_0i, po_1i)])
                        for po_0i, po_1i in zip(phase_0_old, phase_1_old)]
            new_vars = [np.var([pn_0ij - pn_1ij for pn_0ij, pn_1ij in zip(pn_0i, pn_1i)])
                        for pn_0i, pn_1i in zip(phase_0_new, phase_1_new)]

            # f_l constraint:
            t_max = acc_len[-1] * 10
            min_ratio = np.log10(-(np.log(1 / t_max) - 1.5 + np.euler_gamma))

            # Partition data:
            used_indexes = [0] * len(acc_len)
            same = False # pylint: disable=invalid-name
            while not same:
                vars_ = [0.0] * len(acc_len)
                for i, _ in enumerate(acc_len):
                    if used_indexes[i] == 0:
                        vars_[i] = new_vars[i] # type: ignore
                    else:
                        vars_[i] = old_vars[i] # type: ignore
                opt_fun: Callable[[List[float]], float] = lambda x: sum(((np.log(var_i) - 2 * np.log(acc_i) - np.log(10**x[0] - 10**x[1] * np.log(acc_i)))**2 for acc_i, var_i in zip(acc_len, vars_))) # pylint: disable=cell-var-from-loop,line-too-long
                const_fun: Callable[[List[float]], float] = lambda x: x[0] - x[1] - min_ratio # pylint: disable=cell-var-from-loop
                approx_sol: List[float] = minimize(opt_fun, [0, 0],
                                                   constraints={'type': 'ineq',
                                                                'fun': const_fun})['x']
                approx_y = [10**approx_sol[0] * acc_i**2 \
                            - 10**approx_sol[1] * np.log(acc_i) * acc_i**2
                            for acc_i in acc_len]
                old_indexes = list(used_indexes)
                same = True # pylint: disable=invalid-name
                for i, (nv_i, ov_i, ap_i) in enumerate(zip(new_vars, old_vars, approx_y)):
                    if abs(np.log(nv_i) - np.log(ap_i)) < abs(np.log(ov_i) - np.log(ap_i)):
                        used_indexes[i] = 0
                    else:
                        used_indexes[i] = 1
                    if old_indexes[i] != used_indexes[i]:
                        same = False # pylint: disable=invalid-name
            used_avs = [avo_i if u_i == 1 else avn_i
                        for u_i, avo_i, avn_i in zip(used_indexes, avs_o, avs_n)]

            # Store data:
            data_to_write.append([chip, file_index])
            data_to_write.append(acc_len)
            data_to_write.append([4 * np.pi**2 * var_i for var_i in vars_])
            data_to_write.append([4 * np.pi**2 * var_i for var_i in used_avs])

            chips.append(chip)
            c_accs.append(acc_len)
            c_vars.append([4 * np.pi**2 * var_i for var_i in vars_])
            c_avars.append([4 * np.pi**2 * var_i for var_i in used_avs])
    store_data.write_data(data_to_write, over_write=True)
    if args.q:
        sys.exit()
else:
    if not store_data.file_exist:
        if args.v:
            print(f'File: {store_data.file_path} does not exist!')
        sys.exit()
    data_r = store_data.read_data()
    if data_r is None:
        if args.v:
            print(f'Error in data: {store_data.file_path}!')
            sys.exit()
    assert data_r is not None
    nb_data = int(len(data_r) / 4)
    for chip_i in range(nb_data):
        chips.append(int(data_r[chip_i * 4][0]))
        c_accs.append(data_r[chip_i * 4 + 1])
        c_vars.append(data_r[chip_i * 4 + 2])
        c_avars.append(data_r[chip_i * 4 + 3])

if args.v:
    for chip, accs, vars_, avars in zip(chips, c_accs, c_vars, c_avars):
        print(chip)
        plt.loglog(accs, vars_, 'bo')
        plt.loglog(accs, avars, 'rx')
        plt.show()

graph_maker = g_m.GraphMaker('allan_var.svg', figure_size=(1, 1), folder_name='figures')
graph_maker.create_grid(size=(1, 5), x_ratios=[1, 0.05, 1, 0.05, 1],
                        marg_mid_hor=0, marg_mid_ver=0, marg_top=0.81, marg_left=0.12)

ax_1 = graph_maker.create_ax(x_slice=2, y_slice=0, # pylint: disable=invalid-name
                             x_scale='log10', y_scale='log10',
                             x_label='Accumulation time',
                             x_unit='s', show_y_labels=False,
                             max_nb_x_ticks=6, title_pad=27,
                             title='Sample versus sample Allan variance',
                             x_lim=(X_MIN, X_MAX), y_lim=(Y_MIN, Y_MAX),
                             x_grid=True, y_grid=True)
ax_2 = graph_maker.create_ax(x_slice=4, y_slice=0, # pylint: disable=invalid-name
                             x_scale='log10', y_scale='log10',
                             share_y=ax_1, show_y_labels=False,
                             max_nb_x_ticks=6,
                             x_lim=(X_MIN, X_MAX), y_lim=(Y_MIN, Y_MAX),
                             x_grid=True, y_grid=True)
ax_0 = graph_maker.create_ax(x_slice=0, y_slice=0, # pylint: disable=invalid-name
                             x_scale='log10', y_scale='log10',
                             show_legend=True, legend_loc='center',
                             legend_bbox=[0, 1, 3.1, 0.17],
                             y_label='Phase variance', share_y=ax_1,
                             y_unit=r'rad\textsuperscript{2}',
                             nb_leg_cols=4, max_nb_x_ticks=6,
                             leg_font_size=0.55,
                             x_lim=(X_MIN, X_MAX), y_lim=(Y_MIN, Y_MAX),
                             max_nb_y_ticks=8,
                             x_grid=True, y_grid=True)
axs: List[int] = [ax_0, ax_1, ax_2]

# Plot data:
for ax, accs, vars_, avars in zip(axs, c_accs, c_vars, c_avars):
    graph_maker.plot(ax, xs=accs, ys=vars_, line_style='none', color=0,
                     marker='dot', label='Sample variance')
    graph_maker.plot(ax, xs=accs, ys=avars, color=1,
                     label='Sample Allan variance', line_style='none',
                     marker='tri_up', line_width=0.4)

# Chip labels:
for chip_i, ax in enumerate(axs):
    graph_maker.text(ax, x=np.sqrt(X_MIN * X_MAX), y=Y_MAX / 20, s=f'Chip {chip_i}',
                     border_color='white')

# Generate SVG:
graph_maker.write_svg()
