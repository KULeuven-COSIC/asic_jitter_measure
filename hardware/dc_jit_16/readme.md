# `dc_jit_16` Module
![Layout](dc_jit_16.png)

## Cell Hierarchy

`dc_jit_16` **256** (number MOS pairs)
- `dc_jit_8` **128** *x2*

## Netlist

```
.SUBCKT dc_jit_16 CLK IN LAST OUT<0> OUT<1> OUT<2> OUT<3> OUT<4> OUT<5> OUT<6> OUT<7> OUT<8> OUT<9>
                  + OUT<10> OUT<11> OUT<12> OUT<13> OUT<14> OUT<15> RST RST' VDD VSS
    Xi1 CLK INT LAST OUT<8> OUT<9> OUT<10> OUT<11> OUT<12> OUT<13> OUT<14> OUT<15> RST RST' VDD VSS
        + dc_jit_8
    Xi0 CLK IN INT OUT<0> OUT<1> OUT<2> OUT<3> OUT<4> OUT<5> OUT<6> OUT<7> RST RST' VDD VSS dc_jit_8
.ENDS
```
