# Measurement Data Folder

This folder contains all measurement data. Different measurements are available:
- **m1**: DC stage delay characterization by using a Monte Carlo method.
- **m3**: Measure phase difference variance at multiple accumulation time points.

## Folder structure

This measurement folder contains the following sub-folders:
- *m1/*: m1 measurement data.
- *m3/*: m3 measurement data.
- *readout/*: The Python scripts used to perform the measurements.

Additionally, the following Python modules are available:
- **file_manager.py**: Measurement data file manager module.
- **helper.py**: Measurement data helper functionality.
- **read_asic.py**: Main ASIC readout module.