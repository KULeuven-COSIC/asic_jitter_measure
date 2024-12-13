# Phase Variance Measurement

Measure phase difference variance at multiple accumulation time points.

## Measurement Conditions:

The measurements are performed with the following operating conditions:
- **Temperature**: 15 °C
- **Supply voltage**: 1.2 V
- **Number of samples collected per accumulation time point**: 100, and 1000
- **Chip numbers**:
    - **2**: *DC configuration*: 0-0-0-0, 0-0-1-0, 0-0-15-0, 1-0-0-0, 1-0-1-0, 1-0-15-0, 15-0-0-0, 15-0-1-0, and 15-0-15-0
    - **3**: *DC configuration*: 0-0-0-0, 0-0-1-0, 0-0-15-0, 1-0-0-0, 1-0-1-0, 1-0-15-0, 15-0-0-0, 15-0-1-0, and 15-0-15-0
    - **4**: *DC configuration*: 0-0-0-0, 0-0-1-0, 0-0-15-0, 1-0-0-0, 1-0-1-0, 1-0-15-0, and 15-0-1-0

## Data Format

The stored phases are normalized to the RO period length.

| Column 0 | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| Experiment number | Accumulation length range | RO0 period | RO1 period | Processed RO0 phase samples | Processed RO1 phase samples | Raw RO0 phase samples | Raw RO1 phase samples |
| Unit: - | Unit: s | Unit: s | Unit: s | Unit: - | Unit: - | Unit: - | Unit: - |