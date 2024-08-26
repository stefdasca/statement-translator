## Task

A permutation of $N$ elements is given. You need to sort the permutation with a minimum cost, using the following operation: you can swap any two adjacent elements, with the cost of the operation being the minimum of those two elements. For example, if the permutation is $3 1 2$, you would swap $1$ and $3$ with a cost of $1$, then swap $3$ and $2$ with a cost of $2$.

## Input data

The input file `costperm.in` contains on the first line the natural number $N$. The second line contains $N$ natural numbers representing the given permutation.

## Output data

In the output file `costperm.out` you need to print the minimum cost to sort the permutation.

## Constraints

$1 \leq N \leq 100\ 000$

For tests worth $30$ points, $N$ will be at most $5\ 000$

## Example

`costperm.in`

$3$

$3 1 2$

`costperm.out`

$3$