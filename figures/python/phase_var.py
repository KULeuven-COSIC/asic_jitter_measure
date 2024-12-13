"""Generate estimated variance of the phase difference figure."""
import argparse
import sys
from os import getcwd, listdir
from os.path import join, isfile, basename
from typing import List, Callable, cast
import numpy as np
from scipy.optimize import minimize # type: ignore
import matplotlib.pyplot as plt
sys.path.append(getcwd())
from lib import graph_maker as g_m # pylint: disable=wrong-import-position
from lib import store_data as s_d # pylint: disable=wrong-import-position
from measurements import file_manager as f_m # type: ignore # pylint: disable=wrong-import-position
from measurements import helper as h_p # type: ignore # pylint: disable=wrong-import-position

TEMP = 15
SUP = 1.2
NB_CHIPS = 5
CONF = (0, 0, 0, 0)
N = 100
SSC_VARS = [0.48e-18, 0.2e-18, 0.1e-18, 0.28e-18, 0.09e-18, 0.04e-18, 0.09e-18]

RAW_DATA_FOLDER = join('measurements', 'm3')

DEGREE_LINE_STYLES: List[str] = ['dotted', 'dashed', 'dashdotted']
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
c_quants: List[float] = []
c_setups: List[float] = []
c_acc_lens: List[List[float]] = []
c_vars: List[List[float]] = []
c_approxs: List[List[float]] = []

store_data = s_d.StoreData(name='phase_var')

if args.d:

    def check_cond(file_name_):
        """Check if the given file_name is valid."""
        parsed = parse_m3_file_name(file_name_)
        return (parsed[2] == TEMP) & (parsed[3] == SUP) & (parsed[5][0] == CONF[0]) \
            & (parsed[5][1] == CONF[1]) & (parsed[5][2] == CONF[2]) & (parsed[5][3] == CONF[3]) \
            & (parsed[4] == N)

    def parse_m3_file_name(file_name_):
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
    chip_files: List[List[str]] = [[] for i in range(NB_CHIPS)]
    for f in cond_files:
        c = parse_m3_file_name(basename(f))[1]
        chip_files[c] += [f]

    nb_chips = 0 # pylint: disable=invalid-name
    for chip in range(NB_CHIPS):
        if len(chip_files[chip]) == 0:
            continue
        nb_chips += 1
    if args.v:
        print(f'Number chips: {nb_chips}')

    data_to_write: List[List[float]] = []

    for chip in range(NB_CHIPS):
        if not chip_files[chip]:
            continue
        n_s = [parse_m3_file_name(basename(chip_files[chip][i]))[4]
               for i in range(len(chip_files[chip]))]
        for file_index in range(len(chip_files[chip])):
            parsed_file_name = parse_m3_file_name(basename(chip_files[chip][file_index]))
            if parsed_file_name[4] != max(n_s):
                continue
            file_manager = f_m.FileManager(chip_files[chip][file_index])
            data = file_manager.read_file(col_arrays=[False, False, False, False,
                                                      True, True, True, True],
                                          col_ints=[True, False, False, False,
                                                    False, False, False, False])
            assert data is not None
            exp = data[0]
            acc_len = cast(List[float], data[1])
            ro_per_0 = data[2]
            ro_per_1 = data[3]
            phase_0_new = cast(List[List[float]],
                               [list(data[4][i]) for i in range(len(data[4]))]) # type: ignore
            phase_1_new = cast(List[List[float]],
                               [list(data[5][i]) for i in range(len(data[5]))]) # type: ignore
            phase_0_old = cast(List[List[float]],
                               [list(data[6][i]) for i in range(len(data[6]))]) # type: ignore
            phase_1_old = cast(List[List[float]],
                               [list(data[7][i]) for i in range(len(data[7]))]) # type: ignore

            vs = [np.var(po_0) for po_0 in phase_0_old]
            avs = [0.0] * len(phase_0_old)
            for i, po_0i in enumerate(phase_0_old):
                avs[i] = sum(((po_0i[j] - po_0i[j - 1])**2
                              for j in range(1, len(po_0i)))) * 0.5 / (len(phase_0_old[i]) - 1)
            if args.v:
                plt.loglog(acc_len, vs)
                plt.loglog(acc_len, avs)
                plt.show()

            # Quantization noise:
            helper = h_p.Helper(chip, temp=TEMP, sup=SUP, dev='0', verbose=False)
            delays_n_0 = helper.load_dc_delays()[1]
            delays_n_1 = helper.load_dc_delays()[3]
            lsb_0 = max(delays_n_0)
            lsb_1 = max(delays_n_1)
            if args.v:
                print(f'LSB delays0n = {lsb_0}')
                print(f'LSB delays1n = {lsb_1}')
            q_var_0 = (lsb_0)**2 / 12 / np.median(ro_per_0)**2 * 4 * np.pi**2
            q_var_1 = (lsb_1)**2 / 12 / np.median(ro_per_1)**2 * 4 * np.pi**2
            tot_var = cast(float, q_var_0 + q_var_1) # This is quantization noise
            if args.v:
                print(f'Quantization variance DC0: {q_var_0}')
                print(f'Quantization variance DC1: {q_var_1}')
                print(f'Total quantization variance: {tot_var}')

            # Setup noise:
            max_sigma = max(SSC_VARS)
            y_setup = cast(float, 4 * np.pi**2 * (1 / np.median(ro_per_0) \
                                                  - 1 / np.median(ro_per_1))**2 * max_sigma)
            if args.v:
                print(f'Setup noise: {y_setup}')
                print(f'RO0 frequency: {1 / np.median(ro_per_0) / 1e6} MHz')
                print(f'RO1 frequency: {1 / np.median(ro_per_1) / 1e6} MHz')

            # Construct vars:
            old_vars = [np.var([po_0ij - po_1ij for po_0ij, po_1ij in zip(po_0i, po_1i)])
                        for po_0i, po_1i in zip(phase_0_old, phase_1_old)]
            new_vars = [np.var([pn_0ij - pn_1ij for pn_0ij, pn_1ij in zip(pn_0i, pn_1i)])
                       for pn_0i, pn_1i in zip(phase_0_new, phase_1_new)]

            # f_l constraint:
            t_max = acc_len[-1] * 10
            min_ratio = np.log10(-(np.log(1 / t_max) - 1.5 + np.euler_gamma))
            if args.v:
                print(f'f_l constraint: {min_ratio}')

            # Partition data:
            used_indexes = [0] * len(acc_len)
            same = False # pylint: disable=invalid-name
            vars_: List[float]
            while not same:
                vars_ = [0] * len(acc_len)
                for i, _ in enumerate(acc_len):
                    if used_indexes[i] == 0:
                        vars_[i] = new_vars[i] # type: ignore
                    else:
                        vars_[i] = old_vars[i] # type: ignore
                opt_fun: Callable[[List[float]], float] \
                    = lambda x: sum(((np.log(var_i) - 2 * np.log(acc_i) \
                                      - np.log(10**x[0] \
                                      - 10**x[1] * np.log(acc_i)))**2
                                     for var_i, acc_i in zip(vars_, acc_len))) # pylint: disable=cell-var-from-loop
                constr_fun: Callable[[List[float]], float] = lambda x: x[0] - x[1] - min_ratio # pylint: disable=cell-var-from-loop
                approx_sol = minimize(opt_fun, [0, 0],
                                      constraints={'type': 'ineq', 'fun': constr_fun})['x']
                approx_y = [10**approx_sol[0] * acc_i**2 \
                            - 10**approx_sol[1] * np.log(acc_i) * acc_i**2
                            for acc_i in acc_len]
                old_indexes = list(used_indexes)
                same = True # pylint: disable=invalid-name
                for i, (new_vi, old_vi, app_yi) in enumerate(zip(new_vars, old_vars, approx_y)):
                    if abs(np.log(new_vi) - np.log(app_yi)) < abs(np.log(old_vi) - np.log(app_yi)):
                        used_indexes[i] = 0
                    else:
                        used_indexes[i] = 1
                    if old_indexes[i] != used_indexes[i]:
                        same = False # pylint: disable=invalid-name
            approx_sol = [np.log10(4 * np.pi**2) + app for app in approx_sol]
            approx_y = [10**approx_sol[0] * acc_i**2 - 10**approx_sol[1] * np.log(acc_i) * acc_i**2
                        for acc_i in acc_len]
            if args.v:
                print(f'c20 = {10**approx_sol[0] / (1 / np.median(ro_per_0)**2 + 1 / np.median(ro_per_1)**2)}') # pylint: disable=line-too-long
                print(f'c21 = {-10**approx_sol[1] / (1 / np.median(ro_per_0)**2 + 1 / np.median(ro_per_1)**2)}') # pylint: disable=line-too-long

            # Store data:
            data_to_write.append([chip, file_index, tot_var, y_setup])
            data_to_write.append(acc_len)
            data_to_write.append([4 * np.pi**2 * var_i for var_i in vars_])
            data_to_write.append(approx_y)

            chips.append(chip)
            c_quants.append(tot_var)
            c_setups.append(y_setup)
            c_acc_lens.append(acc_len)
            c_vars.append([4 * np.pi**2 * var_i for var_i in vars_]) # type: ignore
            c_approxs.append(approx_y)
    store_data.write_data(data_to_write, over_write=True)
    if args.q:
        sys.exit()
else:
    if not store_data.file_exist:
        if args.v:
            print(f'File: {store_data.file_path} does not exist!')
        sys.exit()
    data_r = store_data.read_data() # type: ignore
    if data_r is None:
        if args.v:
            print(f'Error in data: {store_data.file_path}!')
            sys.exit()
    assert data_r is not None
    nb_data = int(len(data_r) / 4)
    for chip_i in range(nb_data):
        chips.append(int(data_r[chip_i * 4][0]))
        c_quants.append(data_r[chip_i * 4][2])
        c_setups.append(data_r[chip_i * 4][3])
        c_acc_lens.append(data_r[chip_i * 4 + 1])
        c_vars.append(data_r[chip_i * 4 + 2])
        c_approxs.append(data_r[chip_i * 4 + 3])

if args.v:
    for chip, accs, quant, setup, vars_, approxs \
        in zip(chips, c_acc_lens, c_quants, c_setups, c_vars, c_approxs):
        print(chip)
        plt.loglog(accs, vars_, 'o')
        plt.loglog(accs, approxs)
        plt.axhline(y=quant, color='green')
        plt.axhline(y=setup, color='purple')
        plt.show()

graph_maker = g_m.GraphMaker('phase_var.svg', figure_size=(1, 1), folder_name='figures')
graph_maker.create_grid(size=(1, 5), x_ratios=[1, 0.05, 1, 0.05, 1],
                        marg_mid_hor=0, marg_mid_ver=0, marg_top=0.81, marg_left=0.12)

ax_1 = graph_maker.create_ax(x_slice=2, y_slice=0, # pylint: disable=invalid-name
                             x_scale='log10', y_scale='log10',
                             x_label='Accumulation time',
                             x_unit='s', show_y_labels=False,
                             max_nb_x_ticks=6, title_pad=27,
                             title='Estimated phase difference variance',
                             x_lim=(X_MIN, X_MAX), y_lim=(Y_MIN, Y_MAX))
ax_2 = graph_maker.create_ax(x_slice=4, y_slice=0, # pylint: disable=invalid-name
                             x_scale='log10', y_scale='log10',
                             share_y=ax_1, show_y_labels=False,
                             max_nb_x_ticks=6,
                             x_lim=(X_MIN, X_MAX), y_lim=(Y_MIN, Y_MAX))
ax_0 = graph_maker.create_ax(x_slice=0, y_slice=0, # pylint: disable=invalid-name
                             x_scale='log10', y_scale='log10',
                             show_legend=True, legend_loc='center',
                             legend_bbox=[0, 1, 3.1, 0.17],
                             y_label='Phase variance', share_y=ax_1,
                             y_unit=r'rad\textsuperscript{2}',
                             nb_leg_cols=4, max_nb_x_ticks=6,
                             leg_font_size=0.55,
                             x_lim=(X_MIN, X_MAX), y_lim=(Y_MIN, Y_MAX),
                             max_nb_y_ticks=8)
axs: List[int] = [ax_0, ax_1, ax_2]

# Plot polys:
for degree, line_style in zip(range(1, 4), DEGREE_LINE_STYLES):
    a_max = int(np.floor(np.log10(Y_MAX) - degree * np.log10(X_MIN)))
    a_min = int(np.ceil(np.log10(Y_MIN) - degree * np.log10(X_MAX)))
    for a in range(a_min + 1, a_max, 4):
        for ax in axs:
            xs: List[float] = np.logspace(np.log10(X_MIN), np.log10(X_MAX),
                                          100, endpoint=True) # type: ignore
            ys: List[float] = [10**a * ac**degree for ac in xs]
            xs, ys = zip(*[(x, y) for x, y in zip(xs, ys) if (y >= Y_MIN) & (y <= Y_MAX)]) # type: ignore # pylint: disable=line-too-long
            graph_maker.plot(ax, xs=xs, ys=ys, line_style=line_style, color='grey',
                             line_width=0.5, alpha=0.5)

# Plot data:
for ax, accs, quant, setup, vars_, approxs \
    in zip(axs, c_acc_lens, c_quants, c_setups, c_vars, c_approxs):
    graph_maker.plot(ax, xs=accs, ys=vars_, line_style='none', color=0,
                     marker='dot', label='Measurement')
    graph_maker.plot(ax, xs=accs, ys=approxs, color=1, label='Model fit')
    xs = np.logspace(np.log10(X_MIN), np.log10(X_MAX), 10) # type: ignore
    graph_maker.plot(ax, xs=xs, ys=[quant]*10, line_style='dashed',
                     color=2, label='Quantization error')
    graph_maker.plot(ax, xs=xs, ys=[setup]*10, line_style='dotted',
                     color=3, label='Set-up error')

# Chip labels:
for chip_i, ax in enumerate(axs):
    graph_maker.text(ax, x=np.sqrt(X_MIN * X_MAX), y=Y_MAX / 20, s=f'Chip {chip_i}',
                     border_color='white')

# Generate SVG:
graph_maker.write_svg()
