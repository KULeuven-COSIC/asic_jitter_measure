# `freq_scaler16` Module
![Layout](freq_scaler16.png)

## Cell Hierarchy

`freq_scaler16` **240** (number MOS pairs)
- `freq_scaler8` **120** *x2*

## Netlist

```
.SUBCKT freq_scaler16 clk out<0> out<1> out<2> out<3> out<4> out<5> out<6> out<7> out<8> out<9>
                      + out<10> out<11> out<12> out<13> out<14> out<15> q' rst rst' vdd vss
    Xi1 net17 out<8> out<9> out<10> out<11> out<12> out<13> out<14> out<15> q' rst rst' vdd vss
        + freq_scaler8
    Xi0 clk out<0> out<1> out<2> out<3> out<4> out<5> out<6> out<7> net17 rst rst' vdd vss
        + freq_scaler8
.ENDS
```
