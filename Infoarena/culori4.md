## Task

You are given a natural number $N$ and a matrix with $N$ rows and $N$ columns. Each element in the matrix is either $1$, $2$, $3$, $4$, $5$ or $?$. You are asked to determine in how many ways the elements $?$ can be filled with values from $1$ to $5$ such that the matrix does NOT contain two adjacent elements of the same value.

## Input data

The input file `culori4.in` will contain a single natural number $N$ on the first line. The next $N$ lines will contain $N$ characters from the set $\{1, 2, 3, 4, 5, ?\}$.

## Output data

The output file `culori4.out` must contain a single natural number representing the number of ways the elements $?$ can be filled with values from $1$ to $5$ so that the matrix does not have $2$ adjacent elements with the same value.

## Constraints and clarifications

$1 \leq N \leq 10$

The number of $?$ in the matrix $\leq 18$

## Example

`culori4.in` 

`2` 

`2?` 

`3?`

`culori4.out`

`13` 

## Explanation

The $13$ solutions are

$21$ $21$ $21$ $23$ $23$ $23$ $23$ $24$ $24$ $24$ $25$ $25$ $25$

$32$ $34$ $35$ $31$ $32$ $34$ $35$ $31$ $32$ $35$ $31$ $32$ $34$