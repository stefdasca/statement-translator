```markdown
A matrix $A$ with $N$ rows and $N$ columns is considered. Its elements belong to the set $\\{0,1,2\\}$. In each row and each column, the values of the elements are arranged in increasing order.

Let there be two elements in the matrix located at row $i_1$ and column $j_1$ and respectively $i_2$ and $j_2$, where $i_1 \\leq i_2$ and $j_1 \\leq j_2$. A submatrix of $A$, having the top-left and bottom-right corners at $(i_1, j_1)$ and $(i_2, j_2)$, is formed by all elements located in the rows between $i_1$ and $i_2$ inclusive, and columns between $j_1$ and $j_2$ inclusive. We call a constant submatrix a submatrix of matrix $A$, having all elements equal.

# Task

Write a program that determines the maximum number $K$ of elements in a constant submatrix of $A$ and the number of constant submatrices formed by $K$ elements.

# Input data

In the `submat.in` file, the first line contains the natural number $N$. The next $N$ lines each contain a pair of natural numbers, separated by a space:

The first number on line $i+1$ in the file represents the ordinal number of the first column on line $i$ in matrix $A$ where the element is equal to $1$. If no element on line $i$ is equal to $1$, this number has the value $0$.
The second number on line $i+1$ in the file represents the ordinal number of the first column on line $i$ in matrix $A$ where the element is equal to $2$. If no element on line $i$ is equal to $2$, this number has the value $0$.

# Output data

The output file `submat.out` will contain on the first line a pair of natural numbers separated by a space, representing, in order, the maximum number of elements in a constant submatrix of $A$ and the number of constant submatrices formed by this maximum number of determined elements.

# Constraints and clarifications

* $1 \\leq N \\leq 5\ 000$
* We consider the rows and columns of the matrix $A$ numbered from $1$ to $N$.

# Example

`submat.in`
```
8
4 0
4 8
4 8
3 7
3 6
3 5
2 3
0 2
```

`submat.out`
```
12 6
```

## Explanation

The matrix corresponding to the input file is:
$ \\begin{pmatrix}  0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 \\\\ 0 & 0 & 0 & 1 & 1 & 1 & 1 & 2 \\\\ 0 & 0 & 0 & 1 & 1 & 1 & 1 & 2 \\\\ 0 & 0 & 1 & 1 & 1 & 1 & 2 & 2 \\\\ 0 & 0 & 1 & 1 & 1 & 2 & 2 & 2 \\\\ 0 & 0 & 1 & 1 & 2 & 2 & 2 & 2 \\\\ 0 & 1 & 2 & 2 & 2 & 2 & 2 & 2 \\\\ 0 & 2 & 2 & 2 & 2 & 2 & 2 & 2 \\end{pmatrix} $

The maximum number of elements in a constant submatrix is $12$. There are $6$ constant submatrices formed by $12$ elements, namely the ones with corners at: $(1,1)$ and $(6,2); (1,4)$ and $(4,6); (1,4)$ and $(3,7); (5,6)$ and $(8,8); (7,3)$ and $(8,8); (6,5)$ and $(8,8)$.
```