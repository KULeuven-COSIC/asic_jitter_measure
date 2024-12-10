# `inv_bank_8` Module
![Layout](inv_bank_8.png)

## Cell Hierarchy

`inv_bank_8` **8** (number MOS pairs)
- `inv` **1** *x8*

## Netlist

```
.SUBCKT inv_bank_8 IN<0> IN<1> IN<2> IN<3> IN<4> IN<5> IN<6> IN<7> OUT<0> OUT<1> OUT<2> OUT<3>
                   + OUT<4> OUT<5> OUT<6> OUT<7> VDD VSS
    Xi7 IN<7> OUT<7> VDD VSS inv
    Xi6 IN<6> OUT<6> VDD VSS inv
    Xi5 IN<5> OUT<5> VDD VSS inv
    Xi4 IN<4> OUT<4> VDD VSS inv
    Xi3 IN<3> OUT<3> VDD VSS inv
    Xi2 IN<2> OUT<2> VDD VSS inv
    Xi1 IN<1> OUT<1> VDD VSS inv
    Xi0 IN<0> OUT<0> VDD VSS inv
.ENDS
```
