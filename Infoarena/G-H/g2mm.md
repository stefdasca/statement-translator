## Task

You are given a connected and undirected graph $G$ with $N$ nodes and $M$ edges. The distance between two nodes $x$ and $y$ in a graph $G$, dist$_G(x,y)$, is defined as the minimum number of edges that need to be traversed to go from one node to the other. The square of a graph $G$ (denoted by $G^2$) is defined as follows: it has the same nodes as graph $G$, and there is an edge between two nodes $x$ and $y$ if and only if $dist_G(x,y) \leq 2$ (the distance between nodes $x$ and $y$ is at most $2$ in the graph $G$). Determine, if it exists, a perfect matching in $G^2$. A perfect matching in a graph $H$ consists of $N/2$ edges such that each of the $N$ nodes of $H$ appears as one of the $2$ endpoints of exactly one single edge in the matching.

## Input data

The first line of the input file `g2mm.in` contains the integers $N$ and $M$, separated by a space. The following $M$ lines contain $2$ integers $x$ and $y$, separated by a space, representing two nodes in the graph that are connected by an edge. The nodes of the graph are numbered from $1$ to $N$.

## Output data

The first line of the output file `g2mm.out` will contain the integer $A$, having the value $1$ if there exists a perfect matching in the square of the given graph, or $0$ otherwise. If $A=1$, then the next $N/2$ lines will contain $2$ integers $x$ and $y$, describing an edge of the found perfect matching.

## Constraints

$1 \leq N \leq 30\ 000$

$N$ even

$N-1 \leq M \leq 200\ 000$

## Example

`g2mm.in`
```
8 11
1 3
2 3
3 5
5 4
4 8
8 6
6 1 
7 8
7 6
3 7
5 6
1 5 
4 6
8 2 
7 1 
3
```

`g2mm.out`
```
1 
3 7
```