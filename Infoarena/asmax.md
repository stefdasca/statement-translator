# Asmax

Consider an undirected, connected, acyclic graph (tree) with $N$ vertices, where each vertex $i$ has an associated integer value $V_i$. A subtree of the given tree is defined as a non-empty connected subgraph of it (which can even coincide with the given tree).

## Task

Detemine a subtree of a given tree such that the sum of the values associated with the vertices contained in the subtree is maximum.

## Input data

The first line of the input file `asmax.in` contains the integer $N$, representing the number of vertices of the tree. The second line of the file contains $N$ integer values, representing the values associated with the nodes. The $A_i$-th value of this sequence represents the value associated with node $i$. The following $N-1$ lines contain two distinct integers $a$ and $b$, separated by a space, indicating that there is an edge between the vertex numbered $a$ and the one numbered $b$.

## Output data

In the file `asmax.out`, print the maximum sum of a subtree of the given tree.

## Constraints and clarifications

$1 \leq N \leq 16000$

$-1000 \leq V_i \leq 1000$

The vertices are numbered with distinct numbers between $1$ and $N$.

## Example

`asmax.in`
```
5
-1 1 3 1 -1
4
1 1
3 1
2 4
5 4
```

`asmax.out`
```
4
```

## Explanation

The subtree containing the vertices $1, 2, 3$ and $4$ has a sum of $4$.