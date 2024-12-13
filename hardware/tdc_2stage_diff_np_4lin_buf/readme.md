# `tdc_2stage_diff_np_4lin_buf` Module
![Layout](tdc_2stage_diff_np_4lin_buf.png)

## Cell Hierarchy

`tdc_2stage_diff_np_4lin_buf` **116** (number MOS pairs)
- `inv_wn` **1** *x4*
- `dff_st_ar` **15** *x2*
- `nand2` **2** *x4*
- `nor2` **2** *x2*
- `inv` **1** *x2*
- `tdc_stage_diff_np_4lin_buf` **34** *x2*

## Netlist

```
.SUBCKT tdc_2stage_diff_np_4lin_buf buf0_n buf0_p buf1_n buf1_p conf0_n<0> conf0_n<1> conf0_n<2>
                                    + conf0_n<3> conf0_p<0> conf0_p<1> conf0_p<2> conf0_p<3>
                                    + conf1_n<0> conf1_n<1> conf1_n<2> conf1_n<3> conf1_p<0>
                                    + conf1_p<1> conf1_p<2> conf1_p<3> ff0 ff1 in0_n in0_p in1_n
                                    + in1_p nand0_in nand0_out nand1_in nand1_out out0_n out0_p
                                    + out1_n out1_p rst rst' vdd vss
    Xi19 out_buf1_n buf1_n vdd vss inv_wn
    Xi16 out_buf0_p buf0_p vdd vss inv_wn
    Xi17 out_buf0_n buf0_n vdd vss inv_wn
    Xi18 out_buf1_p buf1_p vdd vss inv_wn
    Xi13 nor0 nand0 ff0 q0' rst rst' vdd vss dff_st_ar
    Xi12 nor1 nand1 ff1 q1' rst rst' vdd vss dff_st_ar
    Xi10 q0' enable0 nand0_out vdd vss nand2
    Xi11 q1' enable1 nand1_out vdd vss nand2
    Xi6 q1' out_buf0_n nand1 vdd vss nand2
    Xi7 q0' out_buf1_p nand0 vdd vss nand2
    Xi9 out_buf0_p nand0_in nor0 vdd vss nor2
    Xi8 out_buf1_n nand1_in nor1 vdd vss nor2
    Xi15 nand0_in enable0 vdd vss inv
    Xi14 nand1_in enable1 vdd vss inv
    Xi1 conf1_n<0> conf1_n<1> conf1_n<2> conf1_n<3> conf1_p<0> conf1_p<1> conf1_p<2> conf1_p<3>
        + in1_n in1_p nand1_in enable1 out_buf1_n out_buf1_p out1_n out1_p vdd vss
        + tdc_stage_diff_np_4lin_buf
    Xi0 conf0_n<0> conf0_n<1> conf0_n<2> conf0_n<3> conf0_p<0> conf0_p<1> conf0_p<2> conf0_p<3>
        + in0_n in0_p nand0_in enable0 out_buf0_n out_buf0_p out0_n out0_p vdd vss
        + tdc_stage_diff_np_4lin_buf
.ENDS
```