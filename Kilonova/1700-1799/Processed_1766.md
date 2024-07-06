# Task

The grass of a rectangular sports field is maintained with a lawn mower. The size of the field is $m$ rows and $n$ columns of square plots with a size of $1 \cdot 1$ meters. The field is surrounded by a fence with two gates placed in two diagonally opposite corners of the field. We will consider that gate one is placed in the top-left corner of the field and gate two in the bottom-right corner.

The worker who maintains the lawn wants to do a fine job and at the same time wants to eliminate the mower's unnecessary movements. He always follows the same "algorithm" for traversing the field: he enters the lawn through gate one and exits through gate two, and between these two gates, he always follows an oblique serpentine path that follows the semi-diagonals of the field so as not to pass through the same portion twice. The way this path is constructed is illustrated in the following example for a field of size $5 \cdot 8$. It can be observed that after mowing the first plot, he always moves horizontally.

~[piatra.png]

In each unit of time, one plot of size $1 \cdot 1$ meters will be mowed. In the previous figure, the numbers represent the unit of time in which the worker mows the grass of the respective plot.

The lawnmower is very sensitive to stones accidentally found in the grass: if the blade of the machine hits a stone, the machine breaks down. Unfortunately, during the last match, an uneducated supporter threw a stone on the field. Unaware of this "minor detail," the worker started his work, but the moment the mower hit the stone, he stopped working.

# Task

Knowing the coordinates of the stone $(row, column)$, calculate in which unit of time the accident occurred.

# Input data

The input file `piatra.in` contains one line, which contains four numbers: $m$, $n$, $l$, $c$ separated by spaces with the following meaning: $m$ and $n$ represent the size of the lawn (number of rows and columns) and $l$ and $c$ represent the coordinates of the stone (row and column).

# Output data

The output file `piatra.out` will contain a single number representing the unit of time when the accident occurred.

# Constraints and clarifications

* $1 \leq m, n \leq 40\ 000$;
* $1 \leq l \leq m$;
* $1 \leq c \leq n$;
* The numbering of rows and columns starts from $1$.

# Example 1

`piatra.in`
```
5 8 2 4
```

`piatra.out`
```
14
```

# Example 2

`piatra.in`
```
5 8 3 6
```

`piatra.out`
```
28
```

# Example 3

`piatra.in`
```
32000 38000 31678 37812
```

`piatra.out`
```
1215869507
```
