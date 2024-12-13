"""Measurement data helper functionality."""
from typing import Optional, Tuple, List, cast
from os import listdir
from os.path import join, isfile
import csv
import matplotlib.pyplot as plt
import numpy as np
from measurements import read_asic_2021_1 as r_a

class Helper:
    """A class containing data helper functionality."""

    _DEFAULT_DB_FOLDER = 'measurements'

    def __init__(self, chip: int, temp: int=25, sup: float=1.2, dev: Optional[str]=None,
                 baud: Optional[int]=None, verbose: bool=False, db_folder: Optional[str]=None):
        self.reader = r_a.ASICReader(dev, baud, verbose)
        self.chip = chip
        self.temp = temp
        self.sup = sup
        self.verbose = verbose
        if not db_folder:
            self._db_folder = Helper._DEFAULT_DB_FOLDER
        else:
            self._db_folder = db_folder

    @property
    def _ro_file(self) -> str:
        """This ro data file."""
        return join(self._db_folder, 'm0',
                    f'm0_chip{self.chip:d}_temp{self.temp:d}_sup{self.sup:3.1f}.csv')

    @property
    def _m1_folder(self) -> str:
        """m1 measurement folder."""
        return join(self._db_folder, 'm1')

    @property
    def _ro_file_exists(self) -> bool:
        """Does this ro data file exists."""
        return isfile(self._ro_file)

    def _print(self, text: str) -> None:
        """Print if verbose."""
        if self.verbose:
            print(text)

    def _get_ro_db(self, offset: int=2) \
        -> Tuple[List[float], List[float], List[float], List[float]]:
        """Get the RO data."""
        if not self._ro_file_exists:
            self._print(f'RO database file: {self._ro_file} does not exist!')
        ro_0_per_int = [0.0] * 256
        ro_0_per_ext = [0.0] * 256
        ro_1_per_int = [0.0] * 256
        ro_1_per_ext = [0.0] * 256
        scaler = 2**offset
        with open(self._ro_file, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            row_index = -1
            for row in reader:
                conf_index = int(row_index / 16)
                if row_index % 16 == offset:
                    ro_0_per_int[conf_index] = float(row[4]) / scaler
                    ro_0_per_ext[conf_index] = float(row[2]) / scaler
                    ro_1_per_int[conf_index] = float(row[5]) / scaler
                    ro_1_per_ext[conf_index] = float(row[3]) / scaler
                row_index += 1
        return ro_0_per_int, ro_0_per_ext, ro_1_per_int, ro_1_per_ext

    def get_ro_conf(self, ro: int, target_per: float) -> Tuple[int, int]:
        """Get RO configuration."""
        acc_length = 0.1
        db = self._get_ro_db()
        pers = [(db[ro * 2][i] + db[1 + ro * 2][i]) / 2 for i in range(256)]
        dists = [0.0] * (256 * 16)
        confs: List[Tuple[int, int]] = [(0, 0)] * (256 * 16)
        for conf in range(256):
            for sca in range(16):
                dists[conf * 16 + sca] = abs(pers[conf] * (2**sca) - target_per)
                confs[conf * 16 + sca] = (conf, sca)
        temp_sorted = sorted(zip(dists, confs))
        sorted_confs = [x for _,x in temp_sorted]
        achieved_dist = np.inf
        last_dists = [np.inf] * 10
        last_confs = [(0, 0)] * 10
        index = -1
        while (achieved_dist / target_per > 0.01) & (index + 1 < 256 * 16):
            index += 1
            candidate = sorted_confs[index]
            self._print(f'Candidate: {index}, conf: {candidate[0]}, sca: {candidate[1]}')
            conf_sca_ext = max(0, 10 - candidate[1])
            conf_sca_int = (candidate[1] - 1) % 16
            self.reader.set_en_clk(False, False)
            self.reader.set_conf(conf_sca_ext, conf_sca_int, candidate[0],
                                 conf_sca_ext, conf_sca_int, candidate[0], 1e-7)
            self.reader.reset_asic(1e-6, core=True)
            self.reader.set_en_clk(True, False)
            per_ext = self.reader.get_ro_per(ro, 1, acc_length)
            assert per_ext is not None
            self.reader.set_en_clk(False, False)
            self.reader.reset_asic(1e-6, core=True)
            self.reader.set_conf(conf_sca_ext, conf_sca_int, candidate[0],
                                 conf_sca_ext, conf_sca_int, candidate[0], 1e-7)
            cnts = self.reader.measure_ro_internal(1, acc_length, 1e-6)
            assert cnts is not None
            per_int = cast(float, acc_length / cnts[ro][0]) # type: ignore
            achieved_per = (per_ext + per_int) / 2
            achieved_dist = abs(achieved_per - target_per)
            last_dists = last_dists[1:] + [achieved_dist]
            last_confs = last_confs[1:] + [candidate]
            self._print(f'Achieved per: {achieved_per}, dist: {achieved_dist}')
            self._print(str(last_dists) + str(last_confs))
            if index >= 9:
                return sorted(zip(last_dists, last_confs))[0][1]
        return candidate

    def characterize_dc(self, nb_exp: int=100, interval_len: float=0.1,
                        visual: bool=False, conf: Optional[List[int]]=None) \
        -> Tuple[List[float], List[float], List[float], List[float]]:
        """Get the DC delays."""
        raw_data = [[0] * nb_exp, [0] * nb_exp, [0] * nb_exp, [0] * nb_exp]
        for i in range(nb_exp):
            self.reader.reset_asic(core=True, conf=True, scan=True)
            self.reader.set_conf(*conf, conf_per=1e-6) # type: ignore
            self.reader.reset_asic(core=True, scan=True)
            data = self.reader.characterize_dc(1, interval_len, 1e-7, 1e-4)
            raw_data[0][i] = data[0][0] # type: ignore
            raw_data[1][i] = data[1][0] # type: ignore
            raw_data[2][i] = data[2][0] # type: ignore
            raw_data[3][i] = data[3][0] # type: ignore
        if visual:
            im0: List[Optional[int]] = [None] * nb_exp
            im1: List[Optional[int]] = [None] * nb_exp
            for i in range(nb_exp):
                im0[i] = raw_data[0][i]
                im1[i] = raw_data[1][i]
            plt.subplot(2, 1, 1)
            plt.imshow(im0) # type: ignore
            plt.subplot(2, 1, 2)
            plt.imshow(im1) # type: ignore
            plt.show()
            plt.plot(raw_data[2])
            plt.plot(raw_data[3])
            plt.show()
            plt.plot([(raw_data[2][i] - raw_data[2][i - 1]) % (2**32) for i in range(1, nb_exp)])
            plt.plot([(raw_data[3][i] - raw_data[3][i - 1]) % (2**32) for i in range(1, nb_exp)])
            plt.show()
        #Remove bubbles:
        bub_free_0: List[List[int]] = []
        bub_free_1: List[List[int]] = []
        for i in range(nb_exp):
            bub_free_0.append(self._remove_bubbles(raw_data[0][i])) # type: ignore
            bub_free_1.append(self._remove_bubbles(raw_data[1][i])) # type: ignore
        if visual:
            im0_: List[List[int]] = []
            im1_: List[List[int]] = []
            for i in range(nb_exp):
                im0_.append(bub_free_0[i])
                im1_.append(bub_free_1[i])
            plt.subplot(2, 1, 1)
            plt.imshow(im0_) # type: ignore
            plt.subplot(2, 1, 2)
            plt.imshow(im1_) # type: ignore
            plt.show()
        #Count number of captured periods:
        nb_periods_0 = [0] * nb_exp
        nb_periods_1 = [0] * nb_exp
        for i in range(nb_exp):
            nb_periods_0[i] = self._get_nb_periods(bub_free_0[i])
            nb_periods_1[i] = self._get_nb_periods(bub_free_1[i])
        #Get edge locations:
        edge_locs_0: List[List[Tuple[int, int]]] = []
        edge_locs_1: List[List[Tuple[int, int]]] = []
        for i in range(nb_exp):
            edge_locs_0.append(self._get_edge_locs(bub_free_0[i]))
            edge_locs_1.append(self._get_edge_locs(bub_free_1[i]))
        if visual:
            im_0: List[List[List[int]]] = [[[0]] * 128 for _ in range(nb_exp)]
            im_1: List[List[List[int]]] = [[[0]] * 128 for _ in range(nb_exp)]
            for i in range(nb_exp):
                for j in range(128):
                    index0 = None
                    for k in range(len(edge_locs_0[i])):
                        if j == edge_locs_0[i][k][0]:
                            index0 = k
                            break
                    index1 = None
                    for k in range(len(edge_locs_1[i])):
                        if j == edge_locs_1[i][k][0]:
                            index1 = k
                            break
                    if index0 is not None:
                        if edge_locs_0[i][index0][1] == 1:
                            col0 = [255, 0, 0]
                        else:
                            col0 = [0, 255, 0]
                    else:
                        if bub_free_0[i][j] == 1:
                            col0 = [255, 255, 255]
                        else:
                            col0 = [0, 0, 0]
                    if index1 is not None:
                        if edge_locs_1[i][index1][1] == 1:
                            col1 = [255, 0, 0]
                        else:
                            col1 = [0, 255, 0]
                    else:
                        if bub_free_1[i][j] == 1:
                            col1 = [255, 255, 255]
                        else:
                            col1 = [0, 0, 0]
                    im_0[i][j] = col0
                    im_1[i][j] = col1
            plt.subplot(2, 1, 1)
            plt.imshow(im_0)
            plt.subplot(2, 1, 2)
            plt.imshow(im_1)
            plt.show()
        #Get edge location statistics:
        edge_p_hist_0 = [0] * 128
        edge_n_hist_0 = [0] * 128
        edge_p_hist_1 = [0] * 128
        edge_n_hist_1 = [0] * 128
        for i in range(nb_exp):
            for j in range(len(edge_locs_0[i])):
                if edge_locs_0[i][j][1] == 1:
                    edge_p_hist_0[edge_locs_0[i][j][0]] += 1
                else:
                    edge_n_hist_0[edge_locs_0[i][j][0]] += 1
            for j in range(len(edge_locs_1[i])):
                if edge_locs_1[i][j][1] == 1:
                    edge_p_hist_1[edge_locs_1[i][j][0]] += 1
                else:
                    edge_n_hist_1[edge_locs_1[i][j][0]] += 1
        if visual:
            plt.subplot(2, 1, 1)
            plt.plot(edge_p_hist_0, '-o')
            plt.plot(edge_n_hist_0, '-x')
            plt.subplot(2, 1, 2)
            plt.plot(edge_p_hist_1, '-o')
            plt.plot(edge_n_hist_1, '-x')
            plt.show()
        #Get counts in last captured period:
        w_s_0: List[Optional[int]] = [0] * nb_exp
        w_s_1: List[Optional[int]] = [0] * nb_exp
        for i in range(nb_exp):
            if len(edge_locs_0[i]) < 3:
                self._print('RO 0 period too slow, full period does not fit '
                            f'inside DC. {bub_free_0[i]}')
                w_s_0[i] = None
                w_s_1[i] = None
                continue
            if len(edge_locs_1[i]) < 3:
                self._print('RO 1 period too slow, full period does not fit '
                            f'inside DC. {bub_free_1[i]}')
                w_s_0[i] = None
                w_s_1[i] = None
                continue
            for j in range(edge_locs_0[i][0][0], edge_locs_0[i][1][0]):
                if edge_locs_0[i][0][1] == 1:
                    w_s_0[i] += edge_n_hist_0[j] # type: ignore
                else:
                    w_s_0[i] += edge_p_hist_0[j] # type: ignore
            for j in range(edge_locs_0[i][1][0], edge_locs_0[i][2][0]):
                if edge_locs_0[i][1][1] == 1:
                    w_s_0[i] += edge_n_hist_0[j] # type: ignore
                else:
                    w_s_0[i] += edge_p_hist_0[j] # type: ignore
            for j in range(edge_locs_1[i][0][0], edge_locs_1[i][1][0]):
                if edge_locs_1[i][0][1] == 1:
                    w_s_1[i] += edge_n_hist_1[j] # type: ignore
                else:
                    w_s_1[i] += edge_p_hist_1[j] # type: ignore
            for j in range(edge_locs_1[i][1][0], edge_locs_1[i][2][0]):
                if edge_locs_1[i][1][1] == 1:
                    w_s_1[i] += edge_n_hist_1[j] # type: ignore
                else:
                    w_s_1[i] += edge_p_hist_1[j] # type: ignore
        if visual:
            plt.subplot(2, 1, 1)
            plt.hist(w_s_0) # type: ignore
            plt.subplot(2,1,2)
            plt.hist(w_s_1) # type: ignore
            plt.show()
        w_0: float = np.mean([x for x in w_s_0 if x is not None]) # type: ignore
        w_1: float = np.mean([x for x in w_s_1 if x is not None]) # type: ignore
        print('W means:')
        print(f'Mean 0: {w_0}')
        print(f'Mean 1: {w_1}')
        #Measure RO periods and calculate absolute DC delays:
        d_ps_0 = [0.0] * 128
        d_ns_0 = [0.0] * 128
        d_ps_1 = [0.0] * 128
        d_ns_1 = [0.0] * 128
        self.reader.reset_asic(core=True, conf=True, scan=True)
        self.reader.set_conf(*conf, conf_per=1e-6) # type: ignore
        self.reader.reset_asic(core=True, scan=True)
        self.reader.set_en_clk(True, False)
        p0 = self.reader.get_ro_per(0, 1, 1)
        p1 = self.reader.get_ro_per(1, 1, 1)
        self.reader.set_en_clk(False, False)
        print('Measured periods:')
        print('Period 0: {p0}')
        print('Period 1: {p1}')
        assert p0 is not None
        assert p1 is not None
        for i in range(128):
            d_ps_0[i] = edge_p_hist_0[i] / w_0 * p0
            d_ns_0[i] = edge_n_hist_0[i] / w_0 * p0
            d_ps_1[i] = edge_p_hist_1[i] / w_1 * p1
            d_ns_1[i] = edge_n_hist_1[i] / w_1 * p1
        if visual:
            plt.subplot(2, 1, 1)
            plt.plot(d_ps_0, '-o')
            plt.plot(d_ns_0, '-x')
            plt.subplot(2, 1, 2)
            plt.plot(d_ps_1, '-o')
            plt.plot(d_ns_1, '-x')
            plt.show()
        return d_ps_0, d_ns_0, d_ps_1, d_ns_1

    def _get_edge_locs(self, data: List[int]) -> List[Tuple[int, int]]:
        """Get the edge locations."""
        result: List[Tuple[int, int]] = []
        for i in range(1, 128):
            if data[i] != data[i - 1]:
                result.append((i, int(data[i - 1] * 2 - 1)))
        return result

    def _get_nb_periods(self, data: List[int]) -> int:
        """Get the number of periods."""
        nb_edges = 0
        for i in range(1, 128):
            if data[i] != data[i - 1]:
                nb_edges += 1
        return (nb_edges - 1) / 2 # type: ignore

    def _remove_bubbles(self, data: List[int]) -> List[int]:
        """Remove bubbles in data."""
        result = self._remove_bubbles_old(data)
        streak = 5
        current = data[0]
        for i in range(1, 128):
            if result[i] != current:
                if streak >= 5:
                    current = result[i]
                else:
                    result[i] = current
                streak = 0
            else:
                streak += 1
        return result

    def _remove_bubbles_old(self, data: List[int]) -> List[int]:
        """Remove bubbles in data."""
        result = [x for x in data] # type: ignore
        new_block: List[int]
        for i in range(125):
            block = result[i:i + 4]
            if block == [0,0,1,0]:
                new_block = [0,0,1,1]
            elif block == [0,1,0,0]:
                new_block = [0,0,0,0]
            elif block == [0,1,0,1]:
                new_block = [0,1,1,1]
            elif block == [0,1,1,0]:
                self._print(f'Found illegal block: {data}')
                return [x for x in data]
            elif block == [1,0,0,1]:
                self._print(f'Found illegal block: {data}')
                return [x for x in data]
            elif block == [1,0,1,0]:
                new_block = [1,0,0,0]
            elif block == [1,0,1,1]:
                new_block = [1,1,1,1]
            elif block == [1,1,0,1]:
                new_block = [1,1,0,0]
            else:
                new_block = [x for x in block]
            result[i:i+4] = new_block
        return result

    def load_dc_delays(self) -> Tuple[List[float], List[float], List[float], List[float]]:
        """Load the DC delays."""
        data_files = [f for f in listdir(self._m1_folder) if isfile(join(self._m1_folder, f))]
        m1_files = [f for f in data_files if f[:2] == 'm1']
        cond_files = [f for f in m1_files if self._check_cond(f)]
        self._print(f'Found {len(cond_files)} DB files:')
        self._print('| A        | N        | C             |')
        self._print('|-------------------------------------|')
        largest = -1.0
        chosen_index = 0
        for i, cf_i in enumerate(cond_files):
            parsed = self._parse_m1_file_name(cf_i)
            self._print(f'| {parsed[4]: 8.2f} | {parsed[5]: 8d} | {parsed[6][0]: 2d}'
                        f'-{parsed[6][1]: 3d}-{parsed[6][2]: 2d}-{parsed[6][3]: 3d} |')
            if parsed[4] * parsed[5] > largest:
                chosen_index = i
                largest = parsed[4] * parsed[5]
        self._print(f'Chosen DB file: {cond_files[chosen_index]}')
        d_p_0s = [0.0] * 128
        d_n_0s = [0.0] * 128
        d_p_1s = [0.0] * 128
        d_n_1s = [0.0] * 128
        with open(join(self._m1_folder, cond_files[chosen_index]), 'r',
                  encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for row in reader:
                index = int(row[0])
                d_p_0s[index] = float(row[1])
                d_n_0s[index] = float(row[2])
                d_p_1s[index] = float(row[3])
                d_n_1s[index] = float(row[4])
        return (d_p_0s, d_n_0s, d_p_1s, d_n_1s)

    def _check_cond(self, file_name: str) -> bool:
        """Check if m1 file matches."""
        parsed = self._parse_m1_file_name(file_name)
        return (parsed[1] == self.chip) & (parsed[2] == self.temp) & (parsed[3] == self.sup)

    def _parse_m1_file_name(self, file_name: str) \
        -> Tuple[int, int, float, float, float, int, List[int]]:
        """Parse m1 file name."""
        parts = file_name.split('_')
        m = int(parts[0][1:])
        c = int(parts[1][4:])
        t = float(parts[2][4:])
        s = float(parts[3][3:])
        a = float(parts[4][3:])
        n = int(parts[5][3:])
        c_parts = parts[6][4:].split('-')
        c_parts[-1] = c_parts[-1].split('.')[0]
        co = [int(p) for p in c_parts]
        return (m, c, t, s, a, n, co)

    def get_phase_v1(self, dc: List[int], ro_per: float, ro: int) -> float:
        """Get the phase from the DC sample."""
        dc = self._remove_bubbles(dc)
        delays = self.load_dc_delays()[2 * ro + 1]
        neg_edge_delays: List[float] = []
        for i in range(127):
            if (dc[i] == 0) & (dc[i + 1] == 1):
                delay = 0.0
                for j in range(i + 1):
                    delay += delays[j]
                delay -= ro_per * len(neg_edge_delays)
                neg_edge_delays.append(delay)
        return np.median(neg_edge_delays) / ro_per # type: ignore

    def process_phases(self, phases: List[float]) -> List[float]:
        """Process the phases."""
        result = [x for x in phases] # type: ignore
        middle_phase = np.median(phases)
        for i, p_i in enumerate(phases):
            if abs(p_i - middle_phase) > 0.5:
                if p_i > middle_phase:
                    result[i] = p_i - 1
                else:
                    result[i] = p_i + 1
        return result

    def get_phase(self, dc: List[int], cnt: int, ro_per: float, ro: int) -> float:
        """Get the phase from the DC sample."""
        dc = self._remove_bubbles(dc)
        nb_neg_edges = cnt
        last_neg_edge: Optional[int] = None
        for i in range(127, 0, -1):
            if (dc[i] == 1) & (dc[i-1] == 0):
                nb_neg_edges += 1
                last_neg_edge = i
        delays = self.load_dc_delays()[ro * 2 + 1]
        time = 0.0
        assert last_neg_edge is not None
        for i in range(0, last_neg_edge):
            time += delays[i]
        return nb_neg_edges + time / ro_per

    def get_total_phase(self, dc: List[int], cnt: int, ro_per: float,
                        ro: int, conf_freq_sca_ext: int) -> float:
        """Get the total phase."""
        init_phase = self.get_phase_v1(dc, ro_per, ro)
        dc = self._remove_bubbles(dc)
        nb_neg_edges = 0
        for i in range(127):
            if (dc[i] == 0) & (dc[i+1] == 1):
                nb_neg_edges += 1
        if conf_freq_sca_ext != 15:
            return init_phase + cnt + nb_neg_edges
        return init_phase + cnt + nb_neg_edges - 0.5
