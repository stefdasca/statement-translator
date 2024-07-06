Non-zero natural numbers $N$ and $D$ are considered.

# Task
Determine the number of pairs of numbers $A$ and $B$, both less than or equal to $N$ and with the property that their greatest common divisor is $D$.

# Input data
The first line of the file `cntgcd.in` contains the numbers $N$ and $D$ separated by a space.

# Output data
The output file `cntgcd.out` will contain a single natural number representing the number of pairs of natural numbers whose greatest common divisor is equal to $D$.

# Constraints and clarifications
- $1 < N \leq 10^9$
- $0 < D \leq N$
- For $40\%$ of the score $1 < N \leq 10^6$.
- For $75\%$ of the score $1 < N \leq 10^8$.
- The pair $(A, B)$ is considered the same as the pair $(B, A)$.

# Example
`cntgcd.in`
```
20 5
```
`cntgcd.out`
```
6
```

## Explanation
The 6 pairs are: $(5,5)$, $(5,10)$, $(5,15)$, $(5,20)$, $(10,15)$, $(15,20)$.