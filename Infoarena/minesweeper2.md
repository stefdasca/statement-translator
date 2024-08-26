# Minesweeper 2

Akiyama found a new game. Minesweeper on a $2*N$ board (a board with $2$ rows and $N$ columns). Akiyama knows that in Minesweeper, the cells in the matrix are of $2$ types: with bombs and without. However, this game is a bit different: the cells on the first row do not contain bombs. Akiyama needs to determine how many possible configurations there are for the second row, knowing for certain cells on row $1$ how many bombs they are adjacent to (vertically or diagonally).

## Input data

The input file `minesweeper2.in` will contain on the first line a natural number $N$. The next line will contain $N$ natural numbers, the $i$-th element representing the number of bombs adjacent to the cell on row $1$, column $i$. If this number is not known, the respective position will have the value $-1$.

## Output data

The output file `minesweeper2.out` will contain a single natural number representing the number of possible configurations for row $2$ of the matrix, modulo $666013$.

## Constraints and clarifications

$1 \leq N \leq 300\ 000$

For $20\%$ of the tests, $N \leq 15$

For another $30\%$, all $N$ cells are known (you will not encounter the value $-1$)

## Example

`minesweeper2.in`

$3$
$1$ $-1$ $-1$

`minesweeper2.out`

$4$

## Explanation

There are $4$ possibilities: $011$, $010$, $101$, $100$ (where $0$ denotes a free cell and $1$ denotes a bomb)