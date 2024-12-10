# ASIC Hardware

This folder contains all the cells used to build the ASIC.
Each cell contains an SVG showing the layout and a netlist.

## File Structure

Each folder corresponds to a hardware module (cell).
Each folder contains the following files:
- *[module name].cir*: A netlist for this module.
- *[module name].svg*: The layout for this module.
- *[module name].png*: A compressed version of the layout for this module.
- *readme.md*: A `readme` file for this module.

## ASIC Hierarchy

The following hierarchy is used in the ASIC (each cell can be expanded to show its components):

<details>
<summary><mark>top_level</mark> <b>34631</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>padframe_v1</mark> <b>25</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>in_pad</mark> <b>1</b> <i>x18</i></summary>
<blockquote>
<details>
<summary><mark>esd_signal_4x</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>esd_pdiode</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>al=5u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_ndiode</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>al=5u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>esd_supply_3_4x_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>esd_supply_3_1x_lt</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>esd_pdiode_lt</mark> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_ndiode_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>pad</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>lt=69.0u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos_io</mark> <b>0</b> <i>x3</i></li>
<li><mark>p_mos_io</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>out_pad</mark> <b>1</b> <i>x7</i></summary>
<blockquote>
<details>
<summary><mark>esd_signal_4x</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>esd_pdiode</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>al=5u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_ndiode</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>al=5u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>esd_supply_3_4x_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>esd_supply_3_1x_lt</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>esd_pdiode_lt</mark> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_ndiode_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>pad</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>lt=69.0u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos_io</mark> <b>0</b> <i>x8</i></li>
<li><mark>p_mos_io</mark> <b>0</b> <i>x8</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>vdd_pad</mark> <b>0</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><mark>pad</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>lt=69.0u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_supply_2_4x_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>esd_supply_2_1x_lt</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>esd_pdiode_lt</mark> <b>0</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_ndiode_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>esd_supply_3_4x_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>esd_supply_3_1x_lt</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>esd_pdiode_lt</mark> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_ndiode_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>vdd_core_pad</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>pad</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>lt=69.0u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_supply_2_4x_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>esd_supply_2_1x_lt</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>esd_pdiode_lt</mark> <b>0</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_ndiode_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>esd_supply_3_4x_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>esd_supply_3_1x_lt</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>esd_pdiode_lt</mark> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_ndiode_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>vss_pad</mark> <b>0</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><mark>pad</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>lt=69.0u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_supply_3_4x_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>esd_supply_3_1x_lt</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>esd_pdiode_lt</mark> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_ndiode_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>vdd_io_pad</mark> <b>0</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>pad</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>lt=69.0u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_supply_3_4x_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>esd_supply_3_1x_lt</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>esd_pdiode_lt</mark> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>esd_ndiode_lt</mark> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>al=10u</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>top_core</mark> <b>34606</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>ctrl_trng_conf_scan_combo</mark> <b>20939</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>ctrl_trng_conf_combo</mark> <b>20170</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>ctrl_trng_combo</mark> <b>15594</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>trng_toplevel</mark> <b>8370</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mux2_10x</mark> <b>70</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x10</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_2b_diff_branch</mark> <b>832</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dec_6_conf_0</mark> <b>38</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dec_stage</mark> <b>5</b> <i>x6</i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_ready_v0</mark> <b>444</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>ff_ready</mark> <b>22</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nor3</mark> <b>3</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>max_ready</mark> <b>161</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>wait_ready</mark> <b>227</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x12</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_2e_2b_diff_np_4lin_buf</mark> <b>350</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tdc_2stage_diff_np_4lin_buf</mark> <b>116</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_stage_diff_np_4lin_buf</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tdc_and_diff</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_buf_diff_np_4lin</mark> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x26</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv_wide</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_2stage_diff_np_4lin_switched_buf</mark> <b>118</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_stage_diff_np_4lin_switched_buf</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tdc_and_diff</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_buf_diff_np_4lin</mark> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x26</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv_wide</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_3b_diff_branch</mark> <b>962</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tdc_2e_3b_diff_np_4lin_buf</mark> <b>466</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tdc_2stage_diff_np_4lin_buf</mark> <b>116</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_stage_diff_np_4lin_buf</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tdc_and_diff</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_buf_diff_np_4lin</mark> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x26</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv_wide</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_2stage_diff_np_4lin_switched_buf</mark> <b>118</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_stage_diff_np_4lin_switched_buf</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tdc_and_diff</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_buf_diff_np_4lin</mark> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x26</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv_wide</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_ready_4</mark> <b>446</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>max_ready</mark> <b>161</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>wait_ready</mark> <b>227</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x12</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>ff_ready_4</mark> <b>24</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nor4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dec_8_conf_0</mark> <b>50</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dec_stage</mark> <b>5</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dc_collection</mark> <b>566</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dc_3e_1b_noconfig</mark> <b>72</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>edge2level_3e</mark> <b>51</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mero_3e_1b</mark> <b>12</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mero_nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>mero_buf</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dc_3e_4b_noconfig</mark> <b>90</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>edge2level_3e</mark> <b>51</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mero_3e_4b</mark> <b>30</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mero_nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>mero_buf</mark> <b>2</b> <i>x12</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dc_3e_3b_noconfig</mark> <b>84</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>edge2level_3e</mark> <b>51</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>mero_3e_3b</mark> <b>24</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mero_nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>mero_buf</mark> <b>2</b> <i>x9</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>singleended2diff</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>mux4</mark> <b>21</b> <i>x9</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dec4_inverted</mark> <b>10</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dc_3e_2b_noconfig</mark> <b>78</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mero_3e_2b</mark> <b>18</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mero_nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>mero_buf</mark> <b>2</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>edge2level_3e</mark> <b>51</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mero_collapse_3e_v2</mark> <b>37</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>xor2</mark> <b>6</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>vdd_gate_1ma</mark> <b>0</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>pch_lvt</mark> <b>0</b> <i></i></li>
<li><mark>nch_lvt</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mux4</mark> <b>21</b> <i>x26</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>vdd_gate_1ma</mark> <b>0</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><mark>pch_lvt</mark> <b>0</b> <i></i></li>
<li><mark>nch_lvt</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dec4_inverted</mark> <b>10</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_4b_diff_branch</mark> <b>1093</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dec_10_conf_0</mark> <b>63</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dec_stage</mark> <b>5</b> <i>x10</i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_2e_4b_diff_np_4lin_buf</mark> <b>582</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tdc_2stage_diff_np_4lin_buf</mark> <b>116</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_stage_diff_np_4lin_buf</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tdc_and_diff</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_buf_diff_np_4lin</mark> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x26</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv_wide</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_2stage_diff_np_4lin_switched_buf</mark> <b>118</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_stage_diff_np_4lin_switched_buf</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tdc_and_diff</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_buf_diff_np_4lin</mark> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x26</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv_wide</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_ready_6</mark> <b>448</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>ff_ready_6</mark> <b>26</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nor5</mark> <b>5</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x5</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x5</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>max_ready</mark> <b>161</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>wait_ready</mark> <b>227</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x12</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_1b_diff_branch</mark> <b>702</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tdc_2e_1b_diff_np_4lin_buf</mark> <b>234</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tdc_2stage_diff_np_4lin_buf</mark> <b>116</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_stage_diff_np_4lin_buf</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tdc_and_diff</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_buf_diff_np_4lin</mark> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x26</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv_wide</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_2stage_diff_np_4lin_switched_buf</mark> <b>118</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_stage_diff_np_4lin_switched_buf</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tdc_and_diff</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_buf_diff_np_4lin</mark> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x26</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>tdc_inv_wide</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dec_4_conf_0</mark> <b>26</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dec_stage</mark> <b>5</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>tdc_ready_2</mark> <b>442</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>max_ready</mark> <b>161</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>wait_ready</mark> <b>227</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x12</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>ff_ready_2</mark> <b>20</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>conf_toplevel</mark> <b>2491</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>conf_control</mark> <b>101</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x9</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>conf_datapath</mark> <b>2381</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_16</mark> <b>240</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>cal_tdc_v0</mark> <b>151</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>ro_2i</mark> <b>20</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv_conf</mark> <b>9</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x9</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x9</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>freqscaler3</mark> <b>45</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv_sd</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>mux4</mark> <b>21</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv_bank_8</mark> <b>8</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_dh</mark> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_wn</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>synchronizer</mark> <b>34</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>equalto52</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x5</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>checkequal_16</mark> <b>119</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>checkequal_8</mark> <b>58</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>xnor2</mark> <b>6</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>shiftreg_52</mark> <b>1144</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>shiftreg_16</mark> <b>352</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>shiftreg_8</mark> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>shiftreg_4</mark> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>shiftreg_4</mark> <b>88</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mux2</mark> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>bit_toplevel</mark> <b>1485</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>bit_datapath</mark> <b>1375</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_16</mark> <b>240</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>synchronizer</mark> <b>34</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>equalto24</mark> <b>16</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>shiftreg_24</mark> <b>528</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>shiftreg_8</mark> <b>176</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>shiftreg_4</mark> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>shiftreg_16</mark> <b>352</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>shiftreg_8</mark> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>shiftreg_4</mark> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>mux2</mark> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>checkequal_16</mark> <b>119</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>checkequal_8</mark> <b>58</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>xnor2</mark> <b>6</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>conf_control</mark> <b>101</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x9</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>async_toplevel</mark> <b>2295</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>async_control_0</mark> <b>47</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x5</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>async_control_1</mark> <b>74</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x5</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>async_datapath_0</mark> <b>430</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>synchronizer</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>asynccounterequal_16</mark> <b>359</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_16</mark> <b>240</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>checkequal_16</mark> <b>119</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>checkequal_8</mark> <b>58</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>xnor2</mark> <b>6</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>async_datapath_1</mark> <b>1726</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounterequal_16</mark> <b>359</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_16</mark> <b>240</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>checkequal_16</mark> <b>119</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>checkequal_8</mark> <b>58</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>xnor2</mark> <b>6</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>asynccounter_32</mark> <b>480</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_16</mark> <b>240</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>shiftreg_32</mark> <b>704</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>shiftreg_16</mark> <b>352</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>shiftreg_8</mark> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>shiftreg_4</mark> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mux2</mark> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>synchronizer</mark> <b>34</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>equalto32</mark> <b>17</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x7</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand4</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mux4</mark> <b>21</b> <i>x7</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>buffer_large</mark> <b>4</b> <i>x10</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer</mark> <b>2</b> <i>x9</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>freq_scaler16</mark> <b>240</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>freq_scaler8</mark> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>freq_scaler4</mark> <b>60</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>freq_scaler2</mark> <b>30</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mux16</mark> <b>105</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mux4</mark> <b>21</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>clkmanager</mark> <b>377</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>ro_2i</mark> <b>20</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv_conf</mark> <b>9</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x9</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x9</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>freq_scaler16</mark> <b>240</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>freq_scaler8</mark> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>freq_scaler4</mark> <b>60</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>freq_scaler2</mark> <b>30</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mux16</mark> <b>105</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mux4</mark> <b>21</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>buffer_large</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_bank_8</mark> <b>8</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mux2</mark> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>oneto18</mark> <b>18</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x18</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>oneto7</mark> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x7</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>conf_268</mark> <b>4569</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>conf_256</mark> <b>4352</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>conf_128</mark> <b>2176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>conf_64</mark> <b>1088</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>conf_32</mark> <b>544</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>conf_16</mark> <b>272</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>conf_8</mark> <b>136</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>conf_4</mark> <b>68</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>conf_2</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>conf_8</mark> <b>136</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>conf_4</mark> <b>68</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>conf_2</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer_large</mark> <b>4</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>conf_4</mark> <b>68</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>conf_2</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>scan_34</mark> <b>769</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>scan_32</mark> <b>704</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>scan_16</mark> <b>352</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_8</mark> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_4</mark> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_2</mark> <b>44</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_1</mark> <b>22</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>scan_2</mark> <b>44</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>scan_1</mark> <b>22</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>buffer_large</mark> <b>4</b> <i>x5</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>jit_top_full</mark> <b>13667</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>jit_top_half</mark> <b>6812</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>clkmanager</mark> <b>377</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>ro_2i</mark> <b>20</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv_conf</mark> <b>9</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x9</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x9</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>freq_scaler16</mark> <b>240</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>freq_scaler8</mark> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>freq_scaler4</mark> <b>60</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>freq_scaler2</mark> <b>30</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mux16</mark> <b>105</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mux4</mark> <b>21</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>buffer_large</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>inv_bank_8</mark> <b>8</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>dc_scan_jit_128</mark> <b>4864</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dc_jit_128</mark> <b>2048</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>dc_jit_64</mark> <b>1024</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dc_jit_32</mark> <b>512</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dc_jit_16</mark> <b>256</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dc_jit_8</mark> <b>128</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dc_jit_4</mark> <b>64</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dc_jit_2</mark> <b>32</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv_jit</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>scan_jit_128</mark> <b>2816</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>scan_jit_64</mark> <b>1408</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_jit_32</mark> <b>704</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_jit_16</mark> <b>352</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_jit_8</mark> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_jit_4</mark> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_jit_2</mark> <b>44</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>asynccounter_32</mark> <b>480</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_16</mark> <b>240</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>asynccounter_8</mark> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>tff_st_ar</mark> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>mux16</mark> <b>105</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>mux4</mark> <b>21</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>conf_16</mark> <b>272</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>conf_8</mark> <b>136</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>conf_4</mark> <b>68</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>conf_2</mark> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar_buf</mark> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>scan_32</mark> <b>704</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>scan_16</mark> <b>352</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_8</mark> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_4</mark> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_2</mark> <b>44</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>scan_1</mark> <b>22</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><mark>mux2</mark> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>dff_st_ar</mark> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><mark>nand2</mark> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3</mark> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>p_mos</mark> <b>0</b> <i>x3</i></li>
<li><mark>n_mos</mark> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nand3_r</mark> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>buffer_large</mark> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>nor2</mark> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x2</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>inv</mark> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i></i></li>
<li><mark>p_mos</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><mark>buffer_large</mark> <b>4</b> <i>x10</i></summary>
<blockquote>
<ul>
<li><mark>n_mos</mark> <b>0</b> <i>x4</i></li>
<li><mark>p_mos</mark> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><mark>decouplecap</mark> <b>0</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><mark>cap</mark> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>

## Make Usage

Use the provided *makefile* to generate the layout figures and netlists.
The following make targets are available:

- `hw_svg`: Generate all SVGs, the corresponding GDS files are required (not provided in the public archive).
- `hw_png`: Generate all PNGs from the SVG files.
- `hw_cir`: Generate all netlists, the corresponding raw netlists are required (not provided in the public archive).
- `hw_md`: Generate all readmes, the corresponding PNG files are required.
- `hw_top_md`: Generate this readme.
- `clean_hw`: Remove all PNGs and readmes.
- `realclean_hw`: `clean_hw` and remove netlists.
- `mrproper_hw`: `realclean_hw`, remove this readme and remove SVGs, note that regenerating the SVGs might take a long time!
