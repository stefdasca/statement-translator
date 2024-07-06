```markdown
A matrix $A$ is considered with the following properties:
- contains $n$ rows and $m$ columns;
- contains only the values $0$ and $1$;
- in each row, the values are placed in ascending order.

We define a submatrix determined by the pair of rows $L1$ and $L2 (L1 \leq L2)$ and the pair of columns $C1$ and $C2 (C1 \leq C2)$ as being all elements of the matrix $A_{i, j}$ for which $L1 \leq i \leq L2$ and $C1 \leq j \leq C2$. If all the elements of a submatrix are equal to $0$, then the submatrix is called null.
On the matrix $A$, we can perform one or more row swap operations. Through such swaps, the rows of the matrix can be rearranged such that the matrix $A$ contains at least one null submatrix with the maximum number of elements.

# Task

Given such a matrix, you need to determine the maximum number of zeros in a null submatrix that can be obtained by rearranging the rows of the given matrix.

# Input data

The input file `submat.in` contains in the first line two natural numbers $n, m$, separated by a space, representing the number of rows and the number of columns of the matrix $A$, respectively. The following $n$ lines of the file describe the $n$ rows of the matrix $A$. On each of the $n$ lines, there will be written $m$ values from the set ${0, 1}$, separated by spaces, representing in order the elements of the respective row.

# Output data

The output file `submat.out` will contain a single line which will contain a natural number representing the maximum number of elements that a null submatrix obtained after rearranging the rows of matrix $A$ contains.

# Constraints and clarifications

* $2 \leq n, m \leq 1\ 000$
* For 60\% of the tests $n, m \leq 100$.

# Example 1

`submat.in`
```
3 5
0 0 0 1 1
0 1 1 1 1
0 0 0 0 1
```

`submat.out`
```
6
```

## Explanation

If we rearrange the rows such that the resulting matrix is the following:
$ \begin{pmatrix} 0 & 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & 1 & 1 & 1 & 1 \end{pmatrix} $
then we observe that the submatrix determined by the first and second row and the first and third column contains $6$ values of $0$ ($6$ being the maximum possible number)
```

I have translated the text while preserving the original format, structure, and terminology as specified. I also double-checked for potential grammar and syntax errors.