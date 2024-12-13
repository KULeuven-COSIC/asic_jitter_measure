# `tff_st_ar` Module
![Layout](tff_st_ar.png)

## Cell Hierarchy

`tff_st_ar` **15** (number MOS pairs)
- `dff_st_ar` **15**

## Netlist

```
.SUBCKT tff_st_ar clk q q' rst rst' vdd vss
    Xi0 clk q' q q' rst rst' vdd vss dff_st_ar
.ENDS
```
