Miruna found a matrix at the bottom of the sea with `n` rows and `m` columns containing natural numbers. For unknown reasons, Mirunel, Miruna's mysterious friend, wants to know the side length of the largest square submatrix that contains at most `k` distinct numbers. The submatrix with the top-left corner `(xs, ys)` and the bottom-right corner `(xd, yd)` consists of all elements in the matrix with row indices in the interval `[xs, xd]` and column indices in the interval `[ys, yd]`.

# Task
Write a program that determines the maximum side length of a submatrix that meets Mirunel's conditions.

# Input data
The input file `submatrix.in` contains on the first line three natural numbers `n, m`, and `k` separated by a single space, having the significance from the statement. On the next `n` lines, there are `m` natural numbers separated by spaces, representing the elements of the matrix.

# Output data
The output file `submatrix.out` will contain a single line that will print a single natural number representing the side length of a submatrix with the property described in the statement.

# Constraints and clarifications
* `1 \leq n, m \leq 300`
* `1 \leq k \leq n * m`
* For `30\%` of the tests `1 \leq n, m \leq 30`
* For `70\%` of the tests `1 \leq n, m \leq 150`

# Examples

`submatrix.in`
```
5 7 3
6 5 7 3 6 6 7
5 7 5 5 7 3 7
3 3 5 3 5 6 7
7 7 5 5 5 6 7
7 7 6 5 6 3 5		
```

`submatrix.out`
```
3
```

Explanation
---

A solution is the submatrix with the top-left corner at position `(2, 3)` and side length `3`, which contains only the elements `3, 5`, and `7`.