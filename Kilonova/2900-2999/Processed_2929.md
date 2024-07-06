A series $b_1, b_2, \dots, b_k$ is called increasing if and only if $b_1 \leq b_2 \leq b_3 \leq \dots \leq b_{k-1} \leq b_k$.

The subarray $[l, r]$ of the series $b$ is the series $b_l, b_{l+1}, b_{l+2}, \dots, b_r$.

# Task

Given $N$ and a series $a_1, a_2, a_3, \dots, a_N$. $Q$ queries of the form $[l, r]$ are given, ask whether the subarray $[l, r]$ is sorted in increasing order ($a_l \leq a_{l+1} \leq a_{l+2} \leq \dots \leq a_r$).

# Input data

The first line of the input file ```crescator.in``` contains the number $N$. The second line contains the series $a_1, a_2, \dots, a_N$.
The third line contains the number $Q$ and the next $Q$ lines contain the pair $l, r$.

# Output data

Print $Q$ lines in the file ```crescator.out``` . The $i$-th line is `YES` if the answer to the $i$-th question is yes, and `NO` otherwise.

# Constraints and clarifications
 
* $1 \leq N, Q \leq 200\ 000$

| # | Points | Constraints |
| - | ------ | ----------- |
| 1 | 10 | $N = 2, Q = 1, l = 1, r = 2$ |
| 2 | 30 | $N, Q \leq 2\ 000$ |
| 3 | 60 | No additional constraints |

# Example
`crescator.in`
```
10
3 7 8 12 4 2 5 5 1 8
7
1 4
2 4
3 5
5 6
6 8
6 9
1 10
```
`crescator.out`
```
YES
YES
NO
NO
YES
NO
NO
```

## Explanation

For the first question, the answer is `YES`, because the subarray $[1, 4]$ is $3, 7, 8, 12$ which is sorted in increasing order.

For the third question, the answer is `NO`, because the subarray $[3, 5]$ is $8, 12, 4$ which is not sorted in increasing order ($12 > 4$).