# `dc_jit_2` Module
![Layout](dc_jit_2.png)

## Cell Hierarchy

`dc_jit_2` **32** (number MOS pairs)
- `dff_st_ar` **15** *x2*
- `inv_jit` **1** *x2*

## Netlist

```
.SUBCKT dc_jit_2 clk in last out<0> out<1> rst rst' vdd vss
    Xi3 clk last out<1> net24 rst rst' vdd vss dff_st_ar
    Xi2 clk int net25 out<0> rst rst' vdd vss dff_st_ar
    Xi1 int last vdd vss inv_jit
    Xi0 in int vdd vss inv_jit
.ENDS
```
