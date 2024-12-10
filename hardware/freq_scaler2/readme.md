# `freq_scaler2` Module
![Layout](freq_scaler2.png)

## Cell Hierarchy

`freq_scaler2` **30** (number MOS pairs)
- `tff_st_ar` **15** *x2*

## Netlist

```
.SUBCKT freq_scaler2 CLK OUT<0> OUT<1> Q' RST RST' VDD VSS
    Xi1 INT OUT<1> Q' RST RST' VDD VSS tff_st_ar
    Xi0 CLK OUT<0> INT RST RST' VDD VSS tff_st_ar
.ENDS
```
