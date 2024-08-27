## Task

Given two arrays of numbers $A$ and $B$, each containing distinct values, find the shortest array that includes both $A$ and $B$ as subsequences. Among solutions with the minimum length, find the lexicographically smallest one.

## Input data

The input file `compunere.in` will contain on the first line the numbers $N$ and $M$, the lengths of the two arrays. The second line will contain the array $A$ and the third line the array $B$.

## Output data

The output file `compunere.out` will contain on the first line $LEN$, the length of the answer. The second line will contain $LEN$ values describing the solution array.

## Constraints and clarifications

$1 \leq N, M \leq 100\ 000$

$-10^9 \leq A[i], B[i] \leq 10^9$

For tests worth 30% of the score:

$N, M \leq 1\ 000$

## Example

`compunere.in`

```
5 3
1 4 5 3 6
1 5 4
```

`compunere.out`

```
6
1 4 5 3 4 6
```