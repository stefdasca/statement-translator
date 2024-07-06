```
We denote $X$ as the set of natural numbers that can be written in the form $2^a \cdot 3^b$. We only consider those numbers for which $0 \leq a \leq D$ and $0 \leq b \leq T$, where $D$ and $T$ are given. For a number $v$ in $X$, we consider its associate to be the value $(C \cdot P) \% Q$ where $C$ is the last digit of $v$ and $P$ and $Q$ are given (for example, for $P = 1$ and $Q = 10$, the associate of $2 \cdot 3^2$ is $8$).

# Task

Determine the maximum value of the sum of the associates of the elements of a subset of $X$ such that for any two elements $u$ and $v$ in that subset, $u$ does not divide $v$ and $v$ does not divide $u$.

# Input data

The file `smsm.in` contains on the first line four natural numbers $D$, $T$, $P$, and $Q$ separated by a space, representing: the maximum power at which $2$ can appear in the numbers from $X$, the maximum power at which $3$ can appear in the numbers from $X$, and the two numbers $P$ and $Q$, with their meanings as described above.

# Output data

The file `smsm.out` will contain a single number, the maximum value of the sum of the associates of the elements of a subset that can be formed.

# Constraints and clarifications

* $1 \leq D, T, P, Q \leq 500$

# Example

`smsm.in`
```
1 1 1 3 
```

`smsm.out`
```
2
```

## Explanation

The numbers in the set $X$ are: $(1, 2, 3, 6)$. Their associates are: $(1, 2, 0, 0)$, respectively. We can choose for the optimal solution either the subset $\{2, 3\}$ or the subset $\{2\}$, both with the sum of associates $2$. Choosing the subset $\{1, 1\}$, with the sum of associates $3$, does not respect the constraint that the elements of the subset do not divide each other.
```