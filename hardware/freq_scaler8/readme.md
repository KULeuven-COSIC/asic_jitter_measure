# `freq_scaler8` Module
![Layout](freq_scaler8.png)

## Cell Hierarchy

`freq_scaler8` **120** (number MOS pairs)
- `freq_scaler4` **60** *x2*

## Netlist

```
.SUBCKT freq_scaler8 CLK OUT<0> OUT<1> OUT<2> OUT<3> OUT<4> OUT<5> OUT<6> OUT<7> Q' RST RST' VDD VSS
    Xi1 net17 OUT<4> OUT<5> OUT<6> OUT<7> Q' RST RST' VDD VSS freq_scaler4
    Xi0 CLK OUT<0> OUT<1> OUT<2> OUT<3> net17 RST RST' VDD VSS freq_scaler4
.ENDS
```
