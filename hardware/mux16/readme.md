# `mux16` Module
![Layout](mux16.png)

## Cell Hierarchy

`mux16` **105** (number MOS pairs)
- `mux4` **21** *x5*

## Netlist

```
.SUBCKT mux16 in<0> in<1> in<2> in<3> in<4> in<5> in<6> in<7> in<8> in<9> in<10> in<11> in<12>
              + in<13> in<14> in<15> out sel<0> sel<1> sel<2> sel<3> vdd vss
    Xi4 in<12> in<13> in<14> in<15> int<3> sel<0> sel<1> vdd vss mux4
    Xi3 in<8> in<9> in<10> in<11> int<2> sel<0> sel<1> vdd vss mux4
    Xi5 int<0> int<1> int<2> int<3> out sel<2> sel<3> vdd vss mux4
    Xi1 in<4> in<5> in<6> in<7> int<1> sel<0> sel<1> vdd vss mux4
    Xi0 in<0> in<1> in<2> in<3> int<0> sel<0> sel<1> vdd vss mux4
.ENDS
```
