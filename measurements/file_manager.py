"""Measurement data file manager module."""
from typing import List, Union, Optional, Any
import csv
from os.path import isfile

class FileManager:
    """Measurement data file maneger class."""

    def __init__(self, file_name: str):
        self.file_name = file_name

    def _file_exists(self):
        """Check if the file exists."""
        if isfile(self.file_name):
            print(f'File: {self.file_name} already exists!')
            return True
        return False

    def init_file(self, col_titles: List[str]):
        """Initialize the file."""
        if self._file_exists():
            return False
        with open(self.file_name, 'w', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(col_titles)
        return True

    def append(self, data_row) -> None:
        """Append data to the file."""
        row_copy: List[Optional[Any]] = [None] * len(data_row)
        for i, dr_i in enumerate(data_row):
            try:
                row_copy[i] = self._array_to_str(dr_i)
            except: # pylint: disable=bare-except
                row_copy[i] = dr_i
        with open(self.file_name, 'a', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(row_copy)

    def _array_to_str(self, array: List[Union[float, int]]) -> str:
        """Convert array to string array."""
        result = str(array[0])
        for i in range(1, len(array)):
            result += ' ' + str(array[i])
        return result

    def _str_to_array(self, stri: str, integer: bool=True) -> Union[List[float], List[int]]:
        """Convert string array to array."""
        parts = stri.split(' ')
        result = [0.0] * len(parts)
        for i, p_i in enumerate(parts):
            if integer:
                result[i] = int(p_i)
            else:
                result[i] = float(p_i)
        return result

    def read_file(self, col_arrays: List[bool], col_ints: List[bool]) \
        -> Optional[List[List[Union[List[int], List[float], int, float]]]]:
        """Read the file and parse the data."""
        if not isfile(self.file_name):
            print(f'File: {self.file_name} does not exist!')
            return None
        result: List[List[Union[List[int], List[float], int, float]]] \
            = [[] for i in range(len(col_arrays))]
        with open(self.file_name, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            next(reader)
            for row in reader:
                for col, c_i in enumerate(col_arrays):
                    if c_i:
                        result[col] += [self._str_to_array(row[col], integer=col_ints[col])]
                    else:
                        if col_ints[col]:
                            result[col] += [int(row[col])]
                        else:
                            result[col] += [float(row[col])]
        return result
