
> No more unnecessary stories  
> -- Scientific Commission, The day before the exam

# Task

Given $A, B$ two strings of lengths $N$, respectively $M$. Determine the longest common subsequence of these two strings with the condition that the difference between the positions of any two consecutive characters in the subsequence is at least $L$ and at most $U$.

Formally, find the maximum $k$ for which there exist two sequences of numbers $1 \le a_1 < a_2 < \dots < a_k \le N$ and $1 \le b_1 < b_2 < \dots < b_k \le M$ such that:
* For any $1 < j \le k$, $L \le a_j - a_{j-1}, b_j - b_{j-1} \le U$
* For any $1 \le j \le k$, $A_{a_j} = B_{b_j}$

# Input data

The first line of the input will contain an integer $T$, the number of test cases. The description of each test case follows.

The first line of each test case will contain the numbers $N, M, L, U$, representing the length of the first string, the length of the second string, and the bounds for the differences between indices, respectively.

The second and third lines of each test will contain the strings $A$ and $B$.

# Output data

For each test case, print a single number on separate lines --- the maximum length of a common subsequence that respects the properties outlined in the statement.

# Constraints and clarifications

* $1 \le N, M \le 6\ 000$, and particularly, that $S_N, S_M \le 6\ 000$, where $S_N$ and $S_M$ represent the sum of all $N$s from all test cases present in a test, respectively the sum of all $M$s from all test cases present in a test;
* $1 \le L \le U \le \max(N, M)$;
* $A$ and $B$ contain only lowercase letters of the Latin alphabet.

|#| Score | Constraints |
|-|-------|-------------|
|1| 9     | $1 \leq S_N, S_M \leq 50$ |
|2| 17    | $1 \leq S_N, S_M \leq 1\ 000$, and $L = 1, U = \max(N, M)$ for any test case |
|3| 16    | $1 \leq S_N, S_M \leq 1\ 000$, and $U = \max(N, M)$ for any test case |
|4| 14    | $1 \leq S_N, S_M \leq 700$ |
|5| 13    | $1 \leq S_N, S_M \leq 1\ 000$ |
|6| 17    | $1 \leq S_N, S_M \leq 3\ 000$ |
|7| 14    | No additional constraints. |

# Example

`stdin`
```
5
6 6 2 4
aaaaaa
aaaaaa
7 8 3 3
axxbxxc
axxxbxxc
7 8 3 4
axxbxxc
axxxbxxc
7 6 1 1
axabaaa
aaaaab
7 9 2 3
ggpxuam
gkxxkszhk
```

`stdout`
```
3
2
3
3
2
```

## Explanation

For the first example, we can take the strings:
* $\\underline{a}a\\underline{a}a\\underline{a}a$
* $a\\underline{a}a\\underline{a}a\\underline{a}$

For the fourth example, we can take the strings:
* $axab\\underline{aaa}$
* $\\underline{aaa}aab$
```
