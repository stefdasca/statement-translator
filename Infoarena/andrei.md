# Andrei

Given an undirected graph with $N$ nodes and $M$ edges colored in one of the colors: white, red, or purple. Partition the set of nodes into two subsets $A$ and $B$ such that: there is no white edge between two nodes in $A$; there is no red edge between two nodes in $B$; there is no purple edge between a node in $A$ and one in $B$.

## Input data

The input file `andrei.in` contains on the first line two natural numbers $N$ and $M$. Each of the following $M$ lines contains three values $A$, $B$ and $C$. $A$ and $B$ represent two nodes between which there is an edge, and $C$ is the color of the edge. $C$ will take the value $0$ if the edge is white, $1$ if it is red, and $2$ if it is purple.

## Output data

In the output file `andrei.out` you will print $N$ numbers from the set $\{0, 1\}$. The $i$-th value will be $0$ if node $i$ is part of subset $A$, or $1$ if it is part of $B$.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$1 \leq M \leq 200\ 000$

It is guaranteed that there is at least one solution.

If there are multiple solutions, you can print any of them.

There can be any number of edges of any color between two nodes.

## Example

`andrei.in`
```
4 4
4 3 0
2 4 1
1 2 0
1 3 1
```

`andrei.out`
```
1 0 1 0
```