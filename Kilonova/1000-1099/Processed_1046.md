After consolidating the resistance structure, it is time to rebuild the wall of the fortress. The wall had a length of $L$ units and a height of $H$ units. As it deteriorated over time, it is no longer rectangular. On each of the $L$ units of length, there exists $V_i$ units of material stacked on top of each other and supported by the foundation, up to a height of $V_i$ units. It is desired to cover the remaining areas so that the wall becomes rectangular, with a height of $H$ units for each of the $L$ units of length.

We have rectangular pieces of material, each with dimensions of one unit. Therefore, we can say that the pieces have dimensions `1 X B` ($1 \leq B \leq L$) and for each value of $B$, we have as many pieces as needed (let's call them type $B$ pieces). For the wall to be stable, the pieces must be placed horizontally, meaning a piece of size `1 X B` will occupy $B$ units in length and one unit in height. It is also known that pieces of the same type $B$ have the same color, different from the color of pieces of other types. To make the wall beautiful, pieces of material of the same color must be used at the same height relative to the foundation. Determine the minimum number of pieces required to rebuild the wall.

# Input data

The input file `consolidare.in` contains on the first line two natural numbers $L$ and $H$, separated by a space, representing, as described above, the length and height that the rebuilt wall must have. The second line contains $L$ nonzero natural numbers, separated by a space, indicating, in order, the height in units of the existing part for each unit of length.

# Output data

The output file `consolidare.out` will contain on the first line a natural value that represents the minimum number of pieces used to build the wall according to the constraints.

# Constraints and clarifications

* $1 \leq L \leq 100 \ 000$
* $1 \leq H \leq 10$
* $0 \leq V_i \leq H$
* It is not allowed for a piece of material to go outside the $L$ units of length.

# Example

`consolidare.in`
```
10 4
0 0 1 3 0 1 1 2 2 2
```

`consolidare.out`
```
9
```

## Explanation

Initially, the wall looks like the image below. On the first row (numbered from the bottom), three pieces of type $1$ are placed. On the second row, two pieces of type $3$ are placed, on the third row, three pieces of type $3$ are placed, and on the fourth row, a single piece of type $10$ is placed.

~[image.png|align=left]