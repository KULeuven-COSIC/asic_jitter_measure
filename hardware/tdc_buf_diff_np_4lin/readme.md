# `tdc_buf_diff_np_4lin` Module
![Layout](tdc_buf_diff_np_4lin.png)

## Cell Hierarchy

`tdc_buf_diff_np_4lin` **26** (number MOS pairs)
- `n_mos` **0** *x26*
- `p_mos` **0** *x26*

## Netlist

```
.SUBCKT tdc_buf_diff_np_4lin conf_n<0> conf_n<1> conf_n<2> conf_n<3> conf_p<0> conf_p<1> conf_p<2>
                             + conf_p<3> in_n in_p out_n out_p vdd vss
    Mm51 conf_n'<3> conf_n<3> vss vss n_mos l=60n w=120.0n m=1
    Mm50 conf_n'<2> conf_n<2> vss vss n_mos l=60n w=120.0n m=1
    Mm49 conf_n'<1> conf_n<1> vss vss n_mos l=60n w=120.0n m=1
    Mm48 conf_n'<0> conf_n<0> vss vss n_mos l=60n w=120.0n m=1
    Mm43 conf_p'<3> conf_p<3> vss vss n_mos l=60n w=120.0n m=1
    Mm42 conf_p'<2> conf_p<2> vss vss n_mos l=60n w=120.0n m=1
    Mm41 conf_p'<1> conf_p<1> vss vss n_mos l=60n w=120.0n m=1
    Mm40 conf_p'<0> conf_p<0> vss vss n_mos l=60n w=120.0n m=1
    Mm35 out_p in_n vss vss n_mos l=60n w=120.0n m=1
    Mm33 out_n in_p vss vss n_mos l=60n w=120.0n m=1
    Mm15 net49 conf_n<3> vss vss n_mos l=60n w=120.0n m=1
    Mm14 net52 conf_n<2> vss vss n_mos l=60n w=120.0n m=1
    Mm13 net53 conf_n<1> vss vss n_mos l=60n w=120.0n m=1
    Mm12 net56 conf_n<0> vss vss n_mos l=60n w=120.0n m=1
    Mm11 out_p out_n net49 vss n_mos l=60n w=120.0n m=1
    Mm10 out_p out_n net52 vss n_mos l=60n w=120.0n m=1
    Mm9 out_p out_n net53 vss n_mos l=60n w=120.0n m=1
    Mm8 out_p out_n net56 vss n_mos l=60n w=120.0n m=1
    Mm7 net57 conf_p<3> vss vss n_mos l=60n w=120.0n m=1
    Mm6 net60 conf_p<2> vss vss n_mos l=60n w=120.0n m=1
    Mm5 net61 conf_p<1> vss vss n_mos l=60n w=120.0n m=1
    Mm4 net64 conf_p<0> vss vss n_mos l=60n w=120.0n m=1
    Mm3 out_n out_p net57 vss n_mos l=60n w=120.0n m=1
    Mm2 out_n out_p net60 vss n_mos l=60n w=120.0n m=1
    Mm1 out_n out_p net61 vss n_mos l=60n w=120.0n m=1
    Mm0 out_n out_p net64 vss n_mos l=60n w=120.0n m=1
    Mm47 conf_n'<3> conf_n<3> vdd vdd p_mos l=60n w=120.0n m=1
    Mm46 conf_n'<2> conf_n<2> vdd vdd p_mos l=60n w=120.0n m=1
    Mm45 conf_n'<1> conf_n<1> vdd vdd p_mos l=60n w=120.0n m=1
    Mm44 conf_n'<0> conf_n<0> vdd vdd p_mos l=60n w=120.0n m=1
    Mm39 conf_p'<3> conf_p<3> vdd vdd p_mos l=60n w=120.0n m=1
    Mm38 conf_p'<2> conf_p<2> vdd vdd p_mos l=60n w=120.0n m=1
    Mm37 conf_p'<1> conf_p<1> vdd vdd p_mos l=60n w=120.0n m=1
    Mm36 conf_p'<0> conf_p<0> vdd vdd p_mos l=60n w=120.0n m=1
    Mm34 out_p in_n vdd vdd p_mos l=60n w=120.0n m=1
    Mm32 out_n in_p vdd vdd p_mos l=60n w=120.0n m=1
    Mm31 out_p out_n net50 vdd p_mos l=60n w=120.0n m=1
    Mm30 out_p out_n net51 vdd p_mos l=60n w=120.0n m=1
    Mm29 out_p out_n net54 vdd p_mos l=60n w=120.0n m=1
    Mm28 out_p out_n net55 vdd p_mos l=60n w=120.0n m=1
    Mm27 net50 conf_p'<3> vdd vdd p_mos l=60n w=120.0n m=1
    Mm26 net51 conf_p'<2> vdd vdd p_mos l=60n w=120.0n m=1
    Mm25 net54 conf_p'<1> vdd vdd p_mos l=60n w=120.0n m=1
    Mm24 net55 conf_p'<0> vdd vdd p_mos l=60n w=120.0n m=1
    Mm23 out_n out_p net58 vdd p_mos l=60n w=120.0n m=1
    Mm22 out_n out_p net59 vdd p_mos l=60n w=120.0n m=1
    Mm21 out_n out_p net62 vdd p_mos l=60n w=120.0n m=1
    Mm20 out_n out_p net63 vdd p_mos l=60n w=120.0n m=1
    Mm19 net58 conf_n'<3> vdd vdd p_mos l=60n w=120.0n m=1
    Mm18 net59 conf_n'<2> vdd vdd p_mos l=60n w=120.0n m=1
    Mm17 net62 conf_n'<1> vdd vdd p_mos l=60n w=120.0n m=1
    Mm16 net63 conf_n'<0> vdd vdd p_mos l=60n w=120.0n m=1
.ENDS
```
