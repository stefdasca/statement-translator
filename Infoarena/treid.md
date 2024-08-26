# ThreeD

A matrix of $N \times M$ integer elements is given. The task is to determine three compact rectangular submatrices, which do not overlap and for which the sum of the elements is maximal.

## Task

Determine the maximum sum that can be obtained.

## Input data

The input file `treid.in` will contain on the first line the number $N$ of rows and the number $M$ of columns, separated by a space. The following $N$ lines will each contain $M$ integers separated by spaces.

## Output data

The output file `treid.out` will contain the required number.

## Constraints and clarifications

$1 \leq N$, $M \leq 200$

The elements of the array will be between $-1000$ and $1000$ inclusive.

## Example

`treid.in`
```
5 4 
2 -1 1 1 
-1 -1 -1 -1 
1 -1 -1 -1 
1 -1 -1 -1 
-1 -1 1 1
```

`treid.out`
```
7
```

## Explanation

One possible solution would be a matrix formed of all the elements of the first row, one formed of the elements $(3, 1)$ and $(4, 1)$, and the third matrix will be formed of the elements $(5, 3)$ and $(5, 4)$.