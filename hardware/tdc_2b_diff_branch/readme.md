# `tdc_2b_diff_branch` Module
![Layout](tdc_2b_diff_branch.png)

## Cell Hierarchy

`tdc_2b_diff_branch` **832** (number MOS pairs)
- `dec_6_conf_0` **38**
- `tdc_ready` **444**
- `tdc_2e_2b_diff_np_4lin_buf` **350**

## Netlist

```
.SUBCKT tdc_2b_diff_branch alarm<0> alarm<1> buf1_p<0> clk conf0_n<0> conf0_n<1> conf0_n<2>
                           + conf0_n<3> conf0_n<4> conf0_n<5> conf0_n<6> conf0_n<7> conf0_n<8>
                           + conf0_n<9> conf0_n<10> conf0_n<11> conf0_p<0> conf0_p<1> conf0_p<2>
                           + conf0_p<3> conf0_p<4> conf0_p<5> conf0_p<6> conf0_p<7> conf0_p<8>
                           + conf0_p<9> conf0_p<10> conf0_p<11> conf1_n<0> conf1_n<1> conf1_n<2>
                           + conf1_n<3> conf1_n<4> conf1_n<5> conf1_n<6> conf1_n<7> conf1_n<8>
                           + conf1_n<9> conf1_n<10> conf1_n<11> conf1_p<0> conf1_p<1> conf1_p<2>
                           + conf1_p<3> conf1_p<4> conf1_p<5> conf1_p<6> conf1_p<7> conf1_p<8>
                           + conf1_p<9> conf1_p<10> conf1_p<11> conf_dec<0> conf_dec<1> conf_dec<2>
                           + conf_dec<3> conf_dec<4> conf_dec<5> conf_maxcycles<0> conf_maxcycles<1>
                           + conf_maxcycles<2> conf_maxcycles<3> conf_maxcycles<4> conf_maxcycles<5>
                           + conf_maxcycles<6> conf_maxcycles<7> conf_waitcycles<0>
                           + conf_waitcycles<1> conf_waitcycles<2> conf_waitcycles<3>
                           + conf_waitcycles<4> conf_waitcycles<5> conf_waitcycles<6>
                           + conf_waitcycles<7> edge0_n edge0_p edge1_n edge1_p enable_e2l ff<0>
                           + ff<1> ff<2> ff<3> ff<4> ff<5> rand_out ready rst rst' vdd vss
    Xi7 conf_dec<0> conf_dec<1> conf_dec<2> conf_dec<3> conf_dec<4> conf_dec<5> ff<0> ff<1> ff<2>
        + ff<3> ff<4> ff<5> rand_out vdd vss dec_6_conf_0
    Xi2 alarm<0> alarm<1> clk conf_maxcycles<0> conf_maxcycles<1> conf_maxcycles<2>
        + conf_maxcycles<3> conf_maxcycles<4> conf_maxcycles<5> conf_maxcycles<6> conf_maxcycles<7>
        + conf_waitcycles<0> conf_waitcycles<1> conf_waitcycles<2> conf_waitcycles<3>
        + conf_waitcycles<4> conf_waitcycles<5> conf_waitcycles<6> conf_waitcycles<7> enable_e2l
        + ff<0> ff<1> ff<2> ff<3> ff<4> ff<5> buf0_p<0> ready rst rst' vdd vss tdc_ready
    Xi1 net025<0> net025<1> net025<2> buf0_p<0> buf0_p<1> buf0_p<2> net024<0> net024<1> net024<2>
        + buf1_p<0> buf1_p<1> buf1_p<2> conf0_n<0> conf0_n<1> conf0_n<2> conf0_n<3> conf0_n<4>
        + conf0_n<5> conf0_n<6> conf0_n<7> conf0_n<8> conf0_n<9> conf0_n<10> conf0_n<11> conf0_p<0>
        + conf0_p<1> conf0_p<2> conf0_p<3> conf0_p<4> conf0_p<5> conf0_p<6> conf0_p<7> conf0_p<8>
        + conf0_p<9> conf0_p<10> conf0_p<11> conf1_n<0> conf1_n<1> conf1_n<2> conf1_n<3> conf1_n<4>
        + conf1_n<5> conf1_n<6> conf1_n<7> conf1_n<8> conf1_n<9> conf1_n<10> conf1_n<11> conf1_p<0>
        + conf1_p<1> conf1_p<2> conf1_p<3> conf1_p<4> conf1_p<5> conf1_p<6> conf1_p<7> conf1_p<8>
        + conf1_p<9> conf1_p<10> conf1_p<11> edge0_n edge0_p edge1_n edge1_p ff<0> ff<1> ff<2> ff<3>
        + ff<4> ff<5> rst rst' vdd vss tdc_2e_2b_diff_np_4lin_buf
.ENDS
```
