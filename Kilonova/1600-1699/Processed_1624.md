```markdown
It is considered a matrix with $N$ rows and $N$ columns that stores only digits. The rows and columns are numbered from $1$ to $N$. Also considered is an array $v$ of length $10$, where $v_i =$ cost of digit $i$ ($i = 0 \dots 9$). We need to determine a path from column $1$ to column $N$, starting from a component located on column $1$ to a component on column $N$, and each step is made from a position $(i, j)$ to one of the neighboring positions on the row or column, namely $(i+1, j)$, $(i-1, j)$, $(i, j+1)$, $(i, j-1)$, provided it does not go out of the matrix. The cost of such a path is the sum of the costs of the components through which the path passes.

# Task

Determine the minimum number of distinct digits through which a path from column $1$ to column $N$ passes. If there are several such paths, then the minimum cost of such a path will be determined.

# Input data

The input file `road.in` contains on the first line the value $N$. The second line contains exactly $10$ natural numbers $v_0$, $v_1$, $ \dots$, $v_9$ separated by a space. On the next $N$ lines are $N$ digits each, without spaces between them.

# Output data

The output file `road.out` will contain on the first line a natural number $K$ representing the minimum number of distinct digits through which a path from column $1$ to column $N$ passes. The second line contains a single natural number representing the minimum cost of a path that passes through $K$ distinct digits.

# Constraints and clarifications

* $2 \leq N \leq 100$
* $1 \leq v_i \leq 100$, $i = 0 \dots 9$

# Example

`road.in`
```
6
8 1 2 1 9 14 8 8 6 9
287566
123444
983070
071311
548739
353665
```

`road.out`
```
3
9
```

## Explanation

The path is marked with a gray background in the matrix below and uses only three distinct digits ($1$, $2$, and $3$), and the cost of the path is $9$.

~[drum.png]

It should be noted that there is another path that uses only three distinct digits (consisting of all elements on the last row), but it has a higher cost.
```