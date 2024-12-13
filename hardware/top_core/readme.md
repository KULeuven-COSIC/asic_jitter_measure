# `top_core` Module
![Layout](top_core.png)

## Cell Hierarchy

`top_core` **34606** (number MOS pairs)
- `ctrl_trng_conf_scan_combo` **20939**
- `jit_top_full` **13667**

## Netlist

```
.SUBCKT top_core jit_conf_clk jit_conf_in jit_conf_rst jit_core_rst jit_dc_clk jit_ro_enable
                 + jit_ro_out0 jit_ro_out1 jit_scan_clk jit_scan_out jit_scan_rst jit_scan_ser
                 + jit_vdd_core jit_vdd_jit0 jit_vdd_jit1 trng_conf_clk trng_conf_in trng_conf_rst
                 + trng_core_rst trng_data_out trng_data_ready trng_ext_clk trng_ro_out
                 + trng_scan_clk trng_scan_out trng_scan_rst trng_scan_ser trng_ser_clk
                 + trng_vdd_core trng_vdd_dc trng_vdd_tdc vss
    Xi0 trng_conf_clk trng_conf_in trng_conf_rst trng_core_rst trng_data_out trng_data_ready
        + trng_ext_clk trng_ro_out trng_scan_clk trng_scan_out trng_scan_rst trng_scan_ser
        + trng_ser_clk trng_vdd_core trng_vdd_dc trng_vdd_tdc vss ctrl_trng_conf_scan_combo
    Xi1 jit_conf_clk jit_conf_in jit_conf_rst jit_core_rst jit_dc_clk jit_ro_enable jit_ro_out0
        + jit_ro_out1 jit_scan_clk jit_scan_out jit_scan_rst jit_scan_ser jit_vdd_core jit_vdd_jit0
        + jit_vdd_jit1 vss jit_top_full
.ENDS
```
