# `single_ended_to_diff` Module
![Layout](single_ended_to_diff.png)

## Cell Hierarchy

`single_ended_to_diff` **2** (number MOS pairs)
- `p_mos` **0** *x2*
- `n_mos` **0** *x2*

## Netlist

```
.SUBCKT single_ended_to_diff in out_n out_p vdd vss
    Mm2 out_n in vdd vdd p_mos l=60n w=480.0n m=4
    Mm3 out_p out_n vdd vdd p_mos l=60n w=480.0n m=4
    Mm1 out_p out_n vss vss n_mos l=60n w=480.0n m=4
    Mm0 out_n in vss vss n_mos l=60n w=480.0n m=4
.ENDS
```
