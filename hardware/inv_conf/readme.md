# `inv_conf` Module
![Layout](inv_conf.png)

## Cell Hierarchy

`inv_conf` **9** (number MOS pairs)
- `p_mos` **0** *x9*
- `n_mos` **0** *x9*

## Netlist

```
.SUBCKT inv_conf conf'<0> conf'<1> conf'<2> conf'<3> conf<0> conf<1> conf<2> conf<3> in out vdd vss
    Mm16 out in vdd vdd p_mos l=60n w=120.0n m=1
    Mm7 out in net16 vdd p_mos l=60n w=120.0n m=1
    Mm6 out in net17 vdd p_mos l=60n w=120.0n m=1
    Mm5 out in net18 vdd p_mos l=60n w=120.0n m=1
    Mm4 out in net19 vdd p_mos l=60n w=120.0n m=1
    Mm3 net16 conf'<3> vdd vdd p_mos l=60n w=120.0n m=1
    Mm2 net17 conf'<2> vdd vdd p_mos l=60n w=120.0n m=1
    Mm1 net18 conf'<1> vdd vdd p_mos l=60n w=120.0n m=1
    Mm0 net19 conf'<0> vdd vdd p_mos l=60n w=120.0n m=1
    Mm17 out in vss vss n_mos l=60n w=120.0n m=1
    Mm15 net20 conf<3> vss vss n_mos l=60n w=120.0n m=1
    Mm14 out in net20 vss n_mos l=60n w=120.0n m=1
    Mm13 net21 conf<2> vss vss n_mos l=60n w=120.0n m=1
    Mm12 out in net21 vss n_mos l=60n w=120.0n m=1
    Mm11 net22 conf<1> vss vss n_mos l=60n w=120.0n m=1
    Mm10 out in net22 vss n_mos l=60n w=120.0n m=1
    Mm9 net23 conf<0> vss vss n_mos l=60n w=120.0n m=1
    Mm8 out in net23 vss n_mos l=60n w=120.0n m=1
.ENDS
```
