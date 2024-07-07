# Task

Given $N$. How many permutations of order $N$ (of the set $\\{1, 2, ..., N\\}$) exist such that $gcd(A_i+1,i+1) > 1$ for any $1 \\le i \\le N$?

# Input data

A single number, $N$.

# Output data

The number of permutations that meet the condition.

# Constraints and clarifications

- $1 \\le N \\le 23$;
- It is observed that the answer is relatively small.

# Example 1

`stdin`
```
4
```

`stdout`
```
2
```

## Explanation

The permutations ${1, 2, 3, 4}$ and ${3, 2, 1, 4}$.

# Example 2

`stdin`
```
19
```

`stdout`
```
318695040
