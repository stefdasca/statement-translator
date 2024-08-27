# Noname 3

You are given $2$ numbers $N$ and $S$. Display an array that meets the following properties:
- The array contains $N$ positive non-zero integer elements
- The sum of the elements is $S$
- The elements of the array are distinct
- The absolute difference between the largest and smallest element in the array is minimal
- If there are multiple solutions where the absolute difference between the largest and smallest element is minimal, the lexicographically smallest solution will be displayed.

## Input data

The input file `noname3.in` will contain $2$ numbers $N$ and $S$.

## Output data

The output file `noname3.out` will contain $N$ numbers representing the elements of the array.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

$1 \leq S \leq 1\ 000\ 000\ 000$

If there is no solution, print $-1$.

An array $A$ is minimal lexicographically if there is no other array $B$ and a position $P$, such that $A_i == B_i$ for any $i$ from $1$ to $P - 1$ and $A_P < B_P$.

## Example

`noname3.in`

$3\ 10$

`noname3.out`

$2\ 3\ 5$