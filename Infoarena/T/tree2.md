## Task

The square of an undirected graph $G$ is a graph $G^2$ that has the same set of vertices as $G$ and contains an edge $(u, v)$ between a pair of vertices $u$ and $v$ if and only if there is a path of length at most 2 edges between $u$ and $v$ in $G$. Given $G^2$ and knowing that $G$ is a tree (an undirected, connected graph that contains no cycles), determine the graph $G$.

## Input data

The input file `tree2.in` contains on the first line the integers $N$ and $M$, representing the number of nodes and the number of edges in $G^2$, respectively. 
The next $M$ lines contain two integers $A$ and $B$, indicating that there is an edge between node $A$ and node $B$ in $G^2$. There will be at most one edge between any two nodes.

## Output data

In the output file `tree2.out`, you will print $N - 1$ lines, corresponding to the $N - 1$ edges of $G$. Each line will contain two integers $A$ and $B$, indicating that there is an edge between nodes $A$ and $B$ in $G$. The edges can be printed in any order.

## Constraints and clarifications

$2 \leq N \leq 333$

Nodes are numbered from 1 to $N$. 
It is guaranteed that there will be at least one tree $G$ whose square is the graph given in the input file. If there are multiple solutions, you can print any of them.

## Example

`tree2.in` 
```
9 19
1 2
1 3
1 4
1 5
2 3
2 4
2 5
2 9
3 4
3 5
3 6
3 7
3 8
3 9
4 5
4 8
5 6
5 7
6 7
```

`tree2.out` 
```
1 3
2 3
2 9
3 4
3 5
4 8
5 6
5 7
```