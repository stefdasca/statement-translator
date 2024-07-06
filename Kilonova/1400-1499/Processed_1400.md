# Task

A **polyomino** is a compact planar geometric shape composed of one or more domino pieces, equal squares with side length $1$. Two pieces are considered adjacent if they share a common side.

**Examples of Polyominoes** with $n$ pieces:

~[Poza1.png|align=left|width=50em]

Two Polyominoes are considered identical if they are composed of the same number of pieces and have the same configuration, or the configuration of one can be obtained by mirroring the other. Otherwise, the two Polyominoes are considered distinct.

|Distinct Polyominoes|~[Poza3.png]|Polyominoes that are not distinct|~[Poza4.png]|
|:-:|:-:|:-:|:-:|

A polyomino can be rotated by ${90^{\large\circ}}$, ${180^{\large\circ}}$, and ${270^{\large\circ}}$, counterclockwise. Rotation results in other Polyominoes that are not necessarily identical to the initial one.

**Example**:

|By rotating the polyomino|~[Poza5.png]|we obtain:|~[Poza6.png]|
|:-:|:-:|:-:|:-:|

None of these Polyominoes is identical to the initial one.

A polyomino is **convex** if, when traversing successively through the rows or columns, no holes are encountered.

|Convex polyomino| ~[932486ef1faaca147083c61dd64b6497.png] | Non-convex polyominoes |~[54404d25b3327902bdcee1baac5eba7f.png]|
|:-:|:-:|:-:|:-:|

A polyomino is **skew convex** (skew polyomino) if it is convex and, when successively traversing the columns from left to right, these do not decrease in height. In other words, the bottom part of the column on the left is always smaller or equal in height to the bottom part of the column on the right. Similarly, the top part of the column on the left is always smaller or equal to the top part of the column on the right.

**Examples**:

|Skew polyominoes|~[Poza7.png]|Polyominoes that are not skew|~[Poza8.png]|
|:-:|:-:|:-:|:-:|

# Task

Determine the number of distinct skew polyominoes that have a perimeter equal to $2 \cdot N+2$. This number can be large, so we are interested in the result modulo $30\ 103$.

# Input data

The input file `poly.in` contains a single natural number $N$.

# Output data

The output file `poly.out` contains on the first line a natural number representing the number of skew polyominoes that have a perimeter equal to $2 \cdot N+2$, printed modulo $30\ 103$.

# Constraints and clarifications

* $2 \leq N \leq 500$

# Example

`poly.in`
```
3
```

`poly.out`
```
5
```

## Explanation

There are $5$ polyominoes that satisfy the task:

~[Poza9.png]