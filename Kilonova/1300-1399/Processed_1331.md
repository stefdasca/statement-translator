```markdown
We define the notion of ordered pair, the pair of natural numbers $(x,y)$ with $x \leq y$. We define the least common multiple of an ordered pair as the least common multiple of the numbers that form the pair.
$k$ natural numbers $n_1, n_2, \dots, n_k$ are given.

# Task
Determine for each of the numbers $n_i (i = 1, 2, \dots ,k)$:

1. how many ordered pairs have the least common multiple equal to $n_i$.
2. among these, the ordered pair that has the minimum sum.

# Input data

The first line of the file `cmmmc.in` contains a natural number $k$. The next $k$ lines of this file will contain one natural number each; line $i + 1$ will contain the number $n_i (i = 1, 2, ..., k)$.

# Output data

The file `cmmmc.out` will contain $k$ lines. Each of these will contain three numbers. The three numbers on line $i$ will represent:
- first, the number of ordered pairs that have the least common multiple equal to $n_i$;
- the next two, the numbers that make up the ordered pair that has the least common multiple equal to $n_i$ and whose sum is minimal, displayed in increasing order.

# Constraints and clarifications

* $1 \leq k \leq 100$ 
* $1 \leq n_i \leq 2\ 000\ 000\ 000$
* For $20\%$ of the tests,  $k \leq 100$ and $n_i \leq 1\ 000$
* Each of the $k$ lines of the `cmmmc.out` file must contain exactly three numbers separated by a space; otherwise, the solution is considered incorrect and $0$ points are awarded for the respective test. Correctly solving task $1$ is worth $40\%$ of a test’s score, while correctly solving task $2$ is worth $60\%$.

# Example

`cmmmc.in`
```
2
10
11
```

`cmmmc.out`
```
5 2 5
2 1 11
```

## Explanation

There are five distinct pairs that have the least common multiple equal to $10$: $(1, 10)$, $(2, 10)$, $(5, 10)$, $(2, 5)$, $(10, 10)$. Among these pairs, the one with the smallest sum is $(2, 5)$.
For $n = 11$ there are two ordered pairs that have the least common multiple $11$: $(1, 11)$, $(11, 11)$. Among these pairs, the one with the smallest sum is $(1, 11)$.
```