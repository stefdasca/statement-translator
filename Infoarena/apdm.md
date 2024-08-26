APDM

We consider a connected, undirected graph with $N$ vertices and $M$ edges. Let $D(i, j)$ be the minimum distance between vertices $i$ and $j$. The diameter of the graph is defined as $\max \{ D(i,j) \mid 1 \leq i < j \leq N \}$.

## Task

Determine the spanning tree with the minimum diameter of the given graph!

## Input data

The first line of the file `apdm.in` contains $N$ and $M$. Each of the following $M$ lines contains two integers in the form $x \; y$, indicating the presence of an edge between vertices $x$ and $y$.

## Output data

The first line of the file `apdm.out` will contain the diameter of the obtained tree.

## Constraints

$3 \leq N \leq 150$

$N \leq M \leq 5000$

## Example

`apdm.in`

```
8 13
1 2
1 5
2 4
1 7
2 3
3 4
3 8
4 5
4 6
5 6
5 7
6 7
6 8
```

`apdm.out`

```
4
```

## Explanation

In the drawing, the edges of a spanning tree with a diameter of 4 are highlighted in green. These edges are: $(1, 5)$, $(2, 4)$, $(3, 4)$, $(4, 5)$, $(4, 6)$, $(5, 7)$, $(6, 8)$.