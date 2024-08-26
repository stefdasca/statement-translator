# Cycle Tree

A cycle tree is an undirected graph that has one of the following properties:
- It is a cycle of length $K$ ( $K \geq 3$ )
- It is a graph obtained by attaching a cycle $C$ of length $K$ ( $K \geq 3$ ) to an edge from a cycle tree $CT$

Attaching a cycle to an edge in a graph means replacing an edge from the cycle with an edge from the graph (and also replacing the two nodes of the edge from the cycle with the two nodes of the edge from the graph).

Given several graphs, determine for each one if it is a cycle tree.

## Input data

The first line of the input file `arbciclu.in` contains a natural number $T$, representing the number of given graphs.
For each given graph, the first line will contain two natural numbers: $N$ and $M$. $N$ is the number of nodes in the graph and $M$ is the number of edges. The next $M$ lines will contain two integers $A$ and $B$, indicating that there is an edge between node $A$ and node $B$. The nodes in the graph are numbered from $1$ to $N$.

## Output data

For each graph, in the given order in the input file, print in the file `arbciclu.out` the string $YES$ if the graph is a cycle tree, or $NO$ otherwise.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq N \leq 100\,000$

$1 \leq M \leq 200\,000$

## Example

`arbciclu.in`
```
2
3 3
1 2
1 3
3 2
4 5
1 2
1 3
3 2
4 3
2 4
```

`arbciclu.out`
```
YES
YES
```

