# Drumuri2

Given a directed acyclic graph with $N$ nodes (numbered from $1$ to $N$) and $M$ arcs. A path in the graph is a sequence of one or more vertices $D = (x_1, x_2, \dots, x_k)$ such that for any $i$ from $\{1, 2, \dots, k-1\}$, there exists an arc $(x_i, x_{i+1})$. We define a covering of the graph as a set of paths in the graph, with the property that every vertex of the graph belongs to at least one path in the set. It is not necessary for the paths in a covering to be disjoint (neither relatively to vertices, nor relatively to arcs).

## Task

Determine the minimum number of paths required to cover a given graph.

## Input data

In the input file `drumuri2.in` the first line contains the natural numbers $N$ and $M$, separated by a space. On each of the following $M$ lines, there is a pair of natural numbers $i$, $j$ $(1 \leq i, j \leq N)$ separated by a space, indicating that there is an arc from vertex $i$ to vertex $j$.

## Output data

The output file `drumuri2.out` will contain a single line representing the minimum number of paths required to cover the graph from the input file.

## Constraints

$1 \leq N \leq 100$ 

$1 \leq M \leq 5000$ 

## Example

`drumuri2.in` 

```
7 7 
1 2 
7 2 
2 3 
2 4 
3 5 
4 5 
4 6
```

`drumuri2.out` 

```
2 
```

## Explanations

$D1$: $1 \to 2 \to 3 \to 5$

$D2$: $7 \to 2 \to 4 \to 6$