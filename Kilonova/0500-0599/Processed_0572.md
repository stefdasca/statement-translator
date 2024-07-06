```markdown
# Task

Given a sequence of numbers $A$ of length $N$, verify if there exist $2$ elements in the sequence that are not coprime.

# Input data

The first line contains $N$. The second line contains the sequence $A$.

# Output data

Print `DA` or `NU`, depending on the answer.

# Constraints and clarifications

- $1 \le N \le 10^5$
- $1 \le A_i \le 5*10^5$

# Example 1

`stdin`
```
5
2 3 1 5 6
```

`stdout`
```
DA
```

## Explanation

The pairs $(2,6)$ and $(3,6)$ are not coprime.

# Example 2

`stdin`

```
4
6 5 77 97 
```

`stdout`

```
NU
```
```