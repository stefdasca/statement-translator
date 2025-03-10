
~[portocalro.png|align=right]

Portocal, the orange cat, has found a tree (an undirected connected acyclic graph) with $N$ nodes numbered from $1$ to $N$. On each edge $i \ (1 \leq i < N)$ connecting nodes $x_i$ and $y_i$, there are $c_i$ delicious snacks for cats.

# Task

Portocal can choose exactly $K$ nodes; for each chosen node, he will walk from the root of the tree to the chosen node and eat the snacks on the edges he passes. Obviously, he can eat the snacks on an edge only once. Since Portocal is a very curious cat, he wants to know the maximum number of snacks he can eat if he optimally chooses the $K$ nodes, assuming the root of the tree was node $i$, for each $i$ from $1$ to $N$.

# Input data

The first line of the input will contain two integers $N$ and $K$, the number of nodes in the tree and the number of nodes that Portocal will choose, respectively. The next $N - 1$ lines will contain three integers each, $x_i, y_i$, and $c_i$, describing the edges of the tree.

# Output data

The $i$-th line of the output (for $1 \leq i \leq N$) should contain the maximum number of snacks Portocal can eat if the root of the tree were $i$.

# Constraints and clarifications

* $1 \leq K \leq N \leq 100 \ 000$
* $0 \leq c_i \leq 1 \ 000 \ 000 \ 000$, for $1 \leq i \leq N$

| # | Points | Constraints   |
| - | ------- | ------------------- |
| 1 | 8      | $N \leq 18$|
| 2 | 11      | $N \leq 200, \ K \leq 20$|
| 3 | 17     | $N \leq 1 \ 000, \ K \leq 100$|
| 4 | 20      | $N \leq 2 \ 000$|
| 5 | 12      | $K = 1$|
| 6 | 32      | No additional constraints.|

# Examples

`stdin`
```
11 3
1 2 5
2 3 3
2 6 5
3 4 4
3 5 2
1 7 6
7 8 4
7 9 5
1 10 1
10 11 1
```

`stdout`
```
28
28
28
32
30
32
28
32
32
29
30
```

## Explanation

If the root is node $1$, then Portocal can choose nodes $4, 6$ and $9$. The paths from the root to the chosen nodes will be $1 - 2 - 3 - 4, 1 - 2 - 6, 1 - 7 - 9$, and the total number of snacks on these paths will be $5 + 3 + 4 + 5 + 6 + 5 = 28$. Note that the snacks on edge $1 - 2$ have been counted only once.

~[arb.png|align=center]
