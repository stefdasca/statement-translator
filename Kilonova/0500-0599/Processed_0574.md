
# Task

You are given an array $A$ of length $N$ and $Q$ queries of the type $St\\ Dr\\ X$.

For each query, answer whether:
There exists a subarray $\\{i_1, i_2, ..., i_k\\}$ of the array $\\{St, St+1, ..., Dr-1, Dr\\}$ with $i_1 < i_2 < ... < i_k$ such that $A_{i_1} + A_{i_2} + ... + A_{i_k} = X$?

# Input data

The first line contains $N$ and $Q$. The second line contains the array $A$. The following $Q$ lines contain $3$ numbers each: $St\\ Dr\\ X$.

# Output data

Print $Q$ lines with the answers. The answer is either `DA` or `NU`.

# Constraints and clarifications

- $1 \\le N, X, A_i \\le 10^3$;
- $1 \\le St \\le Dr \\le N$;
- $1 \\le Q \\le 10^5$.

# Example

`stdin`
```
5 3
1 2 3 4 5
2 3 5
2 3 4
2 4 6
```

`stdout`
```
DA
NU
DA
```
