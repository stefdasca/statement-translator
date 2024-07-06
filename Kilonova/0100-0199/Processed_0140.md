```
An `N`-node tree is given, with nodes numbered from `1` to `N`, where each node has an associated value. `M` operations are performed on the tree. Each operation is either of type `Q` - query or `U` - update. Each operation of either type has several subtypes:
* `1 x` The operation is performed on node `x`
* `2 x` The operation is performed on all nodes in the subtree of `x` (the root of the tree is `1`)
* `3 x y` The operation is performed on all nodes in the path connecting nodes `x` and `y`

If the operation is of type `Q`, the sum of the nodes on which the operation is performed will be displayed on a new line. If the operation is of type `U`, a number `z` will also be read at the end, indicating that each node on which the operation is performed becomes equal to `z`.

# Input data
The first line contains the numbers `N` and `M`. The next line contains the values of the nodes from `1` to `N`. The following `N - 1` lines contain the edges of the tree. The next `M` lines contain the operations in the above format.

# Output data
The result of the `Q` type operations will be printed.

# Constraints and clarifications
* `1 \ \leq N, Q \ \leq 200\ 000`
* The values of the nodes will always be positive numbers `\ \leq 1\ 000\ 000\ 000`

# Example

`stdin`
```
11 8
1 2 1 3 1 1 2 1 1 3 1
1 2
1 3
2 4
2 5
4 6
4 9
4 8
3 7
7 10
7 11
Q 2 2
U 3 6 7 4
Q 1 8
Q 1 4
U 1 1 5
Q 3 5 10
U 2 7 2
Q 2 1
```

`stdout`
```
9
1
4
21
30
```

Explanations
---

For example, the operation `U 3 6 7 4` is an update operation of type `3`, meaning that all nodes on the path `6 - 7` become equal to `4`. The operation `Q 2 1` is a query operation in which we are asked to display the sum of all nodes in the subtree of node `1`.
```
