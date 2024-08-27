# Snake

We have a matrix with 2 rows and $N$ columns. We aim to fill this matrix with numbers from $1$ to $2N$ such that the number $i$ is adjacent to the number $i+1$ for any $1 \leq i < 2N$.

## Task

Given the number $N$ calculate the number of ways to fill the matrix.

## Input data

The file `sarpe.in` contains on the first line the number $N$.

## Output data

The file `sarpe.out` will contain on the first line the number of ways to fill the matrix.

## Constraints and clarifications

$1 \leq N \leq 10$

Two elements in the matrix are adjacent if and only if they are on the same row and in consecutive columns, or in the same column and in consecutive rows.

## Example

`sarpe.in`
```
2
```

`sarpe.out`
```
8
```

## Explanation

1 2 $\dots$  
4 3