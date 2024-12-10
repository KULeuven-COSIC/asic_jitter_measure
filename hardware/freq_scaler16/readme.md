# `freq_scaler16` Module
![Layout](freq_scaler16.png)

## Cell Hierarchy

`freq_scaler16` **240** (number MOS pairs)
- `freq_scaler8` **120** *x2*

## Netlist

```
.SUBCKT freq_scaler16 CLK OUT<0> OUT<1> OUT<2> OUT<3> OUT<4> OUT<5> OUT<6> OUT<7> OUT<8> OUT<9>
                      + OUT<10> OUT<11> OUT<12> OUT<13> OUT<14> OUT<15> Q' RST RST' VDD VSS
    Xi1 net17 OUT<8> OUT<9> OUT<10> OUT<11> OUT<12> OUT<13> OUT<14> OUT<15> Q' RST RST' VDD VSS
        + freq_scaler8
    Xi0 CLK OUT<0> OUT<1> OUT<2> OUT<3> OUT<4> OUT<5> OUT<6> OUT<7> net17 RST RST' VDD VSS
        + freq_scaler8
.ENDS
```
