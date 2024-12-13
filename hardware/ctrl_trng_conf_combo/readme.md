# `ctrl_trng_conf_combo` Module
![Layout](ctrl_trng_conf_combo.png)

## Cell Hierarchy

`ctrl_trng_conf_combo` **20170** (number MOS pairs)
- `ctrl_trng_combo` **15594**
- `one_to_7` **7**
- `conf_268` **4569**

## Netlist

```
.SUBCKT ctrl_trng_conf_combo conf<260> conf<261> conf<262> conf<263> conf<264> conf<265> conf<266>
                             + conf<267> conf_clk conf_in conf_rst core_rst data_out data_ready
                             + ext_clk ro_out scan<0> scan<1> scan<2> scan<3> scan<4> scan<5>
                             + scan<6> scan<7> scan<8> scan<9> scan<10> scan<11> scan<12> scan<13>
                             + scan<14> scan<15> scan<16> scan<17> scan<18> scan<19> scan<20>
                             + scan<21> scan<22> scan<23> scan<24> scan<25> sendfree'<6> ser_clk
                             + vdd_core vdd_dc vdd_tdc vss
    Xi1 conf<253> conf<254> conf<255> conf<256> conf<257> conf<258> conf<259> conf<260> conf<261>
        + conf<262> conf<263> conf<264> conf<265> conf<252> conf<0> conf<1> conf<49> conf<50>
        + conf<67> conf<68> conf<69> conf<70> conf<71> conf<72> conf<73> conf<74> conf<75> conf<76>
        + conf<77> conf<78> conf<79> conf<80> conf<81> conf<82> conf<83> conf<84> conf<85> conf<86>
        + conf<2> conf<3> conf<4> conf<5> conf<266> conf<267> conf<247> conf<248> conf<249>
        + conf<250> conf<48> conf<16> conf<17> conf<18> conf<19> conf<20> conf<21> conf<22> conf<23>
        + conf<24> conf<25> conf<26> conf<27> conf<28> conf<29> conf<30> conf<31> conf<107>
        + conf<108> conf<109> conf<110> conf<111> conf<112> conf<113> conf<114> conf<115> conf<116>
        + conf<117> conf<118> conf<119> conf<120> conf<121> conf<122> conf<123> conf<124> conf<125>
        + conf<126> conf<87> conf<88> conf<89> conf<90> conf<91> conf<92> conf<93> conf<94> conf<95>
        + conf<96> conf<97> conf<98> conf<99> conf<100> conf<101> conf<102> conf<103> conf<104>
        + conf<105> conf<106> conf<147> conf<148> conf<149> conf<150> conf<151> conf<152> conf<153>
        + conf<154> conf<155> conf<156> conf<157> conf<158> conf<159> conf<160> conf<161> conf<162>
        + conf<163> conf<164> conf<165> conf<166> conf<127> conf<128> conf<129> conf<130> conf<131>
        + conf<132> conf<133> conf<134> conf<135> conf<136> conf<137> conf<138> conf<139> conf<140>
        + conf<141> conf<142> conf<143> conf<144> conf<145> conf<146> conf<251> conf<187> conf<188>
        + conf<189> conf<190> conf<191> conf<192> conf<193> conf<194> conf<195> conf<196> conf<197>
        + conf<198> conf<199> conf<200> conf<201> conf<202> conf<203> conf<204> conf<205> conf<206>
        + conf<167> conf<168> conf<169> conf<170> conf<171> conf<172> conf<173> conf<174> conf<175>
        + conf<176> conf<177> conf<178> conf<179> conf<180> conf<181> conf<182> conf<183> conf<184>
        + conf<185> conf<186> conf<227> conf<228> conf<229> conf<230> conf<231> conf<232> conf<233>
        + conf<234> conf<235> conf<236> conf<237> conf<238> conf<239> conf<240> conf<241> conf<242>
        + conf<243> conf<244> conf<245> conf<246> conf<207> conf<208> conf<209> conf<210> conf<211>
        + conf<212> conf<213> conf<214> conf<215> conf<216> conf<217> conf<218> conf<219> conf<220>
        + conf<221> conf<222> conf<223> conf<224> conf<225> conf<226> conf<6> conf<7> conf<8>
        + conf<9> conf<10> conf<11> conf<12> conf<13> conf<14> conf<15> conf<32> conf<33> conf<34>
        + conf<35> conf<36> conf<37> conf<38> conf<39> conf<40> conf<41> conf<42> conf<43> conf<44>
        + conf<45> conf<46> conf<47> conf<59> conf<60> conf<61> conf<62> conf<63> conf<64> conf<65>
        + conf<66> conf<51> conf<52> conf<53> conf<54> conf<55> conf<56> conf<57> conf<58> data_out
        + sendfree'<2> data_ready sendfree'<3> scan<25> sendfree'<4> ext_clk scan<24> sendfree'<5>
        + ro_out core_rst scan<0> scan<1> scan<2> scan<3> scan<4> scan<5> scan<6> scan<7> scan<8>
        + scan<9> scan<10> scan<11> scan<12> scan<13> scan<14> scan<15> scan<16> scan<17> scan<18>
        + scan<19> scan<20> scan<21> scan<22> ser_clk scan<23> sendfree'<1> sendfree'<0> vdd_core
        + vdd_dc vdd_tdc vss ctrl_trng_combo
    Xi2 conf<48> sendfree'<0> sendfree'<1> sendfree'<2> sendfree'<3> sendfree'<4> sendfree'<5>
        + sendfree'<6> vdd_core vss one_to_7
    Xi0 conf_clk conf_in conf<0> conf<1> conf<2> conf<3> conf<4> conf<5> conf<6> conf<7> conf<8>
        + conf<9> conf<10> conf<11> conf<12> conf<13> conf<14> conf<15> conf<16> conf<17> conf<18>
        + conf<19> conf<20> conf<21> conf<22> conf<23> conf<24> conf<25> conf<26> conf<27> conf<28>
        + conf<29> conf<30> conf<31> conf<32> conf<33> conf<34> conf<35> conf<36> conf<37> conf<38>
        + conf<39> conf<40> conf<41> conf<42> conf<43> conf<44> conf<45> conf<46> conf<47> conf<48>
        + conf<49> conf<50> conf<51> conf<52> conf<53> conf<54> conf<55> conf<56> conf<57> conf<58>
        + conf<59> conf<60> conf<61> conf<62> conf<63> conf<64> conf<65> conf<66> conf<67> conf<68>
        + conf<69> conf<70> conf<71> conf<72> conf<73> conf<74> conf<75> conf<76> conf<77> conf<78>
        + conf<79> conf<80> conf<81> conf<82> conf<83> conf<84> conf<85> conf<86> conf<87> conf<88>
        + conf<89> conf<90> conf<91> conf<92> conf<93> conf<94> conf<95> conf<96> conf<97> conf<98>
        + conf<99> conf<100> conf<101> conf<102> conf<103> conf<104> conf<105> conf<106> conf<107>
        + conf<108> conf<109> conf<110> conf<111> conf<112> conf<113> conf<114> conf<115> conf<116>
        + conf<117> conf<118> conf<119> conf<120> conf<121> conf<122> conf<123> conf<124> conf<125>
        + conf<126> conf<127> conf<128> conf<129> conf<130> conf<131> conf<132> conf<133> conf<134>
        + conf<135> conf<136> conf<137> conf<138> conf<139> conf<140> conf<141> conf<142> conf<143>
        + conf<144> conf<145> conf<146> conf<147> conf<148> conf<149> conf<150> conf<151> conf<152>
        + conf<153> conf<154> conf<155> conf<156> conf<157> conf<158> conf<159> conf<160> conf<161>
        + conf<162> conf<163> conf<164> conf<165> conf<166> conf<167> conf<168> conf<169> conf<170>
        + conf<171> conf<172> conf<173> conf<174> conf<175> conf<176> conf<177> conf<178> conf<179>
        + conf<180> conf<181> conf<182> conf<183> conf<184> conf<185> conf<186> conf<187> conf<188>
        + conf<189> conf<190> conf<191> conf<192> conf<193> conf<194> conf<195> conf<196> conf<197>
        + conf<198> conf<199> conf<200> conf<201> conf<202> conf<203> conf<204> conf<205> conf<206>
        + conf<207> conf<208> conf<209> conf<210> conf<211> conf<212> conf<213> conf<214> conf<215>
        + conf<216> conf<217> conf<218> conf<219> conf<220> conf<221> conf<222> conf<223> conf<224>
        + conf<225> conf<226> conf<227> conf<228> conf<229> conf<230> conf<231> conf<232> conf<233>
        + conf<234> conf<235> conf<236> conf<237> conf<238> conf<239> conf<240> conf<241> conf<242>
        + conf<243> conf<244> conf<245> conf<246> conf<247> conf<248> conf<249> conf<250> conf<251>
        + conf<252> conf<253> conf<254> conf<255> conf<256> conf<257> conf<258> conf<259> conf<260>
        + conf<261> conf<262> conf<263> conf<264> conf<265> conf<266> conf<267> conf_rst vdd_core
        + vss conf_268
.ENDS
```
