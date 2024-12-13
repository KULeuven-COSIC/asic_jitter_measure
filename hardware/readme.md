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

The following hierarchy is used in the ASIC, the number in bold gives the number of MOS pairs in that cell (each cell can be expanded to show its components):

<details>
<summary><code>top_level</code> <b>34631</b> <i></i></summary>
<blockquote>
<details>
<summary><code>pad_frame</code> <b>25</b> <i></i></summary>
<blockquote>
<details>
<summary><code>in_pad</code> <b>1</b> <i>x18</i></summary>
<blockquote>
<details>
<summary><code>esd_signal_4x</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>esd_p_diode</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>p_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_n_diode</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>esd_supply_3_4x_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>esd_supply_3_1x_lt</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>esd_p_diode_lt</code> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_n_diode_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>pad</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>bond_pad</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos_io</code> <b>0</b> <i>x3</i></li>
<li><code>p_mos_io</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>out_pad</code> <b>1</b> <i>x7</i></summary>
<blockquote>
<details>
<summary><code>esd_signal_4x</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>esd_p_diode</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>p_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_n_diode</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>esd_supply_3_4x_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>esd_supply_3_1x_lt</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>esd_p_diode_lt</code> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_n_diode_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>pad</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>bond_pad</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos_io</code> <b>0</b> <i>x8</i></li>
<li><code>p_mos_io</code> <b>0</b> <i>x8</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>vdd_pad</code> <b>0</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><code>pad</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>bond_pad</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_supply_2_4x_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>esd_supply_2_1x_lt</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>esd_p_diode_lt</code> <b>0</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_n_diode_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>esd_supply_3_4x_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>esd_supply_3_1x_lt</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>esd_p_diode_lt</code> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_n_diode_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_diode</code> <b>0</b> <i></i></li>
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
<summary><code>vdd_core_pad</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>pad</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>bond_pad</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_supply_2_4x_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>esd_supply_2_1x_lt</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>esd_p_diode_lt</code> <b>0</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_n_diode_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>esd_supply_3_4x_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>esd_supply_3_1x_lt</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>esd_p_diode_lt</code> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_n_diode_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_diode</code> <b>0</b> <i></i></li>
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
<summary><code>vss_pad</code> <b>0</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><code>pad</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>bond_pad</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_supply_3_4x_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>esd_supply_3_1x_lt</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>esd_p_diode_lt</code> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_n_diode_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_diode</code> <b>0</b> <i></i></li>
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
<summary><code>vdd_io_pad</code> <b>0</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>pad</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>bond_pad</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_supply_3_4x_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<details>
<summary><code>esd_supply_3_1x_lt</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>esd_p_diode_lt</code> <b>0</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_diode</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>esd_n_diode_lt</code> <b>0</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_diode</code> <b>0</b> <i></i></li>
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
<summary><code>top_core</code> <b>34606</b> <i></i></summary>
<blockquote>
<details>
<summary><code>ctrl_trng_conf_scan_combo</code> <b>20939</b> <i></i></summary>
<blockquote>
<details>
<summary><code>ctrl_trng_conf_combo</code> <b>20170</b> <i></i></summary>
<blockquote>
<details>
<summary><code>ctrl_trng_combo</code> <b>15594</b> <i></i></summary>
<blockquote>
<details>
<summary><code>trng_top_level</code> <b>8370</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mux2_10x</code> <b>70</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x10</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>tdc_2b_diff_branch</code> <b>832</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dec_6_conf_0</code> <b>38</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dec_stage</code> <b>5</b> <i>x6</i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>tdc_ready</code> <b>444</b> <i></i></summary>
<blockquote>
<details>
<summary><code>ff_ready</code> <b>22</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nor3</code> <b>3</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>max_ready</code> <b>161</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>nand2</code> <b>2</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>wait_ready</code> <b>227</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>nand2</code> <b>2</b> <i>x12</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>tdc_2e_2b_diff_np_4lin_buf</code> <b>350</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tdc_2stage_diff_np_4lin_buf</code> <b>116</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>inv_wn</code> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_stage_diff_np_4lin_buf</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tdc_and_diff</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_buf_diff_np_4lin</code> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x26</i></li>
<li><code>p_mos</code> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv_wide</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>tdc_2stage_diff_np_4lin_switched_buf</code> <b>118</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_stage_diff_np_4lin_switched_buf</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tdc_and_diff</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_buf_diff_np_4lin</code> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x26</i></li>
<li><code>p_mos</code> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv_wide</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
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
<summary><code>tdc_3b_diff_branch</code> <b>962</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tdc_2e_3b_diff_np_4lin_buf</code> <b>466</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tdc_2stage_diff_np_4lin_buf</code> <b>116</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>inv_wn</code> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_stage_diff_np_4lin_buf</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tdc_and_diff</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_buf_diff_np_4lin</code> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x26</i></li>
<li><code>p_mos</code> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv_wide</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>tdc_2stage_diff_np_4lin_switched_buf</code> <b>118</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_stage_diff_np_4lin_switched_buf</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tdc_and_diff</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_buf_diff_np_4lin</code> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x26</i></li>
<li><code>p_mos</code> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv_wide</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
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
<summary><code>tdc_ready_4</code> <b>446</b> <i></i></summary>
<blockquote>
<details>
<summary><code>max_ready</code> <b>161</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>nand2</code> <b>2</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>wait_ready</code> <b>227</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>nand2</code> <b>2</b> <i>x12</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>ff_ready_4</code> <b>24</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nor4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dec_8_conf_0</code> <b>50</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dec_stage</code> <b>5</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dc_collection</code> <b>566</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dc_3e_1b_no_config</code> <b>72</b> <i></i></summary>
<blockquote>
<details>
<summary><code>buffer</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>edge_to_level_3e</code> <b>51</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>mero_3e_1b</code> <b>12</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mero_nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>mero_buf</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dc_3e_4b_no_config</code> <b>90</b> <i></i></summary>
<blockquote>
<details>
<summary><code>buffer</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>edge_to_level_3e</code> <b>51</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>mero_3e_4b</code> <b>30</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mero_nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>mero_buf</code> <b>2</b> <i>x12</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dc_3e_3b_no_config</code> <b>84</b> <i></i></summary>
<blockquote>
<details>
<summary><code>buffer</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>edge_to_level_3e</code> <b>51</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>mero_3e_3b</code> <b>24</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mero_nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>mero_buf</code> <b>2</b> <i>x9</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>single_ended_to_diff</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>mux4</code> <b>21</b> <i>x9</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dec4_inverted</code> <b>10</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dc_3e_2b_no_config</code> <b>78</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mero_3e_2b</code> <b>18</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mero_nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>mero_buf</code> <b>2</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>edge_to_level_3e</code> <b>51</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>mero_collapse_3e</code> <b>37</b> <i></i></summary>
<blockquote>
<details>
<summary><code>xor2</code> <b>6</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>vdd_gate_1ma</code> <b>0</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>p_mos_lvt</code> <b>0</b> <i></i></li>
<li><code>n_mos_lvt</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>mux4</code> <b>21</b> <i>x26</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>vdd_gate_1ma</code> <b>0</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><code>p_mos_lvt</code> <b>0</b> <i></i></li>
<li><code>n_mos_lvt</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dec4_inverted</code> <b>10</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>tdc_4b_diff_branch</code> <b>1093</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dec_10_conf_0</code> <b>63</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dec_stage</code> <b>5</b> <i>x10</i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>tdc_2e_4b_diff_np_4lin_buf</code> <b>582</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tdc_2stage_diff_np_4lin_buf</code> <b>116</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>inv_wn</code> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_stage_diff_np_4lin_buf</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tdc_and_diff</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_buf_diff_np_4lin</code> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x26</i></li>
<li><code>p_mos</code> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv_wide</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>tdc_2stage_diff_np_4lin_switched_buf</code> <b>118</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_stage_diff_np_4lin_switched_buf</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tdc_and_diff</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_buf_diff_np_4lin</code> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x26</i></li>
<li><code>p_mos</code> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv_wide</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
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
<summary><code>tdc_ready_6</code> <b>448</b> <i></i></summary>
<blockquote>
<details>
<summary><code>ff_ready_6</code> <b>26</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nor5</code> <b>5</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x5</i></li>
<li><code>n_mos</code> <b>0</b> <i>x5</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>max_ready</code> <b>161</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>nand2</code> <b>2</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>wait_ready</code> <b>227</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>nand2</code> <b>2</b> <i>x12</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>tdc_1b_diff_branch</code> <b>702</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tdc_2e_1b_diff_np_4lin_buf</code> <b>234</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tdc_2stage_diff_np_4lin_buf</code> <b>116</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv_wn</code> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_stage_diff_np_4lin_buf</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tdc_and_diff</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_buf_diff_np_4lin</code> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x26</i></li>
<li><code>p_mos</code> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv_wide</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>tdc_2stage_diff_np_4lin_switched_buf</code> <b>118</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_stage_diff_np_4lin_switched_buf</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tdc_and_diff</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_buf_diff_np_4lin</code> <b>26</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x26</i></li>
<li><code>p_mos</code> <b>0</b> <i>x26</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>tdc_inv_wide</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
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
<summary><code>dec_4_conf_0</code> <b>26</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dec_stage</code> <b>5</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>tdc_ready_2</code> <b>442</b> <i></i></summary>
<blockquote>
<details>
<summary><code>max_ready</code> <b>161</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>nand2</code> <b>2</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>wait_ready</code> <b>227</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>nand2</code> <b>2</b> <i>x12</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>ff_ready_2</code> <b>20</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
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
<summary><code>conf_top_level</code> <b>2491</b> <i></i></summary>
<blockquote>
<details>
<summary><code>conf_control</code> <b>101</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x9</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>conf_datapath</code> <b>2381</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_16</code> <b>240</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>cal_tdc</code> <b>151</b> <i></i></summary>
<blockquote>
<details>
<summary><code>ro_2i</code> <b>20</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv_conf</code> <b>9</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x9</i></li>
<li><code>n_mos</code> <b>0</b> <i>x9</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>freqscaler3</code> <b>45</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>inv_sd</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>mux4</code> <b>21</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv_bank_8</code> <b>8</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_dh</code> <b>14</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_wn</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>synchronizer</code> <b>34</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>equal_to_52</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x5</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>check_equal_16</code> <b>119</b> <i></i></summary>
<blockquote>
<details>
<summary><code>check_equal_8</code> <b>58</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>xnor2</code> <b>6</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>shift_reg_52</code> <b>1144</b> <i></i></summary>
<blockquote>
<details>
<summary><code>shift_reg_16</code> <b>352</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>shift_reg_8</code> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>shift_reg_4</code> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>shift_reg_4</code> <b>88</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>mux2</code> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>bit_top_level</code> <b>1485</b> <i></i></summary>
<blockquote>
<details>
<summary><code>bit_datapath</code> <b>1375</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_16</code> <b>240</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>synchronizer</code> <b>34</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>equal_to_24</code> <b>16</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>shift_reg_24</code> <b>528</b> <i></i></summary>
<blockquote>
<details>
<summary><code>shift_reg_8</code> <b>176</b> <i></i></summary>
<blockquote>
<details>
<summary><code>shift_reg_4</code> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>shift_reg_16</code> <b>352</b> <i></i></summary>
<blockquote>
<details>
<summary><code>shift_reg_8</code> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>shift_reg_4</code> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>mux2</code> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>check_equal_16</code> <b>119</b> <i></i></summary>
<blockquote>
<details>
<summary><code>check_equal_8</code> <b>58</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>xnor2</code> <b>6</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>conf_control</code> <b>101</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x9</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>async_top_level</code> <b>2295</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_control_0</code> <b>47</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x5</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>async_control_1</code> <b>74</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x5</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>async_datapath_0</code> <b>430</b> <i></i></summary>
<blockquote>
<details>
<summary><code>synchronizer</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>async_counter_equal_16</code> <b>359</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_16</code> <b>240</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>check_equal_16</code> <b>119</b> <i></i></summary>
<blockquote>
<details>
<summary><code>check_equal_8</code> <b>58</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>xnor2</code> <b>6</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
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
<summary><code>async_datapath_1</code> <b>1726</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_equal_16</code> <b>359</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_16</code> <b>240</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>check_equal_16</code> <b>119</b> <i></i></summary>
<blockquote>
<details>
<summary><code>check_equal_8</code> <b>58</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>xnor2</code> <b>6</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>async_counter_32</code> <b>480</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_16</code> <b>240</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>shift_reg_32</code> <b>704</b> <i></i></summary>
<blockquote>
<details>
<summary><code>shift_reg_16</code> <b>352</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>shift_reg_8</code> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>shift_reg_4</code> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x4</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>mux2</code> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>synchronizer</code> <b>34</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i></i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>equal_to_32</code> <b>17</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x7</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand4</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>mux4</code> <b>21</b> <i>x7</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>buffer_large</code> <b>4</b> <i>x10</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer</code> <b>2</b> <i>x9</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>freq_scaler16</code> <b>240</b> <i></i></summary>
<blockquote>
<details>
<summary><code>freq_scaler8</code> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>freq_scaler4</code> <b>60</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>freq_scaler2</code> <b>30</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>mux16</code> <b>105</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mux4</code> <b>21</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>clk_manager</code> <b>377</b> <i></i></summary>
<blockquote>
<details>
<summary><code>ro_2i</code> <b>20</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv_conf</code> <b>9</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x9</i></li>
<li><code>n_mos</code> <b>0</b> <i>x9</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>freq_scaler16</code> <b>240</b> <i></i></summary>
<blockquote>
<details>
<summary><code>freq_scaler8</code> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>freq_scaler4</code> <b>60</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>freq_scaler2</code> <b>30</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>mux16</code> <b>105</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mux4</code> <b>21</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>buffer_large</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_bank_8</code> <b>8</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>mux2</code> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>one_to_18</code> <b>18</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x18</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>one_to_7</code> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x7</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>conf_268</code> <b>4569</b> <i></i></summary>
<blockquote>
<details>
<summary><code>conf_256</code> <b>4352</b> <i></i></summary>
<blockquote>
<details>
<summary><code>conf_128</code> <b>2176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>conf_64</code> <b>1088</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>conf_32</code> <b>544</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>conf_16</code> <b>272</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>conf_8</code> <b>136</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>conf_4</code> <b>68</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>conf_2</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
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
<summary><code>conf_8</code> <b>136</b> <i></i></summary>
<blockquote>
<details>
<summary><code>conf_4</code> <b>68</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>conf_2</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
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
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer_large</code> <b>4</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>conf_4</code> <b>68</b> <i></i></summary>
<blockquote>
<details>
<summary><code>conf_2</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
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
<summary><code>scan_34</code> <b>769</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>scan_32</code> <b>704</b> <i></i></summary>
<blockquote>
<details>
<summary><code>scan_16</code> <b>352</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_8</code> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_4</code> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_2</code> <b>44</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_1</code> <b>22</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>scan_2</code> <b>44</b> <i></i></summary>
<blockquote>
<details>
<summary><code>scan_1</code> <b>22</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>buffer_large</code> <b>4</b> <i>x5</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>jit_top_full</code> <b>13667</b> <i></i></summary>
<blockquote>
<details>
<summary><code>jit_top_half</code> <b>6812</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>clk_manager</code> <b>377</b> <i></i></summary>
<blockquote>
<details>
<summary><code>ro_2i</code> <b>20</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv_conf</code> <b>9</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x9</i></li>
<li><code>n_mos</code> <b>0</b> <i>x9</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>freq_scaler16</code> <b>240</b> <i></i></summary>
<blockquote>
<details>
<summary><code>freq_scaler8</code> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>freq_scaler4</code> <b>60</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>freq_scaler2</code> <b>30</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>mux16</code> <b>105</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mux4</code> <b>21</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>buffer_large</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>inv_bank_8</code> <b>8</b> <i></i></summary>
<blockquote>
<details>
<summary><code>inv</code> <b>1</b> <i>x8</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>dc_scan_jit_128</code> <b>4864</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dc_jit_128</code> <b>2048</b> <i></i></summary>
<blockquote>
<details>
<summary><code>dc_jit_64</code> <b>1024</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dc_jit_32</code> <b>512</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dc_jit_16</code> <b>256</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dc_jit_8</code> <b>128</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dc_jit_4</code> <b>64</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dc_jit_2</code> <b>32</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv_jit</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
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
<summary><code>scan_jit_128</code> <b>2816</b> <i></i></summary>
<blockquote>
<details>
<summary><code>scan_jit_64</code> <b>1408</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_jit_32</code> <b>704</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_jit_16</code> <b>352</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_jit_8</code> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_jit_4</code> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_jit_2</code> <b>44</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>mux2</code> <b>7</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
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
<summary><code>async_counter_32</code> <b>480</b> <i></i></summary>
<blockquote>
<details>
<summary><code>async_counter_16</code> <b>240</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>async_counter_8</code> <b>120</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>tff_st_ar</code> <b>15</b> <i>x8</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>mux16</code> <b>105</b> <i></i></summary>
<blockquote>
<details>
<summary><code>mux4</code> <b>21</b> <i>x5</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i>x3</i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>conf_16</code> <b>272</b> <i></i></summary>
<blockquote>
<details>
<summary><code>conf_8</code> <b>136</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>conf_4</code> <b>68</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>conf_2</code> <b>34</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar_buf</code> <b>17</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
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
<summary><code>scan_32</code> <b>704</b> <i></i></summary>
<blockquote>
<details>
<summary><code>scan_16</code> <b>352</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_8</code> <b>176</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_4</code> <b>88</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_2</code> <b>44</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>scan_1</code> <b>22</b> <i>x2</i></summary>
<blockquote>
<details>
<summary><code>mux2</code> <b>7</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<ul>
<li><code>p_mos</code> <b>0</b> <i></i></li>
<li><code>n_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>dff_st_ar</code> <b>15</b> <i></i></summary>
<blockquote>
<details>
<summary><code>nand2</code> <b>2</b> <i>x4</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3</code> <b>3</b> <i></i></summary>
<blockquote>
<ul>
<li><code>p_mos</code> <b>0</b> <i>x3</i></li>
<li><code>n_mos</code> <b>0</b> <i>x3</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nand3_r</code> <b>4</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
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
<summary><code>buffer_large</code> <b>4</b> <i>x2</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>nor2</code> <b>2</b> <i></i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x2</i></li>
<li><code>p_mos</code> <b>0</b> <i>x2</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>inv</code> <b>1</b> <i>x3</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i></i></li>
<li><code>p_mos</code> <b>0</b> <i></i></li>
</ul>
</blockquote>
</details>
<details>
<summary><code>buffer_large</code> <b>4</b> <i>x10</i></summary>
<blockquote>
<ul>
<li><code>n_mos</code> <b>0</b> <i>x4</i></li>
<li><code>p_mos</code> <b>0</b> <i>x4</i></li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary><code>decouple_cap</code> <b>0</b> <i>x6</i></summary>
<blockquote>
<ul>
<li><code>cap</code> <b>0</b> <i></i></li>
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
