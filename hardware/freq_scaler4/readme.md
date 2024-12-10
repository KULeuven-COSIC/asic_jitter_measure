# `freq_scaler4` Module
![Layout](freq_scaler4.png)

## Cell Hierarchy

`freq_scaler4` **60** (number MOS pairs)
- `freq_scaler2` **30** *x2*

## Netlist

```
.SUBCKT freq_scaler4 CLK OUT<0> OUT<1> OUT<2> OUT<3> Q' RST RST' VDD VSS
    Xi1 net17 OUT<2> OUT<3> Q' RST RST' VDD VSS freq_scaler2
    Xi0 CLK OUT<0> OUT<1> net17 RST RST' VDD VSS freq_scaler2
.ENDS
```
