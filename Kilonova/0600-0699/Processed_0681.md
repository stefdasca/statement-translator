
Passionate about tree problems, Petrică found the following problem: Given a tree with $N$ nodes and **even** costs on the edges.

The distance between two nodes of the tree is equal to the sum of the edge costs on the shortest path between the two nodes.

The value of a tree is defined as the sum of the distances between any $2$ of its nodes.

Petrică has the following operation available, which he can do **once**: choose a path in the tree and halve the cost of all the edges on that path. Help him find the smallest value of a tree obtained after applying the operation.

A path is defined as a sequence of distinct nodes $a_1, a_2, ..., a_K$ (for $K \geq 1$), where there is an edge between $a_i$ and $a_{i+1}$ for any $1 \leq i < K$.

# Input data
The first line contains a positive integer $N$ representing the number of nodes in the tree.

The second line contains $N - 1$ integers $p_2, p_3, ..., p_N$, representing that there is an edge between node $i$ and node $p_i$.

The third line contains $N - 1$ integers $c_2, c_3, ..., c_N$, where $c_i$ represents the cost of the edge between $i$ and $p_i$.

# Output data
Print on the first line an integer representing the minimum value of a tree obtained after applying the operation on the initial tree.

# Constraints and clarifications
* $1 \leq N \leq 10^5$
* $1 \leq p_i < i$ for any $i$ from $2$ to $N$
* $−10^3 \leq c_i \leq 10^3$ for any $i$ from $2$ to $N$
* $c_i$ is even for any $i$ from $2$ to $N$

## Subtask 1 (10 points)
* The tree does not contain any nodes with a degree greater than $2$ (the tree is a path).
## Subtask 2 (25 points)
* $1 \leq N \leq 10^2$
* $0 \leq c_i \leq 10^3$ for any $i$ from $2$ to $N$
## Subtask 3 (15 points)
* $1 \leq N \leq 10^3$
* $0 \leq c_i \leq 10^3$ for any $i$ from $2$ to $N$
## Subtask 4 (20 points)
* $0 \leq c_i \leq 10^3$ for any $i$ from $2$ to $N$
## Subtask 5 (5 points)
* All edge values are equal ($c_i = c_j$ for any $2 \leq i, j \leq N$).
## Subtask 6 (10 points)
* $1 \leq N \leq 10^3$
## Subtask 7 (15 points)
* No additional constraints

# Examples

`stdin`
```
5
1 1 2 1
30 16 38 14
```
`stdout`
```
254
```
`stdin`
```
10
1 1 2 2 3 3 7 7 9
-2 2 -4 4 -6 6 10 2 0
```
`stdout`
```
77
```
```
