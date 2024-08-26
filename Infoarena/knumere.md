## Task

We are given $N$ integers in ascending order. We need to delete $K$ of these numbers such that the maximum difference between any two consecutive remaining numbers is minimized.

## Input data

The input file `knumere.in` contains on the first line the numbers $N$ and $K$, and on the next line the $N$ numbers in ascending order.

## Output data

The output file `knumere.out` will contain the required difference.

## Constraints

All numbers in the input file are in the interval $[-10^9, 10^9]$

$3 \leq N \leq 1\,000\,000$

$1 \leq K \leq N-2$

## Example

`knumere.in`
```
6 2
-1 3 5 11 19 35
```

`knumere.out`
```
6
```