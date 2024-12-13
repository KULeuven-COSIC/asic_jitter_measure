# `jit_top_half` Module
![Layout](jit_top_half.png)

## Cell Hierarchy

`jit_top_half` **6812** (number MOS pairs)
- `clk_manager` **377**
- `dc_scan_jit_128` **4864**
- `async_counter_32` **480**
- `mux16` **105**
- `conf_16` **272**
- `scan_32` **704**
- `buffer_large` **4** *x2*
- `nor2` **2**

## Netlist

```
.SUBCKT jit_top_half conf<15> conf_clk conf_in conf_rst conf_rst' core_rst core_rst' dc_clk
                     + ro_enable ro_out scan_clk scan_in_ser scan_out scan_rst scan_rst' scan_ser
                     + vdd_core vdd_jit vss
    Xi0 ro conf<0> conf<1> conf<2> conf<3> conf<4> conf<5> conf<6> conf<7> conf<8> conf<9> conf<10>
        + conf<11> ro_enable core_rst core_rst' vdd_jit vss clk_manager
    Xi1 dc_clk ro last core_rst core_rst' scan_clk scan_in_ser scan_int scan_rst scan_rst' scan_ser
        + vdd_core vss dc_scan_jit_128
    Xi2 cnt_clk cnt<0> cnt<1> cnt<2> cnt<3> cnt<4> cnt<5> cnt<6> cnt<7> cnt<8> cnt<9> cnt<10>
        + cnt<11> cnt<12> cnt<13> cnt<14> cnt<15> cnt<16> cnt<17> cnt<18> cnt<19> cnt<20> cnt<21>
        + cnt<22> cnt<23> cnt<24> cnt<25> cnt<26> cnt<27> cnt<28> cnt<29> cnt<30> cnt<31> net22
        + core_rst core_rst' vdd_core vss async_counter_32
    Xi3 cnt<8> cnt<9> cnt<10> cnt<11> cnt<12> cnt<13> cnt<14> cnt<15> cnt<16> cnt<17> cnt<18>
        + cnt<19> cnt<20> cnt<21> cnt<22> cnt<23> ro_out_i conf<12> conf<13> conf<14> conf<15>
        + vdd_core vss mux16
    Xi4 conf_clk conf_in conf<0> conf<1> conf<2> conf<3> conf<4> conf<5> conf<6> conf<7> conf<8>
        + conf<9> conf<10> conf<11> conf<12> conf<13> conf<14> conf<15> conf_rst conf_rst' vdd_core
        + vss conf_16
    Xi5 scan_clk cnt<0> cnt<1> cnt<2> cnt<3> cnt<4> cnt<5> cnt<6> cnt<7> cnt<8> cnt<9> cnt<10>
        + cnt<11> cnt<12> cnt<13> cnt<14> cnt<15> cnt<16> cnt<17> cnt<18> cnt<19> cnt<20> cnt<21>
        + cnt<22> cnt<23> cnt<24> cnt<25> cnt<26> cnt<27> cnt<28> cnt<29> cnt<30> cnt<31> scan_int
        + scan_out_i scan_rst scan_rst' scan_ser vdd_core vss scan_32
    Xi7 scan_out_i scan_out vdd_core vss buffer_large
    Xi6 ro_out_i ro_out vdd_core vss buffer_large
    Xi8 last dc_clk cnt_clk vdd_core vss nor2
.ENDS
```
