
# Task

We are given a tree with $N$ nodes rooted at node $1$ whose edges have lengths expressed by non-zero natural numbers and $Q$ queries of the form $u \ v$. For each query, find the sum of the lengths of all distinct paths from a node in the subtree rooted at node $u$ to a node in the subtree rooted at node $v$ modulo $10^9 + 7$. (the length of a path is equal to the sum of the lengths of all edges that compose it).

# Input data

The first line will contain the numbers $N$ and $Q$ representing the number of nodes in the tree and the number of queries, respectively.

The next $N - 1$ lines contain $2$ numbers $p_i \ w_i$, $i=\overline{2,N}$, representing the parent of node $i$ in the tree and the length of the edge between $p_i$ and $i$ (node $1$ is the root of the tree, so it does not have a parent).

The next $Q$ lines will contain one query each.

# Output data

The program will print on the screen on each line the results of the queries in the order they appear in the input.

# Constraints and clarifications

* $1 \leq N \leq 200\ 000$
* $1 \leq Q \leq 500\ 000$
* $1 \leq w_i \leq 1\ 000\ 000\ 000$
* $1 \leq u, v \leq N$
* for each query of type $2$, the subtrees with roots at nodes $u$ and $v$ will not have common nodes.

# Example

`stdin`
```
14 4
1 4
1 3
2 2
2 7
2 10
3 12
3 5
4 8
4 1
5 3
7 6
7 4
8 9
4 8
2 7
9 11
12 8
```

`stdout`
```
129
595
20
55
```

## Explanation

The tree described in the example looks as follows:
~[img1.jpg|width=45em]

For the first query, the paths are:
- From $4$ to $8$ with length $14$
- From $4$ to $14$ with length $23$
- From $9$ to $8$ with length $22$
- From $9$ to $14$ with length $31$
- From $10$ to $8$ with length $15$
- From $10$ to $14$ with length $24$

Total: $14 + 23 + 22 + 31 + 15 + 24 = 129$
