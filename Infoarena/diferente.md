## Task

Tanaka, a fan of matrices with strange properties (such as magic squares, antimagic squares, or Latin squares), has found a new type of matrix: $N-K$-different matrices. An $N-K$-different matrix is any binary matrix with $N$ rows and columns where each pair of adjacent rows (and respectively columns) differ in exactly $K$ positions. It is considered that the first and last row (respectively the column) of a matrix are adjacent. Given two numbers $N$ and $K$, generate an $N-K$-different matrix, or determine that it does not exist.

## Input data

The input file `differente.in` will contain the numbers $N$ and $K$.

## Output data

The output file `diferente.out` will contain:
- if there is no solution, the word `impossible`
- if there is a solution, any $N-K$-different matrix, with elements of a row not separated by spaces.

## Constraints

$K \leq N$

$N \leq 1000$

For 5 points, $K = 2$

For another 5 points, $K = N$

For another 10 points, $K \leq N \leq 4$

For another 40 points, $K$ is even

## Examples

`diferente.in` 

`4 2`

`diferente.out`

`1101`

`0111`

`1101`

`0111`

`diferente.in`

`2 1`

`diferente.out`

`01`

`00`

`diferente.in`

`1 1`

`diferente.out`

`impossible`