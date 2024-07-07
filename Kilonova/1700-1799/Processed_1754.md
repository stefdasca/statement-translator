
# Task

On the real axis, there are $N$ cities, numbered with the numbers $1, 2, 3, \dots, N$. Although in a one-dimensional world things seem to be much simpler, most of the inhabitants are dissatisfied with the long distances traveled between cities to resolve various issues. Thus, for better organization, it was put to a vote and it was decided to promote at most $K$ cities to the rank of administrative center. The centers must be placed in a smart way, so that the maximum distance calculated from each city to the nearest administrative center is as small as possible. Since the administrative costs of such a center are high, a number of administrative centers should be placed in such a way that the maximum distance does not change.

# Input data

In the file `orase.in`, the first line contains the numbers $N$ and $K$ separated by spaces. On the next line contains $N - 1$ non-zero natural numbers, separated by spaces, the $i$-th number representing the distance between cities $i$ and $i + 1$.

# Output data

The file `orase.out` must contain on a single line, separated by spaces, two natural numbers, representing the maximum distance corresponding to an optimal placement of the centers, respectively the number of cities that need to be promoted.

# Constraints and clarifications

* $2 \leq N \leq 1 \ 000 \ 000$
* $1 \leq K \leq \min(N, 1 \ 000)$
* the sum of the $N - 1$ distances does not exceed $2 \ 000 \ 000 \ 000$
* $30\%$ of tests will have $N \leq 1 \ 000$

# Example

`orase.in`
```
7 3
3 1 4 14 4 3
```

`orase.out`
```
4 2
```

## Explanation

One possibility for optimal placement of the centers can be in cities $3$ and $6$.
