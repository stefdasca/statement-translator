The village of Binăreni is in danger due to fires caused in the last month. It is represented by a binary matrix with $N$ rows and $M$ columns. All cells that have caught fire are represented by the value $0$. All cells in which there is no fire, represented by values of $1$, initially contain a house of a villager.

A cell is considered "safe" if it has not caught fire and is in one of the two situations below:
1. It is at the edge of the village (on row $1$, row $N$ or on column $1$, column $M$ of the matrix);
2. At least one of the $4$ neighboring cells in the directions $N$, $W$, $S$, and $E$ are "safe".

Gosu, the most renowned firefighter in the village, wants to save all houses that are not in "safe" cells, using his superpower: he can extinguish all fires in all cells that have caught fire on line $x$ and in all cells that have caught fire on column $y$, by placing himself at their intersection, in cell $(x, y)$. He can place himself both on a cell with fire and on a cell that contains a house. Thus, after using his superpower, all elements on line $x$ and all elements on column $y$ will have the value of $1$.

# Task

Given that Gosu can use his superpower only once, find all possible coordinate pairs $(x, y)$ where he can place himself to save all houses that are in danger.

# Input data
The first line of the input contains two integers $N$ and $M$, separated by a space, representing the dimensions of the matrix.
The next $N$ lines contain $M$ values of $0$ or $1$, separated by spaces, representing the description of the village matrix.

# Output data
In the console, print on different lines and separated by a space, the coordinates of the cells where Gosu can place himself to save all houses. The pairs of coordinates must be printed in lexicographic order. If there is no solution, print $-1$.

# Constraints and clarifications

* $3 \leq N, M \leq 10^3$;
* $A_{i,j} \in \{0,1\}, 1 \leq i \leq N, 1 \leq j \leq M$;
* It is guaranteed that there is at least one house in danger;
* For 30 points, $1 \leq N, M \leq 100$.

# Example 1

`stdin`
```
7 8
0 0 0 0 1 1 0 0
0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 1
0 0 0 1 0 0 0 1
0 0 0 0 0 0 1 0
1 0 0 0 0 0 0 0
```

`stdout`
```
5 1
5 2
5 3
6 1
6 2
6 3
7 3
```

## Explanation

In the first example, the village consists of $9$ houses, of which only $6$ are "safe." The houses in danger are located on the cells $(2, 2)$, $(5, 4)$, and $(6, 7)$. The solution contains $7$ pairs of coordinates, shown in lexicographic order. If he chooses, for instance, the cell $(5, 1)$, Gosu will extinguish the fire in:
- the neighboring cell to the west of the house in cell $(2, 2)$;
- the neighboring cells to the west and east of the house located at $(5, 4)$;
- the neighboring cell to the north of the last house.

All these neighbors then become "safe."
On row $7$ there is only one cell from which Gosu can extinguish the fire in at least one of the neighboring cells of each house in danger: $(7, 3)$. After using his superpower from this cell, the matrix becomes:

~[foc.png]

# Example 2

`stdin`
```
9 9
0 0 0 0 0 0 1 0 1
0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0 1
0 0 0 0 1 0 0 0 1
0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0 0
```

`stdout`
```
-1
```

## Explanation

There are $3$ houses in danger, in the cells $(2, 2)$, $(5, 5)$, and $(8, 8)$. There is no coordinate pair on which Gosu can place himself to save all the $3$ houses.