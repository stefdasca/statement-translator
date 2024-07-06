Let's consider a matrix with $N$ rows and $N$ columns containing natural numbers. In this matrix, we need to place two rooks in distinct positions. We say that an element of the matrix is attacked if it is on the same row or column as one of the two rooks. The elements in the positions of the two rooks are not considered attacked.

The rooks will be placed in such a way that the sum of the attacked elements is as large as possible.

# Task

Write a program to determine the sum of the attacked elements (maximal possible).

# Input data

The input file `ture.in` will contain on the first line a natural number $N$, as described in the statement. Each of the next $N$ lines will contain $N$ natural numbers, representing the elements of the matrix.

# Output data

The output file `ture.out` will contain a single line that will contain the maximal sum.

# Constraints and clarifications

* $2 \leq N \leq 100$
* The elements of the matrix are natural numbers less than or equal to $255$.

# Example

`ture.in`
```
5 
4 2 2 3 3 
4 2 1 4 0 
1 3 4 0 1 
4 3 0 2 3 
0 0 3 0 4 
```

`ture.out`
```
40
```

## Explanation

The first rook will be placed in position $(4,3)$, and the second rook will be placed in position $(2,5)$.