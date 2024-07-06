```markdown
Given two trees $G$ and $H$. Tree $G$ has nodes $G_1, \dots , G_N$, and tree $H$ has nodes $H_1, \dots , H_N$. For any $u$ and $v$, it is guaranteed that there is an edge between $G_u$ and $G_v$ if and only if there is an edge between $H_u$ and $H_v$. All edges in trees $G$ and $H$ _have a length of_ $1$.

The leaves of a tree can be connected with their counterparts in the other tree by an edge _of length_ $0$. In other words, for any $v$, the leaf $G_v$ can be connected by an edge with the leaf $H_v$. If the leaf $G_v$ is connected with the leaf $H_v$, then that leaf is considered **active**, otherwise it is **inactive**.

Initially, all leaves are inactive. We have two types of operations:

* `1 v` — toggle the state of the leaves $G_v$ and $H_v$: they become active from inactive and vice versa;
* `2 u v` — determine the length of the shortest path from node $G_u$ to node $H_v$.

# Input data

The first line of the input file contains two integers $N$ and $Q$ — the number of nodes and the number of operations. Each of the next $N - 1$ lines contain two integers $u, v \ (1 \leq u, v \leq N)$ — the structure of the trees — edges $(G_u, G_v)$ and $(H_u, H_v)$.

Each of the next $q$ lines describe the operations. Each operation is either of the form `1 v` $(1 \leq v \leq N)$, or of the form `2 u v` $(1 \leq u, v \leq N)$.

# Output data

For each operation of type $2$, in the order of input, print an integer on a line — the length of the shortest path between the two given nodes. If such a path does not exist, display $\-1$.

# Constraints and clarifications

* $1 \leq N, Q \leq 200\ 000$
* Let $K$ be the total number of type $2$ operations.

| # | Points | Constraints          |
| - | ------- | ------------------- |
| 1 | 3      | $1 \leq N, Q \leq 16$ |
| 2 | 3      | $1 \leq N \leq 16, 1 \leq Q \leq 200\ 000$      |
| 3 | 2      | $1 \leq N \leq 16, 1 \leq Q \leq 200\ 000$ and $K \leq 5$     |
| 4 | 8      | $1 \leq N, Q \leq 2 \ 000$     |
| 5 | 9      | $1 \leq N, Q \leq 200\ 000$ and $K \leq 5$     |
| 6 | 30      | $1 \leq N, Q \leq 200\ 000$ and all type $1$ operations appear before all type $2$ operations     |
| 7 | 45     | Without additional constraints.      |

# Example 1

`stdin`
```
7 11
1 2
2 3
1 4
2 5
4 6
4 7
1 6
1 3
2 1 6
2 1 2
1 7
2 5 4
2 6 3
1 6
1 3
1 5
2 6 3
```

`stdout`
```
2
3
5
4
6
```

## Explanation

Trees $G$ and $H$ have the following structure.

~[arb1.png]

For the first query, the tree structure is as follows. A possible path is drawn in red. The dotted edges have length $0$.

~[arb2.png]

The second query is shown below.

~[arb3.png]

The third query is shown below.

~[arb4.png]

The fourth query is shown below.

~[arb5.png]

The last query is shown below.

~[arb6.png]

# Example 2

`stdin`
```
2 2
1 2
1 1
2 1 2
```

`stdout`
```
1
```
```