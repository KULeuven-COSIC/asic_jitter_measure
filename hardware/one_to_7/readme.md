# `one_to_7` Module
![Layout](one_to_7.png)

## Cell Hierarchy

`one_to_7` **7** (number MOS pairs)
- `inv` **1** *x7*

## Netlist

```
.SUBCKT one_to_7 in out<0> out<1> out<2> out<3> out<4> out<5> out<6> vdd vss
    Xi6 in out<6> vdd vss inv
    Xi5 in out<3> vdd vss inv
    Xi4 in out<5> vdd vss inv
    Xi3 in out<4> vdd vss inv
    Xi2 in out<2> vdd vss inv
    Xi1 in out<1> vdd vss inv
    Xi0 in out<0> vdd vss inv
.ENDS
```
