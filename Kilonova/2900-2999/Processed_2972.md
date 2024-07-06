> "It's better to use a map than to sort, lol"

# Task

Given a string $a$ consisting of $k$ distinct letters, formed from the first $k$ letters of the alphabet, and a string $b$ of $n$ letters, which contains only letters from the first $k$ letters of the alphabet.

You are asked $q$ questions of the form $l \\ r$, such that $1 \\leq l \\leq r \\leq n$, to which you need to respond with the number of sequences $(i_1, i_2, ..., i_k)$ existing such that $l \\leq i_1 \\lt i_2 \\lt \\dots \\lt i_k \\leq r$ and $b_{i_j} = a_j$, for any $1 \\leq j \\leq k$. Because this number can be very large, only the remainder of its division by $998 \ 244 \ 353$ is required.

# Input data

The first line contains two integers, $k$ and $n$. The next line contains a string of $k$ distinct letters. The third line contains a string of $n$ letters. The fourth line contains a single integer, $q$. The next $q$ lines will contain two numbers $l_i$ and $r_i$, representing the data for the $i$-th question.

# Output data

On the $i$-th line from the $q$ lines, there will be a single integer, the answer for the $i$-th question.

# Constraints and clarifications

* $1 \\leq n, q \\leq 10^5$
* $1 \\leq k \\leq \\min(n, 26)$
| # | Score | Constraints |
| - | ------- | ---------- |
| 0 |  0 | Example |
| 1 | 10 | $n, q \\leq 100, k \\leq 10$ |
| 2 | 12 | $n, q \\leq 1\ 000, k \\leq 10$ |
| 3 |  5 | $k = 1$ |
| 4 | 23 | $k \\leq 5$ |
| 5 | 50 | No additional constraints |

# Example

`stdin`
```
2 12
ab
abababababab
3
3 8
2 5
6 11
```

`stdout`
```
6
1
3
```

## Explanation

For the first question, the subarray is `ababab`, and `ab` appears 6 times: `ABabab`, `AbaBab`, `AbabaB`, `abABab`, `abAbaB`, `ababAB`.

For the second question, the subarray is `baba`, and `ab` appears only one time: `bABa`.

For the third question, the subarray is `bababa`, and `ab` appears 3 times: `bABaba`, `bAbaBa`, `babABa`.