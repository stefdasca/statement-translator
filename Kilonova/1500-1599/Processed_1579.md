A rectangular ornamental wall is made up of $N$ rows of bricks, each row having $M$ identical bricks, placed side by side. Each brick is colored in one of the colors $\\{0, 1, 2, . . . , C_{max}\\}$.

A _square_ with side $L$ on this wall is constituted by the bricks situated on $L$ consecutive rows and $L$ consecutive columns.

We say that a square is _uniformly colored_ if it contains the same number of bricks from each color that appears in that square.

# Task

Write a program that, given the configuration of the wall, determines in this wall a square of maximum side length, uniformly colored.

# Input data

The input file `zid.in` contains on the first line the natural numbers $N\\ M\\ C_{max}$, representing the number of rows of bricks, the number of bricks in each row, and the maximum color, respectively.

The next $N$ lines describe the configuration of the wall from top to bottom; on each of the $N$ lines, there are $M$ natural numbers representing the colors of the bricks on that row, in order, from left to right. The values on the same line are separated by a space.

# Output data

The output file `zid.out` will contain a single line on which $3$ natural numbers $Nr\\ R\\ C$ will be written, separated by a single space, representing the number of bricks existing in a uniformly colored square of maximum side length, and the row and the brick on the row situated in the top-left corner of the uniformly colored square of maximum side length.

# Constraints and clarifications

* $2 \\leq N, M \\leq 250$
* $1 \\leq C_{max} \\leq 9$
* The rows are numbered from top to bottom from $1$ to $N$. The bricks on a row are numbered from left to right from $1$ to $M$.
* If there are multiple uniformly colored squares of maximum side length, the square for which the row number is minimal will be chosen. If there are multiple uniformly colored squares of maximum side length that have the top-left corner on the same minimal row, the leftmost square will be chosen.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 22      | $2 \\leq N, M \\leq 30$ |
| 2 | 23      | $30 < N, M \\leq 100$      |
| 3 | 10      | Bricks are only painted in two colors: $Cmax = 1$      |
| 4 | 45      | $100 < N, M \\leq 250$     |

# Example

`zid.in`
```
6 8 5
1 2 3 5 1 2 3 5
1 2 1 2 3 5 3 5
1 1 1 2 2 3 3 3
1 2 3 5 5 3 2 1
3 3 1 1 2 2 5 5
2 1 2 3 2 5 2 2
```

`zid.out`
```
9 2 4
```

## Explanation

The uniformly colored square of maximum side length, situated on the highest row, the most to the left is:

$ \\ 2 \\ 3 \\ 5$  
$ \\ 2 \\ 2 \\ 3$  
$ \\ 5 \\ 5 \\ 3$  

It contains $9$ bricks, in which the colors $2, 3, 5$ appear $3$ times each. This square has the top-left corner situated on the second row, in the fourth brick of the row (the fourth column).

There are also other uniformly colored squares formed by $9$ bricks, for example:

$ \\ 1 \\ 2 \\ 3$  
$ \\ 3 \\ 3 \\ 1$  
$ \\ 2 \\ 1 \\ 2$  

but this has the top-left corner on row $4$.