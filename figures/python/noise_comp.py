"""Generate compare contribution of different noise types to total excess
phase variance figure."""
import argparse
import math
import sys
import os
from typing import List # pylint: disable=wrong-import-position
# import sympy # type: ignore # pylint: disable=import-error
sys.path.append(os.getcwd())
from lib import graph_maker as g_m # pylint: disable=wrong-import-position

F_H: float = 100e9
F_L: float = 1e-5
HS: List[float] = [1e12, 1e9, 1e5, 1e-8, 1e-15]
TS: List[float] = []
T_START_EXP: int = -15
T_END_EXP: int = 5
for ei in range(0, T_END_EXP - T_START_EXP):
    for ti in range(1, 10):
        TS.append((ti*10**T_START_EXP)*10**ei)
EM: float = 0.5772156649

parser = argparse.ArgumentParser()
parser.add_argument('-v', help='Print process', action='store_true')
parser.add_argument('-d', help='Collect data', action='store_true')
parser.add_argument('-q', help='Quit after data collect', action='store_true')
args = parser.parse_args()

if args.d:
    if args.q:
        sys.exit()

v_0: List[float] = [HS[2]*4*math.pi**2*ti for ti in TS]
v_1: List[float] = [HS[3]*2*math.log(F_H/F_L) for _ in TS]
v_2: List[float] = [HS[4]*2*F_H for _ in TS]
v__1: List[float] = [HS[1]*4*math.pi**2*ti**2*(3-2*EM-2*math.log(2*math.pi*F_L*ti)) for ti in TS]
v__2: List[float] = [HS[0]*16/3*math.pi**4*ti**3 for ti in TS]
# v_t: List[float] = [v__2[i] + v__1[i] + v_0[i] + v_1[i] + v_2[i] for i in range(len(TS))]

graph_maker = g_m.GraphMaker('noise_comp.svg', figure_size=(1, 1), folder_name='figures')
graph_maker.create_grid(size=(1, 1))

ax = graph_maker.create_ax(0, 0, # pylint: disable=invalid-name
                           title='Noise type contributions',
                           x_label='Accumulation time',
                           y_label='Phase variance',
                           x_unit = 's',
                           y_unit=r'rad\textsuperscript{2}',
                           x_scale='log10',
                           y_scale='log10',
                           x_grid=True,
                           show_y_labels=False,
                           show_legend=True,
                           x_lim=(1e-15, 1),
                           y_lim=(1e-7, 1e10),
                           hide_y_ticks=True)

# Plot data:
graph_maker.plot(ax, xs=TS, ys=v_2, label=r'$\alpha = \num{2}$ or $\num{1}$')
graph_maker.plot(ax, xs=TS, ys=v_0, label=r'$\alpha = \num{0}$')
graph_maker.plot(ax, xs=TS, ys=v__1, label=r'$\alpha = \num{-1}$')
graph_maker.plot(ax, xs=TS, ys=v__2, label=r'$\alpha = \num{-2}$')

# Generate SVG:
graph_maker.write_svg()
