Given a sequence of $n$ natural numbers $v_1$, $v_2$, $\dots$, $v_n$, where $v_i$ represents the $i$-th number in the sequence.
A subarray $[x, y]$ of the sequence $v$ (with $1 \leq x \leq y \leq n$) contains all the elements $v_x, v_{x+1}, \dots, v_{y - 1}, v_y$.

# Task

Given two natural numbers $n$ and $k$ and an array $v$ of $n$ natural numbers, write a program that answers the following question: how many subarrays simultaneously contain the smallest $k$ distinct values in the sequence?

# Input data

The input file `secvmin.in` contains the numbers $n$ and $k$ on the first line, and on the second line, it contains the natural numbers $v_1$, $v_2, \dots, v_n$, as described in the statement. The numbers written on the same line are separated by a space.

# Output data

The output file `secvmin.out` will contain a single line where the answer to the task will be written.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000 \ 000$;
* $1 \leq k \leq 5$;
* $1 \leq v_i \leq 1 \ 000 \ 000 \ 000$, for $1 \leq i \leq n$;
* It is guaranteed that the sequence will contain at least $k$ distinct values.

# | Score | Constraints|
| - | -- | ------------|
| 1 | 23 | $k = 1$ |
| 2 | 32 | $k = 2$ |
| 3 | 45 | $3 \leq k \leq 5$ |

# Example 1

`secvmin.in`
```
7 1
1 3 2 2 1 3 2
```

`secvmin.out`
```
19
```

## Explanation

$k=1$. The smallest value in the sequence is $1$. 
The subarrays that contain the value 1 are: $[1, 1]$, $[1, 2]$, $[1, 3]$, $[1, 4]$, $[1, 5]$, $[1, 6]$, $[1, 7]$, $[2, 5]$, $[2, 6]$, $[2, 7]$, $[3, 5]$, $[3, 6]$, $[3, 7]$, $[4, 5]$, $[4, 6]$, $[4, 7]$, $[5, 5]$, $[5, 6]$, $[5, 7]$.

# Example 2

`secvmin.in`
```
7 2
1 5 2 2 1 5 2
```

`secvmin.out`
```
15
```

## Explanation

$k=2$. The smallest value in the sequence is $1$, and the second smallest value in the sequence is $2$.
The subarrays that contain the values $1$ and $2$ are: $[1, 3]$, $[1, 4]$, $[1, 5]$, $[1, 6]$, $[1, 7]$, $[2, 5]$, $[2, 6]$, $[2, 7]$, $[3, 5]$, $[3, 6]$, $[3, 7]$, $[4, 5]$, $[4, 6]$, $[4, 7]$, $[5, 7]$.