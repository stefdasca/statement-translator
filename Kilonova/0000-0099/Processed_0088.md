Here is the translated text:

---

Let `A` be a rectangular matrix of integers with `N` rows numbered from `1` to `N` and `M` columns numbered from `1` to `M`. In the matrix `A`, any two consecutive elements in the same row are distinct.

A valid sequence of integers is defined as either an increasing sequence, a decreasing sequence, an increasing sequence concatenated with a decreasing sequence, or a decreasing sequence concatenated with an increasing sequence. Examples of valid sequences are: `1 2 3 7`, `8 5 2 1`, `3 5 6 2`, `4 1 5 6`.

A submatrix of $A$ with coordinates ($l_1, c_1, l_2, c_2$) is defined as the matrix formed by all elements `A(i,j)`, with $l_1 \\leq i \\leq l_2$ and $c_1 \\leq j \\leq c_2$.

A submatrix of `A` is valid if its rows are valid sequences.

**Attention!** A valid submatrix can have an increasing sequence of numbers on one row, a decreasing sequence on another, an increasing sequence concatenated with a decreasing sequence on the next, etc. Therefore, the rows of a valid submatrix do not necessarily have to be sequences of the same type.

The area of a submatrix is equal to the number of elements that form the submatrix.

# Task
Find a valid submatrix of `A` with maximum area.

# Input data
The first line of the input file `matrice.in` contains the numbers `N` and `M`, separated by a space.
Each of the following `N` lines contains `M` integers separated by a space, representing the elements of the matrix `A`.

# Output data
The output file `matrice.out` will contain a single line on which the coordinates $l_1, c_1, l_2, c_2$ (in this order and separated by a space) of a valid submatrix with maximum area will be written. In case there are multiple solutions with maximum area, print any of them.

# Constraints and clarifications
* `1 \\leq N, M \\leq 1000`
* `70%` of the tests will have `N, M \\leq 600`
* The elements of the matrix `A` are integers in the range `[-30000, 30000]`.

# Example

`matrice.in`
```
2 6
1 2 5 7 9 10
3 4 3 5 1 10
```
`matrice.out`
```
1 1 2 3
```

Explanations
---
The maximum area is `6`. Another solution with maximum area could be `1 1 1 6`, `1 2 2 4`, `1 3 2 5`, or `1 4 2 6`.

