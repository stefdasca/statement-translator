# Subsequences

A sequence of $N$ distinct integers $x_1, x_2, \dots, x_N$ is given.

## Task

Determine the length of the subsequences $x_{i_1}, x_{i_2}, \dots, x_{i_k}$ of maximum length, where $i_1 < i_2 < \dots < i_k$ and $x_{i_1} < x_{i_2} < \dots < x_{i_k}$, as well as their number.

## Input data

The first line of the file `subsiruri.in` contains the natural number $N$, representing the length of the sequence. The next $N$ lines contain one integer each.

## Output data

The first line of the file `subsiruri.out` will contain the natural number $lungmax$, representing the maximum length of the increasing subsequences. The next line will print the number of subsequences of length $lungmax$. This number will be displayed modulo $9901$.

## Constraints and clarifications

$5 \leq n \leq 1000$

$-32000 \leq x_k \leq 32000$

## Example

`subsiruri.in`
```
10
1
-12
3
8
-25
0
7
-18
9
2
```

`subsiruri.out`
```
4
6
```

## Explanation

There are $6$ increasing subsequences of maximum length $4$: 
$1\ 3\ 8\ 9$ 
$1\ 3\ 7\ 9$ 
$-12\ 3\ 8\ 9$ 
$-12\ 3\ 7\ 9$ 
$-12\ 0\ 7\ 9$ 
$-25\ 0\ 7\ 9$