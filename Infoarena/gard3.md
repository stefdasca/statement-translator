# Gard3

The farmer Ion owns a farm in the shape of a convex polygon with $N$ sides. One day, he decides to divide it into $K$ regions, which will also be convex polygons. After the division, he will use each area for a specific purpose (for example, in area $1$ he will plant vineyards, in area $2$ he will raise cows, etc.). To do this, he will construct $K-1$ fences. Each fence will be a segment connecting two vertices of the polygon. The fences will only intersect, if at all, at the vertices of the polygon. Before starting, the farmer Ion wants to know in how many ways he can divide his farm into $K$ regions (to examine them and choose a certain way of dividing).

## Task

Write a program that, for given values $N$ and $K$, will display the number of ways farmer Ion can divide his farm into $K$ regions.

## Input data

The file `gard3.in` contains on the first line the natural numbers $N$ and $K$, separated by a space.

## Output data

The output file `gard3.out` will contain the number of ways to divide the farm into $K$ regions.

## Constraints

$3 \leq N \leq 50$

$1 \leq K \leq N-2$

## Examples

`gard3.in`
```
5 2
```
`gard3.out`
```
5
```

## Explanation

A single fence is built. It will connect one of the pairs of vertices: $(1, 3)$ $(1, 4)$ $(2, 4)$ $(2, 5)$ $(3, 5)$.

`gard3.in`
```
10 7
```
`gard3.out`
```
5005
```