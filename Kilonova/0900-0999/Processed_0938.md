A labyrinth is described as a binary matrix with $N$ rows and $M$ columns, where $0$ represents a free position, and $1$ represents a position with a wall. A path in the labyrinth is a route in the matrix that starts at position $(1, 1)$ and reaches position $(N, M)$ by moving only to positions that have the value 0 and are adjacent to the current position, in one of the four directions: up, down, left, right. The length of a path is equal to the number of visited positions.

We denote by $d_0$ the minimum path length from position $(1, 1)$ to position $(N, M)$. Let $d(i, j)$ be the minimum path length from position $(1, 1)$ to position $(N, M)$ if the position $(i, j)$ is assigned the value $0$. We note that if the position $(i, j)$ initially contains a $0$, then $d_0 = d(i, j)$.

# Task

For each position $(i, j)$, check if $d(i, j) < d_0$.

# Input data

The first line of the file `labirint.in` contains two natural numbers $N$ and $M$, the dimensions of the binary matrix describing the labyrinth. Then, on the following $N$ lines, there will be $M$ binary values, which represent the elements of the matrix describing the labyrinth, not separated by spaces.

# Output data

In the file `labirint.out`, $N$ lines will be written, and on each line, $M$ digits will be written, not separated by spaces. The $j$-th digit on the $i$-th line is $1$ if and only if $d(i, j) < d_0$, otherwise it is $0$.

# Constraints and clarifications

* $1 \leq N, M \leq 1 \ 000$;
* The positions $(1, 1)$ and $(N, M)$ will contain the values $0$.
* It is guaranteed that there is a path in the initial matrix between positions $(1, 1)$ and $(N, M)$.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 10      | $1 \leq N, M \leq 50$, $d_0 = N + M - 1$ |
| 2 | 30      | $1 \leq N, M \leq 50$      |
| 3 | 60      | No additional constraints.      |

# Example

`labirint.in`
```
5 6
010001
000101
011001
010010
001000
```

`labirint.out`
```
010000
000100
001001
010010
001000
```

## Explanation

There are $7$ positions with the value $1$ in the labyrinth which, if replaced with $0$, determine obtaining a path that is shorter than $d_0 = 14$.

For example, if we replace the value in $(1, 2)$ with $0$, we would obtain a path of length $d(1, 2) = 12$.