
# Task
Initially, there existed a sequence of $N$ natural numbers between $1$ and $V$, where $V$ is of the form $2^{k}-1, k \in \mathbb{N}$. This sequence was lost; all that remains is a sequence $Z$ of size $V$ defined as follows: $Z_i = |\{j ~|~ i \& A_j \neq 0,~1 \leq j \leq N \}|$, where $\&$ represents the $AND$ operation on bits. Specifically, $Z_i$ is the number of elements $j$ for which $A_j \& i \neq 0$. You are given the sequence $Z$ and asked for a possible initial sequence.

# Input data

The first line contains the numbers $N$ and $V$. The second line contains the sequence $Z$ (indexed from $1$).

# Output data

A sequence of $N$ numbers between $1$ and $V$ with the meaning from the statement, or $-1$ if no such sequence exists.

# Constraints and clarifications

* $1 \leq N, V \leq 2\cdot10^{5}$;
* $Z$ is indexed from $1$.
* $1 \leq Z[i] \leq 10^{9}$
* Any correct solution is accepted.
* For $30$ points, $V = 3$.

# Example 1

`stdin`
```
2 3
2 0 2
```

`stdout`
```
1 1
```

## Explanation

This is the only possible sequence.

# Example 2

`stdin`
```
1 1
0
```

`stdout`
```
-1
```

## Explanation

No such sequence exists.
