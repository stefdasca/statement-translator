# 12-Perm

A 12-permutation $A_1, A_2, \dots, A_N$ is defined as a permutation of the numbers $1, 2, \dots, N$ such that $|A_i - A_{i+1}| < 3$ for $i = 1, 2, \dots, N-1$.

## Task

Given a natural number $N$, calculate the number of 12-permutations of length $N$.

## Input data
The first line of the input file `12perm.in` contains the natural number $N$ as described above.

## Output data
In the output file `12perm.out` you will print $X$, the number of 12-permutations of length $N$ modulo $1048576$.

## Constraints and clarifications
$1 \leq N \leq 15000000$

$1048576 = 2^{20}$

## Constraints and clarifications
For 70% of the tests $N \leq 5500000$.

## Example

`12perm.in`
```
4
```

`12perm.out`
```
12
```

## Explanation

The $12$ 12-permutations are:
$1 2 3 4$,
$1 2 4 3$,
$1 3 2 4$,
$1 3 4 2$,
$2 1 3 4$,
$2 4 3 1$,
$3 1 2 4$,
$3 4 2 1$,
$4 2 1 3$,
$4 2 3 1$,
$4 3 1 2$,
$4 3 2 1$