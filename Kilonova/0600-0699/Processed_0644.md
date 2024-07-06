## *Echilibrul* unui șir $x_1, x_2, \cdots, x_k$ este egal cu $max (x_1, x_2, \cdots, x_k) - min (x_1, x_2, \cdots, x_k)$.

For example, the *balance* of the sequence $4, 7, 6$ is $7 - 4 = 3$, the *balance* of the sequence $9, 1, 2$ is $9 - 1 = 8$, and the *balance* of the sequence $7, 7, 7$ is $7 - 7 = 0$.

You are given $P$, $N$ and a sequence of $N$ natural numbers $a_1$, $a_2$, $\cdots$, $a_N$.

# Task

If $P$ = 1, find the *balance* of the sequence $a$.

If $P$ = 2, find the minimal *balance* of a subarray of length at least $2$ of the sequence $a$.

# Input data
The first line of the input file `echilibru.in` contains two natural numbers $P$ and $N$ separated by a space. The second line contains $N$ natural numbers separated by a space, representing the sequence $a$.

# Output data

The first line of the output file `echilibru.out` contains a natural number representing the answer to Task 1 if $P$ = 1, otherwise to Task 2.

# Constraints and clarifications
* Due to the high speed of the kilonova evaluator, the time limit is different from that of the contest.
* A subarray of the sequence $a$ is a sequence of elements from consecutive positions in the sequence $a$.
* $P = 1$ or $P = 2$
* $2 \leq N \leq 100\ 000$
* $1 \leq a_i \leq 10^9$
* For 30 points $P = 1$.
* For 20 points $P = 2$, but $N \leq 100$.
* For 20 points $P = 2$, but $100 < N \leq 1\ 000$.

# Example 1
`echilibru.in`
```
1 8
2 5 8 9 3 1 6 25
```
`echilibru.out`
```
24
```
# Example 2
`echilibru.in`
```
2 8
2 5 8 9 3 1 6 25
```
`echilibru.out`
```
1
```
# Example 3
`echilibru.in`
```
2 8
8 5 7 10 7 9 7 3
```
`echilibru.out`
```
2
```

# Explanations
In the first example, the maximum of the sequence is $25$, and the minimum of the sequence is $1$, so the *balance* of the sequence is $25 - 1 = 24$.

In the second example, the minimal *balance* is 1. The selected subarray is the one consisting of the numbers $8$ and $9$ (positions $3$ and $4$). The *balance* of the sequence $8, 9$ is $9 - 8 = 1$.

In the third example, the minimal *balance* is 2. The subarrays that have a *balance* of 2 are: $(5, 7), (7, 9)$ and $(7, 9, 7)$.