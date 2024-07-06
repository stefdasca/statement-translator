Tanaka has a tree (a *tri*) with `N` nodes numbered from `1` to `N`. He wants to color the tree nodes in white or black so that the number of (unordered) reciprocated node pairs is maximized. Two nodes are *reciprocated* if and only if both are white and either are directly connected by an edge, or the unique elementary chain between them contains only black nodes.

# Task
Given a tree with `N` nodes, find the maximum number of reciprocated node pairs that can be achieved.

# Input data
The input file `tricolor.in` will contain in the first line a non-zero natural number `T` representing the number of tests. `T` tests will follow, each test describes a tree for which the task needs to be solved. The first line of a test contains a natural number `N` representing the number of nodes in that tree. On the next `N-1` lines, there will be pairs of integers `x y` separated by a space, which indicate the existence of an edge between node `x` and node `y`.

# Output data
The output file `tricolor.out` will contain `T` lines. Each line will contain the solution for one of the tests, in the same order as in the input file.

# Constraints and clarifications
* `1 \leq T \leq 10`
* `1 \leq N \leq 5 000`
* In any test, `1 \leq x, y \leq N, x ≠ y`
* For `5` points, `T = 1` and `N \leq 15`
* For another `10` points, `T = 1` and `N \leq 20`
* For another `5` points, all described trees have exactly `2` leaves and `N \leq 500`
* For another `10` points, for all described trees there exist exactly two nodes of the tree to which all leaves are connected, situated at the ends of an elementary chain, and `N \leq 500`.
* For another `50` points, `N \leq 500`
* For the remaining `20` points, there are no additional restrictions.

# Example

`tricolor.in`
```
2
8
1 2
2 3
2 4
4 5
5 6
6 7
6 8
2
1 2
```

`tricolor.out`
```
7
1
```

Explanation
---
`T=2`, we have two tests in the input file.
In the first test, the tree has `8` nodes and with an optimal coloring, we can achieve a maximum number of `7` reciprocated node pairs.
\
~[enunt_tricolor1.jpg]
~[enunt_tricolor2.jpg]

The reciprocated pairs are: `(1, 3), (1, 4), (3, 4), (4, 5), (5, 7), (5, 8), (7, 8)`
In the second test, the tree has `2` nodes connected by a single edge. It is optimal to color both nodes in white obtaining one pair of reciprocated nodes.