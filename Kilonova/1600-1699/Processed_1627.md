Consider a sequence of non-zero natural numbers $a_1$, $a_2$, $\\dots$, $a_n$. In this sequence, a V-subarray is a maximal subarray of the form $a_x$, $a_{x+1}$, $\\dots$, $a_y$ with the property that all numbers in the subarray have values less than or equal to $V$. It is maximal because it cannot be extended to the left or right. For example, the sequence $a$ = $2$, $2$, $6$, $4$, $3$, $14$, $7$, $4$, $3$, $36$ has two $7$-subarrays: $2$, $2$, $6$, $4$, $3$ and $7$, $4$, $3$. Also, the sequence has three $4$-subarrays: $2$, $2$; $4$, $3$; $4$, $3$. Note that $2$, $6$, $4$, $3$ is not a 7-subarray because it can be extended at its left end with the number $2$.

# Task

For a given sequence of numbers, you need to answer $Q$ queries denoted $V_1$, $V_2$, $\\dots$, $V_Q$. For each query $i$, given by the natural number $V_i$, you need to find how many $V_i$-subarrays are in the sequence.

# Input data

The input file `vsecvente.in` contains the following:
- The first line contains the natural number $N$.
- The second line contains the $N$ elements of the sequence, separated by a space.
- The third line contains a single natural number $Q$ representing the number of queries.
- The fourth line contains the sequence of $Q$ natural numbers $V_1$, $V_2$, $\\dots$, $V_Q$, separated by a space.

# Output data

The output file `vsecvente.out` will contain $Q$ lines. The $i$-th line will contain the number of $V_i$-subarrays found in the sequence.

# Constraints and clarifications

* $1 \\leq$ all numbers in the input file $\\leq 1 \\ 100 \\ 000$
* For tests totaling $75$ points, $1 \\leq$ all numbers in the input file $\\leq 550 \\ 000$

# Example

`vsecvente.in`
```
10
2 2 6 4 3 14 7 4 3 36
3
7 1 4
```

`vsecvente.out`
```
2
0
3
```

## Explanation

There are three queries:

- There are two $7$-subarrays: $2 \\ 2 \\ 6 \\ 4 \\ 3$ and $7 \\ 4 \\ 3$
- There is no $1$-subarray
- There are three $4$-subarrays: $2 \\ 2$; $4 \\ 3$; and $4 \\ 3$