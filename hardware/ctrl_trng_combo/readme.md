# `ctrl_trng_combo` Module
![Layout](ctrl_trng_combo.png)

## Cell Hierarchy

`ctrl_trng_combo` **15594** (number MOS pairs)
- `trng_top_level` **8370**
- `conf_top_level` **2491**
- `bit_top_level` **1485**
- `async_top_level` **2295**
- `mux4` **21** *x7*
- `buffer_large` **4** *x10*
- `buffer` **2** *x9*
- `freq_scaler16` **240**
- `mux16` **105**
- `inv` **1**
- `clk_manager` **377**
- `mux2` **7**
- `one_to_18` **18**

## Netlist

```
.SUBCKT ctrl_trng_combo conf_clk<0> conf_clk<1> conf_clk<2> conf_clk<3> conf_clk<4> conf_clk<5>
                        + conf_clk<6> conf_clk<7> conf_clk<8> conf_clk<9> conf_clk<10> conf_clk<11>
                        + conf_clkenable conf_clksel conf_ctrlsel<0> conf_ctrlsel<1>
                        + conf_dcedgesel<0> conf_dcedgesel<1> conf_dec0<0> conf_dec0<1> conf_dec0<2>
                        + conf_dec0<3> conf_dec0<4> conf_dec0<5> conf_dec0<6> conf_dec0<7>
                        + conf_dec0<8> conf_dec0<9> conf_dec1<0> conf_dec1<1> conf_dec1<2>
                        + conf_dec1<3> conf_dec1<4> conf_dec1<5> conf_dec1<6> conf_dec1<7>
                        + conf_dec1<8> conf_dec1<9> conf_rooutfreqsel<0> conf_rooutfreqsel<1>
                        + conf_rooutfreqsel<2> conf_rooutfreqsel<3> conf_rooutsel<0>
                        + conf_rooutsel<1> conf_seldc<0> conf_seldc<1> conf_seltdc<0> conf_seltdc<1>
                        + conf_sendfree conf_statecnt<0> conf_statecnt<1> conf_statecnt<2>
                        + conf_statecnt<3> conf_statecnt<4> conf_statecnt<5> conf_statecnt<6>
                        + conf_statecnt<7> conf_statecnt<8> conf_statecnt<9> conf_statecnt<10>
                        + conf_statecnt<11> conf_statecnt<12> conf_statecnt<13> conf_statecnt<14>
                        + conf_statecnt<15> conf_tdc00n<0> conf_tdc00n<1> conf_tdc00n<2>
                        + conf_tdc00n<3> conf_tdc00n<4> conf_tdc00n<5> conf_tdc00n<6> conf_tdc00n<7>
                        + conf_tdc00n<8> conf_tdc00n<9> conf_tdc00n<10> conf_tdc00n<11>
                        + conf_tdc00n<12> conf_tdc00n<13> conf_tdc00n<14> conf_tdc00n<15>
                        + conf_tdc00n<16> conf_tdc00n<17> conf_tdc00n<18> conf_tdc00n<19>
                        + conf_tdc00p<0> conf_tdc00p<1> conf_tdc00p<2> conf_tdc00p<3> conf_tdc00p<4>
                        + conf_tdc00p<5> conf_tdc00p<6> conf_tdc00p<7> conf_tdc00p<8> conf_tdc00p<9>
                        + conf_tdc00p<10> conf_tdc00p<11> conf_tdc00p<12> conf_tdc00p<13>
                        + conf_tdc00p<14> conf_tdc00p<15> conf_tdc00p<16> conf_tdc00p<17>
                        + conf_tdc00p<18> conf_tdc00p<19> conf_tdc01n<0> conf_tdc01n<1>
                        + conf_tdc01n<2> conf_tdc01n<3> conf_tdc01n<4> conf_tdc01n<5> conf_tdc01n<6>
                        + conf_tdc01n<7> conf_tdc01n<8> conf_tdc01n<9> conf_tdc01n<10>
                        + conf_tdc01n<11> conf_tdc01n<12> conf_tdc01n<13> conf_tdc01n<14>
                        + conf_tdc01n<15> conf_tdc01n<16> conf_tdc01n<17> conf_tdc01n<18>
                        + conf_tdc01n<19> conf_tdc01p<0> conf_tdc01p<1> conf_tdc01p<2>
                        + conf_tdc01p<3> conf_tdc01p<4> conf_tdc01p<5> conf_tdc01p<6> conf_tdc01p<7>
                        + conf_tdc01p<8> conf_tdc01p<9> conf_tdc01p<10> conf_tdc01p<11>
                        + conf_tdc01p<12> conf_tdc01p<13> conf_tdc01p<14> conf_tdc01p<15>
                        + conf_tdc01p<16> conf_tdc01p<17> conf_tdc01p<18> conf_tdc01p<19> conf_tdc4b
                        + conf_tdc10n<0> conf_tdc10n<1> conf_tdc10n<2> conf_tdc10n<3> conf_tdc10n<4>
                        + conf_tdc10n<5> conf_tdc10n<6> conf_tdc10n<7> conf_tdc10n<8> conf_tdc10n<9>
                        + conf_tdc10n<10> conf_tdc10n<11> conf_tdc10n<12> conf_tdc10n<13>
                        + conf_tdc10n<14> conf_tdc10n<15> conf_tdc10n<16> conf_tdc10n<17>
                        + conf_tdc10n<18> conf_tdc10n<19> conf_tdc10p<0> conf_tdc10p<1>
                        + conf_tdc10p<2> conf_tdc10p<3> conf_tdc10p<4> conf_tdc10p<5> conf_tdc10p<6>
                        + conf_tdc10p<7> conf_tdc10p<8> conf_tdc10p<9> conf_tdc10p<10>
                        + conf_tdc10p<11> conf_tdc10p<12> conf_tdc10p<13> conf_tdc10p<14>
                        + conf_tdc10p<15> conf_tdc10p<16> conf_tdc10p<17> conf_tdc10p<18>
                        + conf_tdc10p<19> conf_tdc11n<0> conf_tdc11n<1> conf_tdc11n<2>
                        + conf_tdc11n<3> conf_tdc11n<4> conf_tdc11n<5> conf_tdc11n<6> conf_tdc11n<7>
                        + conf_tdc11n<8> conf_tdc11n<9> conf_tdc11n<10> conf_tdc11n<11>
                        + conf_tdc11n<12> conf_tdc11n<13> conf_tdc11n<14> conf_tdc11n<15>
                        + conf_tdc11n<16> conf_tdc11n<17> conf_tdc11n<18> conf_tdc11n<19>
                        + conf_tdc11p<0> conf_tdc11p<1> conf_tdc11p<2> conf_tdc11p<3> conf_tdc11p<4>
                        + conf_tdc11p<5> conf_tdc11p<6> conf_tdc11p<7> conf_tdc11p<8> conf_tdc11p<9>
                        + conf_tdc11p<10> conf_tdc11p<11> conf_tdc11p<12> conf_tdc11p<13>
                        + conf_tdc11p<14> conf_tdc11p<15> conf_tdc11p<16> conf_tdc11p<17>
                        + conf_tdc11p<18> conf_tdc11p<19> conf_tdccal<0> conf_tdccal<1>
                        + conf_tdccal<2> conf_tdccal<3> conf_tdccal<4> conf_tdccal<5> conf_tdccal<6>
                        + conf_tdccal<7> conf_tdccal<8> conf_tdccal<9> conf_tdccnt<0> conf_tdccnt<1>
                        + conf_tdccnt<2> conf_tdccnt<3> conf_tdccnt<4> conf_tdccnt<5> conf_tdccnt<6>
                        + conf_tdccnt<7> conf_tdccnt<8> conf_tdccnt<9> conf_tdccnt<10>
                        + conf_tdccnt<11> conf_tdccnt<12> conf_tdccnt<13> conf_tdccnt<14>
                        + conf_tdccnt<15> conf_tdcmax<0> conf_tdcmax<1> conf_tdcmax<2>
                        + conf_tdcmax<3> conf_tdcmax<4> conf_tdcmax<5> conf_tdcmax<6> conf_tdcmax<7>
                        + conf_tdcwait<0> conf_tdcwait<1> conf_tdcwait<2> conf_tdcwait<3>
                        + conf_tdcwait<4> conf_tdcwait<5> conf_tdcwait<6> conf_tdcwait<7> data_out
                        + data_out_i<3> data_ready data_ready_i<3> enable_e2l enable_e2l_i<3>
                        + ext_clk ro_enable ro_enable_i<3> ro_out rst scan_out<0> scan_out<1>
                        + scan_out<2> scan_out<3> scan_out<4> scan_out<5> scan_out<6> scan_out<7>
                        + scan_out<8> scan_out<9> scan_out<10> scan_out<11> scan_out<12>
                        + scan_out<13> scan_out<14> scan_out<15> scan_out<16> scan_out<17>
                        + scan_out<18> scan_out<19> scan_out<20> scan_out<21> scan_out<22> ser_clk
                        + trng_rst trng_rst'_i<3> trng_rst_i<3> vdd_core vdd_dc vdd_tdc vss
    Xi0 alarm0<0> alarm0<1> alarm1<0> alarm1<1> alarm_dc clk conf_dec0<0> conf_dec0<1> conf_dec0<2>
        + conf_dec0<3> conf_dec0<4> conf_dec0<5> conf_dec0<6> conf_dec0<7> conf_dec0<8> conf_dec0<9>
        + conf_dec1<0> conf_dec1<1> conf_dec1<2> conf_dec1<3> conf_dec1<4> conf_dec1<5> conf_dec1<6>
        + conf_dec1<7> conf_dec1<8> conf_dec1<9> conf_seldc<0> conf_seldc<1> conf_seltdc<0>
        + conf_seltdc<1> conf_tdc00n<0> conf_tdc00n<1> conf_tdc00n<2> conf_tdc00n<3> conf_tdc00n<4>
        + conf_tdc00n<5> conf_tdc00n<6> conf_tdc00n<7> conf_tdc00n<8> conf_tdc00n<9> conf_tdc00n<10>
        + conf_tdc00n<11> conf_tdc00n<12> conf_tdc00n<13> conf_tdc00n<14> conf_tdc00n<15>
        + conf_tdc00n<16> conf_tdc00n<17> conf_tdc00n<18> conf_tdc00n<19> conf_tdc00p<0>
        + conf_tdc00p<1> conf_tdc00p<2> conf_tdc00p<3> conf_tdc00p<4> conf_tdc00p<5> conf_tdc00p<6>
        + conf_tdc00p<7> conf_tdc00p<8> conf_tdc00p<9> conf_tdc00p<10> conf_tdc00p<11>
        + conf_tdc00p<12> conf_tdc00p<13> conf_tdc00p<14> conf_tdc00p<15> conf_tdc00p<16>
        + conf_tdc00p<17> conf_tdc00p<18> conf_tdc00p<19> conf_tdc01n<0> conf_tdc01n<1>
        + conf_tdc01n<2> conf_tdc01n<3> conf_tdc01n<4> conf_tdc01n<5> conf_tdc01n<6> conf_tdc01n<7>
        + conf_tdc01n<8> conf_tdc01n<9> conf_tdc01n<10> conf_tdc01n<11> conf_tdc01n<12>
        + conf_tdc01n<13> conf_tdc01n<14> conf_tdc01n<15> conf_tdc01n<16> conf_tdc01n<17>
        + conf_tdc01n<18> conf_tdc01n<19> conf_tdc01p<0> conf_tdc01p<1> conf_tdc01p<2>
        + conf_tdc01p<3> conf_tdc01p<4> conf_tdc01p<5> conf_tdc01p<6> conf_tdc01p<7> conf_tdc01p<8>
        + conf_tdc01p<9> conf_tdc01p<10> conf_tdc01p<11> conf_tdc01p<12> conf_tdc01p<13>
        + conf_tdc01p<14> conf_tdc01p<15> conf_tdc01p<16> conf_tdc01p<17> conf_tdc01p<18>
        + conf_tdc01p<19> conf_tdc4b conf_tdc10n<0> conf_tdc10n<1> conf_tdc10n<2> conf_tdc10n<3>
        + conf_tdc10n<4> conf_tdc10n<5> conf_tdc10n<6> conf_tdc10n<7> conf_tdc10n<8> conf_tdc10n<9>
        + conf_tdc10n<10> conf_tdc10n<11> conf_tdc10n<12> conf_tdc10n<13> conf_tdc10n<14>
        + conf_tdc10n<15> conf_tdc10n<16> conf_tdc10n<17> conf_tdc10n<18> conf_tdc10n<19>
        + conf_tdc10p<0> conf_tdc10p<1> conf_tdc10p<2> conf_tdc10p<3> conf_tdc10p<4> conf_tdc10p<5>
        + conf_tdc10p<6> conf_tdc10p<7> conf_tdc10p<8> conf_tdc10p<9> conf_tdc10p<10>
        + conf_tdc10p<11> conf_tdc10p<12> conf_tdc10p<13> conf_tdc10p<14> conf_tdc10p<15>
        + conf_tdc10p<16> conf_tdc10p<17> conf_tdc10p<18> conf_tdc10p<19> conf_tdc11n<0>
        + conf_tdc11n<1> conf_tdc11n<2> conf_tdc11n<3> conf_tdc11n<4> conf_tdc11n<5> conf_tdc11n<6>
        + conf_tdc11n<7> conf_tdc11n<8> conf_tdc11n<9> conf_tdc11n<10> conf_tdc11n<11>
        + conf_tdc11n<12> conf_tdc11n<13> conf_tdc11n<14> conf_tdc11n<15> conf_tdc11n<16>
        + conf_tdc11n<17> conf_tdc11n<18> conf_tdc11n<19> conf_tdc11p<0> conf_tdc11p<1>
        + conf_tdc11p<2> conf_tdc11p<3> conf_tdc11p<4> conf_tdc11p<5> conf_tdc11p<6> conf_tdc11p<7>
        + conf_tdc11p<8> conf_tdc11p<9> conf_tdc11p<10> conf_tdc11p<11> conf_tdc11p<12>
        + conf_tdc11p<13> conf_tdc11p<14> conf_tdc11p<15> conf_tdc11p<16> conf_tdc11p<17>
        + conf_tdc11p<18> conf_tdc11p<19> conf_tdcmax<0> conf_tdcmax<1> conf_tdcmax<2>
        + conf_tdcmax<3> conf_tdcmax<4> conf_tdcmax<5> conf_tdcmax<6> conf_tdcmax<7> conf_tdcwait<0>
        + conf_tdcwait<1> conf_tdcwait<2> conf_tdcwait<3> conf_tdcwait<4> conf_tdcwait<5>
        + conf_tdcwait<6> conf_tdcwait<7> dcedge0<1> dcedge0<2> dcedge0<3> dcedge1<1> dcedge1<2>
        + dcedge1<3> dcedge2<1> dcedge2<2> dcedge2<3> enable_e2l ro_enable ff0<0> ff0<1> ff0<2>
        + ff0<3> ff0<4> ff0<5> ff0<6> ff0<7> ff1<0> ff1<1> ff1<2> ff1<3> ff1<4> ff1<5> ff1<6> ff1<7>
        + int0 int1 ro_out_i<0> ro_out_i<1> ro_out_i<2> rand0 rand1 ready0 ready1 trng_rst trng_rst'
        + conf_dcedgesel<0> conf_dcedgesel<1> sendfree'<8> sendfree'<9> sendfree'<16> sendfree'<0>
        + sendfree'<1> sendfree'<12> sendfree'<2> sendfree'<3> sendfree'<13> sendfree'<10>
        + sendfree'<11> sendfree'<17> sendfree'<4> sendfree'<5> sendfree'<14> sendfree'<6>
        + sendfree'<7> sendfree'<15> vdd_core vdd_dc vdd_tdc vss trng_top_level
    Xi1 enable_e2l_i<0> cal_out0 cal_out1 cal_out2 ro_out_i<3> ro_enable_i<0> clk conf_statecnt<0>
        + conf_statecnt<1> conf_statecnt<2> conf_statecnt<3> conf_statecnt<4> conf_statecnt<5>
        + conf_statecnt<6> conf_statecnt<7> conf_statecnt<8> conf_statecnt<9> conf_statecnt<10>
        + conf_statecnt<11> conf_statecnt<12> conf_statecnt<13> conf_statecnt<14> conf_statecnt<15>
        + conf_tdccal<0> conf_tdccal<1> conf_tdccal<2> conf_tdccal<3> conf_tdccal<4> conf_tdccal<5>
        + conf_tdccal<6> conf_tdccal<7> conf_tdccal<8> conf_tdccal<9> data_out_i<0> data_ready_i<0>
        + trng_rst_i<0> trng_rst'_i<0> rst_i rst'_i ser_clk scan_out<3> scan_out<0> scan_out<1>
        + scan_out<2> scan_out<5> alarm0<0> alarm0<1> ff0<0> ff0<1> ff0<2> ff0<3> ff0<4> ff0<5>
        + ff0<6> ff0<7> int0 ready0 alarm1<0> alarm1<1> ff1<0> ff1<1> ff1<2> ff1<3> ff1<4> ff1<5>
        + ff1<6> ff1<7> int1 ready1 scan_out<4> vdd_core vss conf_top_level
    Xi2 alarm_dc clk conf_statecnt<0> conf_statecnt<1> conf_statecnt<2> conf_statecnt<3>
        + conf_statecnt<4> conf_statecnt<5> conf_statecnt<6> conf_statecnt<7> conf_statecnt<8>
        + conf_statecnt<9> conf_statecnt<10> conf_statecnt<11> conf_statecnt<12> conf_statecnt<13>
        + conf_statecnt<14> conf_statecnt<15> data_out_i<1> data_ready_i<1> trng_rst_i<1>
        + trng_rst'_i<1> ro_out_i<1> enable_e2l_i<1> ro_enable_i<1> rand0 rand1 rst_i rst'_i
        + conf_sendfree ser_clk scan_out<9> scan_out<6> scan_out<7> scan_out<8> scan_out<11>
        + alarm0<0> alarm0<1> ready0 alarm1<0> alarm1<1> ready1 scan_out<10> vdd_core vss
        + bit_top_level
    Xi3 clk scan_out<17> scan_out<21> conf_statecnt<0> conf_statecnt<1> conf_statecnt<2>
        + conf_statecnt<3> conf_statecnt<4> conf_statecnt<5> conf_statecnt<6> conf_statecnt<7>
        + conf_statecnt<8> conf_statecnt<9> conf_statecnt<10> conf_statecnt<11> conf_statecnt<12>
        + conf_statecnt<13> conf_statecnt<14> conf_statecnt<15> conf_tdccnt<0> conf_tdccnt<1>
        + conf_tdccnt<2> conf_tdccnt<3> conf_tdccnt<4> conf_tdccnt<5> conf_tdccnt<6> conf_tdccnt<7>
        + conf_tdccnt<8> conf_tdccnt<9> conf_tdccnt<10> conf_tdccnt<11> conf_tdccnt<12>
        + conf_tdccnt<13> conf_tdccnt<14> conf_tdccnt<15> data_out_i<2> data_ready_i<2>
        + trng_rst_i<2> trng_rst'_i<2> scan_out<18> enable_e2l_i<2> ro_enable_i<2> rst_i rst'_i
        + ser_clk scan_out<22> scan_out<12> scan_out<13> scan_out<14> scan_out<15> scan_out<16>
        + scan_out<20> ready0 ready1 scan_out<19> vdd_core vss async_top_level
    Xi26 ro_out_i<0> ro_out_i<1> ro_out_i<2> ro_out_i<3> ro_out_sel conf_rooutsel<0>
         + conf_rooutsel<1> vdd_core vss mux4
    Xi15 ro_enable_i<0> ro_enable_i<1> ro_enable_i<2> ro_enable_i<3> net028 conf_ctrlsel<0>
         + conf_ctrlsel<1> vdd_core vss mux4
    Xi13 enable_e2l_i<0> enable_e2l_i<1> enable_e2l_i<2> enable_e2l_i<3> net024 conf_ctrlsel<0>
         + conf_ctrlsel<1> vdd_core vss mux4
    Xi11 data_ready_i<0> data_ready_i<1> data_ready_i<2> data_ready_i<3> net0162 conf_ctrlsel<0>
         + conf_ctrlsel<1> vdd_core vss mux4
    Xi9 data_out_i<0> data_out_i<1> data_out_i<2> data_out_i<3> net012 conf_ctrlsel<0>
        + conf_ctrlsel<1> vdd_core vss mux4
    Xi5 trng_rst'_i<0> trng_rst'_i<1> trng_rst'_i<2> trng_rst'_i<3> net0157 conf_ctrlsel<0>
        + conf_ctrlsel<1> vdd_core vss mux4
    Xi4 trng_rst_i<0> trng_rst_i<1> trng_rst_i<2> trng_rst_i<3> net0149 conf_ctrlsel<0>
        + conf_ctrlsel<1> vdd_core vss mux4
    Xi36 net073 clk vdd_core vss buffer_large
    Xi33 rst rst_i vdd_core vss buffer_large
    Xi32 rst' rst'_i vdd_core vss buffer_large
    Xi30 net0142 ro_out vdd_core vss buffer_large
    Xi16 net028 ro_enable vdd_core vss buffer_large
    Xi14 net024 enable_e2l vdd_core vss buffer_large
    Xi12 net0162 data_ready vdd_core vss buffer_large
    Xi10 net012 data_out vdd_core vss buffer_large
    Xi7 net0157 trng_rst' vdd_core vss buffer_large
    Xi6 net0149 trng_rst vdd_core vss buffer_large
    Xi25 cal_out2 dcedge2<1> vdd_core vss buffer
    Xi24 cal_out1 dcedge2<3> vdd_core vss buffer
    Xi23 cal_out0 dcedge2<2> vdd_core vss buffer
    Xi22 cal_out2 dcedge1<2> vdd_core vss buffer
    Xi21 cal_out1 dcedge1<1> vdd_core vss buffer
    Xi20 cal_out0 dcedge1<3> vdd_core vss buffer
    Xi19 cal_out2 dcedge0<3> vdd_core vss buffer
    Xi18 cal_out1 dcedge0<2> vdd_core vss buffer
    Xi17 cal_out0 dcedge0<1> vdd_core vss buffer
    Xi28 ro_out_sel rooutfreq<0> rooutfreq<1> rooutfreq<2> rooutfreq<3> rooutfreq<4> rooutfreq<5>
         + rooutfreq<6> rooutfreq<7> rooutfreq<8> rooutfreq<9> rooutfreq<10> rooutfreq<11>
         + rooutfreq<12> rooutfreq<13> rooutfreq<14> rooutfreq<15> net0138 rst_i rst'_i vdd_core vss
         + freq_scaler16
    Xi29 rooutfreq<0> rooutfreq<1> rooutfreq<2> rooutfreq<3> rooutfreq<4> rooutfreq<5> rooutfreq<6>
         + rooutfreq<7> rooutfreq<8> rooutfreq<9> rooutfreq<10> rooutfreq<11> rooutfreq<12>
         + rooutfreq<13> rooutfreq<14> rooutfreq<15> net0142 conf_rooutfreqsel<0>
         + conf_rooutfreqsel<1> conf_rooutfreqsel<2> conf_rooutfreqsel<3> vdd_core vss mux16
    Xi31 rst rst' vdd_core vss inv
    Xi34 gen_clk conf_clk<0> conf_clk<1> conf_clk<2> conf_clk<3> conf_clk<4> conf_clk<5> conf_clk<6>
         + conf_clk<7> conf_clk<8> conf_clk<9> conf_clk<10> conf_clk<11> conf_clkenable rst_i rst'_i
         + vdd_core vss clk_manager
    Xi35 gen_clk ext_clk net073 conf_clksel vdd_core vss mux2
    Xi37 conf_sendfree sendfree'<0> sendfree'<1> sendfree'<2> sendfree'<3> sendfree'<4> sendfree'<5>
         + sendfree'<6> sendfree'<7> sendfree'<8> sendfree'<9> sendfree'<10> sendfree'<11>
         + sendfree'<12> sendfree'<13> sendfree'<14> sendfree'<15> sendfree'<16> sendfree'<17>
         + vdd_core vss one_to_18
.ENDS
```
