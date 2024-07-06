# Task

A square matrix $A$ that has $P$ rows and $P$ columns is symmetric if and only if for any indices $i$ and $j$ between $1$ and $P$, we have that $A_{i, j} = A_{j, i}$. Therefore, the matrix in Figure 1 is symmetric, while the one in Figure 2 is not because there is at least one pair of indices (for example $i = 2$ and $j = 3$), for which $A_{i, j}$ is different from $A_{j, i}$.

~[fig.png|align=center|width=32em]

For a given matrix with $M$ rows and $N$ columns, we define the submatrix with vertices $(l_1, c_1)$ and $(l_2, c_2)$, with $1 \\leq l_1 \\leq l_2 \\leq M$ and $1 \\leq c_1 \\leq c_2 \\leq N$, as the array formed from all elements with coordinates $i$ and $j$ such that $l_1 \\leq i \\leq l_2$ and $c_1 \\leq j \\leq c_2$.

# Task

Given a matrix with $M$ rows and $N$ columns in which all elements are natural numbers. Let $L$ be the maximum side length of a symmetric submatrix in this matrix. For each size $i$ between $1$ and $L$, determine how many symmetric submatrices with side $i$ exist in the given matrix.

# Input data

The first line of the file `simetric.in` contains the numbers $M$ and $N$, separated by exactly one space, representing the number of rows, and respectively the number of columns, of the matrix that is read in. Each of the next $M$ lines contains $N$ natural numbers, separated by exactly one space, representing the elements of the matrix.

# Output data

The output file `simetric.out` contains exactly $L$ lines, where $L$ is the maximum side length of a symmetric submatrix in the given matrix. Line $i$ contains the number of symmetric submatrices with side $i$.

# Constraints and clarifications

* $2 \\leq M, N \\leq 400$
* The elements of the matrix are natural numbers ranging between $1$ and $30 \ 000$.

# Example

`simetric.in`
```
4 5
5 1 3 6 9
1 6 2 8 9
3 2 7 5 1
9 8 5 3 8
```

`simetric.out`
```
20
3
2
```

## Explanation

There are $20$ symmetric submatrices with side $1$ (each cell is considered a submatrix), $3$ symmetric submatrices with side $2$ and $2$ with side $3$. The symmetric submatrices with side $3$ are:

$ \\begin{bmatrix}\n5 & 1 & 3 \\\\\n1 & 6 & 2 \\\\\n3 & 2 & 7 \\\\\n\\end{bmatrix}  $ respectively $ \\begin{bmatrix}\n6 & 2 & 8 \\\\\n2 & 7 & 5 \\\\\n8 & 5 & 3 \\\\\n\\end{bmatrix}  $