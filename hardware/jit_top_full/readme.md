# `jit_top_full` Module
![Layout](jit_top_full.png)

## Cell Hierarchy

`jit_top_full` **13667** (number MOS pairs)
- `jit_top_half` **6812** *x2*
- `inv` **1** *x3*
- `buffer_large` **4** *x10*

## Netlist

```
.SUBCKT jit_top_full conf_clk conf_in conf_rst core_rst dc_clk ro_enable ro_out0 ro_out1 scan_clk
                     + scan_out scan_rst scan_ser vdd_core vdd_jit0 vdd_jit1 vss
    Xi1 net034 conf_clk_i conf_int conf_rst_i conf_rst'_i core_rst_i core_rst'_i dc_clk_i ro_enable
        + ro_out1 scan_clk_i scan_out_int scan_out scan_rst_i scan_rst'_i scan_ser_i vdd_core
        + vdd_jit1 vss jit_top_half
    Xi0 conf_int conf_clk_i conf_in conf_rst_i conf_rst'_i core_rst_i core_rst'_i dc_clk_i ro_enable
        + ro_out0 scan_clk_i scan_out scan_out_int scan_rst_i scan_rst'_i scan_ser_i vdd_core
        + vdd_jit0 vss jit_top_half
    Xi4 scan_rst scan_rst' vdd_core vss inv
    Xi3 conf_rst conf_rst' vdd_core vss inv
    Xi2 core_rst core_rst' vdd_core vss inv
    Xi14 dc_clk dc_clk_i vdd_core vss buffer_large
    Xi13 conf_clk conf_clk_i vdd_core vss buffer_large
    Xi12 scan_clk scan_clk_i vdd_core vss buffer_large
    Xi11 scan_ser scan_ser_i vdd_core vss buffer_large
    Xi10 scan_rst scan_rst_i vdd_core vss buffer_large
    Xi9 scan_rst' scan_rst'_i vdd_core vss buffer_large
    Xi8 conf_rst' conf_rst'_i vdd_core vss buffer_large
    Xi7 conf_rst conf_rst_i vdd_core vss buffer_large
    Xi6 core_rst core_rst_i vdd_core vss buffer_large
    Xi5 core_rst' core_rst'_i vdd_core vss buffer_large
.ENDS
```
