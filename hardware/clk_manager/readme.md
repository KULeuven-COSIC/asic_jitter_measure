# `clk_manager` Module
![Layout](clk_manager.png)

## Cell Hierarchy

`clk_manager` **377** (number MOS pairs)
- `ro_2i` **20**
- `freq_scaler16` **240**
- `mux16` **105**
- `buffer_large` **4**
- `inv_bank_8` **8**

## Netlist

```
.SUBCKT clk_manager clk conf_clk<0> conf_clk<1> conf_clk<2> conf_clk<3> conf_clk<4> conf_clk<5>
                    + conf_clk<6> conf_clk<7> conf_clk<8> conf_clk<9> conf_clk<10> conf_clk<11>
                    + enable rst rst' vdd vss
    Xi0 conf_clk'<0> conf_clk'<1> conf_clk'<2> conf_clk'<3> conf_clk'<4> conf_clk'<5> conf_clk'<6>
        + conf_clk'<7> conf_clk<0> conf_clk<1> conf_clk<2> conf_clk<3> conf_clk<4> conf_clk<5>
        + conf_clk<6> conf_clk<7> enable mux_in<15> vdd vss ro_2i
    Xi1 mux_in<15> mux_in<0> mux_in<1> mux_in<2> mux_in<3> mux_in<4> mux_in<5> mux_in<6> mux_in<7>
        + mux_in<8> mux_in<9> mux_in<10> mux_in<11> mux_in<12> mux_in<13> mux_in<14> net010 net11
        + rst rst' vdd vss freq_scaler16
    Xi3 mux_in<0> mux_in<1> mux_in<2> mux_in<3> mux_in<4> mux_in<5> mux_in<6> mux_in<7> mux_in<8>
        + mux_in<9> mux_in<10> mux_in<11> mux_in<12> mux_in<13> mux_in<14> mux_in<15> net17
        + conf_clk<8> conf_clk<9> conf_clk<10> conf_clk<11> vdd vss mux16
    Xi2 net17 clk vdd vss buffer_large
    Xi4 conf_clk<0> conf_clk<1> conf_clk<2> conf_clk<3> conf_clk<4> conf_clk<5> conf_clk<6>
        + conf_clk<7> conf_clk'<0> conf_clk'<1> conf_clk'<2> conf_clk'<3> conf_clk'<4> conf_clk'<5>
        + conf_clk'<6> conf_clk'<7> vdd vss inv_bank_8
.ENDS
```
