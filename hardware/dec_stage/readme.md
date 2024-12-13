# `dec_stage` Module
![Layout](dec_stage.png)

## Cell Hierarchy

`dec_stage` **5** (number MOS pairs)
- `inv` **1**
- `nor2` **2**
- `nand2` **2**

## Netlist

```
.SUBCKT dec_stage conf_rand ff_in ff_prev out vdd vss
    Xi0 ff_in net3 vdd vss inv
    Xi1 ff_prev net3 net4 vdd vss nor2
    Xi2 net4 conf_rand out vdd vss nand2
.ENDS
```
