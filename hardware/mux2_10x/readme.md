# `mux2_10x` Module
![Layout](mux2_10x.png)

## Cell Hierarchy

`mux2_10x` **70** (number MOS pairs)
- `mux2` **7** *x10*

## Netlist

```
.SUBCKT mux2_10x in0<0> in0<1> in0<2> in0<3> in0<4> in0<5> in0<6> in0<7> in0<8> in0<9> in1<0> in1<1>
                 + in1<2> in1<3> in1<4> in1<5> in1<6> in1<7> in1<8> in1<9> out<0> out<1> out<2>
                 + out<3> out<4> out<5> out<6> out<7> out<8> out<9> sel vdd vss
    Xi0 in0<0> in1<0> out<0> sel vdd vss mux2
    Xi9 in0<9> in1<9> out<9> sel vdd vss mux2
    Xi8 in0<8> in1<8> out<8> sel vdd vss mux2
    Xi7 in0<7> in1<7> out<7> sel vdd vss mux2
    Xi6 in0<6> in1<6> out<6> sel vdd vss mux2
    Xi5 in0<5> in1<5> out<5> sel vdd vss mux2
    Xi4 in0<4> in1<4> out<4> sel vdd vss mux2
    Xi3 in0<3> in1<3> out<3> sel vdd vss mux2
    Xi2 in0<2> in1<2> out<2> sel vdd vss mux2
    Xi1 in0<1> in1<1> out<1> sel vdd vss mux2
.ENDS
```
