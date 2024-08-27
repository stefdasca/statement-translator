## Task

In what more abstract world can you live than in an undirected graph with $N$ nodes and $M$ edges? Unfortunately, this abstraction has not eliminated all worldly problems. The inhabitants of the graph immediately divided into tribes, each of the $N$ nodes being a member of one of the $K$ existing tribes. The inhabitants of the graph are very cautious in their relationships with members of other tribes than the one to which they belong. One way this caution manifests is that an inhabitant of node $X$ who belongs to tribe $T$ will dare to travel to node $Y$, also part of tribe $T$, if and only if there exists a path between $X$ and $Y$ with the property that each intermediate node of the path is either from tribe $T$ or neighbors at least one node from tribe $T$. Such a route is considered safe. We say that two nodes belonging to the same tribe are connected if there is a safe route between them. We define a connected component of tribe $T$ as a maximal subset of nodes that are part of tribe $T$ with the property that any two nodes in the subset are connected, in the newly defined sense. For each of the $K$ tribes, you are asked to display the number of connected components it is partitioned into.

## Input data

The input file `tribes.in` will contain on its first line the values $N$ $M$ $K$, representing the number of nodes in the graph, the number of edges in the graph, and the number of tribes, respectively. This is followed by a line with $N$ values between $1$ and $K$, the $a_i$-th of these values, meaning that the node numbered $i$ belongs to the tribe numbered $X$. This is followed by $M$ lines, each containing a pair of numbers $U$ $V$, indicating that there is an undirected edge between nodes $U$ and $V$ in this graph.

## Output data

The output file `tribes.out` will contain $K$ lines, each containing a single value, the $a_i$-th of these representing the number of connected components tribe number $i$ is partitioned into.

## Constraints and clarifications

$1 \leq K \leq N \leq 100\ 000$

$1 \leq M \leq 150\ 000$

For tests worth $30$ points, the following conditions also hold:

$N \leq 1000$ 
respectively
$M \leq 3\ 000$

Each node has at least one edge.

It is possible that some of the $K$ tribes are empty. For these tribes, the answer is $0$.

This problem has full feedback.

## Example

`tribes.in`
`7 6 3`
`1 2 2 1 1 3 3`
`1 2`
`2 3`
`3 4`
`3 5`
`2 6`
`7 5`

`tribes.out`
`1`
`1`
`2`