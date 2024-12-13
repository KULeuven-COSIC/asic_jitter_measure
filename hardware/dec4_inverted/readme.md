# `dec4_inverted` Module
![Layout](dec4_inverted.png)

## Cell Hierarchy

`dec4_inverted` **10** (number MOS pairs)
- `inv` **1** *x2*
- `nand2` **2** *x4*

## Netlist

```
.SUBCKT dec4_inverted out<0> out<1> out<2> out<3> sel<0> sel<1> vdd vss
    Xi1 sel<1> sel'<1> vdd vss inv
    Xi0 sel<0> sel'<0> vdd vss inv
    Xi6 sel<0> sel<1> out<3> vdd vss nand2
    Xi5 sel'<0> sel<1> out<2> vdd vss nand2
    Xi4 sel<0> sel'<1> out<1> vdd vss nand2
    Xi3 sel'<0> sel'<1> out<0> vdd vss nand2
.ENDS
```
