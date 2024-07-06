*~~Matei Nakayama~~ Mihai received a cactus.*

A cactus is an undirected connected graph in which each node is part of **at most one cycle**. Consider a cactus with $N$ nodes and $M$ edges of various lengths. It does not contain loops (i.e., edges between a node and itself) or parallel edges (i.e., two or more edges between a single pair of nodes).  
\
Mihai wants to remove edges from the cactus graph to obtain a tree as lightweight as possible. The distance between two nodes in the tree is equal to the sum of the lengths of the edges on the shortest path between the two nodes. The weight of a tree is defined as the sum of the distances between any two unordered pairs of distinct nodes — the pair $(1,2)$ is equivalent to the pair $(2,1)$.

Help Mihai find the **minimum weight** of a tree obtained by removing some edges from the cactus.

# Input data
The first line of the input file contains two numbers $N$, representing the number of nodes in the graph, and $M$, representing the number of edges in the graph.  
Each of the following $M$ lines contains three numbers $x$, $y$, and $z$, representing an edge with a length of $z$ between nodes $x$ and $y$.

# Output data
The output file will contain a single number, representing the minimum weight of a tree that can be obtained from the initial cactus by removing some edges.

# Constraints and clarifications
- $1 \leq N \leq 100\ 000$
- $N-1 \leq M \leq 200\ 000$
- $0 \leq z \leq 1\ 000\ 000\ 000$
- **It is guaranteed that the answer is at most $10^{18}$**.

|# | Score | Constraints|
| - | - | ------------|
|1|4|The graph is a chain (contains no cycles and each node has a degree of at most 2).|
|2|6|The graph is a tree (contains no cycles).|
|3|12|$1\leq N\leq 15$|
|4|25|$1\leq N\leq 1\ 000$|
|5|38|The graph is a cycle (each node has a degree of 2).|
|6|15|No additional constraints|

# Examples
`cactus.in`
```
6 6
1 2 8
1 3 2
3 2 1
1 4 3
4 5 2
2 6 4
```
`cactus.out`
```
80
```
Edge $(1, 2)$ is removed.
\
`cactus.in`
```
12 14
1 2 7
2 3 3
1 3 7
3 4 2
4 5 5
5 6 10
6 4 3
4 7 4
7 8 2
8 9 5
9 10 8
10 11 1
11 7 9
10 12 3
```
`cactus.out`
```
787
```
Edges $(1, 2)$, $(5, 6)$, $(9, 10)$ are removed.