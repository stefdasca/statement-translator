```markdown
We are given $N$ natural numbers $s_1$, $s_2$, $\\dots$, $s_N$ and $Q$ queries of the form $a \\ b$.

# Task

Determine for each query $[a; b]$ the number of subsequences formed from distinct elements of the subarray $s_a$, $s_{a+1}$, $s_{a+2}$, $\\dots$, $s_b$. By subarray of the array $s$, we understand any sequence of elements found at consecutive positions $s_a$, $s_{a+1}$, $s_{a+2}$, $\\dots$, $s_b$, with $1 \\leq a \\leq b \\leq N$.

By subsequence of the array $s$, we understand any sequence of elements found at positions in strictly increasing order but not necessarily consecutive, $s_{a_1}$, $s_{a_2}$, $\\dots$, $s_{a_k}$ with $1 \\leq a_1 < a_2 < \\dots < a_k \\leq N$.

# Input data

The input file `dss.in` contains on the first line the numbers $N$ and $Q$. The second line contains $N$ natural numbers separated by a space. The following $Q$ lines contain two natural numbers $a \\ b$, separated by space, representing the endpoints of the given query intervals.

# Output data

In the output file `dss.out` each of the first $Q$ lines contains a natural number representing the number of all distinct subsequences contained in the subarray from the corresponding query.

# Constraints and clarifications

* $1 \\leq N \\leq 400 \\ 000$
* $1 \\leq Q \\leq 10 \\ 000$
* $1 \\leq s_k \\leq N$
* $1 \\leq a \\leq b \\leq N$
* The number of subsequences for each query will be calculated modulo $1 \\ 000 \\ 000 \\ 007$

# Example

`dss.in`
```
5 3
1 2 3 2 3
1 4
2 5
1 3
```

`dss.out`
```
11
8
7
```

## Explanation

- The subsequences formed from distinct elements in the subarray $s[1 \\dots 4$] = $(1 \\ 2 \\ 3 \\ 2)$ are $1$, $2$, $3$, $2$, $1 \\ 2$, $1 \\ 3$, $1 \\ 2$, $2 \\ 3$, $3 \\ 2$, $1 \\ 2 \\ 3$, $1 \\ 3 \\ 2$, so a total of $11$ subsequences.
- The subsequences formed from distinct elements in the subarray $s[2 \\dots 5$] = $(2 \\ 3 \\ 2 \\ 3)$ are $2$, $3$, $2$, $3$, $2 \\ 3$, $2 \\ 3$, $3 \\ 2$, $2 \\ 3$, so $8$ subsequences.
- The subsequences formed from distinct elements in the subarray $s[1 \\dots 3$] = $(1 \\ 2 \\ 3)$ are $1$, $2$, $3$, $1 \\ 2$, $1 \\ 3$, $2 \\ 3$, $1 \\ 2 \\ 3$, so $7$ subsequences.
```