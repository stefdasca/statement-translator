## Task

A connected and undirected graph is given. An edge needs to be cut in such a way that it becomes bipartite (connected or not).

## Input data

The input file `bip.in` contains, on the first line, the number $T$ of tests, then lines that describe each test as follows:
- the first line contains the numbers $N$ of nodes and $M$ of edges, separated by a space
- on the following $M$ lines, the edges with indices $0$, $1$, $\dots$, $M-1$ described through an unordered pair of numbers separated by a space, representing the nodes

It is guaranteed that the edges do not repeat and that, initially, the graph is not bipartite.

## Output data

In the output file `bip.out` there are $T$ descriptions of the answer for each test, as follows:
- the first line contains the number of edges that can be removed such that the graph becomes bipartite;
- if this number is nonzero, the second line contains the indices of these edges, in increasing order and separated by a space

## Constraints and clarifications

Let $Q$ be the sum of the numbers $M$ from the $T$ tests.
- $3 \leq N \leq M \leq 50\ 000$
- $Q \leq 150\ 000$
- For 20 points, $Q \leq 500$
- For an additional 10 points, the graph contains a single cycle
- For an additional 40 points, $Q \leq 30\ 000$

## Example

`bip.in`
```
3
3 3
1 2
2 3
3 1
4 6
1 2
1 3
1 4
2 3
2 4
3 4
7 8
1 2
2 3
3 4
4 5
5 6
6 7
6 3
7 1
```

`bip.out`
```
3
0 1 2
0
1
4 0 1 5
```