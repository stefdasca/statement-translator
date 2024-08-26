## Task

Given an undirected graph with $N$ nodes and $M$ edges, find the subgraph with the maximum number of nodes such that the minimum degree of a node in the subgraph is as large as possible (the degree of the node is calculated within the subgraph and not the entire initial graph).

## Input data

The input file `gminmax.in` contains on the first line the numbers $N$ and $M$ separated by a space. The next $M$ lines each contain two numbers $x$ and $y$ indicating that there is an edge between $x$ and $y$.

## Output data

The output file `gminmax.out` will contain two numbers separated by a space representing the maximum minimum degree that can be obtained in a subgraph and the maximum size of a subgraph that meets this property.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 500\ 000$

There will be no double edges or self-loops.

## Example

`gminmax.in`

```
7 10
1 2
1 3
1 4
2 3
2 4
3 4
4 5
5 6
6 4
3 7
```

`gminmax.out`

```
3 4
```

## Explanation

If we choose the subgraph formed by the nodes $1$, $2$, $3$, and $4$, the minimum degree of a node is $3$. No other subgraph has a minimum degree of a node greater than $3$ and this subgraph is the largest that respects this degree.