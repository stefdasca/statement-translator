# Color

Consider a complete graph with $N$ vertices where the edges are colored either red or black. In this graph, monochromatic triangles can be formed (three vertices connected by edges of the same color).

## Task

Write a program that determines the number of monochromatic triangles for a given colored graph.

## Input data

The input file `color.in` contains: 
$N$ 
$S$
$x_1 \; y_1$ 
$x_2 \; y_2$
$\dots$ 
$x_s \; y_s$
$N$ - the number of vertices in the graph,
$S$ - the number of red edges,
$x_i \; y_i$ - the endpoints of the $i$-th red edge.

## Output data

The output file `color.out` contains on the first line the number of monochromatic triangles.

## Constraints

$1 \leq N \leq 4\ 000$

$1 \leq S \leq 500\ 000$

The same edge does not appear multiple times in the input file.

Edges not appearing in the input file are colored, obviously, black.

## Example

`color.in`

```
4
4
1 2
2 3
4 3
4 2
```

`color.out`

```
1
```