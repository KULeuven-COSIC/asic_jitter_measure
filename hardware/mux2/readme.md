# `mux2` Module
![Layout](mux2.png)

## Cell Hierarchy

`mux2` **7** (number MOS pairs)
- `nand2` **2** *x3*
- `p_mos` **0**
- `n_mos` **0**

## Netlist

```
.SUBCKT mux2 IN0 IN1 OUT SEL VDD VSS
    Xi2 net16 net15 OUT VDD VSS nand2
    Xi1 SEL IN1 net15 VDD VSS nand2
    Xi0 IN0 net14 net16 VDD VSS nand2
    Mm0 net14 SEL VDD VDD p_mos l=60n w=240.0n m=1
    Mm1 net14 SEL VSS VSS n_mos l=60n w=240.0n m=1
.ENDS
```
