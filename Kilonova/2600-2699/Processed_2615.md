A sequence is called good if the sum of the elements is equal to the number of elements. More precisely, a sequence $x_1, x_2, \dots, x_k$ is called good if $x_1 + x_2 + x_3 + \ldots + x_k = k$.
The subarray $[l \dots r]$ of a sequence $x_1, x_2, \dots x_k$ is the sequence formed by the values $x_l, x_{l+1}, x_{l+2}, \dots, x_r$ in this order.

# Task

Given $C$, $N$, and a sequence $a_1, a_2, \dots, a_N$ of $N$ natural numbers, respond to the following 3 tasks:
1. If $C=1$, you must print `YES` if the sequence $a$ is good and `NO` otherwise.
2. If $C=2$, you must print a sequence $b_1, b_2, \dots, b_N$ with the property that the number of good subarrays in $b$ is as large as possible. (Note that the sequence $a$ has no connection with this task).
3. If $C=3$, you must print the number of good subarrays of the sequence $a$.

# Input data

The input file `bun.in` contains:
- The first line contains the number $C$.
- The second line contains the number $N$.
- The third line contains the sequence $a_1, a_2, \dots, a_N$.

# Output data

The output file `bun.out` must contain the answer to the corresponding task on the first line.

# Constraints and clarifications

* $C \in \lbrace 1, 2, 3 \rbrace$
* $2 \leq N \leq 100\ 000$
* $0 \leq a_i \leq 3$ **(!!!)**

| # | Score | Constraints |
|---|-------|-------------|
| 1 | 20    | $C=1$       |
| 2 | 20    | $C=2$       |
| 3 | 20    | $C=3$, $N \leq 3000$ |
| 4 | 20    | $C=3$, $a_i \geq 1$ for each $i$ from $1$ to $N$ |
| 5 | 20    | $C=3$, $N > 3000$   |

# Example 1

`bun.in`
```
1
6
0 1 2 0 3 0
```

`bun.out`
```
YES
```

## Explanation

In the first example, we have $0 + 1 + 2 + 0 + 3 + 0 = 6$, so the sequence is good.

# Example 2

`bun.in`
```
1
2
0 1
```

`bun.out`
```
NO
```

## Explanation

In the second example, we have $0 + 1 = 1 \neq 2$, so the sequence is not good.

# Example 3

`bun.in`
```
2
2
2 3
```

`bun.out`
```
1 1
```

## Explanation

In the third example, we can form the sequence $\lbrace 1, 1 \rbrace$ which has 3 good subarrays.

# Example 4

`bun.in`
```
3
8
1 1 2 0 0 0 1 3
```

`bun.out`
```
11
```

## Explanation

In the last example, we have 11 good subarrays. These are $\lbrace (1, 1)$; $(1, 2)$; $(1, 4)$; $(1, 8)$; $(2, 2)$; $(2, 4)$; $(2, 8)$; $(3, 4)$; $(3, 8)$; $(5, 8)$; $(7, 7) \rbrace$.