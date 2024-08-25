# Orient

A directed graph with $N$ nodes and $M$ edges is given. Each edge is associated with a cost, called the reorientation cost. Reorienting an edge means that if there is an edge $(a, b)$ in the graph (i.e., an edge from node $a$ to node $b$), the edge is removed and replaced with an edge $(b, a)$ (from node $b$ to node $a$), and the operation costs the reorientation cost of the respective edge. In addition, a cycle in a graph is defined as a sequence of nodes $(v_1, v_2, \dots, v_k)$, with the property that for any $i \leq k-1$ there exists an edge from node $v_i$ to node $v_{i+1}$ in the graph, and also an edge from node $v_k$ to node $v_1$. 

## Task

Reorient a number of edges in the given graph so that it contains at least one cycle, while minimizing the total cost of all operations. It is guaranteed that there are some edges (possibly $0$) that can be reoriented to form a cycle.

## Input data

The input file `orient.in` contains on the first line two natural numbers $N$ and $M$, separated by a space, representing the number of nodes and the number of edges in the graph, respectively. The next $M$ lines each contain three natural numbers $a$, $b$, and $c$, with $a$ different from $b$, separated by spaces. There is an edge oriented from node $a$ to node $b$ in the graph, with the reorientation cost equal to $c$.

## Output data

The output file `orient.out` will contain on the first line a single natural number, representing the minimum cost obtained by convenient reorientation of some edges, so that the graph contains at least one cycle.

## Constraints and clarifications

$2 \leq N \leq 1000$ 

$2 \leq M \leq 3000$ 

$1 \leq$ the cost of an edge $\leq 5000$

Between two nodes $a$ and $b$ in the graph there is at most one edge (regardless of its orientation).

If the graph already contains a cycle, the answer to the problem will be $0$. 

A cycle does not necessarily have to contain all $N$ nodes of the graph. 

A cycle can contain a minimum of $2$ nodes.

## Example

`orient.in` 

```
5 5
1 2 2
3 2 10
3 4 3
4 1 1
4 5 4
```

`orient.out` 

```
6
```

## Explanation

We can reorient the edges $(4, 1)$, $(3, 4)$, and $(1, 2)$, obtaining a cost equal to $1 + 3 + 2 = 6$, and the cycle $(1, 2, 3, 4)$. 

Another option would have been to reorient the edge $(3, 2)$, but this would have resulted in a higher cost: $10$.