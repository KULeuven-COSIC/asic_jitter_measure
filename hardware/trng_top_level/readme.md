# `trng_top_level` Module
![Layout](trng_top_level.png)

## Cell Hierarchy

`trng_top_level` **8370** (number MOS pairs)
- `mux2_10x` **70**
- `tdc_2b_diff_branch` **832** *x2*
- `tdc_3b_diff_branch` **962** *x2*
- `dc_collection` **566**
- `mux4` **21** *x26*
- `vdd_gate_1ma` **0** *x8*
- `dec4_inverted` **10**
- `tdc_4b_diff_branch` **1093** *x2*
- `tdc_1b_diff_branch` **702** *x2*

## Netlist

```
.SUBCKT trng_top_level alarm0<0> alarm0<1> alarm1<0> alarm1<1> alarm_dc clk conf_dec0<0>
                       + conf_dec0<1> conf_dec0<2> conf_dec0<3> conf_dec0<4> conf_dec0<5>
                       + conf_dec0<6> conf_dec0<7> conf_dec0<8> conf_dec0<9> conf_dec1<0>
                       + conf_dec1<1> conf_dec1<2> conf_dec1<3> conf_dec1<4> conf_dec1<5>
                       + conf_dec1<6> conf_dec1<7> conf_dec1<8> conf_dec1<9> conf_seldc<0>
                       + conf_seldc<1> conf_seltdc<0> conf_seltdc<1> conf_tdc00n<0> conf_tdc00n<1>
                       + conf_tdc00n<2> conf_tdc00n<3> conf_tdc00n<4> conf_tdc00n<5> conf_tdc00n<6>
                       + conf_tdc00n<7> conf_tdc00n<8> conf_tdc00n<9> conf_tdc00n<10>
                       + conf_tdc00n<11> conf_tdc00n<12> conf_tdc00n<13> conf_tdc00n<14>
                       + conf_tdc00n<15> conf_tdc00n<16> conf_tdc00n<17> conf_tdc00n<18>
                       + conf_tdc00n<19> conf_tdc00p<0> conf_tdc00p<1> conf_tdc00p<2> conf_tdc00p<3>
                       + conf_tdc00p<4> conf_tdc00p<5> conf_tdc00p<6> conf_tdc00p<7> conf_tdc00p<8>
                       + conf_tdc00p<9> conf_tdc00p<10> conf_tdc00p<11> conf_tdc00p<12>
                       + conf_tdc00p<13> conf_tdc00p<14> conf_tdc00p<15> conf_tdc00p<16>
                       + conf_tdc00p<17> conf_tdc00p<18> conf_tdc00p<19> conf_tdc01n<0>
                       + conf_tdc01n<1> conf_tdc01n<2> conf_tdc01n<3> conf_tdc01n<4> conf_tdc01n<5>
                       + conf_tdc01n<6> conf_tdc01n<7> conf_tdc01n<8> conf_tdc01n<9> conf_tdc01n<10>
                       + conf_tdc01n<11> conf_tdc01n<12> conf_tdc01n<13> conf_tdc01n<14>
                       + conf_tdc01n<15> conf_tdc01n<16> conf_tdc01n<17> conf_tdc01n<18>
                       + conf_tdc01n<19> conf_tdc01p<0> conf_tdc01p<1> conf_tdc01p<2> conf_tdc01p<3>
                       + conf_tdc01p<4> conf_tdc01p<5> conf_tdc01p<6> conf_tdc01p<7> conf_tdc01p<8>
                       + conf_tdc01p<9> conf_tdc01p<10> conf_tdc01p<11> conf_tdc01p<12>
                       + conf_tdc01p<13> conf_tdc01p<14> conf_tdc01p<15> conf_tdc01p<16>
                       + conf_tdc01p<17> conf_tdc01p<18> conf_tdc01p<19> conf_tdc4b conf_tdc10n<0>
                       + conf_tdc10n<1> conf_tdc10n<2> conf_tdc10n<3> conf_tdc10n<4> conf_tdc10n<5>
                       + conf_tdc10n<6> conf_tdc10n<7> conf_tdc10n<8> conf_tdc10n<9> conf_tdc10n<10>
                       + conf_tdc10n<11> conf_tdc10n<12> conf_tdc10n<13> conf_tdc10n<14>
                       + conf_tdc10n<15> conf_tdc10n<16> conf_tdc10n<17> conf_tdc10n<18>
                       + conf_tdc10n<19> conf_tdc10p<0> conf_tdc10p<1> conf_tdc10p<2> conf_tdc10p<3>
                       + conf_tdc10p<4> conf_tdc10p<5> conf_tdc10p<6> conf_tdc10p<7> conf_tdc10p<8>
                       + conf_tdc10p<9> conf_tdc10p<10> conf_tdc10p<11> conf_tdc10p<12>
                       + conf_tdc10p<13> conf_tdc10p<14> conf_tdc10p<15> conf_tdc10p<16>
                       + conf_tdc10p<17> conf_tdc10p<18> conf_tdc10p<19> conf_tdc11n<0>
                       + conf_tdc11n<1> conf_tdc11n<2> conf_tdc11n<3> conf_tdc11n<4> conf_tdc11n<5>
                       + conf_tdc11n<6> conf_tdc11n<7> conf_tdc11n<8> conf_tdc11n<9> conf_tdc11n<10>
                       + conf_tdc11n<11> conf_tdc11n<12> conf_tdc11n<13> conf_tdc11n<14>
                       + conf_tdc11n<15> conf_tdc11n<16> conf_tdc11n<17> conf_tdc11n<18>
                       + conf_tdc11n<19> conf_tdc11p<0> conf_tdc11p<1> conf_tdc11p<2> conf_tdc11p<3>
                       + conf_tdc11p<4> conf_tdc11p<5> conf_tdc11p<6> conf_tdc11p<7> conf_tdc11p<8>
                       + conf_tdc11p<9> conf_tdc11p<10> conf_tdc11p<11> conf_tdc11p<12>
                       + conf_tdc11p<13> conf_tdc11p<14> conf_tdc11p<15> conf_tdc11p<16>
                       + conf_tdc11p<17> conf_tdc11p<18> conf_tdc11p<19> conf_tdcmax<0>
                       + conf_tdcmax<1> conf_tdcmax<2> conf_tdcmax<3> conf_tdcmax<4> conf_tdcmax<5>
                       + conf_tdcmax<6> conf_tdcmax<7> conf_tdcwait<0> conf_tdcwait<1>
                       + conf_tdcwait<2> conf_tdcwait<3> conf_tdcwait<4> conf_tdcwait<5>
                       + conf_tdcwait<6> conf_tdcwait<7> dcedge0<1> dcedge0<2> dcedge0<3> dcedge1<1>
                       + dcedge1<2> dcedge1<3> dcedge2<1> dcedge2<2> dcedge2<3> enable_e2l
                       + enable_mero ff0<0> ff0<1> ff0<2> ff0<3> ff0<4> ff0<5> ff0<6> ff0<7> ff1<0>
                       + ff1<1> ff1<2> ff1<3> ff1<4> ff1<5> ff1<6> ff1<7> int0 int1 mero_int<0>
                       + mero_int<1> mero_int<2> rand_out0 rand_out1 ready0 ready1 rst rst'
                       + sel_dcedge<0> sel_dcedge<1> tdc0_ff4<0> tdc0_ff5<0> tdc0_ff5<3> tdc0_ff6<0>
                       + tdc0_ff6<1> tdc0_ff6<3> tdc0_ff7<0> tdc0_ff7<1> tdc0_ff7<3> tdc1_ff4<0>
                       + tdc1_ff5<0> tdc1_ff5<3> tdc1_ff6<0> tdc1_ff6<1> tdc1_ff6<3> tdc1_ff7<0>
                       + tdc1_ff7<1> tdc1_ff7<3> vdd_core vdd_dc vdd_tdc vss
    Xi81 tdc03_ff<0> tdc03_ff<1> tdc03_ff<2> tdc03_ff<3> tdc03_ff<4> tdc03_ff<5> tdc03_ff<6>
         + tdc03_ff<7> tdc03_ff<8> tdc03_ff<9> tdc13_ff<0> tdc13_ff<1> tdc13_ff<2> tdc13_ff<3>
         + tdc13_ff<4> tdc13_ff<5> tdc13_ff<6> tdc13_ff<7> tdc13_ff<8> tdc13_ff<9> tdc0_ff0<3>
         + tdc0_ff1<3> tdc0_ff2<3> tdc0_ff3<3> tdc0_ff4<3> tdc1_ff0<3> tdc1_ff1<3> tdc1_ff2<3>
         + tdc1_ff3<3> tdc1_ff4<3> conf_tdc4b vdd_core vss mux2_10x
    Xi77 tdc1_alarm0<1> tdc1_alarm1<1> tdc1_int<1> clk conf_tdc10n<0> conf_tdc10n<1> conf_tdc10n<2>
         + conf_tdc10n<3> conf_tdc10n<4> conf_tdc10n<5> conf_tdc10n<6> conf_tdc10n<7> conf_tdc10n<8>
         + conf_tdc10n<9> conf_tdc10n<10> conf_tdc10n<11> conf_tdc10p<0> conf_tdc10p<1>
         + conf_tdc10p<2> conf_tdc10p<3> conf_tdc10p<4> conf_tdc10p<5> conf_tdc10p<6> conf_tdc10p<7>
         + conf_tdc10p<8> conf_tdc10p<9> conf_tdc10p<10> conf_tdc10p<11> conf_tdc11n<0>
         + conf_tdc11n<1> conf_tdc11n<2> conf_tdc11n<3> conf_tdc11n<4> conf_tdc11n<5> conf_tdc11n<6>
         + conf_tdc11n<7> conf_tdc11n<8> conf_tdc11n<9> conf_tdc11n<10> conf_tdc11n<11>
         + conf_tdc11p<0> conf_tdc11p<1> conf_tdc11p<2> conf_tdc11p<3> conf_tdc11p<4> conf_tdc11p<5>
         + conf_tdc11p<6> conf_tdc11p<7> conf_tdc11p<8> conf_tdc11p<9> conf_tdc11p<10>
         + conf_tdc11p<11> conf_dec1<0> conf_dec1<1> conf_dec1<2> conf_dec1<3> conf_dec1<4>
         + conf_dec1<5> conf_tdcmax<0> conf_tdcmax<1> conf_tdcmax<2> conf_tdcmax<3> conf_tdcmax<4>
         + conf_tdcmax<5> conf_tdcmax<6> conf_tdcmax<7> conf_tdcwait<0> conf_tdcwait<1>
         + conf_tdcwait<2> conf_tdcwait<3> conf_tdcwait<4> conf_tdcwait<5> conf_tdcwait<6>
         + conf_tdcwait<7> edge1_n edge1_p edge2_n edge2_p enable_e2l tdc1_ff0<1> tdc1_ff1<1>
         + tdc1_ff2<1> tdc1_ff3<1> tdc1_ff4<1> tdc1_ff5<1> tdc1_randout<1> tdc1_ready<1> rst rst'
         + vdd_tdc_int1<1> vss tdc_2b_diff_branch
    Xi73 tdc0_alarm0<1> tdc0_alarm1<1> tdc0_int<1> clk conf_tdc00n<0> conf_tdc00n<1> conf_tdc00n<2>
         + conf_tdc00n<3> conf_tdc00n<4> conf_tdc00n<5> conf_tdc00n<6> conf_tdc00n<7> conf_tdc00n<8>
         + conf_tdc00n<9> conf_tdc00n<10> conf_tdc00n<11> conf_tdc00p<0> conf_tdc00p<1>
         + conf_tdc00p<2> conf_tdc00p<3> conf_tdc00p<4> conf_tdc00p<5> conf_tdc00p<6> conf_tdc00p<7>
         + conf_tdc00p<8> conf_tdc00p<9> conf_tdc00p<10> conf_tdc00p<11> conf_tdc01n<0>
         + conf_tdc01n<1> conf_tdc01n<2> conf_tdc01n<3> conf_tdc01n<4> conf_tdc01n<5> conf_tdc01n<6>
         + conf_tdc01n<7> conf_tdc01n<8> conf_tdc01n<9> conf_tdc01n<10> conf_tdc01n<11>
         + conf_tdc01p<0> conf_tdc01p<1> conf_tdc01p<2> conf_tdc01p<3> conf_tdc01p<4> conf_tdc01p<5>
         + conf_tdc01p<6> conf_tdc01p<7> conf_tdc01p<8> conf_tdc01p<9> conf_tdc01p<10>
         + conf_tdc01p<11> conf_dec0<0> conf_dec0<1> conf_dec0<2> conf_dec0<3> conf_dec0<4>
         + conf_dec0<5> conf_tdcmax<0> conf_tdcmax<1> conf_tdcmax<2> conf_tdcmax<3> conf_tdcmax<4>
         + conf_tdcmax<5> conf_tdcmax<6> conf_tdcmax<7> conf_tdcwait<0> conf_tdcwait<1>
         + conf_tdcwait<2> conf_tdcwait<3> conf_tdcwait<4> conf_tdcwait<5> conf_tdcwait<6>
         + conf_tdcwait<7> edge0_n edge0_p edge1_n edge1_p enable_e2l tdc0_ff0<1> tdc0_ff1<1>
         + tdc0_ff2<1> tdc0_ff3<1> tdc0_ff4<1> tdc0_ff5<1> tdc0_randout<1> tdc0_ready<1> rst rst'
         + vdd_tdc_int0<1> vss tdc_2b_diff_branch
    Xi78 tdc1_alarm0<2> tdc1_alarm1<2> tdc1_int<2> clk conf_tdc10n<0> conf_tdc10n<1> conf_tdc10n<2>
         + conf_tdc10n<3> conf_tdc10n<4> conf_tdc10n<5> conf_tdc10n<6> conf_tdc10n<7> conf_tdc10n<8>
         + conf_tdc10n<9> conf_tdc10n<10> conf_tdc10n<11> conf_tdc10n<12> conf_tdc10n<13>
         + conf_tdc10n<14> conf_tdc10n<15> conf_tdc10p<0> conf_tdc10p<1> conf_tdc10p<2>
         + conf_tdc10p<3> conf_tdc10p<4> conf_tdc10p<5> conf_tdc10p<6> conf_tdc10p<7> conf_tdc10p<8>
         + conf_tdc10p<9> conf_tdc10p<10> conf_tdc10p<11> conf_tdc10p<12> conf_tdc10p<13>
         + conf_tdc10p<14> conf_tdc10p<15> conf_tdc11n<0> conf_tdc11n<1> conf_tdc11n<2>
         + conf_tdc11n<3> conf_tdc11n<4> conf_tdc11n<5> conf_tdc11n<6> conf_tdc11n<7> conf_tdc11n<8>
         + conf_tdc11n<9> conf_tdc11n<10> conf_tdc11n<11> conf_tdc11n<12> conf_tdc11n<13>
         + conf_tdc11n<14> conf_tdc11n<15> conf_tdc11p<0> conf_tdc11p<1> conf_tdc11p<2>
         + conf_tdc11p<3> conf_tdc11p<4> conf_tdc11p<5> conf_tdc11p<6> conf_tdc11p<7> conf_tdc11p<8>
         + conf_tdc11p<9> conf_tdc11p<10> conf_tdc11p<11> conf_tdc11p<12> conf_tdc11p<13>
         + conf_tdc11p<14> conf_tdc11p<15> conf_dec1<0> conf_dec1<1> conf_dec1<2> conf_dec1<3>
         + conf_dec1<4> conf_dec1<5> conf_dec1<6> conf_dec1<7> conf_tdcmax<0> conf_tdcmax<1>
         + conf_tdcmax<2> conf_tdcmax<3> conf_tdcmax<4> conf_tdcmax<5> conf_tdcmax<6> conf_tdcmax<7>
         + conf_tdcwait<0> conf_tdcwait<1> conf_tdcwait<2> conf_tdcwait<3> conf_tdcwait<4>
         + conf_tdcwait<5> conf_tdcwait<6> conf_tdcwait<7> edge1_n edge1_p edge2_n edge2_p
         + enable_e2l tdc1_ff0<2> tdc1_ff1<2> tdc1_ff2<2> tdc1_ff3<2> tdc1_ff4<2> tdc1_ff5<2>
         + tdc1_ff6<2> tdc1_ff7<2> tdc1_randout<2> tdc1_ready<2> rst rst' vdd_tdc_int1<2> vss
         + tdc_3b_diff_branch
    Xi74 tdc0_alarm0<2> tdc0_alarm1<2> tdc0_int<2> clk conf_tdc00n<0> conf_tdc00n<1> conf_tdc00n<2>
         + conf_tdc00n<3> conf_tdc00n<4> conf_tdc00n<5> conf_tdc00n<6> conf_tdc00n<7> conf_tdc00n<8>
         + conf_tdc00n<9> conf_tdc00n<10> conf_tdc00n<11> conf_tdc00n<12> conf_tdc00n<13>
         + conf_tdc00n<14> conf_tdc00n<15> conf_tdc00p<0> conf_tdc00p<1> conf_tdc00p<2>
         + conf_tdc00p<3> conf_tdc00p<4> conf_tdc00p<5> conf_tdc00p<6> conf_tdc00p<7> conf_tdc00p<8>
         + conf_tdc00p<9> conf_tdc00p<10> conf_tdc00p<11> conf_tdc00p<12> conf_tdc00p<13>
         + conf_tdc00p<14> conf_tdc00p<15> conf_tdc01n<0> conf_tdc01n<1> conf_tdc01n<2>
         + conf_tdc01n<3> conf_tdc01n<4> conf_tdc01n<5> conf_tdc01n<6> conf_tdc01n<7> conf_tdc01n<8>
         + conf_tdc01n<9> conf_tdc01n<10> conf_tdc01n<11> conf_tdc01n<12> conf_tdc01n<13>
         + conf_tdc01n<14> conf_tdc01n<15> conf_tdc01p<0> conf_tdc01p<1> conf_tdc01p<2>
         + conf_tdc01p<3> conf_tdc01p<4> conf_tdc01p<5> conf_tdc01p<6> conf_tdc01p<7> conf_tdc01p<8>
         + conf_tdc01p<9> conf_tdc01p<10> conf_tdc01p<11> conf_tdc01p<12> conf_tdc01p<13>
         + conf_tdc01p<14> conf_tdc01p<15> conf_dec0<0> conf_dec0<1> conf_dec0<2> conf_dec0<3>
         + conf_dec0<4> conf_dec0<5> conf_dec0<6> conf_dec0<7> conf_tdcmax<0> conf_tdcmax<1>
         + conf_tdcmax<2> conf_tdcmax<3> conf_tdcmax<4> conf_tdcmax<5> conf_tdcmax<6> conf_tdcmax<7>
         + conf_tdcwait<0> conf_tdcwait<1> conf_tdcwait<2> conf_tdcwait<3> conf_tdcwait<4>
         + conf_tdcwait<5> conf_tdcwait<6> conf_tdcwait<7> edge0_n edge0_p edge1_n edge1_p
         + enable_e2l tdc0_ff0<2> tdc0_ff1<2> tdc0_ff2<2> tdc0_ff3<2> tdc0_ff4<2> tdc0_ff5<2>
         + tdc0_ff6<2> tdc0_ff7<2> tdc0_randout<2> tdc0_ready<2> rst rst' vdd_tdc_int0<2> vss
         + tdc_3b_diff_branch
    Xi80 alarm_dc conf_seldc<0> conf_seldc<1> dcedge0<1> dcedge0<2> dcedge0<3> dcedge1<1> dcedge1<2>
         + dcedge1<3> dcedge2<1> dcedge2<2> dcedge2<3> edge0_n edge0_p edge1_n edge1_p edge2_n
         + edge2_p enable_e2l enable_mero mero_int<0> mero_int<1> mero_int<2> rst rst' sel_dcedge<0>
         + sel_dcedge<1> vdd_core vdd_dc vss dc_collection
    Xi56 tdc1_ff7<0> tdc1_ff7<1> tdc1_ff7<2> tdc1_ff7<3> ff1<7> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi55 tdc1_ff6<0> tdc1_ff6<1> tdc1_ff6<2> tdc1_ff6<3> ff1<6> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi54 tdc1_ff5<0> tdc1_ff5<1> tdc1_ff5<2> tdc1_ff5<3> ff1<5> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi53 tdc1_ff4<0> tdc1_ff4<1> tdc1_ff4<2> tdc1_ff4<3> ff1<4> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi52 tdc1_ff3<0> tdc1_ff3<1> tdc1_ff3<2> tdc1_ff3<3> ff1<3> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi51 tdc1_ff2<0> tdc1_ff2<1> tdc1_ff2<2> tdc1_ff2<3> ff1<2> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi50 tdc1_ff1<0> tdc1_ff1<1> tdc1_ff1<2> tdc1_ff1<3> ff1<1> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi49 tdc0_ff7<0> tdc0_ff7<1> tdc0_ff7<2> tdc0_ff7<3> ff0<7> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi48 tdc0_ff6<0> tdc0_ff6<1> tdc0_ff6<2> tdc0_ff6<3> ff0<6> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi47 tdc0_ff5<0> tdc0_ff5<1> tdc0_ff5<2> tdc0_ff5<3> ff0<5> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi46 tdc0_ff4<0> tdc0_ff4<1> tdc0_ff4<2> tdc0_ff4<3> ff0<4> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi45 tdc0_ff3<0> tdc0_ff3<1> tdc0_ff3<2> tdc0_ff3<3> ff0<3> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi44 tdc0_ff2<0> tdc0_ff2<1> tdc0_ff2<2> tdc0_ff2<3> ff0<2> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi43 tdc0_ff1<0> tdc0_ff1<1> tdc0_ff1<2> tdc0_ff1<3> ff0<1> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi42 tdc1_randout<0> tdc1_randout<1> tdc1_randout<2> tdc1_randout<3> rand_out1 conf_seltdc<0>
         + conf_seltdc<1> vdd_core vss mux4
    Xi41 tdc1_ff0<0> tdc1_ff0<1> tdc1_ff0<2> tdc1_ff0<3> ff1<0> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi40 tdc1_alarm1<0> tdc1_alarm1<1> tdc1_alarm1<2> tdc1_alarm1<3> alarm1<1> conf_seltdc<0>
         + conf_seltdc<1> vdd_core vss mux4
    Xi39 tdc1_alarm0<0> tdc1_alarm0<1> tdc1_alarm0<2> tdc1_alarm0<3> alarm1<0> conf_seltdc<0>
         + conf_seltdc<1> vdd_core vss mux4
    Xi38 tdc1_int<0> tdc1_int<1> tdc1_int<2> tdc1_int<3> int1 conf_seltdc<0> conf_seltdc<1> vdd_core
         + vss mux4
    Xi37 tdc1_ready<0> tdc1_ready<1> tdc1_ready<2> tdc1_ready<3> ready1 conf_seltdc<0>
         + conf_seltdc<1> vdd_core vss mux4
    Xi36 tdc0_ff0<0> tdc0_ff0<1> tdc0_ff0<2> tdc0_ff0<3> ff0<0> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss mux4
    Xi35 tdc0_alarm1<0> tdc0_alarm1<1> tdc0_alarm1<2> tdc0_alarm1<3> alarm0<1> conf_seltdc<0>
         + conf_seltdc<1> vdd_core vss mux4
    Xi34 tdc0_alarm0<0> tdc0_alarm0<1> tdc0_alarm0<2> tdc0_alarm0<3> alarm0<0> conf_seltdc<0>
         + conf_seltdc<1> vdd_core vss mux4
    Xi33 tdc0_int<0> tdc0_int<1> tdc0_int<2> tdc0_int<3> int0 conf_seltdc<0> conf_seltdc<1> vdd_core
         + vss mux4
    Xi32 tdc0_ready<0> tdc0_ready<1> tdc0_ready<2> tdc0_ready<3> ready0 conf_seltdc<0>
         + conf_seltdc<1> vdd_core vss mux4
    Xi31 tdc0_randout<0> tdc0_randout<1> tdc0_randout<2> tdc0_randout<3> rand_out0 conf_seltdc<0>
         + conf_seltdc<1> vdd_core vss mux4
    Xi69 seltdc_dec<3> vdd_tdc vdd_tdc_int1<3> vss vdd_gate_1ma
    Xi68 seltdc_dec<3> vdd_tdc vdd_tdc_int0<3> vss vdd_gate_1ma
    Xi67 seltdc_dec<2> vdd_tdc vdd_tdc_int0<2> vss vdd_gate_1ma
    Xi66 seltdc_dec<2> vdd_tdc vdd_tdc_int1<2> vss vdd_gate_1ma
    Xi63 seltdc_dec<1> vdd_tdc vdd_tdc_int0<1> vss vdd_gate_1ma
    Xi62 seltdc_dec<1> vdd_tdc vdd_tdc_int1<1> vss vdd_gate_1ma
    Xi58 seltdc_dec<0> vdd_tdc vdd_tdc_int1<0> vss vdd_gate_1ma
    Xi57 seltdc_dec<0> vdd_tdc vdd_tdc_int0<0> vss vdd_gate_1ma
    Xi59 seltdc_dec<0> seltdc_dec<1> seltdc_dec<2> seltdc_dec<3> conf_seltdc<0> conf_seltdc<1>
         + vdd_core vss dec4_inverted
    Xi75 tdc0_alarm0<3> tdc0_alarm1<3> tdc0_int<3> clk conf_tdc00n<0> conf_tdc00n<1> conf_tdc00n<2>
         + conf_tdc00n<3> conf_tdc00n<4> conf_tdc00n<5> conf_tdc00n<6> conf_tdc00n<7> conf_tdc00n<8>
         + conf_tdc00n<9> conf_tdc00n<10> conf_tdc00n<11> conf_tdc00n<12> conf_tdc00n<13>
         + conf_tdc00n<14> conf_tdc00n<15> conf_tdc00n<16> conf_tdc00n<17> conf_tdc00n<18>
         + conf_tdc00n<19> conf_tdc00p<0> conf_tdc00p<1> conf_tdc00p<2> conf_tdc00p<3>
         + conf_tdc00p<4> conf_tdc00p<5> conf_tdc00p<6> conf_tdc00p<7> conf_tdc00p<8> conf_tdc00p<9>
         + conf_tdc00p<10> conf_tdc00p<11> conf_tdc00p<12> conf_tdc00p<13> conf_tdc00p<14>
         + conf_tdc00p<15> conf_tdc00p<16> conf_tdc00p<17> conf_tdc00p<18> conf_tdc00p<19>
         + conf_tdc01n<0> conf_tdc01n<1> conf_tdc01n<2> conf_tdc01n<3> conf_tdc01n<4> conf_tdc01n<5>
         + conf_tdc01n<6> conf_tdc01n<7> conf_tdc01n<8> conf_tdc01n<9> conf_tdc01n<10>
         + conf_tdc01n<11> conf_tdc01n<12> conf_tdc01n<13> conf_tdc01n<14> conf_tdc01n<15>
         + conf_tdc01n<16> conf_tdc01n<17> conf_tdc01n<18> conf_tdc01n<19> conf_tdc01p<0>
         + conf_tdc01p<1> conf_tdc01p<2> conf_tdc01p<3> conf_tdc01p<4> conf_tdc01p<5> conf_tdc01p<6>
         + conf_tdc01p<7> conf_tdc01p<8> conf_tdc01p<9> conf_tdc01p<10> conf_tdc01p<11>
         + conf_tdc01p<12> conf_tdc01p<13> conf_tdc01p<14> conf_tdc01p<15> conf_tdc01p<16>
         + conf_tdc01p<17> conf_tdc01p<18> conf_tdc01p<19> conf_dec0<0> conf_dec0<1> conf_dec0<2>
         + conf_dec0<3> conf_dec0<4> conf_dec0<5> conf_dec0<6> conf_dec0<7> conf_dec0<8>
         + conf_dec0<9> conf_tdcmax<0> conf_tdcmax<1> conf_tdcmax<2> conf_tdcmax<3> conf_tdcmax<4>
         + conf_tdcmax<5> conf_tdcmax<6> conf_tdcmax<7> conf_tdcwait<0> conf_tdcwait<1>
         + conf_tdcwait<2> conf_tdcwait<3> conf_tdcwait<4> conf_tdcwait<5> conf_tdcwait<6>
         + conf_tdcwait<7> edge0_n edge0_p edge1_n edge1_p enable_e2l tdc03_ff<0> tdc03_ff<1>
         + tdc03_ff<2> tdc03_ff<3> tdc03_ff<4> tdc03_ff<5> tdc03_ff<6> tdc03_ff<7> tdc03_ff<8>
         + tdc03_ff<9> tdc0_randout<3> tdc0_ready<3> rst rst' vdd_tdc_int0<3> vss tdc_4b_diff_branch
    Xi79 tdc1_alarm0<3> tdc1_alarm1<3> tdc1_int<3> clk conf_tdc10n<0> conf_tdc10n<1> conf_tdc10n<2>
         + conf_tdc10n<3> conf_tdc10n<4> conf_tdc10n<5> conf_tdc10n<6> conf_tdc10n<7> conf_tdc10n<8>
         + conf_tdc10n<9> conf_tdc10n<10> conf_tdc10n<11> conf_tdc10n<12> conf_tdc10n<13>
         + conf_tdc10n<14> conf_tdc10n<15> conf_tdc10n<16> conf_tdc10n<17> conf_tdc10n<18>
         + conf_tdc10n<19> conf_tdc10p<0> conf_tdc10p<1> conf_tdc10p<2> conf_tdc10p<3>
         + conf_tdc10p<4> conf_tdc10p<5> conf_tdc10p<6> conf_tdc10p<7> conf_tdc10p<8> conf_tdc10p<9>
         + conf_tdc10p<10> conf_tdc10p<11> conf_tdc10p<12> conf_tdc10p<13> conf_tdc10p<14>
         + conf_tdc10p<15> conf_tdc10p<16> conf_tdc10p<17> conf_tdc10p<18> conf_tdc10p<19>
         + conf_tdc11n<0> conf_tdc11n<1> conf_tdc11n<2> conf_tdc11n<3> conf_tdc11n<4> conf_tdc11n<5>
         + conf_tdc11n<6> conf_tdc11n<7> conf_tdc11n<8> conf_tdc11n<9> conf_tdc11n<10>
         + conf_tdc11n<11> conf_tdc11n<12> conf_tdc11n<13> conf_tdc11n<14> conf_tdc11n<15>
         + conf_tdc11n<16> conf_tdc11n<17> conf_tdc11n<18> conf_tdc11n<19> conf_tdc11p<0>
         + conf_tdc11p<1> conf_tdc11p<2> conf_tdc11p<3> conf_tdc11p<4> conf_tdc11p<5> conf_tdc11p<6>
         + conf_tdc11p<7> conf_tdc11p<8> conf_tdc11p<9> conf_tdc11p<10> conf_tdc11p<11>
         + conf_tdc11p<12> conf_tdc11p<13> conf_tdc11p<14> conf_tdc11p<15> conf_tdc11p<16>
         + conf_tdc11p<17> conf_tdc11p<18> conf_tdc11p<19> conf_dec1<0> conf_dec1<1> conf_dec1<2>
         + conf_dec1<3> conf_dec1<4> conf_dec1<5> conf_dec1<6> conf_dec1<7> conf_dec1<8>
         + conf_dec1<9> conf_tdcmax<0> conf_tdcmax<1> conf_tdcmax<2> conf_tdcmax<3> conf_tdcmax<4>
         + conf_tdcmax<5> conf_tdcmax<6> conf_tdcmax<7> conf_tdcwait<0> conf_tdcwait<1>
         + conf_tdcwait<2> conf_tdcwait<3> conf_tdcwait<4> conf_tdcwait<5> conf_tdcwait<6>
         + conf_tdcwait<7> edge1_n edge1_p edge2_n edge2_p enable_e2l tdc13_ff<0> tdc13_ff<1>
         + tdc13_ff<2> tdc13_ff<3> tdc13_ff<4> tdc13_ff<5> tdc13_ff<6> tdc13_ff<7> tdc13_ff<8>
         + tdc13_ff<9> tdc1_randout<3> tdc1_ready<3> rst rst' vdd_tdc_int1<3> vss tdc_4b_diff_branch
    Xi72 tdc0_alarm0<0> tdc0_alarm1<0> tdc0_int<0> clk conf_tdc00n<0> conf_tdc00n<1> conf_tdc00n<2>
         + conf_tdc00n<3> conf_tdc00n<4> conf_tdc00n<5> conf_tdc00n<6> conf_tdc00n<7> conf_tdc00p<0>
         + conf_tdc00p<1> conf_tdc00p<2> conf_tdc00p<3> conf_tdc00p<4> conf_tdc00p<5> conf_tdc00p<6>
         + conf_tdc00p<7> conf_tdc01n<0> conf_tdc01n<1> conf_tdc01n<2> conf_tdc01n<3> conf_tdc01n<4>
         + conf_tdc01n<5> conf_tdc01n<6> conf_tdc01n<7> conf_tdc01p<0> conf_tdc01p<1> conf_tdc01p<2>
         + conf_tdc01p<3> conf_tdc01p<4> conf_tdc01p<5> conf_tdc01p<6> conf_tdc01p<7> conf_dec0<0>
         + conf_dec0<1> conf_dec0<2> conf_dec0<3> conf_tdcmax<0> conf_tdcmax<1> conf_tdcmax<2>
         + conf_tdcmax<3> conf_tdcmax<4> conf_tdcmax<5> conf_tdcmax<6> conf_tdcmax<7>
         + conf_tdcwait<0> conf_tdcwait<1> conf_tdcwait<2> conf_tdcwait<3> conf_tdcwait<4>
         + conf_tdcwait<5> conf_tdcwait<6> conf_tdcwait<7> edge0_n edge0_p edge1_n edge1_p
         + enable_e2l tdc0_ff0<0> tdc0_ff1<0> tdc0_ff2<0> tdc0_ff3<0> tdc0_randout<0> tdc0_ready<0>
         + rst rst' vdd_tdc_int0<0> vss tdc_1b_diff_branch
    Xi76 tdc1_alarm0<0> tdc1_alarm1<0> tdc1_int<0> clk conf_tdc10n<0> conf_tdc10n<1> conf_tdc10n<2>
         + conf_tdc10n<3> conf_tdc10n<4> conf_tdc10n<5> conf_tdc10n<6> conf_tdc10n<7> conf_tdc10p<0>
         + conf_tdc10p<1> conf_tdc10p<2> conf_tdc10p<3> conf_tdc10p<4> conf_tdc10p<5> conf_tdc10p<6>
         + conf_tdc10p<7> conf_tdc11n<0> conf_tdc11n<1> conf_tdc11n<2> conf_tdc11n<3> conf_tdc11n<4>
         + conf_tdc11n<5> conf_tdc11n<6> conf_tdc11n<7> conf_tdc11p<0> conf_tdc11p<1> conf_tdc11p<2>
         + conf_tdc11p<3> conf_tdc11p<4> conf_tdc11p<5> conf_tdc11p<6> conf_tdc11p<7> conf_dec1<0>
         + conf_dec1<1> conf_dec1<2> conf_dec1<3> conf_tdcmax<0> conf_tdcmax<1> conf_tdcmax<2>
         + conf_tdcmax<3> conf_tdcmax<4> conf_tdcmax<5> conf_tdcmax<6> conf_tdcmax<7>
         + conf_tdcwait<0> conf_tdcwait<1> conf_tdcwait<2> conf_tdcwait<3> conf_tdcwait<4>
         + conf_tdcwait<5> conf_tdcwait<6> conf_tdcwait<7> edge1_n edge1_p edge2_n edge2_p
         + enable_e2l tdc1_ff0<0> tdc1_ff1<0> tdc1_ff2<0> tdc1_ff3<0> tdc1_randout<0> tdc1_ready<0>
         + rst rst' vdd_tdc_int1<0> vss tdc_1b_diff_branch
.ENDS
```
