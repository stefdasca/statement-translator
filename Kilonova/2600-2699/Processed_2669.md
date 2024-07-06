It is given a permutation $P[1], \dots , P[N]$ of $N$ numbers. A _cycle_ of the permutation is a sequence $i_1, \dots, i_k \in \{1, \dots, N \}$ such that $i_2 = P[i_1]$, $i_3 = P[i_2]$, $\dots$, $i_k = P[i_{k - 1}]$, $i_1 = P[i_k]$. An interval $[x, y]$ is _good_ if there exists a *cycle* $i_1, \dots, i_{y-x+1}$ such that each number $x, x + 1, \dots , y$ appears exactly once in $i_1, \dots , i_{y-x+1}$.

A query consists of two values $x$ and $y$, with $1 \leq x \leq y \leq N$. The answer is the minimum number of swaps that must be applied to the initial permutation so that the interval $[x, y]$ becomes *good*. A swap consists in selecting two positions $i$ and $j$ and swapping the values $P[i]$ and $P[j]$ between them.

**_Attention!_** The queries are independent; that is, the swaps applied for one query are not preserved for the following queries. Moreover, for the query $[x, y]$ it is allowed to swap elements from the interval $[x, y]$ with elements outside the interval $[x, y]$.

# Task

Display the answer for $Q$ queries.

# Input data

The input file `perm.in` contains on the first line two numbers $N$ and $Q$.

The second line contains $N$ values representing, in order, the values $P[1], P[2], \dots, P[N]$.

The next $Q$ lines contain two numbers $x$, $y$ each separated by a space, representing a query.

# Output data

The output file `perm.out` must contain $Q$ lines, each with the answer for one query.

# Constraints and clarifications

* $1 \leq N, Q \leq 300\ 000$
* $1 \leq x \leq y \leq N$

| # | Score | Constraints          |
| - | ------- | ------------------- |
| 1 | 2      | $P[i] = i$ |
| 2 | 11      | $Q = 1$      |
| 3 | 9      | $N, Q \leq 7$      |
| 4 | 18      | $x = 1$      |
| 5 | 40      | $N, Q \leq 100\ 000$      |
| 6 | 20     | Without additional constraints      |

# Example

`perm.in`
```
5 3
4 1 2 3 5
2 4
1 4
1 5
```

`perm.out`
```
1
0
1
```

## Explanation

* To transform the interval $[2, 4]$ into a *good* interval, it is enough to make a single swap between position $1$ and position $2$.
* The interval $[1, 4]$ is already *good*, so no swaps are needed.
* For the last interval, one swap is needed between position $1$ and position $5$.