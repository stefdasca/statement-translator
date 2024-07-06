Ionică has a game whose board contains $N \times M$ towers of distinct heights, arranged in $N$ rows and $M$ columns. The game also includes a ball that Ionică can place on any tower on the board. From any position it is in, the ball will fall onto the neighboring tower of the smallest height, only if its height is strictly smaller than the tower on which the ball is currently placed. Two towers are neighbors if they are on the same row in adjacent columns or in the same column in adjacent rows. The ball will roll until it reaches a tower that has no neighboring tower with a strictly smaller height. The board is surrounded by a border higher than any tower on it.

# Task

Create a program that displays the maximum number of towers the ball can roll over, as well as the smallest height of a tower on which the ball must initially be placed so that it rolls over the maximum number of towers.

# Input data

The input file `bila.in` contains on the first line the natural numbers $N$ and $M$. Each of the next $N$ lines contains $M$ natural numbers representing the heights of the towers on each row of the board. The values written on the same line are separated by spaces.

# Output data

The output file `bila.out` will contain on the first line, separated by a space, two natural numbers $\\text{MAX}$, $\\text{HMIN}$ representing, in order, the maximum number of towers the ball can roll over (including the starting tower) and, respectively, the smallest height of a tower on which the ball can initially be placed so that it rolls over MAX towers.

# Constraints and clarifications

* $1 < N \leq 125$
* $1 < M \leq 125$
* The heights of the towers on the board are distinct pairwise.
* $1 \leq$ Heights of the towers $\leq 65\ 000$
* For each test, $70\\%$ of the score is awarded if the value of $\\text{MAX}$, representing the maximum number of towers the ball can roll over, is correctly determined.

# Example

`bila.in`
```
5 5
109 120 4 5 7
107 212 1 100 8
106 105 103 101 12
6 10 104 102 9
3 2 19 20 21
```

`bila.out`
```
7 101
```

## Explanation

The ball will roll in order over the towers of heights $101$, $12$, $8$, $7$, $5$, $4$, $1$