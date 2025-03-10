
# Task

You are given $n$, $q$, an array of $n$ elements $a_1$, $a_2$, ..., $a_n$, and $q$ queries of the following types:

* `1 pos x`: Change the element $a_{pos}$ to $x$.
* `2 l r`: Display 3 indices $i$, $j$, $k$ such that $a_i = a_j \cdot a_k$, where $l \leq i, j, k \leq r$ and $i, j, k$ are pairwise distinct. If there are no such 3 indices, display `0 0 0`.

# Input data

The first line contains two integers, $n$ and $q$. The next line contains the array $a$ of $n$ natural numbers. The following $q$ lines will contain the $q$ queries.

# Output data

The following lines contain the answer for each query of type 2.

# Constraints and clarifications

* $1 \leq n, q \leq 2 \cdot 10^5$
* $1 \leq a_i, x \leq 50$

| # | Score | Constraints                                              |
|---|-------|----------------------------------------------------------|
| 1 | 13    | $1 \leq n, q \leq 50$                                     |
| 2 | 18    | $1 \leq n, q \leq 500$                                    |
| 3 | 22    | $1 \leq n, q \leq 5\, 000$                                |
| 4 | 47    | No additional constraints                                  |

# Example

`stdin`
```
4 4
1 2 2 1
2 1 3
1 1 2
2 1 3
2 1 4
```

`stdout`
```
2 1 3
0 0 0
2 4 3
```

## Explanation

In the interval $[1, 3]$, if $i=2$, $j=1$ and $k=3$, it results in $2=2 \cdot 1$, which is true, so we can display `2 1 3`. Notice that this is not the only solution.

The element at position $1$ is changed to $2$.

In the interval $[1, 3]$, there are no 3 indices $i, j, k$ such that $a_i = a_j \cdot a_k$, so we display `0 0 0`.
