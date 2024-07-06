```
Given a matrix $A$ of natural numbers, consisting of $N$ rows and $M$ columns. The rows are numbered from top to bottom from $0$ to $N - 1$, and the columns from left to right from $0$ to $M - 1$.

We call the _triangle_ of size $K$ starting from cell $(i, j)$ the set of cells that can be reached starting from $(i, j)$ and making at most $K - 1$ steps, moving one cell up or to the right.

# Task

For each cell $(i, j)$ with $K - 1 \leq i < N$ and $0 \leq j < M - K + 1$, we want to find out:

* The maximum value in the triangle of size $K$ starting from cell $(i, j)$;
* How many times the maximum value in the triangle of size $K$ starting from cell $(i, j)$ appears in the respective triangle.

# Input data

The first line contains the numbers $N, M$ and $K$. Each of the next $N$ lines contains $M$ numbers each. The $j$-th number on the $i$-th such line represents $A_{i, j}$.

# Output data

Two matrices of dimensions $(N - K + 1) \times (M - K + 1)$ will be printed.

Each of the first $N - K + 1$ lines will contain $M - K + 1$ natural numbers. The $j$-th number on the $i$-th such line is the maximum value in the triangle of size $K$ starting from cell $(i - K + 1, j)$.

Each of the next $N - K + 1$ lines will contain $M - K + 1$ natural numbers. The $j$-th number on the $i$-th such line is the number of occurrences of the maximum value in the triangle of size $K$ starting from cell $(i - K + 1, j)$ within that triangle.

# Constraints and clarifications

* $1 \leq N, M \leq 3 \ 000$
* $1 \leq K \leq \min(N, M)$
* $0 \leq A_{i, j} \leq 1 \ 000 \ 000$ for $0 \leq i < N$ and $0 \leq j < M$
* Correctly displaying the maximum value in each triangle earns $40\\%$ of the points.
* For faster reading and printing, we recommend using the line: `ios_base::sync_with_stdio(false)`

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 8      | $1 \leq N, M \leq 20$ |
| 2 | 15      | $1 \leq N, M \leq 100$      |
| 3 | 13      | $A_{i, j} \in \{0, 1\}$ for $0 \leq i < N$ and $0 \leq j < M$ |
| 4 | 28      | $1 \leq N, M \leq 1 \ 500$      |
| 5 | 36      | Without additional constraints. |

# Example 1

`stdin`
```
4 4 2
1 2 6 14
12 3 13 5
11 4 7 8
10 16 9 15
```

`stdout`
```
12 13 13
12 7 13
16 16 15
1 1 1
1 1 1
1 1 1
```

## Explanation

For example, the triangle of size $= 2$ starting at $(1, 1)$ is:
$3$
$4 \ 7$
The maximum value is $7$ and it appears a single time.

In fact, the maximum value in each of the $3 \times 3 = 9$ targeted triangles is unique.

# Example 2

`stdin`
```
2 3 2
4 5 3
4 4 5
```

`stdout`
```
4 5
3 2
```

## Explanation

Two triangles of size $2$ are targeted.

The first one starts at $(1, 0)$:
$4$
$4 \ 4$
The maximum value is $4$ and it appears $3$ times.

The second one starts at $(1, 1)$:
$5$
$4 \ 5$
The maximum value is $5$ and it appears $2$ times.
```