## Task

Given an undirected graph $G=(V,E)$ and three nodes $A,B,C \subseteq V$, determine the minimum cost of the trilateral $(A,B,C)$.

## Input data

The first line of the file `trilant.in` contains two numbers $N,M$ separated by a space, representing the number of nodes and the number of edges in the graph, respectively.

The second line of the input file will contain the numbers $A,B,C$ with the meaning from the statement.

The next $M$ lines will contain three natural numbers $P,Q,T$ describing the existence of an edge from node $P$ to node $Q$ with the cost $T$.

## Output data

The file `trilant.out` will contain on the first line the minimum cost found.

Each of the next three lines will have the following format: $K$, followed by $K$ numbers $x_1,x_2 \dots x_k$, representing one of the three paths that form the required trilateral. The three paths will be displayed with nodes in order from $X$ to $A$, from $X$ to $B$, and from $X$ to $C$.

In case there are multiple solutions, any of them can be displayed.

## Constraints and clarifications

$1 \leq A, B, C \leq N \leq 100000$

$1 \leq M \leq 250000$

$1 \leq$ cost of an edge $\leq 4000000$

For 50% of the tests $N \leq 1000$

The paths that form a trilateral can have different lengths.

Any three paths $(A,X),(B,X),(C,X)$ that form a trilateral will be disjoint two by two, except for the node $X$ (the only common node they will have is $X$).

There will always be a solution.

## Example

`trilant.in`

```
4 3
1 2 3
1 4 1
2 4 1
3 4 1
```

`trilant.out`

```
3
2 4 1
2 4 2
2 4 3
```