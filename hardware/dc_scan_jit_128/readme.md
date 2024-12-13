# `dc_scan_jit_128` Module
![Layout](dc_scan_jit_128.png)

## Cell Hierarchy

`dc_scan_jit_128` **4864** (number MOS pairs)
- `dc_jit_128` **2048**
- `scan_jit_128` **2816**

## Netlist

```
.SUBCKT dc_scan_jit_128 dc_clk dc_in dc_last dc_rst dc_rst' scan_clk scan_in_ser scan_out scan_rst
                        + scan_rst' scan_ser vdd vss
    Xi0 dc_clk dc_in dc_last dc_out<0> dc_out<1> dc_out<2> dc_out<3> dc_out<4> dc_out<5> dc_out<6>
        + dc_out<7> dc_out<8> dc_out<9> dc_out<10> dc_out<11> dc_out<12> dc_out<13> dc_out<14>
        + dc_out<15> dc_out<16> dc_out<17> dc_out<18> dc_out<19> dc_out<20> dc_out<21> dc_out<22>
        + dc_out<23> dc_out<24> dc_out<25> dc_out<26> dc_out<27> dc_out<28> dc_out<29> dc_out<30>
        + dc_out<31> dc_out<32> dc_out<33> dc_out<34> dc_out<35> dc_out<36> dc_out<37> dc_out<38>
        + dc_out<39> dc_out<40> dc_out<41> dc_out<42> dc_out<43> dc_out<44> dc_out<45> dc_out<46>
        + dc_out<47> dc_out<48> dc_out<49> dc_out<50> dc_out<51> dc_out<52> dc_out<53> dc_out<54>
        + dc_out<55> dc_out<56> dc_out<57> dc_out<58> dc_out<59> dc_out<60> dc_out<61> dc_out<62>
        + dc_out<63> dc_out<64> dc_out<65> dc_out<66> dc_out<67> dc_out<68> dc_out<69> dc_out<70>
        + dc_out<71> dc_out<72> dc_out<73> dc_out<74> dc_out<75> dc_out<76> dc_out<77> dc_out<78>
        + dc_out<79> dc_out<80> dc_out<81> dc_out<82> dc_out<83> dc_out<84> dc_out<85> dc_out<86>
        + dc_out<87> dc_out<88> dc_out<89> dc_out<90> dc_out<91> dc_out<92> dc_out<93> dc_out<94>
        + dc_out<95> dc_out<96> dc_out<97> dc_out<98> dc_out<99> dc_out<100> dc_out<101> dc_out<102>
        + dc_out<103> dc_out<104> dc_out<105> dc_out<106> dc_out<107> dc_out<108> dc_out<109>
        + dc_out<110> dc_out<111> dc_out<112> dc_out<113> dc_out<114> dc_out<115> dc_out<116>
        + dc_out<117> dc_out<118> dc_out<119> dc_out<120> dc_out<121> dc_out<122> dc_out<123>
        + dc_out<124> dc_out<125> dc_out<126> dc_out<127> dc_rst dc_rst' vdd vss dc_jit_128
    Xi1 scan_clk dc_out<0> dc_out<1> dc_out<2> dc_out<3> dc_out<4> dc_out<5> dc_out<6> dc_out<7>
        + dc_out<8> dc_out<9> dc_out<10> dc_out<11> dc_out<12> dc_out<13> dc_out<14> dc_out<15>
        + dc_out<16> dc_out<17> dc_out<18> dc_out<19> dc_out<20> dc_out<21> dc_out<22> dc_out<23>
        + dc_out<24> dc_out<25> dc_out<26> dc_out<27> dc_out<28> dc_out<29> dc_out<30> dc_out<31>
        + dc_out<32> dc_out<33> dc_out<34> dc_out<35> dc_out<36> dc_out<37> dc_out<38> dc_out<39>
        + dc_out<40> dc_out<41> dc_out<42> dc_out<43> dc_out<44> dc_out<45> dc_out<46> dc_out<47>
        + dc_out<48> dc_out<49> dc_out<50> dc_out<51> dc_out<52> dc_out<53> dc_out<54> dc_out<55>
        + dc_out<56> dc_out<57> dc_out<58> dc_out<59> dc_out<60> dc_out<61> dc_out<62> dc_out<63>
        + dc_out<64> dc_out<65> dc_out<66> dc_out<67> dc_out<68> dc_out<69> dc_out<70> dc_out<71>
        + dc_out<72> dc_out<73> dc_out<74> dc_out<75> dc_out<76> dc_out<77> dc_out<78> dc_out<79>
        + dc_out<80> dc_out<81> dc_out<82> dc_out<83> dc_out<84> dc_out<85> dc_out<86> dc_out<87>
        + dc_out<88> dc_out<89> dc_out<90> dc_out<91> dc_out<92> dc_out<93> dc_out<94> dc_out<95>
        + dc_out<96> dc_out<97> dc_out<98> dc_out<99> dc_out<100> dc_out<101> dc_out<102>
        + dc_out<103> dc_out<104> dc_out<105> dc_out<106> dc_out<107> dc_out<108> dc_out<109>
        + dc_out<110> dc_out<111> dc_out<112> dc_out<113> dc_out<114> dc_out<115> dc_out<116>
        + dc_out<117> dc_out<118> dc_out<119> dc_out<120> dc_out<121> dc_out<122> dc_out<123>
        + dc_out<124> dc_out<125> dc_out<126> dc_out<127> scan_in_ser scan_out scan_rst scan_rst'
        + scan_ser vdd vss scan_jit_128
.ENDS
```
