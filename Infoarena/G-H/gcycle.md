# Graph Cycle

This is an easy problem. Given a directed graph $G = (V, E)$, determine if there is a cycle in this graph.

## Input data

The file `gcycle.in` will contain on the first line $N$ and $M$ representing the number of nodes and the number of edges in the graph, respectively. The following lines will contain two numbers $x$ and $y$, indicating that there is an edge from node $x$ to node $y$.

## Output data

The file `gcycle.out` will contain on the first line $X$ representing the number of nodes that make up the cycle. On the next line it will contain $X$ numbers, separated by a space, representing the nodes that make up the cycle. The first and last node must be the same. If the graph does not contain any cycles, the value $0$ will be printed.

## Constraints and clarifications

$1 \leq N \leq 50\,000$

$1 \leq M \leq 150\,000$

If the graph contains multiple cycles, you may print any one of them.

## Example

`gcycle.in`
```
4 5
1 2
2 3
1 3
3 1
3 4
```

`gcycle.out`
```
2
3 1
```

## Example

`gcycle.in`
```
4 4
1 2
2 3
1 3
3 4
```

`gcycle.out`
```
0
```

## Explanation

For the first example, the graph contains the cycle: $1 \rightarrow 2 \rightarrow 3 \rightarrow 1$

For the second example, the graph does not contain any cycles.