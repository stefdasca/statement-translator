## Task

An undirected graph with $N$ nodes and $M$ edges is given. A cycle of length $K$ in the graph is a sequence formed by the nodes $X_1$, $X_2$, $X_3$, $\dots$, $X_{K+1}$, with the property that $X_1 = X_{K+1}$. A cycle is elementary if all the nodes except the first and the last are pairwise distinct. It is required to display all the nodes that belong to at least one elementary cycle of odd length with more than one element.

## Input data

The input file `victorie.in` contains on the first line two natural numbers $N$ and $M$, representing the number of nodes and the number of edges of the graph, respectively. Each of the following $M$ lines contain two natural numbers $x$ and $y$ representing an edge in the graph.

## Output data

The output file `victorie.out` contains on the first line a natural number $NR$ representing the number of nodes that belong to at least one elementary cycle of odd length. The second line will contain $NR$ natural numbers in ascending order, representing the indices of the nodes that have this property.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 300\ 000$

The nodes in the graph are numbered from 1 to $N$.

An edge can have both ends in the same node.

## Example

`victorie.in`

```
4 4
1 2
1 3
2 3
2 4
```

`victorie.out`

```
3
1 2 3
```