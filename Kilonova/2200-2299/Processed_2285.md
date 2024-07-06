Here is your translated text:

```
Given a tree with $N$ nodes, numbered from $1$ to $N$, where each node has an associated color. Each color is represented by a number from the set $\{1, 2, \dots, N\}$. We define a component as a set of nodes that form a connected region (non-empty connected subgraph of the tree) in the tree and for which any two nodes in the set have the same color. This set does not have to be necessarily maximal.

# Task

Determine the number of distinct ways to partition all the nodes of the tree into at most $K$ disjoint components. Since this number can be very large, find the remainder when the number is divided by $10^9 + 9$.

Two ways, $M_{1}$ and $M_{2}$ are considered distinct if there are two nodes $u$ and $v$ ($1 \leq u, v \leq N$) that are part of the same component in $M_{1}$ and not part of the same component in $M_{2}$.

# Input data

The first line will contain the numbers $N$ and $K$. The second line will contain $N$ positive integers, each less than or equal to $N$. The $i$-th number represents the color of the $i$-th node. 
The next $N-1$ lines each contain a pair of nodes $(u, v)$ indicating that there is an edge between nodes $u$ and $v$ in the tree.

# Output data

Print a single number representing the number of ways to partition the tree into at most $K$ components, modulo $10^9 + 9$.

# Constraints and clarifications

* $1 \leq K \leq N \leq 200\ 000$;
* $1 \leq u, v \leq N$;
* For 9 points, $1 \leq N \leq 15$, $1 \leq K \leq 4$;
* For another 8 points, $K = 2$;
* For another 9 points, $K = 3$;
* For another 19 points, $1 \leq K \leq N \leq 200$;
* For another 18 points, $1 \leq K \leq N \leq 2\ 000$;
* For the remaining 37 points, there are no additional constraints.

# Example

`stdin`
```
5 3
1 1 1 1 2
2 4
1 2
5 4
3 4
```

`stdout`
```
4
```

## Explanation

We can partition the tree into at most $3$ components in $4$ ways. The four ways are:
- $\{5\}$ and $\{1, 2, 4, 3\}$;
- $\{5\}$, $\{1\}$ and $\{2, 4, 3\}$;  
- $\{5\}$, $\{1, 2\}$ and $\{4, 3\}$;  
- $\{5\}$, $\{1, 2, 4\}$ and $\{3\}$.
```