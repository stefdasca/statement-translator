# Task

Given $N$ points in a $K$-dimensional space, represented by $K$-tuples of integers ($P_{i,1}, P_{i,2}, ..., P_{i,k}$).

# Task

Determine the sum of the squares of the Euclidean distances between all unordered pairs of points, modulo ${2}^{32}$.

# Input data

The first line contains the numbers $N$ and $K$, as described in the problem statement.
Each of the next $N$ lines contains a $K$-tuple of integers, representing the coordinates of point $i$ in the $K$-dimensional space.

# Output data

The first line contains a single integer, the sum of the squares of the Euclidean distances between all unordered pairs of points, modulo ${2}^{32}$.

# Constraints and clarifications

* $1 \leq N \leq 100 \ 000$
* $1 \leq K \leq 100 \ 000$
* $1 \leq NK \leq 200 \ 000$
* $-1 \ 000 \ 000 \ 000 \leq P_{i,j} \leq 1 \ 000 \ 000 \ 000$
* For tests worth $30$ points, ${N}^{2} \cdot K \leq 100 \ 000 \ 000$
* It is recommended to use fastio

# Example 1

`stdin`
```
3 2
0 0
0 1
1 1
```

`stdout`
```
4
```

## Explanation

There are $K = 2$ dimensions.
$D(A, B) + D(A, C) + D(B, C) = 1 + 2 + 1 = 4$.
~[plan.png]