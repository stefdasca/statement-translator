# Queens

On a triangular board with side length $N$, you must place as many queens as possible so that they do not attack each other. A triangular board with side length $N$ has $N$ rows. On row $i$, there are $i$ positions where queens can be placed, and the positions are arranged in a triangular shape, as shown in the image below. Due to the special nature of this board, the queens are also special in the sense that they can move (attack) in $6$ directions. In the above figure, a $6$-sided board is shown, with a queen on row $5$, column $4$. Row and column numbering starts from $1$ (from the top of the board down for rows and from left to right for columns).

## Task

Determine the maximum number of queens that can be placed on a board of size $N$ and a possible placement of them (any of the solutions with the maximum number).

## Input data

The first line of the file contains a natural number $N$, representing the size of the board.

## Output data

The file will contain on the first line a single integer, $X$, representing the maximum number of queens that can be placed. On the next $X$ lines, $2$ numbers separated by a single space will be printed, representing the row and column of the queens.

## Constraints and clarifications

$1 < N < 1\ 001$

If a test has the correct number of queens, but the configuration of the queens is not valid, $30\%$ of the test score is awarded.

## Example

`regine.in` 
```
3
```
`regine.out` 
```
2
2 1
3 3
```

## Explanations

We can place a maximum of $2$ queens: one on row $2$, column $1$ and one on row $3$, column $3$.