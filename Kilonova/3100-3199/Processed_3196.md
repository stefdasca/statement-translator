# Task

We have a tree with $N$ nodes, where each node contains a natural number, and the values found in the nodes form a permutation of the set $\{1,2,\dots,N\}$.

This tree has its root at node $1$ and is special in that each node has at most $4$ children.

The following process is defined:

* Initialize an empty sequence.
* Place a pawn on node $1$, marking it as visited. Add the value of node $1$ to the sequence.
* As long as there are unvisited nodes, move the pawn to a neighboring node of your choice from the node it is currently on, even if it has been visited before.
* If the node where the pawn has arrived has not been visited, mark it as visited and add the node's value to the sequence.
* The pawn can only move to a node that has already been visited if all nodes in the subtree of its current position have been visited.

It is noted that after this process, the sequence we are left with will be a permutation. For how many processes will the resultant sequence be a permutation with an odd number of inversions?

Two processes are considered different if their resultant sequences are different. The answer is calculated modulo $10^9+7$.

# Input data

The first line contains $N$, the number of nodes in the tree. The second line contains $N$ values, the values of the nodes. The following $N-1$ lines contain two values each, representing the endpoints of the tree edges.

# Output data

The first line should contain the number of different traversals resulting in a sequence with an odd number of inversions, modulo $10^9+7$.

# Constraints and clarifications

* $1 \leq N \leq 10^3$
* Each node has at most $4$ children.
* The answer is displayed modulo $10^9+7$.
* For 15 points, $N \leq 18$.
* For another 10 points, $N \leq 100$.
* For another 10 points, each node has at most 2 children.
* For another 25 points, each node has at most 3 children.

# Example 1

`stdin`
```
5
3 1 4 2 5
1 2
1 3
3 4
3 5
```

`stdout`
```
2
```

## Explanation

We can obtain the following sequences from traversals:

- $\{3, 1, 4, 2, 5\}$ — $3$ inversions
- $\{3, 1, 4, 5, 2\}$ — $4$ inversions
- $\{3, 4, 2, 5, 1\}$ — $6$ inversions
- $\{3, 4, 5, 2, 1\}$ — $7$ inversions

We observe that the following sequence is not valid: $\{3, 4, 5, 1, 2\}$.
The pawn would have the following path: $1 \rightarrow 3 \rightarrow 5 \rightarrow 3 \rightarrow 1 \rightarrow 2 \rightarrow 1 \rightarrow 3 \rightarrow 4$.
The pawn is not allowed to move from node $3$ to node $1$ because there are still unvisited nodes in the subtree of node $3$.

# Example 2

`stdin`
```
17
8 12 4 7 3 5 1 17 11 2 6 9 10 14 16 15 13
1 2
1 3
1 4
2 8
2 9
2 10
2 11
4 5
4 6
6 7
10 12
10 13
13 14
13 15
13 16
13 17
```

`stdout`
```
6912
