# `ff_ready_6` Module
![Layout](ff_ready_6.png)

## Cell Hierarchy

`ff_ready_6` **26** (number MOS pairs)
- `nor5` **5** *x2*
- `nand2` **2**
- `dff_st_ar_dh` **14**

## Netlist

```
.SUBCKT ff_ready_6 ff0<0> ff0<1> ff0<2> ff0<3> ff0<4> ff1<0> ff1<1> ff1<2> ff1<3> ff1<4> ff_ready
                   + rst rst' vdd vss
    Xi0 ff0<0> ff0<1> ff0<2> ff0<3> ff0<4> ff_nor0 vdd vss nor5
    Xi1 ff1<0> ff1<1> ff1<2> ff1<3> ff1<4> ff_nor1 vdd vss nor5
    Xi2 ff_nor0 ff_nor1 ff_nand vdd vss nand2
    Xi3 ff_nand ff_ready net18 rst rst' vdd vss dff_st_ar_dh
.ENDS
```
