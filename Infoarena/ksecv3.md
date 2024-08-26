## Ksecv3

Given a sequence of $N$ natural numbers, partition the ENTIRE sequence into $K$ subarrays of equal sum.

## Input data

The input file `ksecv3.in` will contain on the first line 2 natural numbers $N$ and $K$. On the second line, there will be $N$ natural numbers representing the given sequence.

## Output data

The output file `ksecv3.out` will contain on one line $K$ natural numbers representing the end positions of the $K$ subarrays. If no solution exists, print $-1$.

## Constraints and clarifications

$1 \leq K \leq N \leq 100\ 000$

The values of the elements will be between 1 and $1\ 000\ 000\ 000$

## Example

`ksecv3.in`

```
9 3
1 9 4 2 4 1 1 1 7
```

`ksecv3.out`

```
2 5 9
```

## Explanation

The sum of the subarray $(1,2)$ is $10$. The sum of the subarray $(3,5)$ is also $10$, and the sum of the subarray $(6,9)$ is also $10$.