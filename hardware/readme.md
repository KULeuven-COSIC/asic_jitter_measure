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
<summary>`top_level` **34631**</summary>
<blockquote>
<details>
<summary>`padframe_v1` **25**</summary>
<blockquote>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`in_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`out_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`out_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`out_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`out_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`out_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`out_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`out_pad` **1**</summary>
<blockquote>
<details>
<summary>`esd_signal_4x` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode` **0**</summary>
<blockquote>
<ul>
<li>`al=5u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`n_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
<li>`p_mos_io` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vdd_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vdd_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vdd_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vdd_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vdd_core_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_2_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vss_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vss_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vss_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vss_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vss_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vdd_io_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`vdd_io_pad` **0**</summary>
<blockquote>
<details>
<summary>`pad` **0**</summary>
<blockquote>
<ul>
<li>`lt=69.0u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_4x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`esd_supply_3_1x_lt` **0**</summary>
<blockquote>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_pdiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`esd_ndiode_lt` **0**</summary>
<blockquote>
<ul>
<li>`al=10u` **0**</li>
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
<summary>`top_core` **34606**</summary>
<blockquote>
<details>
<summary>`ctrl_trng_conf_scan_combo` **20939**</summary>
<blockquote>
<details>
<summary>`ctrl_trng_conf_combo` **20170**</summary>
<blockquote>
<details>
<summary>`ctrl_trng_combo` **15594**</summary>
<blockquote>
<details>
<summary>`trng_toplevel` **8370**</summary>
<blockquote>
<details>
<summary>`mux2_10x` **70**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2b_diff_branch` **832**</summary>
<blockquote>
<details>
<summary>`dec_6_conf_0` **38**</summary>
<blockquote>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_ready_v0` **444**</summary>
<blockquote>
<details>
<summary>`ff_ready` **22**</summary>
<blockquote>
<details>
<summary>`nor3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`max_ready` **161**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`wait_ready` **227**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2e_2b_diff_np_4lin_buf` **350**</summary>
<blockquote>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_switched_buf` **118**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`tdc_2b_diff_branch` **832**</summary>
<blockquote>
<details>
<summary>`dec_6_conf_0` **38**</summary>
<blockquote>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_ready_v0` **444**</summary>
<blockquote>
<details>
<summary>`ff_ready` **22**</summary>
<blockquote>
<details>
<summary>`nor3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`max_ready` **161**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`wait_ready` **227**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2e_2b_diff_np_4lin_buf` **350**</summary>
<blockquote>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_switched_buf` **118**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`tdc_3b_diff_branch` **962**</summary>
<blockquote>
<details>
<summary>`tdc_2e_3b_diff_np_4lin_buf` **466**</summary>
<blockquote>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_switched_buf` **118**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`tdc_ready_4` **446**</summary>
<blockquote>
<details>
<summary>`max_ready` **161**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`wait_ready` **227**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`ff_ready_4` **24**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_8_conf_0` **50**</summary>
<blockquote>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_3b_diff_branch` **962**</summary>
<blockquote>
<details>
<summary>`tdc_2e_3b_diff_np_4lin_buf` **466**</summary>
<blockquote>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_switched_buf` **118**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`tdc_ready_4` **446**</summary>
<blockquote>
<details>
<summary>`max_ready` **161**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`wait_ready` **227**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`ff_ready_4` **24**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_8_conf_0` **50**</summary>
<blockquote>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dc_collection` **566**</summary>
<blockquote>
<details>
<summary>`dc_3e_1b_noconfig` **72**</summary>
<blockquote>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`edge2level_3e` **51**</summary>
<blockquote>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mero_3e_1b` **12**</summary>
<blockquote>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dc_3e_4b_noconfig` **90**</summary>
<blockquote>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`edge2level_3e` **51**</summary>
<blockquote>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mero_3e_4b` **30**</summary>
<blockquote>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dc_3e_3b_noconfig` **84**</summary>
<blockquote>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`edge2level_3e` **51**</summary>
<blockquote>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_3e_3b` **24**</summary>
<blockquote>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`singleended2diff` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`singleended2diff` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`singleended2diff` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec4_inverted` **10**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dc_3e_2b_noconfig` **78**</summary>
<blockquote>
<details>
<summary>`mero_3e_2b` **18**</summary>
<blockquote>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_nand2` **2**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mero_buf` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`edge2level_3e` **51**</summary>
<blockquote>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mero_collapse_3e_v2` **37**</summary>
<blockquote>
<details>
<summary>`xor2` **6**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`xor2` **6**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`xor2` **6**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`vdd_gate_1ma` **0**</summary>
<blockquote>
<ul>
<li>`pch_lvt` **0**</li>
<li>`nch_lvt` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dec4_inverted` **10**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_4b_diff_branch` **1093**</summary>
<blockquote>
<details>
<summary>`dec_10_conf_0` **63**</summary>
<blockquote>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2e_4b_diff_np_4lin_buf` **582**</summary>
<blockquote>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_switched_buf` **118**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`tdc_ready_6` **448**</summary>
<blockquote>
<details>
<summary>`ff_ready_6` **26**</summary>
<blockquote>
<details>
<summary>`nor5` **5**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor5` **5**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`max_ready` **161**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`wait_ready` **227**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`tdc_4b_diff_branch` **1093**</summary>
<blockquote>
<details>
<summary>`dec_10_conf_0` **63**</summary>
<blockquote>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2e_4b_diff_np_4lin_buf` **582**</summary>
<blockquote>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_switched_buf` **118**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`tdc_ready_6` **448**</summary>
<blockquote>
<details>
<summary>`ff_ready_6` **26**</summary>
<blockquote>
<details>
<summary>`nor5` **5**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor5` **5**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`max_ready` **161**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`wait_ready` **227**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`tdc_1b_diff_branch` **702**</summary>
<blockquote>
<details>
<summary>`tdc_2e_1b_diff_np_4lin_buf` **234**</summary>
<blockquote>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_switched_buf` **118**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`dec_4_conf_0` **26**</summary>
<blockquote>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_ready_2` **442**</summary>
<blockquote>
<details>
<summary>`max_ready` **161**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`wait_ready` **227**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`ff_ready_2` **20**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`tdc_1b_diff_branch` **702**</summary>
<blockquote>
<details>
<summary>`tdc_2e_1b_diff_np_4lin_buf` **234**</summary>
<blockquote>
<details>
<summary>`tdc_2stage_diff_np_4lin_buf` **116**</summary>
<blockquote>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_2stage_diff_np_4lin_switched_buf` **118**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_stage_diff_np_4lin_switched_buf` **34**</summary>
<blockquote>
<details>
<summary>`tdc_and_diff` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_buf_diff_np_4lin` **26**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv` **1**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`tdc_inv_wide` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`dec_4_conf_0` **26**</summary>
<blockquote>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dec_stage` **5**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tdc_ready_2` **442**</summary>
<blockquote>
<details>
<summary>`max_ready` **161**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`wait_ready` **227**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`ff_ready_2` **20**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nor2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`conf_toplevel` **2491**</summary>
<blockquote>
<details>
<summary>`conf_control` **101**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`nand4` **4**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`buffer` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`conf_datapath` **2381**</summary>
<blockquote>
<details>
<summary>`asynccounter_16` **240**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`asynccounter_16` **240**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`asynccounter_16` **240**</summary>
<blockquote>
<details>
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`asynccounter_8` **120**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`cal_tdc_v0` **151**</summary>
<blockquote>
<details>
<summary>`ro_2i` **20**</summary>
<blockquote>
<details>
<summary>`inv_conf` **9**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_conf` **9**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`freqscaler3` **45**</summary>
<blockquote>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`tff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
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
<summary>`inv_sd` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux4` **21**</summary>
<blockquote>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`mux2` **7**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<ul>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv_bank_8` **8**</summary>
<blockquote>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_dh` **14**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv_wn` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3_r` **4**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`inv` **1**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
</blockquote>
</details>
<details>
<summary>`dff_st_ar_buf` **17**</summary>
<blockquote>
<details>
<summary>`dff_st_ar` **15**</summary>
<blockquote>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand2` **2**</summary>
<blockquote>
<ul>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
</ul>
</blockquote>
</details>
<details>
<summary>`nand3` **3**</summary>
<blockquote>
<ul>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`p_mos` **0**</li>
<li>`n_mos` **0**</li>
<li>`n_mos` **0**</li>