# Task

An operation called **flip** on an array $a_1, a_2, \dots, a_N$, consisting only of the digits $0$ and $1$, is performed by the following two steps:

* `Step 1`: Choose two natural numbers $l$, $r$, such that $1 \leq l \leq r \leq N$.
* `Step 2`: For each position $i$ in the interval $[l, r]$, if $a_i$ is $0$, it will change its value to $1$, otherwise it will change its value to $0$. (from $0$ to $1$ and from $1$ to $0$).

Given $N$, the array $a_1, a_2, \dots, a_N$, and $Q$ queries of the form $[st, dr]$:

For each given query, you must find the minimum number of **flip** operations you need to perform, **starting from the initial array**, such that for each position $i$ in the interval $[st, dr]$, $a_i$ is equal to $0$.

Solve this problem and we will reward you with $100$ points! (or, as much as you can...).

The operations performed for each query **DO NOT** persist for the subsequent queries (in other words, all queries start from the initial array).

# Input data

The first line of the input file `flip.in` will contain the number $N$, representing the length of the array, and the second line will contain the array $a_1$, $a_2$, ..., $a_N$. The third line of the file will contain the number $Q$, representing the number of queries. The next $Q$ lines will contain two numbers $st$ and $dr$, which represent the endpoints of the interval for which we want to find the answer to the question in the statement.

# Output data

The output file `flip.out` will contain the answers to the $Q$ queries on separate lines, in the order in which they were given.

# Constraints and clarifications

* $1 \leq N, Q \leq 2 \times 10^5$
* $a_i = \{ 0, 1 \}$
* For each query, $1 \leq st \leq dr \leq N$

| # | Points | Constraints |
| - | ------- | ---------- |
| 1 | 9       | $a_{1}=a_{2}=a_{3}=...=a_{n-1}=a_{n}$ |
| 2 | 7       | For each position $i$, $1 \le i < N$, $a_i \neq a_{i+1}$ |
| 3 | 23      | $1 \leq N, Q \leq 200$ |
| 4 | 21      | $200<N, Q \leq 2 000$ |
| 5 | 40      | $2000<N, Q \leq 2 \times 10^5$ |

# Example 1

`flip.in`
```
5
0 1 0 1 1
3
4 5
4 4
1 4
```

`flip.out`
```
1
1
2
```

## Explanation

For the third query, we need to use the **flip** operation for the intervals $[2, 2]$ and $[4, 4]$.

# Example 2

`flip.in`
```
1
1
1 
1 1
```

`flip.out`
```
1
```

