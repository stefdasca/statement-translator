
During the National Informatics Olympiad, Ninel (Gigel's younger brother) received an undirected connected graph `G` with `N` nodes, numbered from `1` to `N`. He wrote down the adjacency list corresponding to each node. Being mischievous, Gigel changed the adjacency list for one or two nodes, thus altering their adjacent nodes. More precisely, if a node has `X` neighbors, Gigel will still write `X` neighbors, but some of them will not match those written initially by Ninel.

# Task
Knowing both the number of changes made by Gigel and the adjacency lists corresponding to each node after Gigel's changes, it is required to find the node or the `2` nodes whose adjacency lists Gigel has altered.

# Input data
The file `incurcatura.in` contains on the first line a single natural number `P`, representing the number of nodes that have been modified. The second line will contain a single natural number `N`, representing the number of nodes in the graph, and on each of the following `N` lines, separated by a space, there are:
- a natural number $K_i$, representing the number of neighbors of node `i`, both before and after the operations;
- $K_i$ distinct natural numbers from the set `{1, 2, …, n}\{i}`, representing the neighbors of node `i` after performing the operations.

# Output data
If $P=1$ the file `incurcatura.out` will contain on the first line the node that was modified.
If $P=2$ the file `incurcatura.out` will contain on the first line the nodes that were modified, in ascending order, separated by a space.

# Constraints and clarifications
* for the input data, the problem always has a solution
* it is guaranteed that for the input data, the solution is unique
* $3 \leq N \leq 10^5$
* $1 \leq K_i \leq N - 1$, for any $i$ from $1$ to $N$
* $K_1 + K_2 + \ldots + K_n \leq 4 \ 10^5$
* $P \in \{1, 2\}$
* For $40\%$ of the tests, $P = 1$

# Example

`incurcatura.in`
```
2
7
4 7 3 2 4
2 6 1
4 7 6 4 1
4 1 3 5 6
2 4 1
3 7 5 1
1 3
```

`incurcatura.out` 
```
1 6 
```

Explanations
---
Gigel altered the adjacency lists corresponding to nodes `1` and `6`.
