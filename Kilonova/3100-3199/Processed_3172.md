Roxy, the space traveler, is faced with a very abstract problem. Since she has no idea how to solve it, you, as her best friend, need to help her:

She receives an array $c_1, c_2, \dots, c_N$ containing $N$ integers, and $Q$ pairs of endpoints $(L_i, R_i)$, each representing the subarray $c_{L_i}, c_{L_{i+1}}, \dots, c_{R_i}$, where $1 \leq i \leq N$.

# Task

For each pair $(L_i, R_i)$, Roxy is asked for the maximum number of disjoint subarrays with sum $0$ that can be chosen from the subarray $c_{L_i}, c_{L_{i+1}}, \dots, c_{R_i}$. Two subarrays are considered disjoint if they have no elements in common; however, they can still have adjacent endpoints. Note that there may be elements from the queried array that do not form part of any of the chosen subarrays.

# Input data

The first line of the input contains a single integer $N$.

The second line contains $N$ integers separated by spaces $c_1, c_2, \dots, c_N$.

The third line contains the number of queries $Q$.

The following $Q$ lines contain $2$ numbers $L_i$ and $R_i$, representing query $i$.

# Output data

Print $Q$ lines: on the $i$-th line, you must print the answer to query $i$.

# Constraints and clarifications

* $1 \leq N \leq 400 \ 000$
* $1 \leq Q \leq 400 \ 000$
* $-10^9 \leq c_i \leq 10^9$ for $1 \leq i \leq N$
* $1 \leq L_i \leq R_i \leq N$ for $1 \leq i \leq Q$

| # | Score | Constraints |
| - | ------ | ------------------- |
| 1 | 22     | $1 \leq N, Q \leq 5 \ 000$|
| 2 | 39     | $1 \leq N, Q \leq 100 \ 000$ |
| 3 | 39     | No additional constraints. |

# Examples

`stdin`
```
10
1 2 -3 0 1 -4 3 2 -1 1
3
1 10
1 5
2 9
```

`stdout`
```
4
2
2
