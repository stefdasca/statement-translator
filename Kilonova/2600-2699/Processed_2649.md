~[fig1.png|align=right]

Given a tree with $N$ nodes, numbered from $1$ to $N$. Each edge in the tree has a non-zero natural number cost associated with it. An operation consists of choosing an edge with a **strictly** positive cost and decreasing its cost by $1$.

For a node $v$ in the tree and a natural number $k$, let $f(v, k)$ denote the minimum sum of the costs of the paths from node $v$ to the rest of the nodes in the tree that can be obtained by optimally applying **at most** $k$ operations of the type described above.

# Task

You are given $Q$ queries of the form $(v, k_1, k_2)$, where $v$ is a node in the tree, and $k_1$ and $k_2$ are natural numbers such that $k_1 \\leq k_2$. For each query, calculate $\\displaystyle \\sum_{k=k_1}^{k_2} f(v, k)$, which is the sum of the values $f(v, k)$ for $k_1 \\leq k \\leq k_2$, modulo $10^9 + 7$.

# Input data

The first line of the input file `arbore.in` contains the number $N$, representing the number of nodes in the tree.

The following $N - 1$ lines contain 3 numbers $u \\ v \\ w$, representing an edge in the tree between nodes $u$ and $v$, which has a cost $w$.

The next line contains a single number $Q$, representing the number of queries, and the following $Q$ lines each contain three numbers $v \\ k_1 \\ k_2$, with the meaning described in the statement.

# Output data

The output file `arbore.out` must contain $Q$ lines, each containing a natural number which represents the answer to each given query, in the order in which they are given in the input file.

# Constraints and clarifications

* $1 \\leq N \\leq 200\\ 000$
* $1 \\leq Q \\leq 400\\ 000$
* $1 \\leq w \\leq 10^8$
* $0 \\leq k_1 \\leq k_2 \\leq 10^{14}$

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 12      | $N \\leq 2\\ 000, Q \\leq 2\\ 000, k_1 = k_2 = 0$ |
| 2 | 7      | $N \\leq 200\\ 000, Q \\leq 400\\ 000, k_1 = k_2 = 0$      |
| 3 | 13      | $N \\leq 2\\ 000, Q \\leq 2\\ 000, k_1 = k_2$      |
| 4 | 16      | $N \\leq 5\\ 000, Q \\leq 200\\ 000, k_1 = k_2$      |
| 5 | 19      | $N \\leq 100\\ 000, Q \\leq 100\\ 000, k_1 = k_2$      |
| 6 | 14      | $N \\leq 200\\ 000, Q \\leq 400\\ 000, k_1 = k_2$     |
| 7 | 11      | $N \\leq 100\\ 000, Q \\leq 100\\ 000$      |
| 8 | 8      | Without additional constraints.      |

# Examples

`arbore.in`
```
5
1 2 3
2 3 4
2 5 6
1 4 2
4
1 4 5
2 1 1
5 20 22
4 0 0
```

`arbore.out`
```
21
16
0
27
```

## Explanation

The tree has $N = 5$ nodes and is illustrated in _Figure 1_ along with the costs associated with its edges. $Q = 4$ queries are given, as follows.

* First query: For $k = 4$, the operation described in the statement can be applied to the edge $1−2$ three times, and to the edge $1−4$ once, so $f(1, 4) = 11$. For $k = 5$, the operation can be applied to the edge $1−2$ three times, to the edge $2−3$ once, and to the edge $2−5$ once, so $f(1, 5) = 10$. Thus, the answer is $f(1, 4) + f(1, 5) = 11 + 10 = 21$.
* Second query: The cost of the edge $1−2$ can be decreased once, so the answer is $f(1, 1) = 16$.
* Third query: It can be observed that for any $20 \\leq k \\leq 22$, the costs of all edges in the tree can be decreased until they reach the value $0$ (beyond this it is not allowed per the definition of the given operation), so the result is $0$.
* Fourth query: $k_1 = k_2 = 0$, so we have no operations available to decrease the cost of the edges. Thus, the answer is given by the sum of the costs of the paths from node $4$ to the rest of the nodes in the tree, which is $2 + 5 + 9 + 11 = 27$.