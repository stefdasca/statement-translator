
# Task

Given a sequence of $N$ values $A_1, A_2, ..., A_N$. Calculate the number of good pairs $(St, Dr)$. 

A pair $(St, Dr)$ is good if $St \leq Dr$ and there exist at least $3$ values $(i,j,k)$ such that $St \leq i < j < k \leq Dr$ and $A_j - A_i = A_k - A_j$ (i.e., they are in arithmetic progression).

# Input data

The first line contains $N$, and the second line contains the sequence of $N$ values.

# Output data

Print the number of required pairs.

# Constraints and clarifications

* $1 \leq N \leq 10^5$
* $1 \leq A_i \leq 10$

# Example 1

`stdin`
```
5
5 3 4 1 5
```

`stdout`
```
3
```

## Explanation

The pairs are $(1,4),(1,5),(2,5)$. For example, for the pair $(1,4)$, we can choose the values $5, 3, 1$ which are in arithmetic progression.

# Example 2

`stdin`
```
9
10 10 1 3 3 7 2 2 5
```

`stdout`
```
3
```
