```markdown
Given `P`, with cartesian coordinates `(a, b, c)`, and `Q`, with cartesian coordinates `(x, y, z)`, two distinct points in three-dimensional space. On the set of points in space, the ordering relation `<` is defined as follows: a point `P` is smaller than a point `Q` (meaning `P<Q`) if one of the following relations is satisfied:
1) `a < x`;
2) `a = x` and `b < y`;
3) `a = x`, `b = y` and `c < z`.

Let `n` be a non-zero natural number and `M` the set of all points in space whose coordinates `(k, i, j)` are natural numbers and satisfy the conditions: $1 \leq k \leq n, 1 \leq i \leq k, 1 \leq j \leq k$. The number of points in the set `M` is $m = 1 + 4 + 9 + ... + n^2$. The points in the ordered set `M` are numbered with distinct numbers `1, 2, ..., m` in the order in which they appear in it.

A non-zero natural value is associated with each point in the ordered set `M`. Thus, the value $c_1$ is associated with the first point $P_1 \in M$, the value $c_2$ is associated with the second point $P_2 \in M$, ..., the value $c_m$ is associated with the `m`-th point $P_m \in M$, and $P_1 < P_2 < ... < P_m$.

Starting from point $P_1` with coordinates `(1, 1, 1)`, paths are constructed so that the successor of a point on the path with cartesian coordinates `(k, i, j)` can be one of the `3` points in `M` whose coordinates are: `(k + 1, i, j + 1), (k + 1, i + 1, j), (k + 1, i + 1, j + 1)`, for `1 \leq k < n`. For example, if `n > 3`, the successor of the point with coordinates `(3, 1, 2)` can be any of the points with coordinates: `(4, 1, 3), (4, 2, 2), (4, 2, 3)`. If `n = 3`, then the point with coordinates `(3, 1, 2)` has no successor.

The path $A_1, A_2, A_3, ..., A_n$ precedes lexicographically the path $B_1, B_2, B_3, ..., B_n$ if there is an index `j` (`1 \leq j \leq n`) such that $A_i = B_i$ (`1 \leq i < j`) and $A_j < B_j$.

# Task
Write a program that reads the non-zero natural number `n` and the `m` non-zero natural numbers $c_1, c_2, ..., c_m$ and then determines and prints the maximum sum `S` that can be obtained by summing all the values associated with the points on a path constructed as described in the statement, as well as the path for which the maximum sum is obtained. If there are multiple paths for which the maximum sum is obtained, the first path in lexicographic order will be printed.

# Input data
The input file `drum.in` contains:
On the first line, a non-zero natural number `n`.
The second line contains `m` non-zero natural numbers $c_1, c_2, ..., c_m$, separated by spaces, representing the values associated with the points in the ordered set `M`.

# Output data
The output file `drum.out` will contain:
The first line contains a number representing the maximum sum `S`.
The second line contains a path for which the maximum sum `S` is obtained, writing the number of each point on the path in the order they are traversed, with the numbers separated by a single space.

# Constraints and clarifications
* $1 \leq n \leq 30; 1 \leq c_i < 100, 1 \leq i \leq m$
* Points with coordinates `(n, i, j)` have no successors `(1 \leq i \leq n, 1 \leq j \leq n)`
* For the correct maximum sum `S`, 60% of the points are awarded; for a path for which the maximum sum `S` is obtained, 20% of the points are awarded, and for the first path in lexicographic order for which the maximum sum `S` is obtained, 40% of the points are awarded.

# Example

`drum.in`
```
3
3 6 5 7 2 4 5 8 7 6 1 7 8 13
```

`drum.out`
```
18
1 4 13
```

There are `14` points in the set `M`. The maximum sum that can be obtained is `18`, a value that will be written on the first line of the file `drum.out`. There are `2` paths for which the maximum sum is obtained: $(P_1, P_4, P_{13})$ and $(P_1, P_5, P_{14})$. The first path being the smallest (lexicographically) will write on the second line of the file `drum.out` the numbers `1 4 13`, obtaining the maximum points.
```