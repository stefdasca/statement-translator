## Task

Upon learning of Rick's intention to transform into a turkey for Thanksgiving in order to avoid being labeled as a terrorist, President Curtis decides to send an army of turkeys after him. The President's residence is located in city number $1$, while Rick is in city $N$. The cities are connected by $M$ one-way streets of varying lengths. The turkeys start at node $1$ and want to reach Rick, which is in node $N$, by taking the shortest path. Rick has the option to increase the lengths of the edges to slow down the turkey army, but at a certain cost. Specifically, the cost to increase edge $i$ by $j$ units is $A[i][j]$. To buy time, Rick wants to increase the edges of the graph so that the length of the shortest path from $1$ to $N$ is $K$ units longer than it was initially. Additionally, we know that $A[i][j-1] - A[i][j-2] \leq A[i][j] - A[i][j-1]$. Help Rick find the minimum cost for the length of the shortest path from $1$ to $N$ to be at least $K$ units longer than it was initially.

## Input data

The input file `curcani.in` contains on the first line the numbers $N$, $M$ and $K$ representing the number of nodes, the number of edges, and the value by which the length of the shortest path must be increased. On line $i + 1$ $(1 \leq i \leq M)$, there are $x$, $y$, $z$ separated by a space, representing an oriented edge from $x$ to $y$ of length $z$. Next, there are $M$ lines with $K$ numbers each representing the edge enlargement costs. The $j$-th element on line $M + 1 + i$ represents the cost to increase the length of edge $i$ by $j$ units. $(1 \leq i \leq M, 1 \leq j \leq K)$ 

## Output data

The output file `curcani.out` will contain a single value representing the minimum cost required. 

## Constraints and clarifications

$1 \leq K \leq 5$

$1 \leq N \leq 250$

$1 \leq M \leq 1000$

The graph is guaranteed to be acyclic and there is at least one path from $1$ to $N$.

$0 \leq A[i][j] \leq 10^9$

$A[i][j-1] \leq A[i][j]$

Edges have an initial length $\leq 10^9$

There could be multiple edges between the same pair of nodes

### Subtasks

Subtask 1 (10 points): $N \leq 8 ; K \leq 2 ; M \leq 12$

Subtask 2 (20 points): The graph comprises multiple independent chains from $1$ to $N$.

Subtask 3 (20 points): Nodes from $1$ to $N-1$ form a tree, and all its leaves are connected to node $N$. 

Subtask 4 (20 points): $K = 1$.

Subtask 5 (30 points): initial constraints.

## Example

`curcani.in`
```
5 7 1
1 2 4
1 5 4
2 3 1
2 4 2
3 5 3
4 5 2
1 1 3
3 4 2
4 2 6
13 2 1 3
103 1 3 104 1 5
113 3 2 7
2 4 14 2 5 4 2 6 20
5 4 12
5 4 11
4 6 7
4 6 7
4 6 6
12 35 12 35 12 34
11 32 11 32 11 33
11 33 12 36
11 32 12 35 12 36
12 36 11 33 45 
```

`curcani.out`
```
100
```

## Explanation

For the first example, the first $2$ edges need to be incremented by one unit each.

For the second example, you will have to take our word for it.