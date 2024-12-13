"""Generate measured accumulation time variance figure."""
import argparse
import sys
import os
sys.path.append(os.getcwd())
from typing import List # pylint: disable=wrong-import-position
from lib import graph_maker as g_m # pylint: disable=wrong-import-position

DS: List[float] = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
VARS: List[float] = [0.48e-18, 0.2e-18, 0.1e-18, 0.28e-18, 0.09e-18, 0.04e-18, 0.09e-18]

parser = argparse.ArgumentParser()
parser.add_argument('-v', help='Print process', action='store_true')
parser.add_argument('-d', help='Collect data', action='store_true')
parser.add_argument('-q', help='Quit after data collect', action='store_true')
args = parser.parse_args()

if args.d:
    if args.q:
        sys.exit()

if args.v:
    print(f'Delays: {DS}')
    print(f'Vars: {VARS}')

graph_maker = g_m.GraphMaker('acc_time_var.svg', figure_size=(1, 1), folder_name='figures')
graph_maker.create_grid(size=(1, 1), marg_left=0.12)

ax = graph_maker.create_ax(0, 0, # pylint: disable=invalid-name
                           title='Accumulation time variance',
                           x_label='Accumulation time',
                           y_label='Timing variance',
                           x_unit = 's',
                           y_unit=r's\textsuperscript{2}',
                           x_scale='log10',
                           y_scale='log10',
                           x_grid=True,
                           y_grid=True)

# Plot data:
graph_maker.plot(ax, xs=DS, ys=VARS, marker='circle')

# Generate SVG:
graph_maker.write_svg()
