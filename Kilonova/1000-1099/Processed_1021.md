```markdown
Given $N$ and $a_1 \\ a_2 \\ \\dots \\ a_N$. There are $Q$ queries of the form $l$, $r$. For the $i$-th query, you will choose the numbers $l$ and $r$ ($1 \\leq l \\leq r \\leq N$) and you want to know what the maximum of the array would be and how many times it would appear if the subarray $[l..r]$ is **censored**.

* The subarray $[l..r]$ of an array is the array $a_l \\ a_{l+1} \\ a_{l+2} \\dots a_r$.
* By **censoring** a subarray $[l..r]$, we mean replacing $a_i$ with $0$ for each $l \\leq i \\leq r$. For example, if we censor the subarray $[2..4]$ of the array $[1, 2, 3, 4, 5, 6, 7]$, we obtain the array $[1, 0, 0, 0, 5, 6, 7]$.

# Input data

The first line contains two integers, $N$ and $Q$.

The second line contains an array of $N$ natural numbers, representing the array $a$.

The next $Q$ lines each contain a pair of numbers $l$, $r$.

# Output data

The responses to the queries will be displayed on $Q$ lines. The $i$-th line will contain two numbers, representing the answer to the $i$-th question.

# Constraints and clarifications

* $1 \\leq N, Q \\leq 10^6$
* $1 \\leq a_i \\leq 10^9$
* For $44$ points, $N, Q \\leq 5 \ 000$

# Example 1

`stdin`
```
9 6
3 2 3 1 6 7 5 7 7
1 2
1 3
3 6
6 9
1 9
2 8
```

`stdout`
```
7 3
7 3
7 2
6 1
0 9
7 1
```

## Explanation

$N = 9$, $Q = 6$, and $a = [3, 2, 3, 1, 6, 7, 5, 7, 7]$.

For the first query, if we censor the subarray ($1$, $2$), the obtained array is $[0, 0, 3, 1, 6, 7, 5, 7, 7]$, the maximum being $7$ and appearing $3$ times.

For the third query, if we censor the subarray ($3$, $6$), we obtain the array $[3, 2, 0, 0, 0, 0, 5, 7, 7]$, the maximum being $7$ and appearing $2$ times.

For the fourth query, if we censor the subarray ($6$, $9$), we obtain the array $[3, 2, 3, 1, 6, 0, 0, 0, 0]$, the maximum being $6$ and appearing once.

For the fifth query, if we censor the subarray ($1$, $9$), we obtain the array $[0, 0, 0, 0, 0, 0, 0, 0, 0]$, the maximum being $0$ and appearing $9$ times.
```