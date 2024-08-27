## Task

A bipartite graph is a graph whose nodes can be partitioned into two sets such that any edge has its endpoints in distinct sets. In this problem, we consider the graph is already partitioned, with both sets having nodes numbered from $1$ to $N$. Consider a such bipartite graph with $2 * N$ nodes where each node has a degree of $3$ (it is connected to other $3$ nodes). The Great Wise One gives you the following task. You need to orient the graph's edges and assign natural costs within the interval $[1, 3]$ such that for any node, the sum of the costs of the edges entering the node is equal to the sum of the costs of the edges leaving the node. Any solution is accepted.

## Input data

The input file `circulatie.in` will contain on the first line the natural number $N$ representing the number of nodes in the graph. The following $3 * N$ lines will contain $2$ natural numbers $a$ and $b$ each, representing the existence of an edge from node $a$ in the first set to node $b$ in the second set.

## Output data

The output file `circulatie.out` will contain $3 * N$ lines of the form $a \ b \ c$, signifying that the edge $a - b$ (where $a$ is from the first set and $b$ is from the second set) will have the cost $c$. If the edge orientation is $a \rightarrow b$, $c$ will be positive. Otherwise, $c$ will be negative.

## Constraints and clarifications

$3 \leq N \leq 10^5$

## Example

`circulatie.in`

```
3
1 1
1 2
2 3
3 1
2 2
1 3
```

`circulatie.out`

```
1 1 3
1 2 -1
2 3 -2
3 1 3
2 2 1
1 3 -3
```