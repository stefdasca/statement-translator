# Connect

An undirected graph with $n$ nodes and $m$ edges is given. The edges are numbered in the order they appear in the input file. For each pair $(i, j)$ where $1 \leq i \leq j \leq m$, a graph is created with $n$ nodes and the initial edges numbered between $i$ and $j$ inclusive. You need to find how many of these graphs are connected.

## Input data

The input file `connect.in` contains on the first line the numbers $n$ and $m$. Each of the following $m$ lines contains 2 numbers: $u$ and $v$, indicating that there is a bidirectional edge between $u$ and $v$.

## Output data

The output file `connect.out` will contain on a single line the number of connected graphs found.

## Constraints and clarifications

$2 \leq n \leq 50\ 000$

$1 \leq m \leq 200\ 000$

$1 \leq u, v \leq n$

The graph can contain multiple edges between the same 2 nodes.

### Scoring

For 5 points, $n \leq 100$, $m \leq 200$

For another 15 points, $n \leq 2\ 000$, $m \leq 5\ 000$

For another 40 points, $n \leq 200$, $m \leq 200\ 000$

For the remaining 40 points, the initial constraints apply.

## Example

`connect.in`
```
4 4
1 2
2 4
1 3
1 4
```
`connect.out`
```
3
```

## Explanation

The pairs $(i, j)$ for which the resultant graph is connected are $(1, 3)$, $(1, 4)$, and $(2, 4)$.