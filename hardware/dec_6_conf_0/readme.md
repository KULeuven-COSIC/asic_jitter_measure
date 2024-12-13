# `dec_6_conf_0` Module
![Layout](dec_6_conf_0.png)

## Cell Hierarchy

`dec_6_conf_0` **38** (number MOS pairs)
- `dec_stage` **5** *x6*
- `nand3` **3** *x2*
- `nor2` **2**

## Netlist

```
.SUBCKT dec_6_conf_0 conf_dec<0> conf_dec<1> conf_dec<2> conf_dec<3> conf_dec<4> conf_dec<5>
                     + ff_in<0> ff_in<1> ff_in<2> ff_in<3> ff_in<4> ff_in<5> rand_out vdd vss
    Xi23 conf_dec<5> ff_in<5> ff_in<4> stage<5> vdd vss dec_stage
    Xi22 conf_dec<4> ff_in<4> ff_in<3> stage<4> vdd vss dec_stage
    Xi21 conf_dec<3> ff_in<3> ff_in<2> stage<3> vdd vss dec_stage
    Xi20 conf_dec<2> ff_in<2> ff_in<1> stage<2> vdd vss dec_stage
    Xi19 conf_dec<1> ff_in<1> ff_in<0> stage<1> vdd vss dec_stage
    Xi18 conf_dec<0> ff_in<0> ff_in<5> stage<0> vdd vss dec_stage
    Xi25 stage<3> stage<4> stage<5> net023 vdd vss nand3
    Xi24 stage<0> stage<1> stage<2> net026 vdd vss nand3
    Xi26 net026 net023 rand_out vdd vss nor2
.ENDS
```
