"""Generate flicker FM noise estimation error figure."""
import argparse
import math
import sys
import os
from typing import List
import numpy as np
from scipy.special import sici # type: ignore # pylint: disable=no-name-in-module
sys.path.append(os.getcwd())
from lib import graph_maker as g_m # pylint: disable=wrong-import-position

TMIN = 1e-9
TMAX = 1
YMIN = 1e-16
YMAX = 1e-4

F_H = 10e9
F_L = 1e-3

EM: float = 0.57721566490153286060

parser = argparse.ArgumentParser()
parser.add_argument('-v', help='Print process', action='store_true')
parser.add_argument('-d', help='Collect data', action='store_true')
parser.add_argument('-q', help='Quit after data collect', action='store_true')
args = parser.parse_args()

if args.d:
    if args.q:
        sys.exit()

def phi_original(t: float) -> float:
    """Original phi."""
    result = -(math.sin(math.pi*F_H*t))**2/(2*(math.pi*F_H*t)**2)
    result -= (math.sin(2*math.pi*F_H*t))/(2*math.pi*F_H*t) 
    result += sici(2*math.pi*F_H*t)[1] + (math.sin(math.pi*F_L*t))**2/(2*(math.pi*F_L*t)**2)
    result += (math.sin(2*math.pi*F_L*t))/(2*math.pi*F_L*t) - sici(2*math.pi*F_L*t)[1]
    return result

def phi_simple(t: float) -> float:
    """Simplified phi."""
    result = 3/2 - EM - math.log(2*math.pi*F_L*t)
    return result

ts: List[float] = []
for e in range(int(np.ceil(np.log10(TMAX/TMIN)))):
    for ti in range(1, 10):
        ts += [ti * 10**e * TMIN]
y_orig = [phi_original(ti) for ti in ts]
y_simple = [phi_simple(ti) for ti in ts]

rel_diff = [abs(o - s) / o for o, s in zip(y_orig, y_simple)]

graph_maker = g_m.GraphMaker('flicker_fm_est.svg', figure_size=(1, 1), folder_name='figures')
graph_maker.create_grid(size=(1, 1), marg_left=0.12)

ax = graph_maker.create_ax(0, 0, # pylint: disable=invalid-name
                           title='Relative variance difference',
                           x_label='Accumulation time',
                           y_label='Relative difference',
                           x_unit = 's',
                           y_unit= '-',
                           x_scale='log10',
                           y_scale='log10',
                           x_grid=True,
                           y_grid=True,
                           x_lim=(TMIN, TMAX),
                           y_lim=(YMIN, YMAX),
                           max_nb_y_ticks=8)

# Plot data:
graph_maker.plot(ax, xs=ts, ys=rel_diff)

# Generate SVG:
graph_maker.write_svg()
