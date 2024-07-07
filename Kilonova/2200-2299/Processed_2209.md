
# Task

Bujorel has started practicing pomology and has planted a tree (an acyclic connected graph) with $N$ nodes, each node having a given color from an interval $[1, K]$. Now, after the tree has grown, he wants to know, for each color, the sum of the distances between all pairs of nodes in the tree that have that color. The distance between two nodes is defined as the number of edges on the path between the two nodes. 
Since Bujorel used a lot of fertilizer when planting the tree, it has grown very large, and you need to write a program that calculates the sum of the distances between nodes of the same color.

# Input data

The first line of the file `kdist.in` contains two natural numbers $N$ and $K$, the number of nodes in the tree and the number of colors in which the nodes are painted, respectively. The next $N-1$ lines describe the tree, each line containing two natural numbers $x$ and $y$, representing an edge between node $x$ and node $y$. Next, there are $N$ lines, the $i$-th of these lines containing an integer $c$ belonging to the interval $[1, K]$ representing the color of node $i$.

# Output data

The file `kdist.out` will contain $K$ lines, the $i$-th line containing the sum of the distances between all pairs of nodes that have the color $i$.

# Constraints and clarifications

* $1 \leq K \leq N \leq 200\ 000$
* In calculating the sum of the distances between nodes of the same color, each pair of nodes $(x, y)$ will be considered only once.

# Example

`kdist.in`
```
6 3
1 2
1 3
3 4
3 5
5 6
1
2
2
1
2
3
```

`kdist.out`
```
2
6
0
```

## Explanation

For color $1$ we have one pair: $(1, 4)$, with a distance of $2$.
For color $2$ we have 3 pairs: $(2, 3)$ with a distance of $2$, $(2, 5)$ with a distance of $3$, and $(3, 5)$ with a distance of $1$.
For color $3$ we have only one node with this color, so the answer is $0$.
