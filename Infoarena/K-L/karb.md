# Karb

A simple connected undirected graph with $N$ nodes and $M$ edges is given. The edges have a cost of $0$ or $1$. It is required to determine a spanning tree with an exact cost of $K$.

## Input data

The input file `karb.in` contains on the first line the values of $N$, $M$, and $K$. The next $M$ lines contain three numbers $x$, $y$, and $w$, separated by a space, representing the edge $(x, y)$ with cost $w$.

## Output data

The output file `karb.out` should contain $N - 1$ edges out of the $M$, representing the edges of a spanning tree with cost $K$.

## Constraints

$1 \leq N \leq 100\,000$.

$1 \leq M \leq 200\,000$.

There will always be a solution.

## Example

`karb.in`

```
6 8 3
1 3 1
1 2 0
2 3 1
3 4 1
2 4 0
2 5 0
4 6 1
5 6 1
```

`karb.out`

```
1 3
3 4
5 6
2 4
```