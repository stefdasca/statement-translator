## Task

Consider the following grid: $1 \, 1 \, 1 \, 1 \, 1$ $1 \, 2 \, 2 \, 2 \, 2 \, \dots$ $1 \, 2 \, 3 \, 3 \, 3$ $1 \, 2 \, 3 \, 4 \, 4 \, \dots$ $1 \, 2 \, 3 \, 4 \, 5$ $\dots$ $\dots$ $\dots$ $\dots$ The grid extends infinitely to the right and downwards with consecutive natural numbers - diagonally. Given a positive natural number $N$. Determine in the grid a square with sides parallel to the axes; of length equal to $N$ which has the sum of the smallest elements. Print this sum.

## Input data

The input file `quadratum.in` contains on the first line the number of tests $T$ and then on the next $T$ lines different values $N$.

## Output data

For each test print the minimum sum of the elements included in a square from the grid which has side $N$ in the file `quadratum.out`, each on a separate line.

## Constraints

$1 \leq T \leq 20$

$1 \leq N < 10$

$10$

## Example

`quadratum.in`

`
2

1

3 
`

`quadratum.out`

`
1

14 
`

## Explanation

$\dots$