## Task

The map of Erathia is given in the form of a grid with $M$ rows and $N$ columns. The terrain is divided into cells that can be accessible (value is 0) or inaccessible (value is different from 0). Sir Christian wants to reach from the cell with coordinates $(x_1, y_1)$ where the last battle took place to the cell $(x_2, y_2)$ where the capital of his kingdom is located. For this, he has $K$ moves available. A move consists of moving from the current cell to a neighboring cell (horizontally or vertically, but not diagonally). You will need to determine the number of paths Sir Christian can take. A path can contain at most $K$ moves, and Sir Christian can pass multiple times through the same cell, including the cells $(x_1, y_1)$ and $(x_2, y_2)$.

## Input data

The input file `homm.in` contains on the first line three natural numbers $M$, $N$, and $K$, representing the number of rows and columns of the grid, respectively, and the number of moves Sir Christian has available; these numbers are separated by a space. The next $M$ lines contain $N$ integers each, separated by a space, representing the elements of the grid. The last line contains four integers, representing the values $x_1$, $y_1$, $x_2$, and $y_2$.

## Output data

The output file `homm.out` will contain a single number representing the total number of possible paths.

## Constraints

$1 \leq M, N \leq 100$

$1 \leq K \leq 20$

The total number of paths is always less than $1\,000\,000\,000$

All coordinates are given in the order row $(x)$, column $(y)$.

## Examples

`homm.in`
```
5 5 10
0 0 0 0 0
0 2 0 3 0
0 0 1 0 0
0 0 2 0 0
0 0 0 0 0
1 1 5 5
```
`homm.out`
34

`homm.in`
```
5 5 10
0 0 4 0 0
0 2 0 3 0
4 0 1 0 0
0 2 0 0 0
0 0 0 0 0
1 1 5 5
```
`homm.out`
0