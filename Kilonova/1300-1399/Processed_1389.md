Matei has invented a new game with balls. The playing field is a vertical rectangular grid. The grid is divided into $m \times n$ cells, arranged in $m$ rows and $n$ columns. Some of the cells contain obstacles. From the top, from the cells located on the first row, balls are dropped. The balls fall vertically until they hit an obstacle or until they reach the lowest cell in the column they are in. The first ball that hits an obstacle moves horizontally to the adjacent column on the left, then continues to fall. Each of the other balls that hits the same obstacle moves horizontally, to the adjacent column, but in the opposite direction to the ball that hit this obstacle immediately before them, then continues to fall.

# Task

Given the number of balls that are dropped from each cell on the first row and the positions of the obstacles, determine the number of balls that reach each cell on the last row. The positions of the obstacles are indicated by their row and column (the top left corner corresponds to row $1$ and column $1$).

# Input data

The input file `bile.in` contains on the first line, separated by a space, the natural numbers $m$, $n$, and $p$ (number of rows, number of columns, and number of obstacles). The next $p$ lines contain two numbers, separated by a space, representing the positions of the $p$ obstacles. The last $n$ lines contain a natural number each, representing the number of balls launched from each cell on the first row (starting with the first cell on the row).

# Output data

The output file `bile.out` will contain $n$ lines with one number each, representing the number of balls in each cell on the last row (starting with the first cell on this row).

# Constraints and clarifications

* $2 \leq m, n \leq 2 \ 000$
* $0 \leq p \leq 10 \ 000$
* A maximum of $1 \ 000$ balls are launched from each cell;
* There are no obstacles on the first and last row, or the first and last column;
* There are no two adjacent obstacles on a row, column, or diagonal;

# Example

`bile.in`
```
6 7 5
2 3
2 5
4 2
4 4
5 6
4
6
4
5
8
3
5
```

`bile.out`
```
8
0
10
0
9
0
8
```

## Explanation

~[bile.png|align=center]