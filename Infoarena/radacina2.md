## Task

Given $N$ trees, initially each tree contains exactly one node (and no edges): tree $i$ consists of node $i$. We define an operation $UNITE(i, j)$ on the given nodes as follows: the operation is valid only if nodes $i$ and $j$ are the roots of their respective trees; if the tree with root in node $i$ has fewer nodes than the tree with root in $j$, then $j$ becomes the parent of node $i$ (the two trees are united by a directed edge from node $j$ to node $i$); if the tree with root in node $i$ has more nodes than the tree with root in $j$, then $i$ becomes the parent of node $j$ (the two trees are united by a directed edge from node $i$ to node $j$); if the tree with root in node $i$ has the same number of nodes as the tree with root in node $j$, then the node with the larger index becomes the parent of the node with the smaller index (the trees are united by a directed edge, as described above). After performing $N-1$ $UNITE$ operations, a single tree remains. Determine in how many ways (modulo a given natural number $P$) the $UNITE$ operations can be performed so that the remaining tree has its root at node $X$, where $X$ is a given number.

## Input data

The input file `radacina2.in` contains on the first line three natural numbers: $N$ $X$ $P$, separated by spaces, as described above.

## Output data

The output file `radacina2.out` contains on the first line a single natural number, representing the number of ways, modulo $P$, in which the $UNITE$ operations can be performed on the initial $N$ trees (each consisting of only one node), so that after $N-1$ operations, a single tree remains with its root at node $X$.

## Constraints

1 \leq $N$ \leq 70

1 \leq $X$ \leq $N$

1 \leq $P$ \leq 1000000000

Two $UNITE$ operations $(x_1, y_1)$ and $UNITE$(x_2, y_2)$ are considered different if $\{ x_1, y_1 \} \neq \{ x_2, y_2 \}$ (the two sets are different, in other words, there exists a node in one operation that is not in the other). The operation $UNITE (x, y)$ is considered identical to the operation $UNITE (y, x)$.

Two ways of performing the operations are considered different if there exists an index $i$ (1 \leq $i$ \leq $N-1$) such that the $UNITE$ operations performed at step $i$ in the two ways are different.

## Example

`radacina2.in`
```
4 2 666013
```

`radacina2.out`
```
2
```

## Explanation

The two ways of performing the operations are:
1. $UNITE(1, 2)$, $UNITE(2, 3)$, $UNITE(2, 4)$
2. $UNITE(1, 2)$, $UNITE(2, 4)$, $UNITE(2, 3)$