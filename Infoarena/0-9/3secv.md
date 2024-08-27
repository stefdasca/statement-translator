## Task

You are given a number $N$ and an array of $N$ natural numbers. The cost of a subarray is defined as the sum of the elements in the subarray. You need to find 2 positions $P1$ and $P2$ $( P1 < P2 )$ such that the following property is met: Let $A1$ be the cost of the subarray $(1, P1)$, $A2$ be the cost of the subarray $(P1 + 1, P2)$, and $A3$ be the cost of the subarray $(P2 + 1, n)$. You need to choose $P1$ and $P2$ so that the difference between $max(A1, A2, A3)$ and $min(A1, A2, A3)$ is as small as possible. $max(a, b, c)$ represents the maximum value among $a, b$, and $c$, and $min(a, b, c)$ represents the minimum value.

## Input data

The input file `3secv.in` will contain on the first line a natural number $N$, and on the second line $N$ natural numbers representing the given array.

## Output data

The output file `3secv.out` will contain 2 numbers $P1$ and $P2$.

## Constraints and clarifications

$5 \leq N \leq 1\ 000\ 000$ 

The values in the array will be in the range $[1, 1\ 000\ 000\ 000]$

If there are multiple positions with the minimum cost, the one with the smallest $P1$ index will be displayed.

In case of a new tie, the one with the smallest $P2$ index will be displayed.

$P1$ must be different from $P2$.

## Example

`3secv.in`
```
7
7 2 1 5 6 2 3
```

`3secv.out`
```
1 4
```