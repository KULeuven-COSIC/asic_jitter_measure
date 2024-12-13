"""Sweep accumulation time, measure phases multiple times to estimate noise contributions."""
from typing import List
import sys
from os import getcwd
from os.path import join
import traceback
import math
import numpy as np
import matplotlib.pyplot as plt
sys.path.append(getcwd())
from measurements import helper as h_p # pylint: disable=wrong-import-position
from measurements import file_manager as f_m # pylint: disable=wrong-import-position
from lib import time_logger as t_l # pylint: disable=wrong-import-position

CHIP = 4
TEMP = 15
SUP = 1.2
dev = join('/dev', 'ttyUSB1')

CONF = (15, 0, 15, 0)

ACC_POWERS = range(-8, 0)
NB_SAMPLES = 100
VERBOSE = False
WINDOW = 10
NB_WINDOWS = int(NB_SAMPLES / WINDOW)

acc_lengths: List[float] = []
for pi in ACC_POWERS:
    for ti in range(1, 10):
        if (pi <= -8) & (ti <= 2):
            continue
        if (pi >= -1) & (ti >= 4):
            continue
        acc_lengths.append(ti * 10**pi)
print(f'Measure the following accumulation times: {acc_lengths}')

data_file_name = join('measurements', 'm3',
                      f'm3_chip{CHIP:d}_temp{TEMP:d}_sup{SUP:3.1f}_num{NB_SAMPLES}'
                      f'_conf{CONF[0]:d}-{CONF[1]:d}-{CONF[2]:d}-{CONF[3]}.csv')
file_manager = f_m.FileManager(data_file_name)
col_titles = ['Exp', 'Acc length [s]', 'ro0Per [s]', 'ro1Per [s]', 'phases0 (norm) [-]',
              'phases1 (norm) [-]', 'oldPhases0 (norm) [-]', 'oldPhases1 (norm) [-]']
if not file_manager.init_file(col_titles):
    sys.exit()

a = h_p.Helper(CHIP, temp=TEMP, sup=SUP, dev=dev, verbose=False)

logger = t_l.TimeLogger(len(acc_lengths))
logger.start()

a.reader.boot_pots()
for index, acc_len in enumerate(acc_lengths):
    a.reader.set_conf(max(0, 10 - ((CONF[0] + 1) % 16)), CONF[0], CONF[1],
                      max(0, 10 - ((CONF[2] + 1) % 16)), CONF[2], CONF[3], 1e-6)
    a.reader.set_en_clk(True, False)
    ro_0_per = a.reader.get_ro_per(0, 1, 1)
    ro_1_per = a.reader.get_ro_per(1, 1, 1)
    a.reader.set_en_clk(False, False)
    all_good = False # pylint: disable=invalid-name
    block_means_0: List[float] = []
    block_means_1: List[float]
    phases0: List[float]
    phases1: List[float]
    cnts0: List[int]
    cnts1: List[int]
    while not all_good:
        if len(block_means_0) < 4:
            phases0 = [0.0] * (WINDOW * NB_WINDOWS)
            phases1 = [0.0] * (WINDOW * NB_WINDOWS)
            cnts0 = [0] * (WINDOW * NB_WINDOWS)
            cnts1 = [0] * (WINDOW * NB_WINDOWS)
            block_means_0 = []
            block_means_1 = []
        all_good = True # pylint: disable=invalid-name
        wi = len(block_means_0)
        while wi < NB_WINDOWS:
            logger.log(f'WINDOW: {wi}')
            a.reader.set_conf(max(0, 10 - ((CONF[0] + 1) % 16)), CONF[0], CONF[1],
                              max(0, 10 - ((CONF[2] + 1) % 16)), CONF[2], CONF[3], 1e-6)
            a.reader.reset_asic(1e-3, core=True)
            data = a.reader.accumul_jitter(WINDOW, acc_len=acc_len, pulse_len=1e-6, scan_per=1e-7)
            block_phases_0 = [a.get_total_phase(data[0][i], data[2][i], ro_0_per, # type: ignore
                                                0, CONF[0]) for i in range(WINDOW)]
            block_phases_1 = [a.get_total_phase(data[1][i], data[3][i], ro_1_per, # type: ignore
                                                1, CONF[2]) for i in range(WINDOW)]
            if len(block_means_0) > 0:
                if (abs(np.median(block_phases_0) - np.median(block_means_0)) \
                    / np.median(block_means_0) > 0.004) | (math.isnan(np.median(block_phases_0))):
                    logger.log('Found wrong median 0')
                    all_good = False # pylint: disable=invalid-name
                    break
                if (abs(np.median(block_phases_1) - np.median(block_means_1)) \
                    / np.median(block_means_1) > 0.004) | (math.isnan(np.median(block_phases_1))):
                    logger.log('Found wrong median 1')
                    all_good = False # pylint: disable=invalid-name
                    break
            block_means_0 += [np.median(block_phases_0)] # type: ignore
            block_means_1 += [np.median(block_phases_1)] # type: ignore
            phases0[wi * WINDOW:(wi + 1) * WINDOW] = block_phases_0 # type: ignore
            phases1[wi * WINDOW:(wi + 1) * WINDOW] = block_phases_1 # type: ignore
            cnts0[wi * WINDOW:(wi + 1) * WINDOW] = data[2] # type: ignore
            cnts1[wi * WINDOW:(wi + 1) * WINDOW] = data[3] # type: ignore
            wi += 1

    old_phases0 = [x for x in phases0]
    old_phases1 = [x for x in phases1]
    bin_width = 1 # pylint: disable=invalid-name
    for i in range(WINDOW * NB_WINDOWS):
        try:
            phases0[i] = phases0[i] % 1 + int(np.median(old_phases0))
        except: # pylint: disable=bare-except
            print(old_phases0)
            traceback.print_exc()
        while abs(phases0[i] - np.median(old_phases0)) > bin_width / 2:
            if phases0[i] < np.median(old_phases0):
                phases0[i] += 1
            else:
                phases0[i] -= 1
        try:
            phases1[i] = phases1[i]%1 + int(np.median(old_phases1))
        except: # pylint: disable=bare-except
            print(old_phases1)
            traceback.print_exc()
        while abs(phases1[i] - np.median(old_phases1)) > bin_width / 2:
            if phases1[i] < np.median(old_phases1):
                phases1[i] += 1
            else:
                phases1[i] -= 1
    if VERBOSE:
        plt.subplot(2, 1, 1)
        plt.plot(phases0, 'o-', alpha=0.4)
        plt.plot(old_phases0, 'o-', alpha=0.4)
        plt.plot(cnts0, 'o-', alpha=0.4)
        plt.subplot(2, 1, 2)
        plt.plot(phases1, 'o-', alpha=0.4)
        plt.plot(old_phases1, 'o-', alpha=0.4)
        plt.plot(cnts1, 'o-', alpha=0.4)
        plt.show()
    file_manager.append([index, acc_len, ro_0_per, ro_1_per, phases0, phases1,
                         old_phases0, old_phases1])
    logger.iterate()
logger.log('')
