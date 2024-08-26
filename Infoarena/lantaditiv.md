## Task

A sequence of positive integers $a_1, a_2, a_3, \dots, a_n$ is called an "additive chain" if for any $k$ $(1 < k \leq n)$ there exist $i$ and $j$ $(1 \leq i \leq j \leq n)$ such that $a_k = a_i + a_j$. Write a program that, given $a_1 = 1$ and a given $a_n$, determines an additive chain of length less than $150$.

## Input Data

The input file lantaditiv.in contains a single number $a_n$, which is the last element of the sequence that needs to be generated.

## Output Data

The output file lantaditiv.out should contain on the first line the number of elements in the sequence, and on the following line the required sequence, with the terms separated by a space.

## Constraints and clarifications

$1 \leq a_n \leq 10^{12}$

## Example

`lantaditiv.in`

```
4
```

`lantaditiv.out`

```
3
1 2 4
```