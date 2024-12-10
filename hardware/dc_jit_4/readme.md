# `dc_jit_4` Module
![Layout](dc_jit_4.png)

## Cell Hierarchy

`dc_jit_4` **64** (number MOS pairs)
- `dc_jit_2` **32** *x2*

## Netlist

```
.SUBCKT dc_jit_4 CLK IN LAST OUT<0> OUT<1> OUT<2> OUT<3> RST RST' VDD VSS
    Xi1 CLK INT LAST OUT<2> OUT<3> RST RST' VDD VSS dc_jit_2
    Xi0 CLK IN INT OUT<0> OUT<1> RST RST' VDD VSS dc_jit_2
.ENDS
```
