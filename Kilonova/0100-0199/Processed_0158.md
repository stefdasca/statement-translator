# Task
From the `n` participants at the informatics olympiad, `m` pairs of friends can be distinguished. These pairs have some interesting properties:
* if `A` is friends with `B`, then `B` is friends with `A`;
* if $A_1$ is friends with $A_2$, $A_2$ with $A_3$, ..., $A_{k-1}$ with $A_k$ and $A_k$ with $A_1$, then there exists at least one pair `(i, j)`, `1 \leq i, j \leq k`, such that: $A_i$ and $A_j$ are friends and `(i mod k) + 1 \neq j` and `(j mod k) + 1 \neq i`.

A set of 3 friends `A, B` and `C` is called a triangle of friends if `A` is friends with `B`, `B` with `C` and `C` with `A`.

# Task
Find out how many triangles of friends exist.

# Input data
The input file `tric.in` contains, on the first line, the natural numbers `n` and `m` separated by spaces. The following `m` lines contain pairs of numbers `A B`, between `0` and `n - 1`, with the meaning that `A` is friends with `B`.

# Output data
The output file `tric.out` must contain on a single line the number of triangles of friends.

# Constraints and clarifications
* `2 \leq n \leq 100 000`
* `1 \leq m \leq 100 000`
* for `20%` of the tests, `n \leq 300`
* for `50%` of the tests, `n \leq 1000`

# Example

`tric.in` 
```
4 4
0 1
1 2
2 0
2 3
```

`tric.out`
```
1
```