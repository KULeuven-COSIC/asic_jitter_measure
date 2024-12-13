# `ro_2i` Module
![Layout](ro_2i.png)

## Cell Hierarchy

`ro_2i` **20** (number MOS pairs)
- `inv_conf` **9** *x2*
- `nand2` **2**

## Netlist

```
.SUBCKT ro_2i conf'<0> conf'<1> conf'<2> conf'<3> conf'<4> conf'<5> conf'<6> conf'<7> conf<0>
              + conf<1> conf<2> conf<3> conf<4> conf<5> conf<6> conf<7> enable out vdd vss
    Xi1 conf'<4> conf'<5> conf'<6> conf'<7> conf<4> conf<5> conf<6> conf<7> int out vdd vss inv_conf
    Xi0 conf'<0> conf'<1> conf'<2> conf'<3> conf<0> conf<1> conf<2> conf<3> nand_out int vdd vss
        + inv_conf
    Xi2 out enable nand_out vdd vss nand2
.ENDS
```
