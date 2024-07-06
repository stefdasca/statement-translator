Consider square matrices with $N$ rows and $N$ columns that store only values $0$ and $1$, and satisfy the following conditions:

* Each row has exactly two values equal to $1$.
* Each column has exactly two values equal to $1$.
* The matrix does not contain four $1$ values that are the corners of a submatrix.

In the examples below, the first matrix meets all three conditions, but the second matrix does not satisfy the third condition:

~[matcnt.png]

# Task
Determine the number of such matrices. Because this number can be very large, the result will be displayed modulo $200 \\ 003$.

# Input data

The input file `matcnt.in` will contain the natural number $N$.

# Output data

The output file `matcnt.out` will contain on the first line a natural number representing the number of matrices, modulo $200 \\ 003$.

# Constraints and clarifications

* $3 \\leq N \\leq 100 \\ 000$
* For $30\\%$ of the tests, $N \\leq 50$
* For another $30\\%$ of the tests, $N \\leq 1 \\ 000$

# Example 1

`matcnt.in`
```
3
```

`matcnt.out`
```
6
```

## Explanation

The $6$ matrices are:

```
011 011 101 101 110 110
101 110 011 110 011 101
110 101 110 011 101 011
```