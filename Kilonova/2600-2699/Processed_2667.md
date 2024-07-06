> Iaroslav-Menelaos Trapanache, also known as the Thunderbolt of the Lower Danube, or (by his close ones) the Pharaoh, wants to become wiser and is keen to solve a programming problem involving trees that are as equidistant and correct as he purports to be, so he composed the following problem.

**Equidistant Tree.** A rooted tree $A$ is called *equidistant* if all its leaves are at the same distance from the root. (Recall that the distance between two nodes is given by the number of edges in the unique elementary path between the two nodes.)

For example, the following rooted tree at node $1$ is equidistant:
~[graf1.png|width=20em]

, whereas the following tree (also rooted at node $1$) is *not* equidistant:
~[graf2.png|width=14em]

, because the distances from node $1$ to nodes $4$, $5$, $6$ are not all equal.

**Value of a tree.** Consider a tree $A$ with nodes numbered $1, \ldots, N$, where each node $i = 1, \ldots, N$ has a weight $w(i)$ (which can also be negative). The value of the tree $A$, denoted by $\\text{val}(A)$, is defined as follows. Consider any way of consecutively removing the leaves of the tree $A$ *after which the tree becomes or remains equidistant, keeping the root node.* (We can remove a node that becomes a leaf after other nodes are removed.) Let $x_1, \ldots, x_k$ be the nodes remaining after this removal. The value $\\text{val}(A)$ of $A$ is the maximum sum $w(x_1) + \ldots + w(x_k)$ possible for any way of removing leaves from $A$.

For example, consider the second tree mentioned above (the one with $6$ nodes). ***Some of*** the sets of nodes that can remain after removals are $\\{1, 2, 3, 5, 6\\}$ (we remove node $4$), $\\{1, 2, 3, 4\\}$ (we remove nodes $5$, $6$), $\\{1, 2\\}$ (we remove nodes $4$, $5$, $6$, $3$ in this order), and $\\{1\\}$ (we remove nodes $4$, $5$, $6$, $3$, $2$, in this order). If we assign weights $w(1), \ldots, w(6)$ to this tree, then its value is: $\\max(w(1) + w(2) + w(3) + w(5) + w(6),\\ w(1) + w(2) + w(3) + w(4),\\ w(1) + w(2),\\ w(1))$.

# Task

A tree $A$ with $N$ nodes rooted at node $1$ and weights $w(1), \ldots, w(N)$ is given. Let $A_i$ be the subtree of $A$ rooted at node $i$. Calculate $\\text{val}(A_1), \\ldots, \\text{val}(A_N)$.

# Input data

The first row of the input file `echidistant.in` contains the number $N$ of the tree nodes $A$. The second row contains the numbers $w(1), \ldots, w(N)$ in order, separated by spaces. The third row contains $N - 1$ numbers $t(2), \ldots, t(N)$, representing the fact that the tree edges are $2 - t(2)$, $3 - t(3)$, $\ldots$, $N - t(N)$.

# Output data

The only row of the output file `echidistant.out` contains $N$ numbers, namely $\\text{val}(A_1), \\ldots, \\text{val}(A_N)$ separated by spaces, in this order.

# Constraints and clarifications

* $1 \\leq N \\leq 1 \\ 000 \\ 000$
* $-1\\ 000\\ 000\\ 000 \\leq w(i) \\leq 1 \\ 000 \\ 000 \\ 000$ for $1 \\leq i \\leq N$
* $1 \\leq t(i) \\leq N$ for $1 \\leq i \\leq N$

| # | Score | Constraints                                   |
| - | ------- | -------------------------------------------- |
| 1 |    9    | $t(i) = i - 1$ for $2 \\leq i \\leq N$     |
| 2 |   12    | $1 \\leq N \\leq 100$                          |
| 3 |   21    | $1 \\leq N \\leq 5 \\ 000$                      |
| 4 |   44    | $1 \\leq N \\leq 100 \\ 000$                    |
| 5 |   14    | No additional constraints                |

# Example

`echidistant.in`
```
6
0 -10 10 1 -1 -1
1 2 2 3 3
```

`echidistant.out`
```
1 1 10 1 -1 -1
```

## Explanation

This is the second tree from the statement, the one with $6$ nodes, where we assign weights $[0, -10, 10, 1, -1, -1]$ to nodes $[1, 2, 3, 4, 5, 6]$.