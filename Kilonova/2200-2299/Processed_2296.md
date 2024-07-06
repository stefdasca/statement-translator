Here is the translated competitive programming problem statement:

---

A sidewalk of length $N$ and width $L$ needs to be paved with tiles. The tiles are of different types, but for each type, we have an unlimited quantity. The length of each tile type is the same $L$, while the width can be a value among $a_1, a_2, a_3, \dots, a_k$. The sidewalk has $M$ occupied zones on its surface, which will not be paved. These zones always have a square shape with a side of $1$ (representing the location of poles, mailboxes, channels, etc.). The coordinates of these $M$ points $(x_1,y_1), (x_2,y_2), \dots (x_m,y_m)$ are known. ($x$ represents the column, $y$ represents the row of the point).

In the examples below, we see three distinct methods of covering a sidewalk of dimensions $6 \cdot 3$ using two types of tiles: $1 \cdot 3$ and $2 \cdot 3$, having three occupied zones on the sidewalk, namely: $(6,2), (3,1), (6,3)$.

~[trotuar.png]

# Task

Knowing the dimensions of the sidewalk, the types of available tiles, and the coordinates of the occupied zones, determine the number of distinct pavings possible modulo $666 \ 013$.

# Input data

The file `trotuar.in` contains on the first line 4 natural numbers $N$, $L$, $K$, and $M$ separated by a space, representing the length and width of the sidewalk, respectively the number of types of tiles and the number of occupied zones. The next line contains the $K$ widths of the types of tiles: $a_1, a_2, a_3, \dots, a_k$ separated by a space.

The next $M$ lines each contain two natural numbers separated by a space, representing a coordinate $(x_i,y_i)$, for each $1 \leq i \leq m$ of the occupied zones.

# Output data

The file `trotuar.out` will contain a single line, the number of distinct pavings modulo 666013.

# Constraints and clarifications

* $0 < N \leq 100 \ 000$
* $0 < K \leq L \leq 255$
* $0 < a_1, a_2, a_3, \dots, a_k \leq L$ are pairwise distinct
* $0 \leq M \leq 450$
* For $20\%$ of the tests $M = 0$
* It is guaranteed that there exists at least one solution
* It is recommended to use 64-bit integers for the multiplication operation.

# Example

`trotuar.in`
```
6 3 2 3
2 1
6 2
3 1
6 3
```

`trotuar.out`
```
4
```

## Explanation

There are a total of four distinct ways to cover the sidewalk. Three of them are shown in the drawing above.

---

After double-checking, the statement contains no grammar or syntax errors.