## Task

Michael is preparing for his next mission: several terrorists have occupied a triangular-shaped building, taken hostages, and are threatening to kill them if a series of unacceptable demands are not met. Michael wants to eliminate the terrorists with a surprise attack. To have maximum effect, he wants to strategically position and configure a jamming device. The jamming device can be positioned anywhere inside the building and has a configurable range $R$. Activating the device makes any terrorist inside the disc with radius $R$ centered on the jamming device unable to be informed that Michael has launched the attack, allowing Michael to neutralize them without any risk. Michael wants to jam as many terrorists as possible without jamming the area outside the building's perimeter. He provides you with the coordinates of the three points: $A$, $B$, and $C$ that define the building's perimeter, and asks you in return for the coordinates of point $D$, where he should position the jamming device and $R$, the range of this device.

## Input data

The input file `bruiaj.in` contains on the first 3 lines two integers each, representing the coordinates of points $A$, $B$, and $C$ respectively.

## Output data

The output file `bruiaj.out` will contain on the first line two numbers, representing the coordinates of point $D$, and on the second line will contain the number $R$.

## Constraints and clarifications

$-1 000 \leq A_x, A_y, B_x, B_y, C_x, C_y \leq 1 000$

To meet Michael's requirements, the coordinates of point $D$ and the radius $R$ must be calculated with a precision of $10^{-4}$.

## Example

`bruiaj.in`
```
0 0
1 0
0 1
```

`bruiaj.out`
```
0.292893 0.292893
0.292893
```