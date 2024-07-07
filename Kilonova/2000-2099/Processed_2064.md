
# Task

We are given a tree with $n$ nodes, each node having a value assigned to it. The root of the tree is node $1$. Find the sum of the sums of the subtrees of the given tree.

A subtree is defined as a tree rooted at node $i$ and including all nodes that can be reached from node $i$ if we cut the connection between $i$ and its parent.

Note that the subtree of node $1$ is identical to the given tree.

# Input data

The first line contains $n$, the number of nodes in the tree.

The second line contains $n$ values, representing the values of the nodes in the tree.

The next $n - 1$ lines contain the edges of the tree, where edge $(x, y)$ means that there is an edge between nodes $x$ and $y$.

# Output data

The first line contains the required answer.

# Constraints and clarifications

* $1 \leq n \leq 2 \cdot 10^5$.
* $1 \leq v_i \leq 10^6$.

# Example

`stdin`
```
5
5 1 8 3 4
1 2
1 3
2 4
4 5
```

`stdout`
```
48
```

## Explanation

~[tree.png]

For example, the subtree of node $2$ includes nodes $2$, $4$, and $5$. The sum of these values is $1 + 3 + 4 = 8$.
