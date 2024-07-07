
# Task

Given an undirected graph $G$ with $N$ nodes and $M$ edges, and a node $S$. Find the length of the shortest path between $S$ and each node in the graph, including $S$.

We define the shortest path between two nodes $A$ and $B$ as the minimum number of edges in a chain that connects nodes $A$ and $B$.

# Input data

The first line will contain three numbers, $N$, $M$, and $S$, representing the number of nodes and edges in the graph, as well as the starting node. The next $M$ lines contain the description of the graph, each line containing an edge.

# Output data

The first line will contain $N$ numbers, representing the lengths of the shortest paths between $S$ and the other nodes in the graph. If there is an inaccessible node from $S$, $-1$ will be printed for that node.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $1 \leq M \leq 200\ 000$
* $1 \leq A, B \leq N$, $A \neq B$
* There are no duplicate edges.
* For tests worth $40$ points, $N \leq 1\ 000$.

# Example

`stdin`
```
5 5 3
1 2
1 3
1 4
2 3
5 4
```

`stdout`
```
1 1 0 2 3
```
