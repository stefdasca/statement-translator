
# Task

You are given a graph with $N + 1$ nodes numbered from $0$ to $N$. There are edges from node $N$ to all the other $N$ nodes and between any two nodes $A$ and $B$ with the property that $A, B < N$ and $(A + 1) = B \mod N$. It can be observed that the total number of edges is $2 \cdot N$.

You are asked to color the edges of the graph with as few colors as possible such that between any two nodes there exists at least one path that contains only distinct colored edges.

# Input data

The first line of the file `color.in` will contain a single natural number $N$ having the significance from the statement.

# Output data

The file `color.out` will contain on the first line a single natural number $M$ representing the number of colors used. The next $2 \cdot N$ lines will contain three numbers $A$, $B$ and $C$, signifying that the edge between nodes $A$ and $B$ was colored with color $C$.

# Constraints and clarifications

* $3 \leq N \leq 100$
* The colors displayed in the output file must be natural numbers in the range $[1, M]$, where $M$ is the number of colors used.
* The score you will get on each test will be calculated using the formula: $ \displaystyle \left( \frac{raspuns_{optim}}{raspuns_{concurent}} \right) ^2 \cdot 10$

# Example

`color.in`
```
3
```

`color.out`
```
1
0 3 1
1 3 1
2 3 1
0 1 1
1 2 1
2 0 1
```

## Explanation

We have edges between any two nodes, so we can use a single color to color the graph.
