Gigel has progressed today in mathematics and has learned about arithmetic progression. If we have the first element $a$ and a difference $r$, the arithmetic progression is formed as follows: $a, a + r, a + 2 \cdot r, \dots$

# Task

Given a sequence of $n$ numbers, $a_1, a_2, \dots, a_n$. Find the maximum length of a subarray $[l, r]$ of the array $a$ where $1 \leq l \leq r \leq n$, such that there exists an integer $k$ for which $a_i = a_l + k \cdot (i - l)$, for any $i$ such that $l \leq i \leq r$ (in other words, the subarray from $l$ to $r$ should be an arithmetic progression).

# Input data

The first line of the input file `progres.in` contains the integer $n$. The next line contains the $n$ numbers, $a_1, a_2, \dots, a_n$, separated by spaces.

# Output data

The first line of the output file `progres.out` will contain a single integer, the maximum length of a subarray that meets the required conditions.

# Constraints and clarifications

* $2 \leq n \leq 10 ^ 6$
* $1 \leq a_i \leq 10 ^ 9$, for $1 \leq i \leq n$
* For $20$ points, $n \leq 10 \ 000$

# Example 1

`progres.in`
```
10
1 2 3 4 2 7 12 17 22 27
```

`progres.out`
```
6
```

## Explanation

The subarray $(2, 7, 12, 17, 22, 27)$ has a length of $6$ and is an arithmetic progression. There are no longer subarrays that fulfill the conditions.

# Example 2

`progres.in`
```
5
1 2 3 4 5
```

`progres.out`
```
5
```

## Explanation

The entire array is an arithmetic progression!