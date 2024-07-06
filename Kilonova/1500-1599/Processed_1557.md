~[tuburi.jpg|align=right]

On a wall, $n \times m$ pieces were mounted in $n$ rows (numbered from top to bottom, from $1$ to $n$) and $m$ columns (numbered from left to right, from $1$ to $m$). The pieces are tubes or joints of types $1$, $2$, $\dots$, $6$, as shown in the adjacent image.

Ionel can insert a ball into a piece located in row $1$ only if the piece is of type $2$, $4$ or $6$. The ball can descend one level or move horizontally to an adjacent piece if the connection between the pieces allows it, but it cannot ascend due to gravity. The ball cannot pass through the same piece twice and gets stuck when it can no longer move to another piece.

# Task

Two natural numbers $n$, $m$ are read, followed by $n \times m$ numbers from the set $\{1, 2, 3, 4, 5, 6\}$ representing the arrangement of the pieces on the wall. Write a program to solve the following tasks:
1. Determine the maximum number of pieces the ball can pass through until it gets stuck if introduced into one of the pieces in row $1$, having type $2$, $4$ or $6$;
2. For a given row $k$, determine the numbers $c$ and $t$, where $c$ is the minimum column such that by replacing the existing piece in row $k$ and column $c$ with a piece of type $t$, the maximum possible number of pieces the ball can pass through until stuck is obtained. If there are multiple solutions for replacing the piece in row $k$ and column $c$, choose the variant with the minimum $t$.

# Input data

The input file `tuburi.in` contains on the first line a natural number $C$ representing the task that needs to be solved ($1$ or $2$), the second line contains the natural numbers $n$, $m$, representing the dimensions of the wall. On each of the next $n$ lines, there are $m$ numbers belonging to the set $\{1, 2, 3, 4, 5, 6\}$ representing the types of pieces on the wall in order.

If the task is $C=2$, the input file contains additionally, on the $(n+3)$-rd line, a natural number $k$ representing the number of a row of pieces. The values written on the same line are separated by a space.

# Output data

The output file `tuburi.out` will contain a single line:
- If $C=1$, then the first line of the file will contain a natural number representing the result of task $1$.
- If $C=2$, then the first line of the file will contain two natural numbers $c$ and $t$, separated by a space, with the significance from the statement.

# Constraints and clarifications

* $2 \leq n, m \leq 500$;
* For tests worth $40$ points, the task is $1$.

# Example 1

`tuburi.in`
```
1
5 6
2 2 1 6 4 3
1 6 2 5 1 6
2 5 2 5 2 2
2 3 4 3 4 3
2 1 5 6 5 6
```

`tuburi.out`
```
9
```

## Explanation

~[tuburi_ex.jpg|align=right]

The input data corresponds to the adjacent image. The path corresponding to the maximum number of pieces is: $(1,4)$, $(1,3)$, $(2,3)$, $(3,3)$, $(4,3)$, $(4,4)$, $(5,4)$, $(5,3)$, $(5,2)$.

# Example 2

`tuburi.in`
```
2
5 6
2 2 1 6 4 3
1 6 2 5 1 6
2 5 2 5 2 2
2 3 4 3 4 3
2 1 5 6 5 6
5
```

`tuburi.out`
```
4 5
```

## Explanation

By replacing the piece in row $5$, column $4$ with a piece of type $5$, the maximum number of pieces the ball can pass through will be $12$.