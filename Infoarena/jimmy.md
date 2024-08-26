Jimmy

Jimmy studies at the university Advanced Algorithms on Graphs. His latest assignment consists of finding a maximum matching in a special type of graph. This graph is undirected, has $N$ nodes, and each node has a degree of 3. Moreover, the graph is bi-connected in terms of edges (i.e., at least 2 edges need to be removed for the graph to become disconnected). A matching is a subset of the edges of the graph such that any two edges in the subset do not have a common endpoint. A maximum matching is one with maximal cardinality. Given a series of special graphs with the above-mentioned properties, find the cardinality of a maximum matching for each graph.

## Task

## Input data

The first line of the input file `jimmy.in` contains the integer $T$, representing the number of graphs described below. The description of each graph contains on the first line the even integer $N$, representing the number of nodes of the graph. Each of the next $\frac{3N}{2}$ lines contains 2 integers, $A$ and $B$, separated by a space, indicating that there is an edge between node $A$ and node $B$. The nodes are numbered from $1$ to $N$.

## Output data

For each of the $T$ graphs given in the input file, print in the output file `jimmy.out` one line containing the cardinality of a maximum matching.

## Constraints

$1 \leq T \leq 50$

$4 \leq N \leq 5000$

## Example

`jimmy.in`
```
2
4
1 2
1 3
1 4
2 3
2 4
3 4
4
1 2
1 3
1 4
2 3
2 4
3 4
```

`jimmy.out`
```
2
2
```