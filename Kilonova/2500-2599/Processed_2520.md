
# Task

You are given a map of size $N \times N$ which contains free spaces (denoted by `.`) and occupied spaces (denoted by `#`). Answer $Q$ queries of the form $i_1\\ j_1\\ i_2\\ j_2$, where you need to find the minimum distance from cell $(i_1, j_1)$ to cell $(i_2, j_2)$.

# Input data

```
N
A[0][0] A[0][1] ... A[0][N-1]
A[1][0] A[1][1] ... A[1][N-1]
...
A[N-1][0] A[N-1][1] ... A[N-1][N-1]
(N lines and N columns, '.' or '#', without spaces)
Q
i1[0] j1[0] i2[0] j2[0]
i1[1] j1[1] i2[1] j2[1]
...
i1[Q-1] j1[Q-1] i2[Q-1] j2[Q-1]
```

# Output data

```
ans[0]
ans[1]
...
ans[Q-1]
```

# Constraints and clarifications
* It is recommended to use [fastio](https://www.geeksforgeeks.org/fast-io-for-competitive-programming/).
* $1 \le N \le 690$
* $1 \le Q \le 100\ 000$
* $0 \le i_1, j_1, i_2, j_2 < N$
* If there is no solution, the output will be `-1`.
* At most $1\%$ (rounded up) of all cells are occupied (except for the example).
* The tests are randomly generated.

# Example

`stdin`
```
5
#...#
#....
#.#..
..#..
..#..
5
3 0 3 3
2 1 2 3
0 4 2 4
3 4 2 1
0 1 2 3
```

`stdout`
```
7
4
-1
6
4
```

## Explanation

For the first query, the distance from cell $(3, 0)$ to cell $(3, 3)$ is $7$. A possible path is the following: $(3, 0)$, $(3, 1)$, $(2, 1)$, $(1, 1)$, $(1, 2)$, $(1, 3)$, $(2, 3)$, $(3, 3)$.

```
#...#
#***.
#*#*.
1*#2.
..#..
```

```
