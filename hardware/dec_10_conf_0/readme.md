# `dec_10_conf_0` Module
![Layout](dec_10_conf_0.png)

## Cell Hierarchy

`dec_10_conf_0` **63** (number MOS pairs)
- `dec_stage` **5** *x10*
- `nand2` **2**
- `nand4` **4** *x2*
- `nor3` **3**

## Netlist

```
.SUBCKT dec_10_conf_0 conf_dec<0> conf_dec<1> conf_dec<2> conf_dec<3> conf_dec<4> conf_dec<5>
                      + conf_dec<6> conf_dec<7> conf_dec<8> conf_dec<9> ff_in<0> ff_in<1> ff_in<2>
                      + ff_in<3> ff_in<4> ff_in<5> ff_in<6> ff_in<7> ff_in<8> ff_in<9> rand_out vdd
                      + vss
    Xi30 conf_dec<9> ff_in<9> ff_in<8> stage<9> vdd vss dec_stage
    Xi28 conf_dec<7> ff_in<7> ff_in<6> stage<7> vdd vss dec_stage
    Xi27 conf_dec<6> ff_in<6> ff_in<5> stage<6> vdd vss dec_stage
    Xi23 conf_dec<5> ff_in<5> ff_in<4> stage<5> vdd vss dec_stage
    Xi22 conf_dec<4> ff_in<4> ff_in<3> stage<4> vdd vss dec_stage
    Xi21 conf_dec<3> ff_in<3> ff_in<2> stage<3> vdd vss dec_stage
    Xi20 conf_dec<2> ff_in<2> ff_in<1> stage<2> vdd vss dec_stage
    Xi19 conf_dec<1> ff_in<1> ff_in<0> stage<1> vdd vss dec_stage
    Xi18 conf_dec<0> ff_in<0> ff_in<9> stage<0> vdd vss dec_stage
    Xi29 conf_dec<8> ff_in<8> ff_in<7> stage<8> vdd vss dec_stage
    Xi31 stage<8> stage<9> net038 vdd vss nand2
    Xi25 stage<4> stage<5> stage<6> stage<7> net023 vdd vss nand4
    Xi24 stage<0> stage<1> stage<2> stage<3> net026 vdd vss nand4
    Xi26 net026 net023 net038 rand_out vdd vss nor3
.ENDS
```
