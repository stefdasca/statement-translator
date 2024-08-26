# BestSubarray

Given $3$ natural numbers $N$, $K$, $S$ and an array of $N$ natural numbers. This array must be split into at most $K$ subarrays such that the sum of the costs of the subarrays is minimized. The cost of a subarray is the absolute difference between $S$ and the sum of the elements of the subarray.

## Input data

The input file `secvbest.in` will contain on the first line $3$ natural numbers $N$, $K$ and $S$. The second line will contain $N$ natural numbers representing the given array.

## Output data

The output file `secvbest.out` will contain $K$ values separated by a space. The $i$-th value represents the minimum cost if the array must be split into exactly $i$ subarrays.

## Constraints and clarifications

$1 \leq K \leq N \leq 100\ 000$

$1 \leq K \leq 30$

The values of the array and $S$ will be in the interval $[1, 1\,000\,000\,000]$ 

## Example

`secvbest.in`
```
5 3 10 
5 5 2 9 8
```

`secvbest.out`
```
19 9 3
```
