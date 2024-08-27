# Paths

Portocal, the orange cat, has found a tree (an undirected, connected, acyclic graph) with $N$ nodes numbered from 1 to $N$. On each edge $i$ $(1 \leq i < N)$ that connects nodes $x_i$ and $y_i$, there are $c_i$ snacks for cats. Portocal can choose exactly $K$ nodes; for each chosen node, he will walk from the root of the tree to the chosen node and eat the snacks on the edges he traverses. Obviously, he can eat the snacks on an edge only once. Since Portocal is a very curious cat, he wants to know what is the maximum number of snacks he can eat by optimally choosing the $K$ nodes, if the root of the tree was node $i$, for each $i$ from 1 to $N$.

## Input data

The input file `paths.in` will contain on the first line two integers $N$ and $K$, the number of nodes in the tree and respectively the number of nodes that Portocal will choose. The next $N - 1$ lines will contain 3 integers each, $x_i$, $y_i$ and $c_i$, describing the edges of the tree.

## Output data

The $i$-th line of the output file `paths.out` $(for\ 1 \leq i \leq N)$ should contain the maximum number of snacks that Portocal can eat if the root of the tree were node $i$.

## Constraints and clarifications

$1 \leq K \leq N \leq 100\,000$

$0 \leq c_i \leq 1\,000\,000\,000$

For 8 points, $N \leq 18$

For 12 points, $N \leq 200$ and $K \leq 20$

For 16 points, $N \leq 1000$ and $K \leq 100$

For 20 points, $N \leq 2000$

For 12 points, $K = 1$

## Example

`paths.in`
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
`paths.out`
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

If the root is node $1$, then Portocal can choose nodes $4$, $6$, and $9$. The paths from the root to the chosen nodes will be $1 - 2 - 3 - 4$, $1 - 2 - 6$, $1 - 7 - 9$ and the total number of snacks on these paths will be $5 + 3 + 4 + 5 + 6 + 5 = 28$. Note that the snacks on the edge $1 - 2$ have been counted only once.