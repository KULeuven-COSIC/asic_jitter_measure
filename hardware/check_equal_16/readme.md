# `check_equal_16` Module
![Layout](check_equal_16.png)

## Cell Hierarchy

`check_equal_16` **119** (number MOS pairs)
- `check_equal_8` **58** *x2*
- `nand2` **2**
- `inv` **1**

## Netlist

```
.SUBCKT check_equal_16 equal in0<0> in0<1> in0<2> in0<3> in0<4> in0<5> in0<6> in0<7> in0<8> in0<9>
                       + in0<10> in0<11> in0<12> in0<13> in0<14> in0<15> in1<0> in1<1> in1<2> in1<3>
                       + in1<4> in1<5> in1<6> in1<7> in1<8> in1<9> in1<10> in1<11> in1<12> in1<13>
                       + in1<14> in1<15> vdd vss
    Xi1 eq1 in0<8> in0<9> in0<10> in0<11> in0<12> in0<13> in0<14> in0<15> in1<8> in1<9> in1<10>
        + in1<11> in1<12> in1<13> in1<14> in1<15> vdd vss check_equal_8
    Xi0 eq0 in0<0> in0<1> in0<2> in0<3> in0<4> in0<5> in0<6> in0<7> in1<0> in1<1> in1<2> in1<3>
        + in1<4> in1<5> in1<6> in1<7> vdd vss check_equal_8
    Xi2 eq0 eq1 net3 vdd vss nand2
    Xi3 net3 equal vdd vss inv
.ENDS
```
