## Task

You are given an array $P$ of length $N$ with distinct elements from the set $\{1,2,\dots,N\}$. For each position $i$ in array $P$, find the smallest position $j$ such that $P[j] < P[i]$ and $j < i$. If such a position does not exist, consider $-1$ as the solution.

## Input data

The input file `findmin.in` contains on the first line $N$, representing the length of the array, and the second line contains $N$ natural numbers, representing the elements of the array $P$.

## Output data

The output file `findmin.out` will contain on the first line $N$ numbers separated by a single space, where the $i$-th number represents the answer for the $i$-th element in the array.

## Constraints and clarifications

$1 \leq N \leq 10^6$ 

$1 \leq P[i] \leq N$ 

The array $P$ is 1-indexed.

## Example

`findmin.in`

```
7
5 6 7 3 1 4 2
```

`findmin.out`

```
-1 1 1 -1 -1 4 5
```

## Explanation