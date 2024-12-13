# `shift_reg_24` Module
![Layout](shift_reg_24.png)

## Cell Hierarchy

`shift_reg_24` **528** (number MOS pairs)
- `shift_reg_8` **176**
- `shift_reg_16` **352**

## Netlist

```
.SUBCKT shift_reg_24 clk in<0> in<1> in<2> in<3> in<4> in<5> in<6> in<7> in<8> in<9> in<10> in<11>
                     + in<12> in<13> in<14> in<15> in<16> in<17> in<18> in<19> in<20> in<21> in<22>
                     + in<23> in_ser out rst rst' sel_ser vdd vss
    Xi0 clk in<0> in<1> in<2> in<3> in<4> in<5> in<6> in<7> in_ser net17 rst rst' sel_ser vdd vss
        + shift_reg_8
    Xi1 clk in<8> in<9> in<10> in<11> in<12> in<13> in<14> in<15> in<16> in<17> in<18> in<19> in<20>
        + in<21> in<22> in<23> net17 out rst rst' sel_ser vdd vss shift_reg_16
.ENDS
```
