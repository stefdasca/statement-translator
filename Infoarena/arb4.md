# Arb4

A graph with $N$ nodes and $M$ edges is given. The first $N - 1$ edges form a minimum cost spanning tree. For each edge $i$ in the tree, you need to determine with which edge it should be replaced, in case edge $i$ is deleted, such that the cost of the spanning tree remains minimal.

## Task

The input file `arb4.in` will contain on the first line 2 natural numbers $N$ and $M$. The next $M$ lines will contain 3 natural numbers $a$ $b$ $c$ representing an edge from $a$ to $b$ with a cost $c$. The initial tree is formed by the first $N - 1$ edges from the $M$ edges.

## Input Data

The input file `arb4.in` will contain on the first line 2 natural numbers $N$ and $M$. Each of the next $M$ lines will contain 3 natural numbers $a$ $b$ $c$ representing an edge from $a$ to $b$ with a cost $c$. The first $N - 1$ edges from the $M$ edges form the initial tree.

## Output Data

The output file `arb4.out` will contain $N - 1$ lines. Line $i$ will contain the index of the edge that would be used if edge $i$ is removed from the tree. If edge $i$ cannot be replaced, print $-1$.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 250\ 000$

edges have distinct costs pairwise within the interval $[1,1\ 000\ 000\ 000]$

the first $N - 1$ edges form a minimum cost spanning tree in the given graph

nodes and edges are numbered from $0$

between any two nodes there is at most one edge

and there is no edge from a node to itself

## Example

`arb4.in`

```
5 10 
3 2 1 
4 2 2 
0 3 3 
1 4 4 
0 4 456867131 
1 3 33364433 
0 1 49309036 
3 4 975587959 
0 2 139619699 
2 1 767959053
```

`arb4.out`

```
5
5
6
5
6
```