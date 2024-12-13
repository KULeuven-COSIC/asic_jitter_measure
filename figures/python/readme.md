# Figure Generation Python Scripts

This folder contains the figure generation Python scripts.

## Scripts

The scripts are divided in the following categories.

### Noisy Oscillator Model

- **flicker_fm_est.py**: Generate flicker FM noise estimation error figure.
- **noise_comp.py***: Generate compare contribution of different noise types to total excess phase variance figure.

### Measurement Set-up

- **acc_time_var.py**: Generate measured accumulation time variance figure.
- **dc_charac.py***: Generate measured stage delay distributions figure.

### Phase Difference Measurement

- **phase_var.py**: Generate estimated variance of the phase difference figure.
- **noise_corner.py**: Generate flicker noise corner figure.
- **allan_var.py**: Generate sample variance versus sample Allan variance figure.


## Script Options

The following script arguments are available:
- `-v`: Enable verbose output.
- `-d`: Generate processed data and store in the *data/* folder.
- `-q`: Quit the script as soon as the processed data is generated, without generating the figure. Should only be used in combination with the `-d` argument.
- `-l`: For lengthy execution times, the log option might be available, indicating the time required to execute the script.