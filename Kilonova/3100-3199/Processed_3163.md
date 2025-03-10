
# Task

Given a natural number $N$ and a natural number $X$. Display how many subsets of $\{1, 2, 3, \dots, N\}$ have the **XOR** sum $X$.

# Input data

The first line will contain two integers, $N$ and $X$.

# Output data

The first line will contain a single integer, the answer modulo $10^9 + 7$.

# Constraints and clarifications

* $1 \leq N \leq 10^9$
* $0 \leq X \leq 10^9$
* The XOR sum of the empty set $\varnothing$ is considered to be $0$.
* For $10$ points we have $N = 10$.
* For another $20$ points we have $N \leq 5\ 000$.

# Example 1

`stdin`
```
1 1
```

`stdout`
```
1
```

# Example 2

`stdin`
```
3 0
```

`stdout`
```
2
```

## Explanation

We have two subsets with XOR sum $0$: $\varnothing$ and $\{1, 2, 3\}$.
