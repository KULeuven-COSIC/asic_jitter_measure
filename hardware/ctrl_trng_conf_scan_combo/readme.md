# `ctrl_trng_conf_scan_combo` Module
![Layout](ctrl_trng_conf_scan_combo.png)

## Cell Hierarchy

`ctrl_trng_conf_scan_combo` **20939** (number MOS pairs)
- `ctrl_trng_conf_combo` **20170**
- `scan_34` **769**

## Netlist

```
.SUBCKT ctrl_trng_conf_scan_combo conf_clk conf_in conf_rst core_rst data_out data_ready ext_clk
                                  + ro_out scan_clk scan_out scan_rst scan_ser ser_clk vdd_core
                                  + vdd_dc vdd_tdc vss
    Xi0 scan<26> scan<27> scan<28> scan<29> scan<30> scan<31> scan<32> scan<33> conf_clk conf_in
        + conf_rst core_rst data_out data_ready ext_clk ro_out scan<0> scan<1> scan<2> scan<3>
        + scan<4> scan<5> scan<6> scan<7> scan<8> scan<9> scan<10> scan<11> scan<12> scan<13>
        + scan<14> scan<15> scan<16> scan<17> scan<18> scan<19> scan<20> scan<21> scan<22> scan<23>
        + scan<24> scan<25> net21 ser_clk vdd_core vdd_dc vdd_tdc vss ctrl_trng_conf_combo
    Xi1 scan_clk scan<0> scan<1> scan<2> scan<3> scan<4> scan<5> scan<6> scan<7> scan<8> scan<9>
        + scan<10> scan<11> scan<12> scan<13> scan<14> scan<15> scan<16> scan<17> scan<18> scan<19>
        + scan<20> scan<21> scan<22> scan<23> scan<24> scan<25> scan<26> scan<27> scan<28> scan<29>
        + scan<30> scan<31> scan<32> scan<33> net21 scan_out scan_rst scan_ser vdd_core vss scan_34
.ENDS
```
