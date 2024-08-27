Grarb

Given an undirected graph $G$ with $N$ nodes numbered from $1$ to $N$ and $M$ edges, determine the minimum number of edges that need to be removed and the minimum number of edges that need to be added in the graph $G$ so that it becomes a tree.

## Task

## Input data

The input file `grarb.in` contains on the first line two natural numbers $N$ and $M$ representing the number of nodes and the number of edges of $G$ respectively. On each of the following $M$ lines contain two natural numbers $x$ and $y$ indicating that there is an edge between nodes $x$ and $y$. There can be multiple edges between two nodes and there can be edges from a node to itself.

## Output data

In the output file `grarb.out`, the first line will contain the minimum number of edges that need to be removed, and the second line will contain the minimum number of edges that need to be added for the graph $G$ to be transformed into a tree.

## Constraints

$1 \leq N \leq 100\,000$

$1 \leq M \leq 200\,000$

## Example

`grarb.in`
```
6 5
1 2 
1 3 
2 4 
1 4 
5 6 
```

`grarb.out`
```
1 
1 
```

## Explanation

One possible solution is to remove the edge $(1,4)$ and to add the edge $(2,5)$.