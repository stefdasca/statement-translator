```markdown
# Task

Given an array of numbers $A$ of length $N$, with $A_1 = 1$ and each $A_i$ being a multiple of $A_{i-1}$, and a number $K$. In one operation, we choose a term from $A$ and subtract its value from $K$, the array $A$ remains unchanged.

What is the minimum number of operations required for $K$ to become 0?

# Input data

The first line contains $N$ and $K$. The second line contains the array $A$.

# Output data

Print the minimum number of operations.

# Constraints and clarifications

- $1 \le N, A_i, K \le 10^5$

# Example

`stdin`
```
4 14
1 3 3 9
```

`stdout`
```
4
```

## Explanation

$14 - 3 - 1 - 9 - 1 = 0$
```