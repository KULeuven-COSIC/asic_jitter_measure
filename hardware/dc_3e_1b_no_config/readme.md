# `dc_3e_1b_no_config` Module
![Layout](dc_3e_1b_no_config.png)

## Cell Hierarchy

`dc_3e_1b_no_config` **72** (number MOS pairs)
- `buffer` **2** *x3*
- `edge_to_level_3e` **51**
- `mero_3e_1b` **12**
- `nor2` **2**
- `inv` **1**

## Netlist

```
.SUBCKT dc_3e_1b_no_config enable_e2l enable_mero int0 int1 int2 out0 out1 out2 rst rst' vdd vss
    Xi11 mero_out2 int2 vdd vss buffer
    Xi9 mero_out0 int0 vdd vss buffer
    Xi10 mero_out1 int1 vdd vss buffer
    Xi1 int1 enable_e2l out0 out1 out2 rst rst' vdd vss edge_to_level_3e
    Xi5 enable_int mero_out0 mero_out1 mero_out2 vdd vss mero_3e_1b
    Xi12 out2 net10 enable_int vdd vss nor2
    Xi13 enable_mero net10 vdd vss inv
.ENDS
```
