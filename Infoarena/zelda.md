## Task

Link, the hero of the legend, must conquer the castle of an evil wizard! He enters a mysterious room, where he sees a complicated mechanism. The mechanism takes the form of a tree with $n$ nodes, where each edge has an integer cost. At various times, the lengths of the tree's edges change. After a few hours of unsuccessful trials, Link realizes that, in order to pass through the room, he will have to calculate the compression cost (defined below) of several chains in the tree.

More specifically, Link has $q$ queries of two types. For each query, either Link observes a change in the length of an edge, or he wants to find out the compression cost of a chain. Can you help Link solve all the queries?

Compression cost: The compression cost of a chain is calculated as follows: all the nodes in the chain are identified, then the sum of the lengths of all chains in the resulting tree is calculated. For example, if we consider a tree with $6$ nodes and edges $(1, 2)$, $(2, 3)$, $(4, 5)$, $(5, 6)$, $(2, 5)$, all with a cost of $1$, and we want to calculate the compression cost of the chain from $1$ to $6$, we first identify all the nodes in the chain $1, 2, 5, 6$, the tree thus becoming one with $3$ vertices, and edges $(4, 1)$, $(1, 3)$. Then, we calculate the sum of the lengths of all chains in the tree. This sum is $4$, since there are $3$ chains with length $0$, $2$ with length $1$, and $1$ with length $2$. Note! The tree does not change after calculating a compression cost.

## Input data

The input file `zelda.in` will contain on the first line the number $n$ as described above, followed by $n - 1$ lines, each containing $3$ numbers $x$ $y$ $z$, indicating that there is an edge between nodes $x$ and $y$ with length $z$. On the next line will be the number $q$, followed by $q$ lines, each having one of the following forms:

- $0$ $x$ $y$ $z$, representing the update operation, indicating that the length of the edge between nodes $x$ and $y$ becomes $z$
- $1$ $x$ $y$, representing the query operation, for which the compression cost of the chain between nodes $x$ and $y$ must be calculated, modulo $1000000007$

## Output data

The output file `zelda.out` will contain a number of lines equal to the number of queries, each line containing the answer to its query.

## Constraints and clarifications

- $2 \leq n \leq 100000$
- $1 \leq q \leq 100000$
- $1 \leq x, y \leq n$, for any edge in the tree
- $0 \leq z \leq 1000000000$, for any update/edge in the tree

For each update operation, it is guaranteed that the edge $x$ $y$ exists in the tree

For $20$ points, $n \leq 100$, $q \leq 200$, and the input does not have update operations

For another $20$ points, the input does not have update operations

## Example

`zelda.in`
```
3
1 2 10
1 3 4
8
1 1 1
1 1 2
1 1 3
1 2 3
0 1 2 2
1 3 3
1 1 2
1 2 3
```

`zelda.out`
```
28
4
10
0
12
4
0
```

## Explanation

In this explanation, length$(i, j)$ is the length of the chain with endpoints in $i$ and $j$. We will ignore chains formed from a single node, as they always have a length equal to $0$.

For the first query, the compression is applied to the chain formed from a single node. Thus, the tree does not change, and its cost is: length$(1, 2) +$ length$(1, 3) +$ length$(2, 3) = 10 + 4 + 14 = 28$.

For the second query, the compression is applied to the chain $1-2$. Thus, the tree will contain a single edge (the one between node $1$ and node $3$ with a cost of $4$), and its cost becomes: length$(1, 3) = 4$.

For the third query, the compression is applied to the chain $1-3$. Thus, the tree will contain a single edge (the one between node $1$ and node $2$ with a cost of $10$), and its cost becomes: length$(1, 2) = 10$.

For the fourth query, the compression is applied to the chain $2-3$. Thus, the tree will be compressed into a single node, and will not have any remaining edges, and its cost becomes $0$.

Next is an update of the edge from $1$ to $2$, whose value becomes $2$.

For the fifth query, the compression is applied to the chain formed from a single node. Thus, the tree does not change, and its cost is: length$(1, 2) +$ length$(1, 3) +$ length$(2, 3) = 2 + 4 + 6 = 12$.

For the sixth query, the compression is applied to the chain $1-2$. Thus, the tree will contain a single edge (the one between node $1$ and node $3$ with a cost of $4$), and its cost becomes: length$(1, 3) = 4$.

For the seventh query, the compression is applied to the chain $2-3$. Thus, the tree will be compressed into a single node, and will not have any remaining edges, and its cost becomes $0$.