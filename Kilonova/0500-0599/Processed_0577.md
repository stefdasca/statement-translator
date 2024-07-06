# Task

We randomly select $M$ permutations of order $N$ each. We denote $inv(P)$ as the number of inversions in permutation $P$.

What is the expected value of the number of indices $(i, j)$, such that $1 \le i < j \le M$ and $inv(P_i) = inv(P_j)$?

# Input data

The first line contains $N$, $M$.

# Output data

Print the expected value from the statement, modulo $998244353$, which is a prime number.

# Constraints and clarifications

- $1 \le N \le 300$;
- $1 \le M \le 10^5$.

## Observation

There exists a solution for:
- $1 \le N \le 5000$;
- $1 \le M \le 10^{18}$.

# Example

`stdin`
```
2 2
```

`stdout`
```
499122177
```

## Explanation

The possible permutations can be:
- $\{1,\ 2\}, \{1,\ 2\}$ with 1 good pair.
- $\{1,\ 2\}, \{2,\ 1\}$ with 0 good pairs.
- $\{2,\ 1\}, \{1,\ 2\}$ with 0 good pairs.
- $\{2,\ 1\}, \{2,\ 1\}$ with 1 good pair.

Thus, the expected value is $\frac{1}{2}$ which is $499122176$ under the modulo from the statement.