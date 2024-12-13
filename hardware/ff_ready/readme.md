# `ff_ready` Module
![Layout](ff_ready.png)

## Cell Hierarchy

`ff_ready` **22** (number MOS pairs)
- `nor3` **3** *x2*
- `nand2` **2**
- `dff_st_ar_dh` **14**

## Netlist

```
.SUBCKT ff_ready ff0<0> ff0<1> ff0<2> ff1<0> ff1<1> ff1<2> ff_ready rst rst' vdd vss
    Xi0 ff0<0> ff0<1> ff0<2> ff_nor0 vdd vss nor3
    Xi1 ff1<0> ff1<1> ff1<2> ff_nor1 vdd vss nor3
    Xi2 ff_nor0 ff_nor1 ff_nand vdd vss nand2
    Xi3 ff_nand ff_ready net18 rst rst' vdd vss dff_st_ar_dh
.ENDS
```
