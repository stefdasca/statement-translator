In the land of Nowhere, there exist $N$ nests. The nests are represented on a plane either as circles or as rectangles with sides parallel to the axes. For two nests $A$ and $B$, we say that $A$ is nested within $B$ if every point inside or on the boundary of nest $A$ is inside or on the boundary of nest $B$. We call a nesting a subset of nests $A_1, A_2, A_3, \dots, A_k$, in which $A_i$ is nested in $A_{i+1}$ for each $1 \leq i < k$.

# Task

For the given $N$ nests, write a program that finds the maximum cardinality of a nesting. The cardinality of a nesting is equal to the number of nests that make up the nesting.

# Input data

The input file `cuiburi.in` contains on the first line the natural number $N$, representing the number of nests. On the next $N$ lines, the $N$ nests will be described as follows: the first number $t$ on each line will be $0$ or $1$. If $t$ is $0$, then the line will also contain $4$ natural numbers $l_x$, $l_y$, $r_x$, $r_y$, separated by spaces. The pair $(l_x, l_y)$ represents the bottom-left corner of the rectangle, while the pair $(r_x, r_y)$ represents the top-right corner of the rectangle. If $t$ is $1$, then the line will contain $3$ more natural numbers $x$, $y$, $r$, where $(x, y)$ is the center of the circle and $r$ is the radius of the circle.

# Output data

The output file `cuiburi.out` will contain a single natural number representing the maximum cardinality of a nesting.

# Constraints and clarifications

* Nests can intersect.
* $1 \leq N \leq 2 \ 000$
* $l_x \leq r_x$
* $l_y \leq r_y$
* For $20\%$ of tests, $N \leq 20$
* For $30\%$ of tests, all nests will be rectangles
* For $30\%$ of tests, all nests will be circles
* The coordinates and radii are natural numbers less than or equal to $30 \ 000$

# Example

`cuiburi.in`
```
8
0 1 1 5 5
0 6 1 8 2
1 9 9 2
0 3 1 5 3
0 2 2 4 4
1 3 3 1
0 2 2 4 4
0 9 9 11 15
```

`cuiburi.out`
```
4
```

## Explanation

The nesting with maximum cardinality consists of nests with indices $6$, $5$, $7$, $1$.