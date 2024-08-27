## Task

Akane has some interesting ideas about matrices: She only cares about matrices whose values are taken from the set $\{a, b, c, d, e\}$. She considers a matrix $A$ to be lexicographically smaller than a matrix $B$ if and only if the string formed by concatenating the rows of $A$ is lexicographically smaller than the string formed by concatenating the rows of $B$. Her favorite matrices are called Akanic matrices. A matrix is Akanic if and only if:
- Any continuous submatrix of 2 rows and 2 columns contains distinct elements.
- Any two continuous submatrices of 2 rows and 2 columns that have at least one common position contain different sets of values.

Akane’s favorite object is a sheet of paper on which $T$ Akanic matrices are written, which in total do not contain more than $1\ 000\ 000$ characters. Her colleague Tanaka has hidden this sheet and refuses to return it. Akane remembers the dimensions of each matrix on the sheet, as well as the number of Akanic matrices of the same dimension that are lexicographically smaller than each respective matrix. Can you help her recover the values of the matrices?

## Input data

The input file `akanemat.in` contains on the first line the number $T$. There will follow $T$ lines, and each line will contain 3 integers $N$, $M$, $K$, where $N$ and $M$ represent the dimensions of a matrix on the sheet, and $K$ represents the number of matrices of the same dimension that are lexicographically smaller than the matrix on the sheet.

## Output data

In the output file `akanemat.out`, print the $T$ required matrices, in the order from the input file. If the required matrix does not exist, print $-1$.

## Constraints

$1 \leq T \leq 100\ 000$

$3 \leq N, M \leq 1\ 000\ 000$

$0 \leq K \leq 1\ 000\ 000\ 000$

## Example

`akanemat.in`
```
1 3 3 1
```

`akanemat.out`
```
abc
ced
dab
```