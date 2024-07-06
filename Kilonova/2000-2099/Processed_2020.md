# Task

In the absence of the princess with green eyes, her enchanted realm has been invaded by termites! The enchanted realm is known to be organized as a connected undirected graph, where each edge has an assigned length. The princess cannot combat this invasion, but she has obtained valuable information about these termites. It is known that the invasion started simultaneously from exactly $K$ nodes, at a moment we will denote by $0$. These termites, once they reach a node, instantly eat it, reproduce, and move along the incident edges of the node to the neighboring nodes. Thus, if a termite reaches a node at time $T$, at the same moment the termites will eat it, reproduce, and move towards other nodes. The princess also knows that their travel time is constant and that they traverse an edge of length $L$ in exactly $L$ seconds. Once a node is eaten, it will disappear from the graph, but not necessarily the incident edges (the edge will remain in the graph as long as it is incident to at least one node). In other words, an edge will disappear only when both nodes at its ends are eaten.

The princess cannot save her entire kingdom, but she would like to know if she could save some treasures located in certain nodes of the graph. Thus, she will ask $Q$ questions of the form $A\\ B\\ T$ with the following meaning: knowing that the princess is at node $A$ at moment $T$, and the treasure is at node $B$, how many seconds will pass until there is no longer any path between her and the treasure (this can also happen in cases where node $A$ or node $B$ is eaten). If from moment $T$ there is no path between the two nodes, then $0$ will be printed.

# Task

Help the princess by correctly answering all $Q$ questions.

# Input data

The input file `termite.in` contains on the first line $4$ natural numbers: $n$ – the number of nodes in the graph, $m$ - the number of edges in the graph, $k$ – the number of nodes from which the termites started, and $Q$ – the number of questions. The second line of the file will contain $k$ values, indicating the index of the nodes where the termites appeared at moment $0$. The following $m$ lines will contain $3$ values each: $a, b$ and $L$, indicating that there is an edge of length $L$ between nodes $a$ and $b$. The following $Q$ lines in the input file will represent the queries, in the form $A \\ B \\ T$, indicating how many seconds the princess has from moment $T$ until there is no longer a path between nodes $A$ and $B$.

# Output data

The output file `termite.out` will contain $Q$ lines with a single natural number each, representing the answers to the $Q$ questions.

# Constraints and clarifications

* $1 \leq n, k \leq 300\ 000$
* $1 \leq m, Q \leq 400\ 000$
* The lengths of the edges are natural numbers less than $1\ 000$

# Example

`termite.in`
```
5 6 1 3
5
1 2 3
1 5 3
2 3 2
2 4 1
3 4 1
3 5 2
1 3 1
1 4 3
2 5 1
```

`termite.out`
```
1
0
0
```