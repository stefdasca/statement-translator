## Task

Let $A$ be an array of $N$ distinct natural numbers. We say that $A$ is compact if there exists an interval $[a, b]$ of length $N$ such that all the numbers in $A$ are within this interval. We say that $A$ is supercompact if any prefix of it is compact. For example, the array $[2, 4, 3, 5]$ is compact but not supercompact. The array $[4, 3, 2, 5]$ is supercompact. Given a permutation $P$, determine the length of the longest supercompact subsequence of it. Recall that a subsequence of an array of numbers is obtained by deleting some elements from the original array (possibly none). Thus, $[3, 5, 1]$ is a subsequence of the array $[3, 2, 4, 5, 6, 1]$, but $[3, 4]$ is not a subsequence of the array $[4, 5, 3]$.

## Input data

The input file `compact2.in` will contain on its first line the number $N$, representing the size of $P$. The second line will contain $N$ natural numbers that form a permutation.

## Output data

The output file `compact2.out` will contain exactly one natural number, the length of the longest supercompact subsequence of the permutation $P$.

## Constraints and clarifications

$1 \leq N \leq 1\ 000\ 000$

For 10% of the score, $N \leq 20$

For 30% of the score, $N \leq 1000$

## Example

`compact2.in`
```
5
4 2 5 1 3
```

`compact2.out`
```
3
```