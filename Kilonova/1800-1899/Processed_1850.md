Here’s the translated competitive programming problem statement:

## Task

You are given an undirected graph with $n$ nodes and associated edge costs. Several queries of the form $(i, j, k)$ are made with the meaning: Is node $k$ on a minimum cost path from node $i$ to node $j$?

## Input data

The input file `pedrumuriminime.in` contains on the first line two natural numbers $n$ and $m$ representing the number of nodes and the number of edges of the given graph. The next $m$ lines contain three natural numbers, separated by a space, $x \ y \ c$ meaning there is a bidirectional edge from $x$ to $y$ with cost $c$.
The next line contains a number $q$, representing the number of queries.
The next $q$ lines contain three numbers $i \ j \ k$, with the meaning described above.

## Output data

The output file `pedrumuriminime.out` will contain $q$ values of $0$ and $1$, without spaces, representing the responses to the queries ($1$ represents an affirmative answer).

## Constraints and clarifications

* $1 \leq n \leq 300$
* $1 \leq m \leq$ maximum possible number of edges in the graph
* $1 \leq q \leq 100 \ 000$
* Given edges are distinct
* $x \not = y$ in all input data
* Edge costs are non-zero natural numbers up to $1 \ 000 \ 000$
* In each triplet $i, j, k$ are different from each other
* The cost of a path is defined as the sum of the edge costs on that path

## Example

`pedrumuriminime.in`
```
4 4
1 2 3
1 3 1
2 3 1
1 4 5
2
1 2 3
1 2 4
```

`pedrumuriminime.out`
```
10
```