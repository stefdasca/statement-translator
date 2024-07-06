```markdown
# Task

Given an array of $N$ natural numbers. There are also $Q$ queries of the form $[l, r]$, where the sum of all subarrays of consecutive elements is required. More formally, for each query $[l, r]$, the result of the function $F(l, r) = \\sum_{i=l}^{r} \\sum_{j=i}^{r} S(i, j)$ is required, where $S(l, r)$ is the sum of all elements in the subarray $[l, r]$.

# Input data

```
N Q
A[1] A[2] ... A[N]
L[1] R[1]
L[2] R[2]
...
L[Q] R[Q]
```

# Output data

```
S[1]
S[2]
...
S[Q]
```

# Constraints and clarifications

* It is recommended to use [fastio](https://www.geeksforgeeks.org/fast-io-for-competitive-programming/).
* $1 \\leq N, Q \\leq 500\\ 000$
* $0 \\leq A[i] \\leq 1\\ 000\\ 000\\ 000$
* $1 \\leq l \\leq r \\leq N$
* Since the answers are too large to be represented by the default data types in C++, they will be displayed modulo ${2}^{32}$.

|#|Score|Constraints|
|-|-|-|
|1|20|$1 \\leq N, Q \\leq 500$|
|2|10|$1 \\leq N, Q \\leq 2\\ 500$|
|3|20|$1 \\leq N, Q \\leq 50\\ 000$|
|4|50|$1 \\leq N, Q \\leq 500\\ 000$|

# Example

`stdin`
```
5 4
5 3 2 4 2
3 4
3 5
4 5
1 5
```

`stdout`
```
12
28
12
109
```

## Explanation

For the first query (subarray $[3, 4]$), the sum is $2 + 4 + (2 + 4) = 12$.

For the second query (subarray $[3, 5]$), the sum is $2 + 4 + 2 + (2 + 4) + (4 + 2) + (2 + 4 + 2) = 28$.

For the third query (subarray $[4, 5]$), the sum is $4 + 2 + (4 + 2) = 12$.

For the fourth query (subarray $[1, 5]$), the sum is $5 + 3 + 2 + 4 + 2 + (5 + 3)$  $+\\ (3 + 2) + (2 + 4) + (4 + 2) + (5 + 3 + 2)$  $+\\ (3 + 2 + 4) + (2 + 4 + 2) + (5 + 3 + 2 + 4) + (3 + 2 + 4 + 2)$  $+\\ (5 + 3 + 2 + 4 + 2) = 109$.
```