It is considered a tree (an acyclic connected graph) with `N` vertices, without a fixed root. Any of the vertices can be chosen as the root. Let's assume that vertex `T` has been chosen. Between any vertex and `T` there exists a unique path that contains each vertex of the tree at most once (a path between vertices `i` and `j` is a sequence of vertices that starts with `i`, ends with `j`, and between any two consecutive vertices there exists an edge in the tree). Each vertex `i` (including `T`) must be assigned a value $V_i$, greater than or equal to `0`, such that the sum of the values of the vertices on the path between `i` and the root `T`, divided by `K`, leaves a remainder $R_i$. The cost of the tree with the root fixed in `T`, $C_T$, is defined as the sum of the values associated with each node. Among all possible choices of values $V_i$ that satisfy the previously stated condition, one must choose the one for which $C_T$ is minimal.

It is easily observed that choosing a different vertex as the root, for example, vertex `S` (different from `T`), $C_S$ is not necessarily equal to $C_T$.

# Task
Given a tree with `N` vertices, an integer `K` and the values $R_i, i=1,2,...,N$, corresponding to each vertex, determine those vertices `T` that can be chosen as the root, for which the cost $C_T$ is minimal (i.e., $C_T \leq C_S$, for any `S` different from `T`), as well as the respective cost.

# Input data
The first line of the input file `asmin.in` contains `2` integer values: `N` and `K`. The next `N-1` lines contain two integer numbers `a b`, separated by a space, indicating that there exists an edge between vertices `a` and `b`. The vertices are numbered from `1` to `N`. The next line contains `N` integer numbers, representing the values $R_i, i=1,2,...,N$.

# Output data
The first line of the output file `asmin.out` will contain two integer values: `C` and `M`. `C` represents the minimum possible cost of the tree. `M` represents the number of vertices that can be chosen as the root for which the cost `C` is obtained. The second line contains `M` integer numbers separated by a space, written in ascending order, representing the numbers of the vertices that can be chosen as the root such that the cost `C` is obtained.

# Constraints and clarifications
* `2 \leq N \leq 16\ 000`
* `2 \leq K \leq 1000`
* $0 \leq R_i \leq K-1$
* At least `40%` of the tests used for evaluation will have `N \leq 1000`
 
# Example

`asmin.in`
```
5 3
1 2
1 3
2 4
2 5
0 1 2 1 0
```

`asmin.out`
```
5 2
1 5
```

## Explanations

The two obtained trees (together with the values associated with the vertices) are as follows:
\
~[asmin.png]