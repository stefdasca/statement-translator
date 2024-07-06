~[albina_1.jpg|align=right]
The queen of the hive is away, and the $N$ newly born bees need to be fed. Maya is the bee responsible for this task. Maya makes a plan to be able to act. For each bee, Maya starts from an initial cell that contains the necessary amount of honey and moves from cell to cell until she reaches the bee she will feed.

A honeycomb is made up of columns numbered with capital English alphabet letters from $A$ to $Z$, and the position of each cell on a column is identified by values $1$, $2$, $3$, $4$, $5$, $\\dots$ from bottom to top, as shown in the figure. Each honeycomb cell is hexagonal. From one cell, you can reach the $6$ neighboring cells by moving in the directions: 1 - up, 2 - up right, 3 - down right, etc. (as shown in the adjacent figure).

~[albina_2.jpg|align=right]
The honeycomb is circular, so after column $Z$ comes, to the right, column $A$, and before column $A$ is, to the left, column $Z$.

# Task

Knowing the addresses of the cells from which Maya will start, it is required to:
1. Display the columns that contain the most initial cells.
2. Additionally, knowing the sequences of moves Maya will make to reach each bee, it is required to provide the addresses of the $N$ destination cells.

# Input data

The input file `maya.in` contains:
- The first line contains the natural number $C$ ($1$ or $2$) representing the task requirement.
- The next line contains the natural number $N$ representing the number of initial cells.
- The following line contains $N$ addresses separated by a space, each address being in the form `ColumnNumber`.

For task $2$, there will be $N$ more lines, each containing:
- A natural number representing the number of moves, followed by a space, and then a sequence of digits $1$, $2$, $3$, $4$, $5$ or $6$ (without spaces between them) representing the directions in which Maya will move to reach the destination cell.

# Output data

The output file `maya.out`:
- If the task is $1$, will contain a sequence of capital letters in alphabetical order, separated by a space, representing the columns that contain the maximum number of initial cells;
- If the task is $2$, will contain $N$ lines each formed of addresses in the form ColumnNumber representing the destination cells.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$;
* Each sequence of moves is at most $200$ digits long;
* In the tests, there won't be movements in direction $4$ for cells in the first positions of each column ($\text{A1}$, $\text{B1}$, $\text{C1}$, $\dots$, $\text{Z1}$), and there won't be movements in directions $3$ and $5$ for each of the columns: $\text{B1}$, $\text{D1}$, $\text{F1}$, $\text{H1}$, $\dots$;
* Each column can contain at most $5 \ 000$ cells vertically.

# Example 1

`maya.in`
```
1
5
D2 A3 A7 E2 D101
```

`maya.out`
```
A D
```

## Explanation

Column $A$ contains two initial cells, column $D$ also two, and column $E$ only one. The columns with the most initial cells are $A$ and $D$.

# Example 2

`maya.in`
```
2
5
D2 A3 A7 E2 D101
3 123
7 1111111
6 121212
4 1156
7 4444441
```

`maya.out`
```
F3
A10
D12
C4
D96
```

## Explanation

For the initial cell $\\text{D2}$, the bee's path is: `D2 D3 E3 F3`.

~[albina_3.jpg]