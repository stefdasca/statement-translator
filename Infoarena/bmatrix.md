# BMatrix

We consider a binary matrix of size $m \times n$ (the elements of the matrix are $0$ or $1$).

## Task

Determine the maximum area that can be covered by two rectangles containing only elements with the value $0$.

## Input data

The input file `bmatrix.in` contains on the first line two integers $m$ and $n$, separated by a single space, which represent the dimensions of the matrix. Each of the following $m$ lines contains $n$ numbers which can have the values $0$ or $1$ and are not separated by spaces.

## Output data

The output file `bmatrix.out` must contain a single number, which represents the maximum area that can be covered by two rectangles containing only elements with the value $0$.

## Constraints and clarifications

$1 \leq m$

$n \leq 200$

the two rectangles cannot overlap.

## Example

`bmatrix.in`

$6 \quad 8$

$10000000$

$10000000$

$11100011$

$00100011$

$00100011$

$00111111$

`bmatrix.out`

$23$