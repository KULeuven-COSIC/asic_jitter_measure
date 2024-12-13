# `tdc_1b_diff_branch` Module
![Layout](tdc_1b_diff_branch.png)

## Cell Hierarchy

`tdc_1b_diff_branch` **702** (number MOS pairs)
- `tdc_2e_1b_diff_np_4lin_buf` **234**
- `dec_4_conf_0` **26**
- `tdc_ready_2` **442**

## Netlist

```
.SUBCKT tdc_1b_diff_branch alarm<0> alarm<1> buf1_p<0> clk conf0_n<0> conf0_n<1> conf0_n<2>
                           + conf0_n<3> conf0_n<4> conf0_n<5> conf0_n<6> conf0_n<7> conf0_p<0>
                           + conf0_p<1> conf0_p<2> conf0_p<3> conf0_p<4> conf0_p<5> conf0_p<6>
                           + conf0_p<7> conf1_n<0> conf1_n<1> conf1_n<2> conf1_n<3> conf1_n<4>
                           + conf1_n<5> conf1_n<6> conf1_n<7> conf1_p<0> conf1_p<1> conf1_p<2>
                           + conf1_p<3> conf1_p<4> conf1_p<5> conf1_p<6> conf1_p<7> conf_dec<0>
                           + conf_dec<1> conf_dec<2> conf_dec<3> conf_maxcycles<0> conf_maxcycles<1>
                           + conf_maxcycles<2> conf_maxcycles<3> conf_maxcycles<4> conf_maxcycles<5>
                           + conf_maxcycles<6> conf_maxcycles<7> conf_waitcycles<0>
                           + conf_waitcycles<1> conf_waitcycles<2> conf_waitcycles<3>
                           + conf_waitcycles<4> conf_waitcycles<5> conf_waitcycles<6>
                           + conf_waitcycles<7> edge0_n edge0_p edge1_n edge1_p enable_e2l ff<0>
                           + ff<1> ff<2> ff<3> rand_out ready rst rst' vdd vss
    Xi1 net31<0> net31<1> buf0_p<0> buf0_p<1> net30<0> net30<1> buf1_p<0> buf1_p<1> conf0_n<0>
        + conf0_n<1> conf0_n<2> conf0_n<3> conf0_n<4> conf0_n<5> conf0_n<6> conf0_n<7> conf0_p<0>
        + conf0_p<1> conf0_p<2> conf0_p<3> conf0_p<4> conf0_p<5> conf0_p<6> conf0_p<7> conf1_n<0>
        + conf1_n<1> conf1_n<2> conf1_n<3> conf1_n<4> conf1_n<5> conf1_n<6> conf1_n<7> conf1_p<0>
        + conf1_p<1> conf1_p<2> conf1_p<3> conf1_p<4> conf1_p<5> conf1_p<6> conf1_p<7> edge0_n
        + edge0_p edge1_n edge1_p ff<0> ff<1> ff<2> ff<3> rst rst' vdd vss
        + tdc_2e_1b_diff_np_4lin_buf
    Xi7 conf_dec<0> conf_dec<1> conf_dec<2> conf_dec<3> ff<0> ff<1> ff<2> ff<3> rand_out vdd vss
        + dec_4_conf_0
    Xi2 alarm<0> alarm<1> clk conf_maxcycles<0> conf_maxcycles<1> conf_maxcycles<2>
        + conf_maxcycles<3> conf_maxcycles<4> conf_maxcycles<5> conf_maxcycles<6> conf_maxcycles<7>
        + conf_waitcycles<0> conf_waitcycles<1> conf_waitcycles<2> conf_waitcycles<3>
        + conf_waitcycles<4> conf_waitcycles<5> conf_waitcycles<6> conf_waitcycles<7> enable_e2l
        + ff<0> ff<1> ff<2> ff<3> buf0_p<0> ready rst rst' vdd vss tdc_ready_2
.ENDS
```
