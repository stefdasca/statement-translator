
# Task

Given an undirected graph $G$ with $N$ nodes and $M$ edges, determine the number of connected components in the given graph.

A connected component is a maximal subset of nodes in the graph such that for any two nodes $A$ and $B$ in that subset, it is possible to reach $A$ from $B$ using one or more edges.

# Input data

The first line contains two numbers, $N$ and $M$, representing the number of nodes and edges in the graph. The next $M$ lines contain the graph's description, each line containing an edge.

# Output data

The first line contains a single number representing the number of connected components in the graph.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $1 \leq M \leq 200\ 000$
* $1 \leq A, B \leq N$, $A \neq B$
* There are no identical edges.
* For tests worth $40$ points, $N \leq 1\ 000$.

# Example 1

`stdin`
```
6 3
1 2
1 4
3 5
```

`stdout`
```
3
```

## Explanation

Nodes $1$, $2$, and $4$ are in the same connected component. 
Nodes $3$ and $5$ are in the same connected component. 
Node $6$ is in its own connected component.

Thus, we have $3$ connected components.

# Example 2

`stdin`
```
4 2
1 2
3 4
```

`stdout`
```
2
```
```
