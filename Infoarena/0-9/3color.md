# 3color

We define a coloring of an undirected graph as a set of colors associated with its nodes, such that any two adjacent nodes have different colors. We call a graph $k$-colorable if there exists a coloring of the graph that contains at most $k$ distinct colors. Given an undirected graph with $V$ nodes numbered from $0$ to $V - 1$ and $E$ edges that is $3$-colorable, you are asked to find a $100$-coloring of it.

## Input data

The input file `3color.in` contains, on the first line, the integers $V$ and $E$ as described above. The following $E$ lines contain two integers $x$ and $y$ representing an edge from node $x$ to node $y$.

## Output data

In the output file `3color.out`, print $V$ numbers between $0$ and $99$, representing the colors assigned to the nodes.

## Constraints and clarifications

$1 \leq V \leq 1000$

$1 \leq E \leq 15000$

If there is more than one solution, you may print any.

## Example

`3color.in`

```
6 9
0 1
0 2
0 4
0 5
0 3
1 2
2 5
2 3
2 4
```

`3color.out`

```
0 1 2 3 4 5
```

## Explanation

We can assign a different color to each node.