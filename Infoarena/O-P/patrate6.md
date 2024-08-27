## Task

We define a power-square as being a square with a side length in the form of $2 ^ x$, where $x$ is a natural number. Several such squares are given. The task is to find the power-square of minimum area that can include all the given power-squares. We say that a square can include $N$ other squares if there is a way to place the $N$ squares, on a plane, inside the larger square. The $N$ squares must not intersect each other and must not have portions outside the square that contains them. However, they can have common edges with each other or with the containing square.

## Input data

The input file `patrate6.in` will contain a natural number $N$ on the first line, the number of power-squares. The second line will contain $N$ natural numbers, each number $x$ describing a power-square with a side length of $2 ^ x$.

## Output data

The output file `patrate6.out` will contain on the first line the number $R$, meaning that the power-square with a side length of $2 ^ R$ is the power-square of minimum area that can include all the power-squares described in the input file.

## Constraints and clarifications

$1 \leq N \leq 10 ^ 5$

$0 \leq x \leq 10 ^ 9$

where $2 ^ x$ is the side length of a square

For $60\%$ of the tests

$0 \leq x \leq 10 ^ 6$

## Example

`patrate6.in` 
```
4
1 0 1 2 3
```

`patrate6.out` 
```
3
```

## Explanation