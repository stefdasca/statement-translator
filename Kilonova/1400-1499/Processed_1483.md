
Tudor received an educational game called â€œRoboÈ›elâ€ with which he will learn the cardinal points North, East, South, West. The game consists of a robot that moves on a board in the form of a square matrix, divided into $R$ rows and $R$ columns. Each cell, at the intersection of a row and a column, is either an â€œemptyâ€ cell or a *signal* cell, in which case it is labeled with one of the letters `N`, `E`, `S`, `V`, representing $4$ possible directions of movement. When the robot reaches a â€œsignal cellâ€, it changes its direction as follows:

* If the cell is labeled with `N` then the robot will move from bottom to top
* If the cell is labeled with `E` then the robot will move from left to right
* If the cell is labeled with `S` then the robot will move from top to bottom
* If the cell is labeled with `V` then the robot will move from right to left

Two signal cells form a *blocking* pair if:

* They are on the same row and contain the letters `E` and `V`, the cell with `E` has a smaller column than the one labeled `V`, and between them, on the same row, there are no other signal cells.
* They are on the same column and contain the letters `S` and `N`, the cell with `S` has a smaller row than the one labeled `N` and between them, on the same column, there are no other signal cells.

~[figura1.png|align=right]
In $Figure \\ 1$, for example, there are $2$ blocking pairs: The pair $(1, 2)$, $(5, 2)$ and the pair $(2,3)$, $(2, 5)$. The robot starts from cell $(1, 1)$, located on the first row and the first column and if this one is empty, it moves within the first row, from left to right. If the starting cell $(1, 1)$ is a signal, then the robot will move in the direction indicated by the letter with which it is labeled.
Considering that the robot moves on the board, it stops **only** in the following situations:

* The robot enters an empty cell located on the first or last row, or the first or last column, in which case if it maintained the current movement direction it would leave the board.
* The robot enters a â€œsignal cellâ€ of a blocking pair and will stop in the other cell of the pair.

~[figura23.png|align=right]
For example, in $Figure \\ 2$, the robot reaches the empty cell $(3, 5)$ where it stops. In $Figure \\ 3$, the robot will stop in cell $(4, 1)$ because if it changed direction to East, it would return to the last visited signal cell, $(4, 3)$.
The robot moves one cell at a time, in the direction of movement.

# Task

Write a program that, knowing the number $R$ of rows and columns and the $K$ signal cells, determines:

1. All blocking pairs on the board
2. The number of steps taken in each direction: North, East, South, and West

# Input data

The input file `robotel.in` contains on the first line the natural number $P$ representing the task from the problem that needs to be solved, on the second line, separated by a space, the natural number $R$ and the natural number $K$, and on the following $K$ lines, two natural numbers and a character, separated by a space representing, in order, the row, column, and letter of a signal cell.

# Output data

If the value of $P$ is $1$, only task $1$ will be solved. The output file `robotel.out` will contain the blocking pairs, for each pair of cells displaying $4$ natural numbers separated by a space, representing, in order, the row, column of the first signal cell, and the row and column of the second signal cell. The pairs of cells will be displayed in order according to the rule: a pair $L_1 \\ C_1 \\ L_2 \\ C_2$ will be displayed before the pair $L_3 \\ C_3 \\ L_4 \\ C_4$ if $L_1 < L_3$ or $L_1 = L_3$ and $C_1 < C_3$, meaning the pair with the first cell having a smaller row than the first cell of the other pair or for equal rows, the pair with the smaller column will be displayed first. If there are no such pairs of cells, the output file will display the value $0$.
If the value of $P$ is $2$, only task $2$ will be solved. The output file `robotel.out` will contain $4$ natural numbers separated by a space, representing, in order, the number of steps taken by the robot in the directions North, East, South, and West.

# Constraints and clarifications

* $2 \leq R \leq 200$
* $1 \leq K \leq R \cdot R$
* For the correct solution of each task, $50$ points are awarded
* A signal cell contains a single letter
* For task $2$ it is guaranteed that in all tests the robot's movement stops!

# Example 1

`robotel.in`
```
1
5 4
1 3 S
3 1 E
5 1 N
5 3 V
```

`robotel.out`
```
0 
```

## Explanation

There are no blocking pairs on the board that could stop the robot.

# Example 2

`robotel.in`
```
1
5 3
1 3 S
4 1 E
4 3 V
```

`robotel.out`
```
4 1 4 3 
```

## Explanation

The blocking pair consists of the cells $(4, 1)$ labeled with `E` and $(4, 3)$ labeled with `V`. If the robot reaches one of these cells, it will stop at the other cell.

# Example 3

`robotel.in`
```
1
5 5
1 3 S
2 5 S
4 1 E
4 3 V
5 5 N
```

`robotel.out`
```
2 5 5 5
4 1 4 3
```

## Explanation

The signal cell on row $2$, column $5$ is labeled `S`, and the signal cell on row $5$, column $5$ is labeled `N`. If the robot reaches one of these cells, it will stop at the other cell. The same thing happens for the cell with the letter `E` on row $4$, column $1$ and the cell with the letter `V` on row $4$, column $3$.

# Example 4

`robotel.in`
```
2
5 3
1 3 S
4 1 E
4 3 V
```

`robotel.out`
```
0 2 3 2
```

## Explanation

The number of steps taken in the direction:
North: $0$ steps
East: $2$ steps in cells $(1, 2)$, $(1, 3)$
South: $3$ steps in cells $(2, 3)$, $(3, 3)$, $(4, 3)$
West: $2$ steps in cells $(4, 2)$, $(4, 1)$

# Example 5

`robotel.in`
```
2
5 4
1 3 S
3 1 E
5 1 N
5 3 V
```

`robotel.out`
```
2 6 4 2
```

## Explanation

The number of steps taken in the direction:
North: $2$ steps in cells $(4, 1)$, $(3, 1)$
East: $6$ steps in cells $(1, 2)$, $(1, 3)$, $(3, 2)$, $(3, 3)$, $(3, 4)$, $(3, 5)$
South: $4$ steps in cells $(2, 3)$, $(3, 3)$, $(4, 3)$, $(5, 3)$
West: $2$ steps in cells $(5, 2)$, $(5, 1)$
```
