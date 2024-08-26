## Task

HM has a matrix of $N \times N$ elements and an array of $M$ distinct elements. He wants to fit the array over the matrix as if it were a snake: he chooses a position $ (x, y) $ for the beginning of the array and then fits the remaining elements by moving to any of the eight adjacent elements of the current position (of course without going outside the matrix). HM would like to know in how many ways he can fit the array over the given matrix. 

## Input data

The input file `sarpe2.in` contains two numbers $N$ and $M$ representing the dimensions of the matrix and the size of the array to be fitted, respectively. The second line of the file contains $M$ distinct elements representing the elements of the array to be fitted. The following $N$ lines, with $N$ elements each, describe the matrix, the $j$-th element on the $i$-th line representing the value at row $i$ and column $j$ of the matrix. 

## Output data

The output file `sarpe2.out` must print the number of ways the array can be fitted over the matrix modulo $666013$. 

## Constraints and clarifications

$1 \leq N \leq 1\ 000$

$1 \leq M \leq 100\ 000$

The array and the matrix contain elements in the interval $ [0, 100\ 000] $ 

## Example

`sarpe2.in`

`4 3`

`1 5 4`

`0 1 5 4`

`1 5 4 3`

`4 7 8 2`

`0 5 4 1`

`sarpe2.out`

`6`