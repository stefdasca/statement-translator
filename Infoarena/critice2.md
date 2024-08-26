# Critice2

Given an undirected connected graph with $N$ nodes and $M$ edges. There are also $E$ fictive edges, an edge $i$ from these $E$ has the probability $P[i]$ to appear in the graph. We want to know the average number of critical edges in the graph.

## Input data

The input file `critice2.in` will contain on the first line two natural numbers $N$ and $M$ with the meaning from the statement. The next $M$ lines will contain $M$ pairs of numbers representing the edges in the initial graph. On the $M+2$ line, there will be a natural number $E$, with the meaning from the statement. The next $E$ lines will contain $E$ triplets of numbers $x$ $y$ $p$, representing the fact that we will add the edge $x-y$ with probability $p$ in the final graph.

## Output data

In the output file `critice2.out` you must print with a precision of 4 decimal places the average number of critical edges in the final graph.

## Constraints and clarifications

$1 \leq N \leq 100\,000$

$1 \leq M, E \leq 200\,000$

Edges can repeat and there can be edges from a node to itself

An edge is considered critical if removing it from the graph would make the graph no longer connected

The answer is considered correct if the difference between what you print and the result of the committee is at most $0.0001$

## Example

`critice2.in` `critice2.out`
```
4 4
1 2
2 3
2 4
3 4
1
1 4 0.3
0.700000
```

`critice2.in` `critice2.out`
```
8 9
1 2
2 3
3 4
4 1
1 5
5 6
6 7
7 5
7 8
3
2 8 0.5
6 8 0.123
4 7 0.752
0.562500
```

`critice2.in` `critice2.out`
```
5 5
1 2
1 2
3 1
3 4
4 5
2
1 1 0.283000
1 5 0.510200
1.469400
```

## Explanations

For the first example: with a probability of $0.7$, none of the $E$ edges appear. The resulting graph has a single critical edge. With a probability of $0.3$, that edge appears in the graph, and thus the graph no longer has any critical edges. The answer is therefore $0.7 \times 1 + 0.3 \times 0 = 0.7$.