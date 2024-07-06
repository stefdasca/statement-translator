```markdown
# Task

Given an undirected graph with $n$ nodes, constructed according to the following rule: there is an edge from $i$ to $j$ if and only if $|i - j|$ is a prime number.

Determine the length of the shortest path from node $1$ to node $n$ or print $-1$ if this is not possible.

# Input data

The first line will contain $t$, the number of tests. The next $t$ lines will contain the values of $n$ corresponding to each graph.

# Output data

For each test, print the answer to the question or $-1$, as the case may be.

# Constraints and clarifications

* $1 \leq t \leq 100$
* $1 \leq n \leq 10^9$

# Example

`stdin`
```
6
1
7
13
50
493
8
```

`stdout`
```
0
2
2
2
2
1
```
```