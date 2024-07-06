Given an undirected graph by the number of nodes $N$, the number of edges $M$, and $M$ pairs of nodes representing the edges. The nodes are labeled with $1, 2, \dots, N$. We want to determine the connected components and check which of them are Eulerian subgraphs.

# Task

Given an undirected graph by $N$, $M$, and $M$ pairs of nodes with the above meaning, we are required to:
1. The maximum number of nodes in a connected component.
2. The number of connected components that are Eulerian subgraphs.

# Input data

The first line of the input file `compeuler.in` contains the task number $C$, the second line contains $N$ and $M$ separated by a space, and the next $M$ lines contain pairs of nodes separated by a space representing the edges.

# Output data

The first line of the output file `compeuler.out` will contain a single number representing the maximum number of nodes in a connected component, if the task is $C = 1$, respectively, the number of connected components that are Eulerian subgraphs, if the task is $C = 2$.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000$;
* $1 \leq M \leq 10 \ 000$;
* For correctly solving task $1$, $20$ points will be awarded.
* For correctly solving task $2$, $80$ points will be awarded.

# Example 1

`compeuler.in`
```
1
6 4
1 4
5 2
3 2
3 5
```

`compeuler.out`
```
3
```

## Explanation

$C = 1$. There are $3$ connected components with the set of nodes each: $\{1,4\}$, $\{2,3,5\}$, $\{6\}$. So, $3$ is the maximum number of nodes in a connected component.

# Example 2

`compeuler.in`
```
2
6 4
1 4
5 2
3 2
3 5
```

`compeuler.out`
```
1
```

## Explanation

$C = 2$. There are $3$ connected components with the set of nodes each: $\{1,4\}$, $\{2,3,5\}$, $\{6\}$. Among these $3$ connected components, only the second one is an Eulerian subgraph.