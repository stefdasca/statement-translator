
# Task

We are given $A$, $B$, $C$ and $N$.
<br>
If we consider the sequence $X$ defined as follows:
$X_1$ = $A$
$X_i$ = $(X_{i-1}*B + C)$ % $666013$, $1 < i \leq N$
What is the minimum possible value of $X_i \oplus X_j$, $1 \leq i < j \leq N$?

# Input data

The first line contains the four integers $A$, $B$, $C$, and $N$.

# Output data

The first line will contain a single number representing the minimum XOR of a pair of numbers.

# Constraints and clarifications

* $0 \leq A, B, C \leq 10^5$
* $2 \leq N \leq 10^{12}$

# Example 1

`stdin`
```
1 2 2 5
```

`stdout`
```
5
```

## Explanation

The sequence $X$ is: ${1, 4, 10, 22, 46}$
The pair $(i,j)$ is $(1,2)$
```
