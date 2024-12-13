"""ASIC readout script."""
from typing import Optional, Union, List, Tuple
try:
    import serial # type: ignore
except ModuleNotFoundError:
    print('Serial import failed')
from os.path import join
import time
import matplotlib.pyplot as plt
import numpy as np

# Unless otherwise noted, units of time are always s.
# This script is to be used with FPGA project: "ASIC2021_1_Readout_JIT"

class ASICReader:
    """ASIC readout class."""

    def __init__(self, dev: Optional[str]=None, baud: Optional[int]=None,
                 verbose: bool=False, period: float=500e-9):
        if dev is None:
            self.dev = join('/dev', 'ttyUSB1')
        else:
            self.dev = dev
        if baud is None:
            self.baud = 115200
        else:
            self.baud = baud
        self.verbose = verbose
        self.per = period
        if self.dev != '0':
            self.ser = serial.Serial(self.dev, self.baud)
        self.scope_per: Optional[float] = None
        self.signals: Optional[List[int]] = None
        self.nb_scope_samples: Optional[int] = None
        self.signal_names = ['All 0', 'All 1', 'SCAN_OUT', 'RO_OUT0', 'RO_OUT1',
                             'CONF_IN', 'CONF_CLK', 'CONF_RST', 'SCAN_SER',
                             'SCAN_CLK', 'SCAN_RST', 'CORE_RST', 'RO_ENABLE',
                             'DC_CLK']
        self.current_conf: Optional[Tuple[int, int, int, int, int, int]] = None

    def _print(self, txt: str) -> None:
        """Print if verbose."""
        if self.verbose:
            print(txt)

    def _write(self, bys: List[int]) -> None:
        self._print(f'Write {len(bys)} bytes: [{bys}]')
        self.ser.write(bytes(bys))

    def _read(self, number: int, timeout: Optional[float]=None, error_pos: bool=False) \
        -> Optional[List[int]]:
        nb_received = 0
        result: List[int] = []
        last_time = time.time()
        prev_nb_received = 0
        while nb_received < number:
            waiting = self.ser.in_waiting
            data = [x for x in self.ser.read(min(number - nb_received, waiting))] # pylint: disable=unnecessary-comprehension
            if error_pos:
                if not nb_received:
                    if data is not None:
                        if len(data) > 0:
                            if data[0] == 255:
                                self._print('Error received during scan out')
                                data = data[1:]
            result += data
            final_result = self._remove_escape(result)
            nb_received = len(final_result)
            if nb_received == prev_nb_received:
                time_diff = time.time() - last_time
                if timeout is not None:
                    if time_diff >= timeout:
                        self._print('Read timeout')
                        return None
            else:
                prev_nb_received = nb_received
                last_time = time.time()
        self._print(f'Read {len(final_result)} bytes: [{[x for x in final_result]}]') # pylint: disable=unnecessary-comprehension
        return final_result

    def _remove_escape(self, bys: List[int]) -> List[int]:
        if len(bys) < 1:
            return bys
        result = [bys[0]]
        i = 1
        while i < len(bys):
            if bys[i] == 1:
                i += 2
                if i - 1 < len(bys):
                    result.append(bys[i-1])
                continue
            result.append(bys[i])
            i += 1
        return result

    def clear_uart_buffers(self) -> None:
        """Keep reading untill buffers are empty."""
        while self.ser.in_waiting > 0:
            self.ser.read()

    def set_scope(self, signal0: int, signal1: int, signal2: int, signal3: int,
                  trigger: int, sample_per: float, nb_samples: int) -> None:
        """
        - Signals: 0: all zero, 1: all one, 2: SCAN_OUT, 3: RO_OUT0, 4: RO_OUT1,
                   5: CONF_IN, 6: CONF_CLK, 7: CONF_RST, 8: SCAN_SER, 9: SCAN_CLK,
                   10: SCAN_RST, 11: CORE_RST, 12: RO_ENABLE, 13: DC_CLK.
        - Trigger: 0 and 1: trigger now, rest: same as signals
        - sample_per: sample period [s]
        - nb_samples: number of samples (max 32 768)
        """
        if (signal0 < 0) | (signal0 > 13):
            self._print(f'signal0 out of range: {signal0}')
            return
        if (signal1 < 0) | (signal1 > 13):
            self._print(f'signal1 out of range: {signal1}')
            return
        if (signal2 < 0) | (signal2 > 13):
            self._print(f'signal2 out of range: {signal2}')
            return
        if (signal3 < 0) | (signal3 > 13):
            self._print(f'signal3 out of range: {signal3}')
            return
        if (trigger < 0) | (trigger > 13):
            self._print(f'trigger out of range: {trigger}')
            return
        if (sample_per < 10e-9) | (sample_per > (2**32 - 1) * 10e-9):
            self._print(f'sample period out of range: {sample_per}')
            return
        if (nb_samples < 0) | (nb_samples > 4 * 2**13):
            self._print(f'Number of samples out of range: {nb_samples}')
            return
        if nb_samples % 2 != 0:
            self._print('Number of samples should be even')
            return
        self.scope_per = sample_per
        self.signals = [signal0, signal1, signal2, signal3]
        sample_per = int(sample_per / 10e-9 + 0.5)
        self.nb_scope_samples = nb_samples
        self._write([5, signal3, signal2, signal1, signal0, trigger, int(sample_per / 256**3),
                     int(sample_per / 256**2) % 256, int(sample_per / 256) % 256,
                     sample_per % 256, int(nb_samples / 256**3), int(nb_samples / 256**2) % 256,
                     int(nb_samples / 256) % 256, nb_samples % 256])

    def _get_scope(self) -> Optional[List[Optional[int]]]:
        scope_window = 1024
        if self.nb_scope_samples is None:
            self._print('First setup scope by running: \'set_scope(...)\'')
            return None
        self.clear_uart_buffers()
        self._write([6])
        times = int(np.floor((self.nb_scope_samples / 2 + 2) / scope_window))
        last_window = (int(self.nb_scope_samples / 2 + 2)) % scope_window
        data: List[Optional[int]] = []
        for _ in range(times):
            data += self._read(scope_window) # type: ignore
        data += self._read(last_window) # type: ignore
        self.nb_scope_samples = None
        return data

    def plot_scope(self) -> None:
        """Plot the scope output."""
        data = self._get_scope()
        if data is None:
            return
        assert self.scope_per is not None
        assert self.signals is not None
        s0 = []
        s1 = []
        s2 = []
        s3 = []
        t = []
        time_ = 0.0
        data = data[1:-1]
        for d_i in data:
            for j in range(2):
                d = int(d_i / 16**(1 - j)) % 16
                s0 += [d % 2]
                s1 += [int(d / 2) % 2]
                s2 += [int(d / 4) % 2]
                s3 += [int(d / 8)]
                t += [time_]
                time_ += self.scope_per
        leg = []
        plt.plot(t, [4.5 + x for x in s0])
        leg += [self.signal_names[self.signals[0]]]
        plt.plot(t, [3+x for x in s1])
        leg += [self.signal_names[self.signals[1]]]
        plt.plot(t, [1.5+x for x in s2])
        leg += [self.signal_names[self.signals[2]]]
        plt.plot(t, [0+x for x in s3])
        leg += [self.signal_names[self.signals[3]]]
        plt.legend(leg)
        plt.show()

    def reset_scope(self) -> None:
        """Reset the scope."""
        self._get_scope()

    def read_scan(self, scan_per: Optional[float]=None) \
        -> Optional[Tuple[List[int], List[int], int, int]]:
        """Read out scan chain."""
        if scan_per is None:
            scan_per = self.per
        if (scan_per < 0) | (scan_per > (2**32-1)*10e-9):
            self._print(f'Scan period out of range: {scan_per}')
            return None
        est_time = 320 * scan_per * 1.5 + 0.1
        scan_per = int(scan_per / 10e-9 + 0.5)
        self._write([2, int(scan_per / 256**3), int(scan_per / 256**2) % 256,
                     int(scan_per / 256) % 256, scan_per % 256])
        data = self._read(42, est_time, True)
        if data is None:
            self._print(f'Scan returned invalid response: {data}')
            return None
        if (data[0] != 5) | (data[-1] != 0):
            self._print(f'Scan returned invalid response: {data}')
            return None
        data = data[1:-1]
        dc_0_cnt_array = data[20:24]
        dc_1_cnt_array = data[0:4]
        dc_0_dc_array = data[24:40]
        dc_1_dc_array = data[4:20]
        dc_0_cnt = 0
        dc_1_cnt = 0
        for i in range(4):
            dc_0_cnt *= 256
            dc_0_cnt += dc_0_cnt_array[i]
            dc_1_cnt *= 256
            dc_1_cnt += dc_1_cnt_array[i]
        dc_0 = [0] * 128 #dc_0[0] is bit closest to RO, dc_0[127] is bit closest to cnt.
        dc_1 = [0] * 128
        for i in range(16):
            dc_0_by = dc_0_dc_array[15 - i]
            dc_1_by = dc_1_dc_array[15 - i]
            for j in range(8):
                dc_0[i * 8 + j] = (dc_0_by >> j) % 2
                dc_1[i * 8 + j] = (dc_1_by >> j) % 2
        return (dc_0, dc_1, dc_0_cnt, dc_1_cnt)

    def measure_ro(self, which_ro: Union[int, float], nb_samples: Union[int, float],
                   interval_len: float=1e-3) -> Optional[Tuple[float, float]]:
        """Measure the RO period and period variance."""
        if (which_ro < 0) | (which_ro > 1):
            self._print(f'Invalid RO selected: {which_ro}')
            return None
        which_ro = int(which_ro + 0.5)
        if (nb_samples <= 0) | (nb_samples >= 2**32):
            self._print(f'Number samples out of range: {nb_samples}')
            return None
        nb_samples = int(nb_samples)
        if (interval_len <= 0) | (interval_len > (2**32 - 1) * 10e-9):
            self._print(f'Interval length out of range: {interval_len}')
        est_time = interval_len * nb_samples * 1.5 + 0.1
        interval_len = int(interval_len / 10e-9 + 0.5)
        self._write([0, int(nb_samples / 256**3), int(nb_samples / 256**2) % 256,
                     int(nb_samples / 256) % 256, nb_samples % 256,
                     int(interval_len / 256**3), int(interval_len / 256**2) % 256,
                     int(interval_len / 256) % 256, interval_len % 256, which_ro])
        data = self._read(2 + 4 * nb_samples, est_time)
        if data is None:
            self._print(f'RO measure returned invalid response: {data}')
            return None
        if (data[0] != 2) | (data[-1] != 0):
            self._print(f'RO measure returned invalid response: {data}')
            return None
        data = data[1:-1]
        cnts = [0] * nb_samples
        for i in range(nb_samples):
            bys = data[i * 4:i * 4 + 4]
            for j in range(4):
                cnts[i] *= 256
                cnts[i] += bys[j]
        pers = [0.0] * nb_samples
        for i in range(nb_samples):
            if cnts[i] == 0:
                return (0.0, 0.0)
            pers[i] = 10e-9*interval_len/cnts[i]
        return (10e-9 * interval_len / np.mean(cnts), np.std(pers)) # type: ignore

    def get_ro_per(self, which_ro: int, nb_samples: int=10, interval_len: float=1e-3) \
        -> Optional[float]:
        """
        This method takes into account the current configuration and scales the measured
        period length accordingly.
        """
        if self.current_conf is None:
            self._print('First set the ASIC configuration before running this method.')
            return None
        periods = self.measure_ro(which_ro, nb_samples, interval_len)
        assert periods is not None
        period = periods[0]
        if period == 0:
            self._print('Measured frequency: 0 Hz')
            return 0
        self._print(f'Measured frequency: {1 / period / 1e6} MHz')
        period /= 2**(9 + self.current_conf[3 * which_ro])
        self._print(f'Clock frequency: {1 / period / 1e6} MHz')
        if self.current_conf[3 * which_ro + 1] != 15:
            internal_period = period / (2**(1 + self.current_conf[3 * which_ro + 1]))
        else:
            internal_period = period
        self._print(f'Actual RO frequency: {1 / internal_period / 1e6} MHz')
        return period

    def reset_asic(self, pulse_len: Optional[float]=None, conf: bool=False,
                   scan: bool=False, core: bool=False) -> None:
        """Reset the ASIC."""
        if pulse_len is None:
            pulse_len = self.per
        if (pulse_len <= 0) | (pulse_len > (2**32 - 1) * 10e-9):
            self._print(f'Pulse length out of range: {pulse_len}')
            return
        est_time = pulse_len * 1.5 + 0.1
        pulse_len = int(pulse_len / 10e-9 + 0.5)
        self._write([1, core * 4 + scan * 2 + conf * 1, int(pulse_len / 256**3),
                     int(pulse_len / 256**2) % 256, int(pulse_len / 256) % 256,
                     pulse_len % 256])
        data = self._read(1, est_time)
        if data is None:
            self._print(f'Reset returned invalid response: {data}')
            return
        if data[0] != 0:
            self._print('Reset returned invalid response: {data}')
            return
        return

    def proceed(self) -> None:
        """Send proceed."""
        self._write([7])

    def set_conf(self, dc_0_freq_sca_ext: Union[int, float], dc_0_freq_sca_int: Union[int, float],
                 dc_0_inv_strength: Union[int, float],
                 dc_1_freq_sca_ext: Union[int, float], dc_1_freq_sca_int: Union[int, float],
                 dc_1_inv_strength: Union[int, float],
                 conf_per: Optional[float]=None) -> None:
        """Set the configuration."""
        if conf_per is None:
            conf_per = self.per
        if (conf_per <= 0) | (conf_per > (2**32 - 1) * 10e-9):
            self._print(f'Conf period out of range: {conf_per}')
            return
        est_time = 32 * conf_per + 0.1
        conf_per = int(conf_per / 10e-9 + 0.5)
        if (dc_0_freq_sca_ext < 0) | (dc_0_freq_sca_ext > 15):
            self._print('External frequency scaler 0 configuration out of '
                        f'range: {dc_0_freq_sca_ext}')
            return
        dc_0_freq_sca_ext = int(dc_0_freq_sca_ext)
        if (dc_0_freq_sca_int < 0) | (dc_0_freq_sca_int > 15):
            self._print('Internal frequency scaler 0 configuration out of '
                        f'range: {dc_0_freq_sca_int}')
            return
        dc_0_freq_sca_int = int(dc_0_freq_sca_int)
        if (dc_1_freq_sca_ext < 0) | (dc_1_freq_sca_ext > 15):
            self._print('External frequency scaler 1 configuration out of '
                        f'range: {dc_1_freq_sca_ext}')
            return
        dc_1_freq_sca_ext = int(dc_1_freq_sca_ext)
        if (dc_1_freq_sca_int < 0) | (dc_1_freq_sca_int > 15):
            self._print('Internal frequency scaler 1 configuration out of '
                        f'range: {dc_1_freq_sca_int}')
            return
        dc_1_freq_sca_int = int(dc_1_freq_sca_int)
        if (dc_0_inv_strength < 0) | (dc_0_inv_strength > 255):
            self._print('Inverter drive strength 0 configuration out of '
                        f'range: {dc_0_inv_strength}')
            return
        dc_0_inv_strength = int(dc_0_inv_strength)
        if (dc_1_inv_strength < 0) | (dc_1_inv_strength > 255):
            self._print('Inverter drive strength 1 configuration out of '
                        f'range: {dc_1_inv_strength}')
            return
        dc_1_inv_strength = int(dc_1_inv_strength)
        self.clear_uart_buffers()
        self._write([3, int(conf_per / 256**3), int(conf_per / 256**2)%256,
                     int(conf_per / 256)%256, conf_per % 256,
                     dc_1_freq_sca_ext * 16 + dc_1_freq_sca_int, dc_1_inv_strength,
                     dc_0_freq_sca_ext * 16 + dc_0_freq_sca_int, dc_0_inv_strength])
        data = self._read(1, est_time)
        if data is None:
            self._print(f'Configure returned invalid response: {data}')
            return None
        if data[0] != 0:
            self._print(f'Configure returned invalid response: {data}')
            return None
        self.current_conf = (dc_0_freq_sca_ext, dc_0_freq_sca_int, dc_0_inv_strength,
                             dc_1_freq_sca_ext, dc_1_freq_sca_int, dc_1_inv_strength)

    def measure_ro_internal(self, nb_samples: Union[int, float], interval_len: float=1e-3,
                            scan_per: Optional[float]=None) \
        -> Optional[Tuple[List[Optional[int]], List[Optional[int]]]]:
        """measure RO internal counters."""
        if (nb_samples <= 0) | (nb_samples >= 2**32):
            self._print(f'Number samples out of range: {nb_samples}')
            return None
        nb_samples = int(nb_samples)
        if (interval_len <= 0) | (interval_len > (2**32 - 1) * 10e-9):
            self._print(f'Interval length out of range: {interval_len}')
            return None
        est_time = interval_len * 1.5 + 0.1
        interval_len = int(interval_len / 10e-9 + 0.5)
        self.clear_uart_buffers()
        self._write([4, 0, int(interval_len / 256**3), int(interval_len / 256**2) % 256,
                     int(interval_len / 256) % 256, interval_len % 256, int(nb_samples / 256**3),
                     int(nb_samples / 256**2) % 256, int(nb_samples / 256) % 256,
                     nb_samples % 256, 0, 0, 0, 0])
        dc_0_cnts: List[Optional[int]] = [0] * nb_samples
        dc_1_cnts: List[Optional[int]] = [0] * nb_samples
        for i in range(nb_samples):
            data = self._read(1, est_time)
            if data is None:
                self._print(f'Measure RO {i + 1} returned invalid response: {data}')
                return None
            if data[0] != 3:
                self._print(f'Measure RO {i + 1} returned invalid response: {data}')
                return None
            if i == nb_samples - 1:
                data = self._read(1, est_time)
                if data is None:
                    self._print(f'Measure RO did not finish properly: {data}')
                else:
                    if data[0] != 0:
                        self._print(f'Measure RO did not finish properly: {data}')
            scan_out = self.read_scan(scan_per)
            if scan_out is None:
                self._print(f'Scan {i + 1} returned invalid response: {scan_out}')
                dc_0_cnts[i] = None
                dc_1_cnts[i] = None
            else:
                dc_0_cnts[i] = scan_out[2]
                dc_1_cnts[i] = scan_out[3]
            self._write([7])
        return (dc_0_cnts, dc_1_cnts)

    def characterize_dc(self, nb_samples: int, interval_len: float=1e-3,
                        pulse_len: float=1e-6, scan_per: Optional[float]=None) \
        -> Optional[Tuple[List[Optional[List[int]]], List[Optional[List[int]]],
                          List[Optional[int]], List[Optional[int]]]]:
        """Characterize the DCs."""
        if (nb_samples <= 0) | (nb_samples >= 2**32):
            self._print(f'Number samples out of range: {nb_samples}')
            return None
        nb_samples = int(nb_samples)
        if (interval_len <= 0) | (interval_len > (2**32 - 1) * 10e-9):
            self._print(f'Interval length out of range: {interval_len}')
            return None
        est_time = interval_len * 1.5 + 0.1
        if (pulse_len <= 0) | (pulse_len > (2**32 - 1) * 10e-9):
            self._print(f'Pulse length out of range: {pulse_len}')
            return None
        if pulse_len > interval_len:
            self._print('WARNING: pulse length > interval length')
        if scan_per is None:
            scan_per = self.per
        if pulse_len + 320 * scan_per > interval_len:
            self._print('WARNING: pulse length added with scan time > interval length')
        interval_len = int(interval_len / 10e-9 + 0.5)
        pulse_len = int(pulse_len / 10e-9 + 0.5)
        self.clear_uart_buffers()
        self._write([4, 1, int(pulse_len / 256**3), int(pulse_len / 256**2) % 256,
                     int(pulse_len / 256) % 256, pulse_len % 256, int(nb_samples / 256**3),
                     int(nb_samples / 256**2) % 256, int(nb_samples / 256) % 256,
                     nb_samples % 256, int(interval_len / 256**3), int(interval_len / 256**2) % 256,
                     int(interval_len / 256) % 256, interval_len % 256])
        dc_0_dcs: List[Optional[List[int]]] = [None] * nb_samples
        dc_1_dcs: List[Optional[List[int]]] = [None] * nb_samples
        dc_0_cnts: List[Optional[int]] = [0] * nb_samples
        dc_1_cnts: List[Optional[int]] = [0] * nb_samples
        for i in range(nb_samples):
            data = self._read(1, est_time)
            if data is None:
                self._print(f'Characterise DC {i + 1} returned invalid response: {data}')
                return None
            if data[0] != 3:
                self._print(f'Characterise DC {i + 1} returned invalid response: {data}')
                return None
            if i == nb_samples - 1:
                data = self._read(1, est_time)
                if data is None:
                    self._print(f'Characterise DC did not finish properly: {data}')
                else:
                    if data[0] != 0:
                        self._print(f'Characterise DC did not finish properly: {data}')
            scan_out = self.read_scan(scan_per)
            if scan_out is None:
                self._print(f'Scan {i + 1} returned invalid response: {scan_out}')
                dc_0_dcs[i] = None
                dc_1_dcs[i] = None
                dc_0_cnts[i] = None
                dc_1_cnts[i] = None
            else:
                dc_0_dcs[i] = scan_out[0]
                dc_1_dcs[i] = scan_out[1]
                dc_0_cnts[i] = scan_out[2]
                dc_1_cnts[i] = scan_out[3]
            self._write([7])
        return (dc_0_dcs, dc_1_dcs, dc_0_cnts, dc_1_cnts)

    def accumul_jitter(self, nb_samples: int, acc_len: float=1e-3,
                       pulse_len: float=1e-6, scan_per: Optional[float]=None) \
        -> Optional[Tuple[List[Optional[List[int]]], List[Optional[List[int]]],
                          List[Optional[int]], List[Optional[int]]]]:
        """Accumulate jitter."""
        if (nb_samples <= 0) | (nb_samples >= 2**32):
            self._print(f'Number samples out of range: {nb_samples}')
            return None
        nb_samples = int(nb_samples)
        if (acc_len <= 0) | (acc_len > (2**32-1)*10e-9):
            self._print(f'Accumulation length out of range: {acc_len}')
            return None
        est_time = acc_len * 1.5 + 0.1
        if (pulse_len <= 0) | (pulse_len > (2**32 - 1) * 10e-9):
            self._print(f'Pulse length out of range: {pulse_len}')
            return None
        if scan_per is None:
            scan_per = self.per
        acc_len = int(acc_len / 10e-9 + 0.5)
        pulse_len = int(pulse_len / 10e-9 + 0.5)
        self.clear_uart_buffers()
        self._write([4, 2, int(pulse_len / 256**3), int(pulse_len / 256**2) % 256,
                     int(pulse_len / 256) % 256, pulse_len % 256,
                     int(nb_samples / 256**3), int(nb_samples / 256**2) % 256,
                     int(nb_samples / 256) % 256, nb_samples % 256, int(acc_len / 256**3),
                     int(acc_len / 256**2) % 256, int(acc_len / 256) % 256, acc_len % 256])
        dc_0_dcs: List[Optional[List[int]]] = [None] * nb_samples
        dc_1_dcs: List[Optional[List[int]]] = [None] * nb_samples
        dc_0_cnts: List[Optional[int]] = [0] * nb_samples
        dc_1_cnts: List[Optional[int]] = [0] * nb_samples
        for i in range(nb_samples):
            data = self._read(1, est_time)
            if data is None:
                self._print(f'Accumulate jitter {i + 1} returned invalid response: {data}')
                return None
            if data[0] != 3:
                self._print(f'Accumulate jitter {i + 1} returned invalid response: {data}')
                return None
            if i == nb_samples - 1:
                data = self._read(1, est_time)
                if data is None:
                    self._print(f'Accumulate jitter did not finish properly: {data}')
                else:
                    if data[0] != 0:
                        self._print(f'Accumulate jitter did not finish properly: {data}')
            scan_out = self.read_scan(scan_per)
            if scan_out is None:
                self._print('Scan {i + 1} returned invalid response: {scan_out}')
                dc_0_dcs[i] = None
                dc_1_dcs[i] = None
                dc_0_cnts[i] = None
                dc_1_cnts[i] = None
            else:
                dc_0_dcs[i] = scan_out[0]
                dc_1_dcs[i] = scan_out[1]
                dc_0_cnts[i] = scan_out[2]
                dc_1_cnts[i] = scan_out[3]
            self._write([7])
        return (dc_0_dcs, dc_1_dcs, dc_0_cnts, dc_1_cnts)

    def set_en_clk(self, ro_enable: Union[int, float, bool], dc_clk: Union[int, float, bool]) \
        -> None:
        """Set enable and clock."""
        if (ro_enable < 0) | (ro_enable > 1):
            self._print(f'RO enable out of range: {ro_enable}')
            return
        ro_enable = int(ro_enable + 0.5)
        if (dc_clk < 0) | (dc_clk > 1):
            self._print(f'DC clock out of range: {dc_clk}')
            return
        dc_clk = int(dc_clk + 0.5)
        self._write([4, 3, 0, 0, 0, dc_clk, 0, 0, 0, ro_enable, 0, 0, 0, 0])

    def _send_pot(self, data: List[int], clk_per: Optional[float]=200e-9) -> None:
        """Send potentiometer configuration."""
        if not clk_per:
            clk_per = 200e-9
        if (clk_per <= 0) | (clk_per > (2**32 - 1) * 10e-9):
            self._print(f'Clock period out of range: {clk_per}')
            return
        if clk_per < 173e-9:
            self._print(f'WARNING: clock period is likely too small: {clk_per} < 173e-9')
        est_time = clk_per * 65 + 0.1
        clk_per = int(clk_per / 10e-9 / 2 + 0.5) * 2
        if len(data) != 8:
            self._print('Data should be 8 bytes')
            return
        for i in range(8):
            if (data[i] < 0) | (data[i] > 255):
                self._print(f'Data[{i}] out of range: {data[i]}')
                return
        self.clear_uart_buffers()
        self._write([8, int(clk_per / 256**3), int(clk_per / 256**2) % 256,
                     int(clk_per / 256) % 256, clk_per % 256, *data])
        answer = self._read(1, est_time)
        if answer is None:
            self._print(f'Send pot returned invalid response: {answer}')
            return
        if answer[0] != 0:
            self._print(f'Send pot returned invalid response: {answer}')

    def write_pot_code(self, pot_nb: int, code: int, clk_per: Optional[float]=None) -> None:
        """Send the potentiometer codes.
        POT numbers:
            0:  J0
            1:  J1
            2:  JC
            3:  TC
            4:  TD
            5:  TT
            6:  IO
        """
        if (pot_nb < 0) | (pot_nb > 6):
            self._print(f'Pot number out of range: {pot_nb}')
            return
        if (code < 0) | (code > 255):
            self._print(f'Pot code out of range: {code}')
            return
        data_part = (3 - int(pot_nb / 2)) * 2
        pot_i = pot_nb % 2
        data = [0] * 8
        data[data_part] = 16 + 2 * (pot_i) + (1 - pot_i)
        data[data_part + 1] = code
        self._send_pot(data, clk_per)

    def soft_shdn_pot(self, pot_nb: int, clk_per: Optional[float]=None) -> None:
        """Send soft shutdown to potentiometers.
        POT numbers:
            0:  J0
            1:  J1
            2:  JC
            3:  TC
            4:  TD
            5:  TT
            6:  IO
        """
        if (pot_nb < 0) | (pot_nb > 6):
            self._print(f'Pot number out of range: {pot_nb}')
            return
        data_part = (3 - int(pot_nb / 2)) * 2
        pot_i = pot_nb % 2
        data = [0] * 8
        data[data_part] = 32 + 2 * (pot_i) + (1 - pot_i)
        self._send_pot(data, clk_per)

    def reset_pot(self, pulse_width: float=200e-9) -> None:
        """Reset the potentiometers."""
        if (pulse_width <= 0) | (pulse_width > (2**32 - 1) * 10e-9):
            self._print(f'Pulse width out of range: {pulse_width}')
            return
        if pulse_width < 173e-9:
            self._print(f'WARNING: pulse width is likely too small: {pulse_width} < 173e-9')
        est_time = pulse_width * 1.5 + 0.1
        pulse_width = int(pulse_width / 10e-9 / 2 + 0.5) * 2
        self.clear_uart_buffers()
        self._write([9, int(pulse_width / 256**3), int(pulse_width / 256**2) % 256,
                     int(pulse_width / 256) % 256, pulse_width % 256])
        answer = self._read(1, est_time)
        if answer is None:
            self._print(f'Reset pot returned invalid response: {answer}')
            return
        if answer[0] != 0:
            self._print(f'Reset pot returned invalid response: {answer}')

    def set_pot_shdn(self, shdn: int) -> None:
        """Set potentiometer shutdown."""
        if (shdn < 0) | (shdn > 1):
            self._print(f'SHDN out of range: {shdn}')
            return
        shdn = int(shdn + 0.5)
        self._write([10, shdn])

    def boot_pots(self, j0: int=88, j1: int=88, jc: int=88, td: int=86,
                  tt: int=86, tc: int=88, io: int=215,
                  clk_per: Optional[float]=None) -> None:
        """Boot the potentiometers."""
        self.write_pot_code(0, j0, clk_per)
        self.write_pot_code(1, j1, clk_per)
        self.write_pot_code(2, jc, clk_per)
        self.write_pot_code(4, td, clk_per)
        self.write_pot_code(5, tt, clk_per)
        self.write_pot_code(3, tc, clk_per)
        self.write_pot_code(6, io, clk_per)
        self.set_pot_shdn(1)
