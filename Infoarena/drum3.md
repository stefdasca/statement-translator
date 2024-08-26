## Drum3

Tamara has a square board with $N$ columns and $N$ rows, and a pawn in the top-left corner of the board that can only be moved to the right or downwards. Tamara wonders through how many possible paths can she move the pawn to the bottom-right corner of the board making exactly $K$ direction changes? A direction change represents switching the pawn's movement direction from downwards to right or from right to downwards. Initially, the pawn can move in any direction (downwards or right).

## Example:

$1 \ 2 \ 3 \ 4 \ 5 \ 6 \ 7 \ 8$
`1 x x S o o o o o`
`2 o o x o o o o o `
`3 o o x o o o o o `
`4 o o S x x S o o `
`5 o o o o o x o o `
`6 o o o o o x o o `
`7 o o o o o S x S `
`8 o o o o o o o x`

A path with $5$ direction changes on an $8×8$ board. Direction changes are marked with $S$.

## Input data

The input file `drum3.in` will contain on the first line the numbers $N$ and $K$ representing the size of the board and the number of direction changes, respectively.

## Output data

In the output file `drum3.out` you will print a single number $R$, representing the number of possible paths of the pawn modulo $30013$.

## Constraints 

$3 \leq N \leq 5 \ 000$

$1 \leq K < 2 \cdot (N-1)$

## Example

`drum3.in`
```
4 2
4
4 3
8
5 3
18
```