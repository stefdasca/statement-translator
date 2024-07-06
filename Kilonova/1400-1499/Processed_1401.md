Păcală succeeded in finalizing the agreement with the boyar he served, and according to their deal, the boyar must reward him by giving him a part of his orchard with fruit trees.

The boyar is a very orderly man, so his orchard is a square with a side length of $N$ meters where, in old times, there were planted $N$ rows with $N$ trees each. Any fruit tree could be identified by knowing the row number it is in and its position within that row. Over time, some trees have dried out, and now there are only $P$ trees remaining. Păcală has to delimit in the orchard a square garden with a side length of $K$ meters.

# Task

Knowing the dimensions of the orchard and garden, the number of trees in the orchard, and the position of each tree, determine the maximum number of trees in a square garden with a side length of $K$ and the number of ways the garden can be placed to contain the maximum number of trees.

# Input data

The file `gradina.in` contains:

* The first line contains the natural numbers $N, P$, and $K$, separated by a space, as per the statement;
* The next $P$ lines each contain $2$ natural numbers $L$ and $C$, separated by a space, representing the row number and the position within that row of each tree in the orchard.

# Output data

The file `gradina.out` will contain:

* The first line contains the maximum number of fruit trees in a square garden with a side length of $K$ meters;
* The second line contains the number of possible placements of the garden so that it contains the determined maximum number of trees.

# Constraints and clarifications

* $2 \leq N \leq 1\ 000$
* $1 \leq P \leq N^2$
* $1 \leq K \leq N$

# Example

`gradina.in`
```
12 10 5
4 3
5 5
6 8
7 3
7 7
8 8
9 3
9 6
10 10
10 5
```

`gradina.out`
```
5
8
```

## Explanation

Păcală's garden can have a maximum of $5$ fruit trees.

It can be placed in $8$ ways, having the top-left corner with coordinates: $(5, 3)$, $(5, 4)$, $(5, 5)$, $(6, 3)$, $(6, 4)$, $(6, 5)$, $(6, 6)$, $(7, 3)$.