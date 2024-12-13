# `buffer_large` Module
![Layout](buffer_large.png)

## Cell Hierarchy

`buffer_large` **4** (number MOS pairs)
- `n_mos` **0** *x4*
- `p_mos` **0** *x4*

## Netlist

```
.SUBCKT buffer_large in out vdd vss
    Mm7 out int<2> vss vss n_mos l=60n w=480.0n m=16
    Mm5 int<2> int<1> vss vss n_mos l=60n w=480.0n m=4
    Mm2 int<1> int<0> vss vss n_mos l=60n w=480.0n m=1
    Mm0 int<0> in vss vss n_mos l=60n w=120.0n m=1
    Mm6 out int<2> vdd vdd p_mos l=60n w=480.0n m=16
    Mm4 int<2> int<1> vdd vdd p_mos l=60n w=480.0n m=4
    Mm3 int<1> int<0> vdd vdd p_mos l=60n w=480.0n m=1
    Mm1 int<0> in vdd vdd p_mos l=60n w=120.0n m=1
.ENDS
```
