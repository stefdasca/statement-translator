Given $N$ natural non-zero numbers $a_1$, $a_2$, $ \dots $, $a_N$.

# Task

Construct a minimum number using all the digits of the given numbers such that the digit sequence of each number appears as a subsequence in the constructed minimum number.

# Input data

The first line of the file `catmin.in` contains the natural number $N$. The second line contains the $N$ natural numbers, separated by a space.

# Output data

The first line of the output file `catmin.out` will contain the digits of the constructed minimum number. The digits will not be separated by space.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $1 \leq a_i \leq 1\ 000\ 000\ 000$ for any $i = 1 \dots N$
* We say about $a_{i_1}$, $a_{i_2}$, $ \dots $, $a_{i_k}$ that it is a subsequence of the sequence $a$, if $1 \leq i_1 < i_2 < i_3 < \dots < i_k \leq N$
* For tests valued at $21$ points: $N \leq 500$
* For other tests valued at $33$ points: $N \leq 10\ 000$
* For other tests valued at $46$ points: there are no other constraints

# Example

`catmin.in`
```
3
413 2007 29
```

`catmin.out`
```
200241379
```

## Explanation

The final number will have $9$ digits, that is all the digits of the three given numbers. Numbering the positions of the obtained minimal number with $1$, $2$, $ \dots $, $9$ it is observed that $413$ is a subsequence in the final number and occupies positions $5$, $6$, $7$, the number $2007$ occupies positions $1$, $2$, $3$, $8$, and the number $29$ occupies positions $4$ and $9$. It is easily observed that this number is the smallest that can be constructed under the given conditions.