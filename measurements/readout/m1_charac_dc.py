"""Characterise DCs using a Monte Carlo method."""
import sys
import csv
from os import getcwd
from os.path import join, isfile
sys.path.append(getcwd())
from measurements import helper as h_p # pylint: disable=wrong-import-position


CHIP = 4
TEMP = 15
SUP = 1.2
dev = join('/dev', 'ttyUSB1')

CONF = (15, 0, 15, 0)

ACC_LENGTH = 1
NB_SAMPLES = 1000

data_file_name = join('measurements', 'm1',
                      f'm1_chip{CHIP:d}_temp{TEMP:d}_sup{SUP:3.1f}_acc{ACC_LENGTH}'
                      f'_num{NB_SAMPLES:d}_conf{CONF[0]:d}-{CONF[1]:d}-{CONF[2]:d}'
                      f'-{CONF[3]:d}.csv')

if isfile(data_file_name):
    print(f'File: {data_file_name} already exists!')
    sys.exit()
with open(data_file_name, 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['Stage', 'dP0 [s]', 'dN0 [s]', 'dP1 [s]', 'dN1 [s]'])

a = h_p.Helper(CHIP, temp=TEMP, sup=SUP, dev=dev, verbose=False)
a.reader.boot_pots()
a.reader.reset_asic(core=True, conf=True, scan=True)
a.reader.set_conf(max(0, 10 - ((CONF[0] + 1) % 16)), CONF[0], CONF[1],
                  max(0, 10 - ((CONF[2] + 1) % 16)), CONF[2], CONF[3], 1e-6)
a.reader.reset_asic(core=True, scan=True)
data = a.characterize_dc(nb_exp=NB_SAMPLES, interval_len=ACC_LENGTH, visual=True,
                         conf=[max(0, 10 - ((CONF[0] + 1) % 16)), CONF[0], CONF[1],
                               max(0, 10 - ((CONF[2] + 1) % 16)), CONF[2], CONF[3]])

with open(data_file_name, 'a', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    for i in range(128):
        writer.writerow([i, data[0][i], data[1][i], data[2][i], data[3][i]])
