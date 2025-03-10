
# Task

We are given a tree with $N$ nodes. We denote $dist(x, y)$ as the length of the shortest path between nodes $x$ and $y$.

You are given $Q$ queries of the type $(D_1, D_2, D_3)$. For each query, you must find $4$ nodes $a, b, c, d$ that satisfy the conditions $dist(a, b) = D_1$, $dist(a, c) = D_2$, $dist(a, d) = D_3$, and the paths $a-b$, $a-c$, $a-d$ do not intersect (have no common edge).

# Input data

The first line contains 2 integers, $N \leq 10^5$ and $Q \leq 2 \times 10^5$.
Each of the next $N-1$ lines contains $2$ integers $U_i$ and $V_i$, representing an edge between $U_i$ and $V_i$.
Each of the next $Q$ lines will contain $3$ natural non-zero numbers, representing a query.

# Output data

There will be $Q$ lines. On the $i$-th line, you will print the answer to the $i$-th query. If there exist $4$ nodes that satisfy the query's conditions, you will print `YES` followed by $4$ integers representing these $4$ nodes. If not, you will print only `NO`.

# Constraints and clarifications

|#| Score | Constraints                                      | 
|-|-------|--------------------------------------------------|
|0|   0   | Examples                                         |
|1|  10   | $N, Q \le 10$                                    |
|2|  30   | $N, Q \le 3\ 000$                                 |
|3|  60   | without additional constraints                    |

# Example

`stdin`
```
7 3
7 1
7 4
4 3
6 1
5 6
6 2
3 1 1
1 1 1
2 1 1
```

`stdout`
```
YES 6 4 5 2
YES 6 1 5 2
YES 6 7 5 2
```
