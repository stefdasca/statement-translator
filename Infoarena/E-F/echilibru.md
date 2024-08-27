## Task

Given a set of $2 * N$ stones of different weights, determine if they can be partitioned into two subarrays of equal cardinality (the same number of elements $= N$) such that if we place the two subarrays of stones on the pans of a balance, the balance is in equilibrium.

## Input data

The input file `echilibru.in` contains on the first line the number of tests $T$. On the following $T$ lines are the descriptions of each test: The first number is $N$ and it is followed by $2 * N$ numbers $G_i$, the weight of each stone. These numbers are separated by a single space.

## Output data

For each test, the answer can be encoded by $1$ or $0$, depending on whether it is possible to partition the stones into two subarrays of equal cardinality and equal sum or not. In the file `echilibru.out` print a single number, which represents the base $10$ value of the number represented by $T$ bits encoding the answer for each test in order.

## Constraints and clarifications

$1 \leq N \leq 8$

$1 \leq T \leq 30$

$0 \leq G_i \leq 10^6$

## Example

`echilibru.in`
```
4
2 4 7 6 3
2 4 8 6 7 3
2 4 6 2 5 3
3 1 2 3 4 5 6 10
```

`echilibru.out`
```
10
```

## Explanation

For the first test, the answer is $1$ $(4 + 6 = 7 + 3)$, for the second test, the answer is $0$ (it is not possible to partition), for the third test, the answer is $1$ $(2 + 4 + 5 = 6 + 2 + 3)$, and for the last test, the answer is $0$ (it is not possible to partition). $1010_2 = 10_{10}$ (the first test will determine the value of the most significant bit, the second test the value of the second bit, and $\dots$).