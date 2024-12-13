# `mux2` Module
![Layout](mux2.png)

## Cell Hierarchy

`mux2` **7** (number MOS pairs)
- `nand2` **2** *x3*
- `p_mos` **0**
- `n_mos` **0**

## Netlist

```
.SUBCKT mux2 in0 in1 out sel vdd vss
    Xi2 net16 net15 out vdd vss nand2
    Xi1 sel in1 net15 vdd vss nand2
    Xi0 in0 net14 net16 vdd vss nand2
    Mm0 net14 sel vdd vdd p_mos l=60n w=240.0n m=1
    Mm1 net14 sel vss vss n_mos l=60n w=240.0n m=1
.ENDS
```
