## Task

Consider a communication network consisting of $N$ nodes numbered from $1$ to $N$. The nodes are interconnected in such a way that the network has a tree structure rooted at node $1$. Node $1$ wants to send a message (the same message) to every leaf node in the tree (i.e., it has no children) - this operation is known as multicast. A message can be transmitted only from a node to one of its descendants (including the node itself). Each edge of the tree has an associated cost, and the cost of transmitting a message from a node $X$ to one of its descendants is the sum of the costs of the edges on the unique path from $X$ to $Y$ (if $X = Y$, then the cost is $0$). The total cost of a multicast strategy is equal to the sum of the costs of transmitting each message.

To achieve its goal, node $1$ will use the following multicast strategy:

The strategy consists of $K$ intermediate rounds. In the first round, node $1$ sends an individual message to a subset of nodes $S 1$, such that every leaf node in the tree is a descendant of exactly one node $X$ from $S 1$ (this means that any node $X$ from $S 1$ is not a descendant of any other node $Y$ from $S 1$). In round $i$ $(2 \leq i \leq K)$, each node $X$ from $S i-1$ sends an individual message to a subset of nodes $S i,X$ from its subtree, such that each leaf node that is a descendant of $X$ is a descendant of exactly one node from $S i,X$. The subset of nodes $S i$ is the union of the sets $S i,X$, for each $X$ from $S i-1$. In the end, each node $X$ from $S K$ must send an individual message to each leaf node that is a descendant of $X$.

Given the communication network, the cost of each edge, and the number of intermediate rounds $K$, determine the minimum total cost of a multicast strategy.

## Input data

The first line of the input file `irmcast.in` contains the integer $T$, representing the number of tests to follow. The first line of each test contains 2 integers, separated by a space, $N$ and $K$. The next $N-1$ lines contain 3 integers each: $A$, $B$, and $C$, meaning that node $B$ is a child of node $A$, and the edge $(A,B)$ has a cost of $C$.

## Output data

For each of the $T$ tests given in the input file, print to the output file `irmcast.out` a line containing the minimum total cost of a multicast strategy having the specified properties.

## Constraints

$1 \leq T \leq 21$

$1 \leq N \leq 333$

$1 \leq K \leq 10$

$1 \leq$ cost of any edge $\leq 10\ 000$

## Example

`irmcast.in`

```
1
6 1
1 2 10
1 3 11
2 4 21
2 5 17
3 6 7
```

`irmcast.out`

```
66
```

## Explanation

In the first (and only) intermediate round, node $1$ sends messages to node $6$ (at a cost of $18$) and to node $2$ (at a cost of $10$). The set $S 1$ is $\{2,6\}$. In the end, node $6$ will send a message to itself (at a cost of $0$), and node $2$ will send messages to node $4$ (at a cost of $21$) and to node $5$ (at a cost of $17$). The total cost is $18+10+21+17=66$.