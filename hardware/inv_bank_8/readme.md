# `inv_bank_8` Module
![Layout](inv_bank_8.png)

## Cell Hierarchy

`inv_bank_8` **8** (number MOS pairs)
- `inv` **1** *x8*

## Netlist

```
.SUBCKT inv_bank_8 in<0> in<1> in<2> in<3> in<4> in<5> in<6> in<7> out<0> out<1> out<2> out<3>
                   + out<4> out<5> out<6> out<7> vdd vss
    Xi7 in<7> out<7> vdd vss inv
    Xi6 in<6> out<6> vdd vss inv
    Xi5 in<5> out<5> vdd vss inv
    Xi4 in<4> out<4> vdd vss inv
    Xi3 in<3> out<3> vdd vss inv
    Xi2 in<2> out<2> vdd vss inv
    Xi1 in<1> out<1> vdd vss inv
    Xi0 in<0> out<0> vdd vss inv
.ENDS
```
