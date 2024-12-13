# `ff_ready_2` Module
![Layout](ff_ready_2.png)

## Cell Hierarchy

`ff_ready_2` **20** (number MOS pairs)
- `nand2` **2**
- `dff_st_ar_dh` **14**
- `nor2` **2** *x2*

## Netlist

```
.SUBCKT ff_ready_2 ff0<0> ff0<1> ff1<0> ff1<1> ff_ready rst rst' vdd vss
    Xi2 ff_nor0 ff_nor1 ff_nand vdd vss nand2
    Xi3 ff_nand ff_ready net18 rst rst' vdd vss dff_st_ar_dh
    Xi0 ff0<0> ff0<1> ff_nor0 vdd vss nor2
    Xi1 ff1<0> ff1<1> ff_nor1 vdd vss nor2
.ENDS
```
