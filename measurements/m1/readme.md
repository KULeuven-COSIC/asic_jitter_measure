# DC Characterization

DC stage delay characterization by using a Monte Carlo method.

## Measurement Conditions:

The measurements are performed with the following operating conditions:
- **Temperature**: 15 °C, and 25 °C
- **Supply voltage**: 1.2 V
- **Accumulation time length**: 1 s, 0.1 s, 0.07 s, and 0.09 s
- **Number of samples collected**: 1000
- **Chip numbers**:
    - **2**: *DC configuration*: 0-1-0-1, 0-13-0-5, 0-51-0-51, 15-0-15-0, and 1-235-1-242
    - **3**: *DC configuration*: 0-17-0-17, 0-51-0-51, 0-1-0-1, 1-235-1-235, and 0-13-0-5
    - **4**: *DC configuration*: 0-0-0-0, and 15-0-15-0

## Data Format

| Column 0 | Column 1 | Column 2 | Column 3 | Column 4 |
| -------- | -------- | -------- | -------- | -------- |
| DC stage | delay pos edge DC0 | delay neg edge DC0 | delay pos edge DC1 | delay neg edge DC1 |
| Unit: - | Unit: s | Unit: s | Unit: s | Unit: s |