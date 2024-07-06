```markdown
# Task

Given an undirected graph with $n$ nodes and $m$ edges, remove at most one edge from the graph such that the number of nodes with even degree is as large as possible.

# Input data

The first line contains two integers, $n$ and $m$, representing the number of nodes in the graph. The following $m$ lines contain the edges of the graph.

# Output data

The first line will contain a single integer, the maximum number of nodes with even degree in the graph.

# Constraints and clarifications

* $1 \leq n \leq 100 \ 000$;
* $1 \leq m \leq 200 \ 000$;
* There are no duplicate edges.

# Example

`stdin`
```
5 4
1 2
1 3
2 4
4 5
```

`stdout`
```
3
```
```