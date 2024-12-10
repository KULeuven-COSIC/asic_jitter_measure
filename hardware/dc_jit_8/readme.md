# `dc_jit_8` Module
![Layout](dc_jit_8.png)

## Cell Hierarchy

`dc_jit_8` **128** (number MOS pairs)
- `dc_jit_4` **64** *x2*

## Netlist

```
.SUBCKT dc_jit_8 CLK IN LAST OUT<0> OUT<1> OUT<2> OUT<3> OUT<4> OUT<5> OUT<6> OUT<7> RST RST' VDD
                 + VSS
    Xi1 CLK INT LAST OUT<4> OUT<5> OUT<6> OUT<7> RST RST' VDD VSS dc_jit_4
    Xi0 CLK IN INT OUT<0> OUT<1> OUT<2> OUT<3> RST RST' VDD VSS dc_jit_4
.ENDS
```
