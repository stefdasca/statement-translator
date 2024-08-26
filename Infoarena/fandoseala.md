## Task

Marcel has come across a set of $N$ points with natural coordinates $X_i$ and $Y_i$, with properties that no 2 points are identical, no 3 points are collinear, and no 4 points are concyclic. Unfortunately, Marcel is finicky and very particular, especially when it comes to such a well-chosen set of points. He wants you to find 3 indices $1 \leq a < b < c \leq N$ such that the circle determined by the points $X_a, Y_a; X_b, Y_b; X_c, Y_c$ contains exactly $K$ points among the given ones, either inside or on its boundary.

## Input data

The input file `fandoseala.in` contains the number of tests $T$ on the first line. Each test contains the numbers $N$ and $K$ on the first line, and the next $N$ lines contain pairs of natural numbers $X_i$ and $Y_i$.

## Output data

The output file `fandoseala.out` will contain exactly $T$ lines. On each line, $3$ numbers will be printed, $a, b$ and $c$, a solution for the corresponding test. If $a = b = c = 0$, it will be considered that the test has been omitted.

## Constraints and clarifications

The evaluation will be done using $2$ test files. Both will have $1 \leq N \leq 300$ and the maximum score of $50$ points, with a chance for partial scores. In the first test file, $1 \leq T \leq 1200$, and in the second $1 \leq T \leq 400$.

All coordinates $X_i$ and $Y_i$ are non-zero and less than or equal to $10000$. For each subtest, if there exists any non-zero triplet that does not meet the given conditions, the score of the entire group will be $0$. Otherwise, points will be awarded based on the number of non-zero triplets (hence correct ones), let's denote it $Q$, based on the formula:
Clarification
It is guaranteed that there exists a solution for the test data; $3 \leq K \leq N$

## Example

`fandoseala.in`
```
2
8 4
5 1
5 2
1 3
1000 1000
2 8
9 6
7 3
9 2
3 3
1 1
2 2
1 3
2 6
8
0 0 0
```

`fandoseala.out`
```
2 6 8
0 0 0
```

## Explanation

The circle determined by the points with indices $2, 6, 8$ contains the point with index $7$ inside. 

The score obtained for the example is $25$ points out of a maximum of $50$.