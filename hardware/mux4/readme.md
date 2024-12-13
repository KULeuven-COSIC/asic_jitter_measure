# `mux4` Module
![Layout](mux4.png)

## Cell Hierarchy

`mux4` **21** (number MOS pairs)
- `mux2` **7** *x3*

## Netlist

```
.SUBCKT mux4 in<0> in<1> in<2> in<3> out sel<0> sel<1> vdd vss
    Xi2 net8 net7 out sel<1> vdd vss mux2
    Xi1 in<2> in<3> net7 sel<0> vdd vss mux2
    Xi0 in<0> in<1> net8 sel<0> vdd vss mux2
.ENDS
```
