
Given an undirected connected graph $G$ with $N$ nodes and $M$ edges, each edge having an associated cost.
A partial tree for $G$ is a subgraph with the structure of a tree, which includes all nodes and some of the edges.

# Task

Find a partial tree of the graph $G$ such that the difference between the highest and the lowest cost of an edge is minimal.

# Input data

The input file will contain on the first line the numbers $N$ and $M$, separated by a space. The following $M$ lines will contain the edges of the graph in the form `X Y C`, meaning there exists an undirected edge between $X$ and $Y$ with cost $C$.

# Output data

The output file will contain on the first line the minimal difference between the highest and the lowest cost of the edges of a partial tree in $G$.

# Constraints and clarifications
* $2 \leq N \leq 30\ 000$;
* $1 \leq M \leq 100\ 000$;
* $1 \leq X < Y \leq N$;
* $1 \leq C \leq 1\ 000\ 000\ 000$;
* Between any two nodes, there is at most one edge;
* For $20$ points, $1 \leq M \leq 20$;
* For $20$ points, $2 \leq N \leq 100$ and $1 \leq M \leq 100$;
* For $20$ points, $2 \leq N \leq 1000$ and $1 \leq M \leq 10\ 000$;
* For $20$ points, $M\cdot(M-N)\cdot (M-N) \leq 10^{7}$;
* For $20$ points, there are no additional constraints.

# Example

`weightdif.in`
```
6 10
1 2 2
2 3 1
3 4 2
4 5 1
5 6 2
1 6 1
1 4 20
2 5 5
2 6 6
4 6 7
```

`weightdif.out`
```
1
```

## Explanation

The graph in the example:

~[wd_1.png]

A partial tree with the minimal difference between the maximum and minimum cost of the edges:

~[wd_2.png]
