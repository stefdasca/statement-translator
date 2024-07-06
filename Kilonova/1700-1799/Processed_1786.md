```markdown
The communication network of the city of Ploiești consists of $N$ nodes, numbered from $1$ to $N$. There are $N-1$ pairs of nodes with a direct connection (these nodes are called neighbors). A direct connection ensures communication in both directions between connected nodes. The direct connections are built so that any two nodes in the network can communicate (directly, or indirectly through other nodes). At time $0$, node $1$ has a message it wants to send to all other nodes. To achieve this, at any integer time $t$, any node $x$ that has previously received the message (or which received it exactly at time $t$), can send it to a neighbor $y$ of its own who has not yet received the message. Sending the message takes $1$ unit of time – hence, node $y$ will receive the message at time $t+1$. A node can send the message to several of its neighbors, but not simultaneously.

For security reasons, at certain times within the interval $[0, T)$, the communication nodes are checked. For each node $x$ and each time $t \\ (0 \\leq t \\leq T-1)$, it is known whether node $x$ is checked at time $t$. The duration of the check is $1$ unit of time (thus, if node $x$ is checked at time $t$, the check ends at time $t+1$). At each time a node is checked, it cannot send any messages (but it can receive messages from its neighbors).

# Task

Determine the minimum time after which the message can reach all nodes (in case of an optimal distribution strategy of the message).

# Input data

The first line of the input file `tcast.in` contains $2$ integers, separated by a space: $N$ and $T$. The next $N-1$ lines contain two integers $x$ and $y$, separated by a space, indicating that nodes $x$ and $y$ are neighbors in the communication network. The following $N$ lines contain $T$ integers from the set {$0, 1$}. The $t$-th number on the $i$-th of these lines is $1$, if node $i$ is checked at time $t-1$ (and $0$ otherwise).

# Output data

The output file `tcast.out` will contain a single line which will hold the minimum time after which all nodes receive the message, in case of an optimal distribution strategy of the message.

# Constraints and clarifications

* $1 \\leq N \\leq 2 \\ 000$
* $1 \\leq T \\leq 1 \\ 000$
* The time after which all nodes receive the message can be greater than $T$

# Example 1

`tcast.in`
```
6 5
1 2
2 3
3 6
1 4
4 5
1 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 0 0
0 0 0 0 0
```

`tcast.out`
```
5
```

## Explanation

At time $0$ node $1$ is checked and cannot send the message to any neighbor. At time $1$, node $1$ sends the message to node $4$. At time $2$, node $1$ sends the message to node $2$, and node $4$ sends the message to node $5$. At time $3$, node $2$ sends the message to node $3$, and at time $4$ node $3$ sends the message to node $6$. At time $5$, node $6$ is the last node to receive the message.
```