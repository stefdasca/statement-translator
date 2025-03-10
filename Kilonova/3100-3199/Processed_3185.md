# Task

Let $A$ and $B$ be two arrays of length $N$. An interval $[l,r]$ is considered $\\textbf{sigma}$ if $\\min(B_l,\\dots,B_r) \\leq \\max(A_l,\\dots,A_r) \\leq \\max(B_l,\\dots,B_r)$.

If $S$ represents the set of $\\textbf{sigma}$ intervals, calculate $\\displaystyle \\sum_{[l,r] \\in S} \\max(B_l,B_{l+1},\\dots,B_r)$.

# Input data

The first line contains $t$, the number of test cases. The first line of each test case contains $N$, the number of elements in the two arrays. The next line contains the elements of array $A$, followed by the last line containing the elements of array $B$.

# Output data

Print $t$ numbers, the required sums.

# Constraints and clarifications

* $1 \\leq t \\leq 100$
* $1 \\leq N \\leq 10^5$
* $1 \\leq A_i,B_i \\leq 10^9$
* It is guaranteed that the sum of all $N$ values across all test cases is $\\leq 10^5$.

# Example

`stdin`
```
1
11
2 3 1 6 2 1 6 2 4 2 2
4 3 1 5 2 1 8 5 2 1 2
```

`stdout`
```
311
```

## Explanation

Two of the $\\textbf{sigma}$ intervals are $[1,7]$ and $[8,11]$.