# Queens

Bronzarel has seriously taken up computer science, and with Zaharel's help, he hopes to become a great programmer. Among the first issues he solved was the classic queen problem: given a chess board of size $N \times N$, determine all the ways to place the maximum number of queens on the board such that they do not attack each other (two queens attack each other if they are on the same row, the same column, or the same diagonal). Since the result is computable only for small values of $N$, Bronzarel quickly wrote a program using "backtracking", his favorite method. Seeing him so satisfied with himself, Zaharel told him to write a program that determines just one way to place the queens, but for larger values of $N$. It seems this problem is beyond Bronzarel, as his favorite method is useless this time.

## Task

Write a program in place of Bronzarel that determines one way to place the maximum number of queens on an $N \times N$ chess board.

## Input Data

The first line of the input file dame.in will contain the natural number $N$.

## Output Data

The first line of the output file dame.out will contain the number $Max$, representing the maximum number of queens that can be placed on the board. The following $Max$ lines will contain pairs of natural numbers representing the row and column where a queen will be placed.

## Constraints and clarifications

$1 \leq N \leq 1000$

Rows and columns of the board are numbered from 1 to $N$

For 30$\%$ of the tests $N \leq 25$

and for 60$\%$ of the tests $N \leq 200$

## Example

dame.in
`8`

dame.out
`8`
`1 4`
`2 7`
`3 3`
`4 8`
`5 2`
`6 5`
`7 1`
`8 6`

## Explanations