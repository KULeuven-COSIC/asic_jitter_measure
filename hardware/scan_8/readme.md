# `scan_8` Module
![Layout](scan_8.png)

## Cell Hierarchy

`scan_8` **176** (number MOS pairs)
- `scan_4` **88** *x2*

## Netlist

```
.SUBCKT scan_8 clk in_par<0> in_par<1> in_par<2> in_par<3> in_par<4> in_par<5> in_par<6> in_par<7>
               + in_ser out rst rst' ser vdd vss
    Xi1 clk in_par<4> in_par<5> in_par<6> in_par<7> net13 out rst rst' ser vdd vss scan_4
    Xi0 clk in_par<0> in_par<1> in_par<2> in_par<3> in_ser net13 rst rst' ser vdd vss scan_4
.ENDS
```
