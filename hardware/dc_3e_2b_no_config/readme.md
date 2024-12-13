# `dc_3e_2b_no_config` Module
![Layout](dc_3e_2b_no_config.png)

## Cell Hierarchy

`dc_3e_2b_no_config` **78** (number MOS pairs)
- `mero_3e_2b` **18**
- `edge_to_level_3e` **51**
- `nor2` **2**
- `buffer` **2** *x3*
- `inv` **1**

## Netlist

```
.SUBCKT dc_3e_2b_no_config enable_e2l enable_mero int0 int1 int2 out0 out1 out2 rst rst' vdd vss
    Xi5 enable_int mero_out0 mero_out1 mero_out2 vdd vss mero_3e_2b
    Xi1 int1 enable_e2l out0 out1 out2 rst rst' vdd vss edge_to_level_3e
    Xi12 out2 net014 enable_int vdd vss nor2
    Xi9 mero_out0 int0 vdd vss buffer
    Xi11 mero_out2 int2 vdd vss buffer
    Xi10 mero_out1 int1 vdd vss buffer
    Xi13 enable_mero net014 vdd vss inv
.ENDS
```
