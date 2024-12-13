"""Generate flicker noise corner figure."""
import argparse
import sys
from os import getcwd, listdir
from os.path import join, isfile, basename
from typing import List, Callable, Tuple
import numpy as np
from scipy.optimize import least_squares, fsolve # type: ignore
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
VF_C20S = [0, 0, 11158929933721.31, 985681253777.279, 4807235025297.806]
VF_C21S = [0, 0, -307483.6805409857, -426872092056.26465, -2378175054205.943]

RAW_DATA_FOLDER = join('measurements', 'm3')

X_MIN = 20e-9
X_MAX = 1e-6
Y_MIN = 1e-2
Y_MAX = 8e0

parser = argparse.ArgumentParser()
parser.add_argument('-v', help='Print process', action='store_true')
parser.add_argument('-d', help='Collect data', action='store_true')
parser.add_argument('-q', help='Quit after data collect', action='store_true')
args = parser.parse_args()

chips: List[int] = []
c_xs: List[List[float]] = []
c_ys: List[List[float]] = []
c_y_ls: List[List[float]] = []
c_y_ln: List[List[float]] = []
c_corns: List[Tuple[float, float]] = []

store_data = s_d.StoreData(name='noise_corner')

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
        for chip_file_i in chip_files[chip]:
            parsed_file_name = parse_m3_file_name(basename(chip_file_i))
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

            new_vars = [np.var([pn_0ij - pn_1ij for pn_0ij, pn_1ij in zip(pn_0i, pn_1i)])
                        for pn_0i, pn_1i in zip(phase_0_new, phase_1_new)]
            meas_y_s: List[float] = []
            meas_x_s: List[float] = []
            for acc, new_var in zip(acc_len, new_vars):
                if acc <= X_MAX:
                    meas_x_s.append(acc)
                    meas_y_s.append(new_var * 4 * np.pi**2) # type: ignore

            # Least square quadratic solution:
            opt_fun: Callable[[List[float]], List[float]] \
                = lambda x: [np.log(m_y) - np.log(x[0] + x[1] * m_x + x[2] * m_x**2)
                             for m_x, m_y in zip(meas_x_s, meas_y_s)] # pylint: disable=cell-var-from-loop
            xls = least_squares(opt_fun, [0, 1e5, 1e10],
                                bounds=((0, 0, 0), (np.inf, np.inf, np.inf)))['x']
            if args.v:
                print(xls)
                print(f'Noise strength: {xls[1] / 4 / np.pi**2 / (1 / np.median(ro_per_0)**2 + 1 / np.median(ro_per_1)**2) * 1e15} fs') # pylint: disable=line-too-long

            y_ls_sol_0: List[float] = [xls[0] + xls[1] * x_i for x_i in meas_x_s]

            # ln solution:
            y_ln_sol: List[float] = [VF_C20S[chip] * x_i**2 + VF_C21S[chip]*x_i**2 * np.log(x_i)
                                     for x_i in meas_x_s]

            # Noise corner:
            cor_fun: Callable[[float], float] = lambda x: VF_C20S[chip] * x + VF_C21S[chip]*x * np.log(x) - xls[1]-xls[0] / x # pylint: disable=cell-var-from-loop,line-too-long
            f_noise_corner = fsolve(cor_fun, x0=xls[1] / (VF_C20S[chip] - 16 * VF_C21S[chip]))[0]
            if args.v:
                print(f'Noise corner: {f_noise_corner * 1e9} ns')

            # Store data:
            data_to_write.append([chip, f_noise_corner, xls[0] + xls[1] * f_noise_corner])
            data_to_write.append(meas_x_s)
            data_to_write.append(meas_y_s)
            data_to_write.append(y_ls_sol_0)
            data_to_write.append(y_ln_sol)

            chips.append(chip)
            c_xs.append(meas_x_s)
            c_ys.append(meas_y_s)
            c_y_ls.append(y_ls_sol_0)
            c_y_ln.append(y_ln_sol)
            c_corns.append((f_noise_corner, xls[0] + xls[1] * f_noise_corner))
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
    nb_data = int(len(data_r) / 5)
    for chip_i in range(nb_data):
        chips.append(int(data_r[chip_i * 5][0]))
        c_corns.append((float(data_r[chip_i * 5][1]), float(data_r[chip_i * 5][2])))
        c_xs.append(data_r[chip_i * 5 + 1])
        c_ys.append(data_r[chip_i * 5 + 2])
        c_y_ls.append(data_r[chip_i * 5 + 3])
        c_y_ln.append(data_r[chip_i * 5 + 4])

if args.v:
    for chip, xs, ys, y_ls, y_ln, (cor_x, cor_y) \
        in zip(chips, c_xs, c_ys, c_y_ls, c_y_ln, c_corns):
        print(chip)
        plt.loglog(xs, ys, 'o')
        plt.loglog(xs, y_ls, color='red')
        plt.loglog(xs, y_ln, color='green')
        plt.loglog([cor_x], [cor_y], 'go')
        plt.show()

graph_maker = g_m.GraphMaker('noise_corner.svg', figure_size=(1, 1), folder_name='figures')
graph_maker.create_grid(size=(1, 5), x_ratios=[1, 0.05, 1, 0.05, 1],
                        marg_mid_hor=0, marg_mid_ver=0, marg_top=0.81, marg_left=0.12)

ax_1 = graph_maker.create_ax(x_slice=2, y_slice=0, # pylint: disable=invalid-name
                             x_scale='log10', y_scale='log10',
                             x_label='Accumulation time',
                             x_unit='s', show_y_labels=False,
                             max_nb_x_ticks=6, title_pad=27,
                             title='Flicker noise corner',
                             x_lim=(X_MIN / 1.5, X_MAX * 2), y_lim=(Y_MIN / 2, Y_MAX * 2),
                             y_grid=True, x_grid=True)
ax_2 = graph_maker.create_ax(x_slice=4, y_slice=0, # pylint: disable=invalid-name
                             x_scale='log10', y_scale='log10',
                             share_y=ax_1, show_y_labels=False,
                             max_nb_x_ticks=6,
                             x_lim=(X_MIN / 1.5, X_MAX * 2), y_lim=(Y_MIN / 2, Y_MAX * 2),
                             y_grid=True, x_grid=True)
ax_0 = graph_maker.create_ax(x_slice=0, y_slice=0, # pylint: disable=invalid-name
                             x_scale='log10', y_scale='log10',
                             show_legend=True, legend_loc='center',
                             legend_bbox=[0, 1, 3.1, 0.17],
                             y_label='Phase variance', share_y=ax_1,
                             y_unit=r'rad\textsuperscript{2}',
                             nb_leg_cols=4, max_nb_x_ticks=6,
                             leg_font_size=0.55,
                             x_lim=(X_MIN / 1.5, X_MAX * 2), y_lim=(Y_MIN / 2, Y_MAX * 2),
                             max_nb_y_ticks=8, y_grid=True, x_grid=True)
axs: List[int] = [ax_0, ax_1, ax_2]

# Plot data:
for ax, xs, ys, y_ls, y_ln, (cor_x, cor_y) in zip(axs, c_xs, c_ys, c_y_ls, c_y_ln, c_corns):
    graph_maker.plot(ax, xs=xs, ys=ys, line_style='none', color=0,
                     marker='dot', label='Measurement')
    graph_maker.plot(ax, xs=xs, ys=y_ln, color=1, label='Model fit')
    graph_maker.plot(ax, xs=xs, ys=y_ls, color=2, label='Linear fit')
    graph_maker.plot(ax, xs=[cor_x], ys=[cor_y], line_style='none',
                     color=3, marker='cross', marker_color=3, marker_edge_color='white',
                     label='Noise corner')

# Chip labels:
for chip_i, ax in enumerate(axs):
    graph_maker.text(ax, x=np.sqrt(X_MIN * X_MAX), y=Y_MAX, s=f'Chip {chip_i}',
                     border_color='white')

# Generate SVG:
graph_maker.write_svg()
