# `conf_268` Module
![Layout](conf_268.png)

## Cell Hierarchy

`conf_268` **4569** (number MOS pairs)
- `conf_256` **4352**
- `conf_8` **136**
- `inv` **1**
- `buffer_large` **4** *x3*
- `conf_4` **68**

## Netlist

```
.SUBCKT conf_268 clk in out<0> out<1> out<2> out<3> out<4> out<5> out<6> out<7> out<8> out<9>
                 + out<10> out<11> out<12> out<13> out<14> out<15> out<16> out<17> out<18> out<19>
                 + out<20> out<21> out<22> out<23> out<24> out<25> out<26> out<27> out<28> out<29>
                 + out<30> out<31> out<32> out<33> out<34> out<35> out<36> out<37> out<38> out<39>
                 + out<40> out<41> out<42> out<43> out<44> out<45> out<46> out<47> out<48> out<49>
                 + out<50> out<51> out<52> out<53> out<54> out<55> out<56> out<57> out<58> out<59>
                 + out<60> out<61> out<62> out<63> out<64> out<65> out<66> out<67> out<68> out<69>
                 + out<70> out<71> out<72> out<73> out<74> out<75> out<76> out<77> out<78> out<79>
                 + out<80> out<81> out<82> out<83> out<84> out<85> out<86> out<87> out<88> out<89>
                 + out<90> out<91> out<92> out<93> out<94> out<95> out<96> out<97> out<98> out<99>
                 + out<100> out<101> out<102> out<103> out<104> out<105> out<106> out<107> out<108>
                 + out<109> out<110> out<111> out<112> out<113> out<114> out<115> out<116> out<117>
                 + out<118> out<119> out<120> out<121> out<122> out<123> out<124> out<125> out<126>
                 + out<127> out<128> out<129> out<130> out<131> out<132> out<133> out<134> out<135>
                 + out<136> out<137> out<138> out<139> out<140> out<141> out<142> out<143> out<144>
                 + out<145> out<146> out<147> out<148> out<149> out<150> out<151> out<152> out<153>
                 + out<154> out<155> out<156> out<157> out<158> out<159> out<160> out<161> out<162>
                 + out<163> out<164> out<165> out<166> out<167> out<168> out<169> out<170> out<171>
                 + out<172> out<173> out<174> out<175> out<176> out<177> out<178> out<179> out<180>
                 + out<181> out<182> out<183> out<184> out<185> out<186> out<187> out<188> out<189>
                 + out<190> out<191> out<192> out<193> out<194> out<195> out<196> out<197> out<198>
                 + out<199> out<200> out<201> out<202> out<203> out<204> out<205> out<206> out<207>
                 + out<208> out<209> out<210> out<211> out<212> out<213> out<214> out<215> out<216>
                 + out<217> out<218> out<219> out<220> out<221> out<222> out<223> out<224> out<225>
                 + out<226> out<227> out<228> out<229> out<230> out<231> out<232> out<233> out<234>
                 + out<235> out<236> out<237> out<238> out<239> out<240> out<241> out<242> out<243>
                 + out<244> out<245> out<246> out<247> out<248> out<249> out<250> out<251> out<252>
                 + out<253> out<254> out<255> out<256> out<257> out<258> out<259> out<260> out<261>
                 + out<262> out<263> out<264> out<265> out<266> out<267> rst vdd vss
    Xi0 clk_i in out<0> out<1> out<2> out<3> out<4> out<5> out<6> out<7> out<8> out<9> out<10>
        + out<11> out<12> out<13> out<14> out<15> out<16> out<17> out<18> out<19> out<20> out<21>
        + out<22> out<23> out<24> out<25> out<26> out<27> out<28> out<29> out<30> out<31> out<32>
        + out<33> out<34> out<35> out<36> out<37> out<38> out<39> out<40> out<41> out<42> out<43>
        + out<44> out<45> out<46> out<47> out<48> out<49> out<50> out<51> out<52> out<53> out<54>
        + out<55> out<56> out<57> out<58> out<59> out<60> out<61> out<62> out<63> out<64> out<65>
        + out<66> out<67> out<68> out<69> out<70> out<71> out<72> out<73> out<74> out<75> out<76>
        + out<77> out<78> out<79> out<80> out<81> out<82> out<83> out<84> out<85> out<86> out<87>
        + out<88> out<89> out<90> out<91> out<92> out<93> out<94> out<95> out<96> out<97> out<98>
        + out<99> out<100> out<101> out<102> out<103> out<104> out<105> out<106> out<107> out<108>
        + out<109> out<110> out<111> out<112> out<113> out<114> out<115> out<116> out<117> out<118>
        + out<119> out<120> out<121> out<122> out<123> out<124> out<125> out<126> out<127> out<128>
        + out<129> out<130> out<131> out<132> out<133> out<134> out<135> out<136> out<137> out<138>
        + out<139> out<140> out<141> out<142> out<143> out<144> out<145> out<146> out<147> out<148>
        + out<149> out<150> out<151> out<152> out<153> out<154> out<155> out<156> out<157> out<158>
        + out<159> out<160> out<161> out<162> out<163> out<164> out<165> out<166> out<167> out<168>
        + out<169> out<170> out<171> out<172> out<173> out<174> out<175> out<176> out<177> out<178>
        + out<179> out<180> out<181> out<182> out<183> out<184> out<185> out<186> out<187> out<188>
        + out<189> out<190> out<191> out<192> out<193> out<194> out<195> out<196> out<197> out<198>
        + out<199> out<200> out<201> out<202> out<203> out<204> out<205> out<206> out<207> out<208>
        + out<209> out<210> out<211> out<212> out<213> out<214> out<215> out<216> out<217> out<218>
        + out<219> out<220> out<221> out<222> out<223> out<224> out<225> out<226> out<227> out<228>
        + out<229> out<230> out<231> out<232> out<233> out<234> out<235> out<236> out<237> out<238>
        + out<239> out<240> out<241> out<242> out<243> out<244> out<245> out<246> out<247> out<248>
        + out<249> out<250> out<251> out<252> out<253> out<254> out<255> rst_i rst'_i vdd vss
        + conf_256
    Xi1 clk_i out<255> out<256> out<257> out<258> out<259> out<260> out<261> out<262> out<263> rst_i
        + rst'_i vdd vss conf_8
    Xi3 rst rst' vdd vss inv
    Xi5 rst rst_i vdd vss buffer_large
    Xi4 rst' rst'_i vdd vss buffer_large
    Xi6 clk clk_i vdd vss buffer_large
    Xi2 clk_i out<263> out<264> out<265> out<266> out<267> rst_i rst'_i vdd vss conf_4
.ENDS
```
