# `conf_64` Module
![Layout](conf_64.png)

## Cell Hierarchy

`conf_64` **1088** (number MOS pairs)
- `conf_32` **544** *x2*

## Netlist

```
.SUBCKT conf_64 clk in out<0> out<1> out<2> out<3> out<4> out<5> out<6> out<7> out<8> out<9> out<10>
                + out<11> out<12> out<13> out<14> out<15> out<16> out<17> out<18> out<19> out<20>
                + out<21> out<22> out<23> out<24> out<25> out<26> out<27> out<28> out<29> out<30>
                + out<31> out<32> out<33> out<34> out<35> out<36> out<37> out<38> out<39> out<40>
                + out<41> out<42> out<43> out<44> out<45> out<46> out<47> out<48> out<49> out<50>
                + out<51> out<52> out<53> out<54> out<55> out<56> out<57> out<58> out<59> out<60>
                + out<61> out<62> out<63> rst rst' vdd vss
    Xi1 clk out<31> out<32> out<33> out<34> out<35> out<36> out<37> out<38> out<39> out<40> out<41>
        + out<42> out<43> out<44> out<45> out<46> out<47> out<48> out<49> out<50> out<51> out<52>
        + out<53> out<54> out<55> out<56> out<57> out<58> out<59> out<60> out<61> out<62> out<63>
        + rst rst' vdd vss conf_32
    Xi0 clk in out<0> out<1> out<2> out<3> out<4> out<5> out<6> out<7> out<8> out<9> out<10> out<11>
        + out<12> out<13> out<14> out<15> out<16> out<17> out<18> out<19> out<20> out<21> out<22>
        + out<23> out<24> out<25> out<26> out<27> out<28> out<29> out<30> out<31> rst rst' vdd vss
        + conf_32
.ENDS
```