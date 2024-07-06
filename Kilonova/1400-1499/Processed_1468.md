```markdown
Three positive natural numbers $n, k$ and $w$ are given.

# Task

Write a program that determines the number $m$ of sets of the form $\{x_1, x_2, \ldots, x_k\}$ with positive natural number elements, which simultaneously satisfy the conditions:

* $1 \leq x_1 < x_2 < \ldots < x_k \leq n$
* $x_{i+1} - x_i \geq w, 1 \leq i \leq k - 1$

# Input data

The input file `nmult.in` contains the first line with three positive natural numbers $n, k, w$ separated by a space, as described above.

# Output data

The output file `nmult.out` will contain the first line with the remainder of the division of number $m$ by $666 \ 013$.

# Constraints and clarifications

* $1 \leq n, k, w \leq 1 \ 000 \ 000$

# Example 1

`nmult.in`
```
5 2 2
```

`nmult.out`
```
6
```

## Explanation

$n=5, k=2, w=2$

There are $6$ sets with $2$ elements, such that the difference between any $2$ consecutive terms is at least $2$: $\{1,3\}$, $\{1,4\}$, $\{1,5\}$, $\{2,4\}$, $\{2,5\}$, $\{3,5\}$.

# Example 2

`nmult.in`
```
10 3 4
```

`nmult.out`
```
4
```

## Explanation

$n=10, k=3, w=4$

There are $4$ sets with $3$ elements, such that the difference between any $2$ consecutive terms is at least $4$: $\{1,5,9\}$, $\{1,5,10\}$, $\{1,6,10\}$, $\{2,6,10\}$.

# Example 3

`nmult.in`
```
10 4 4
```

`nmult.out`
```
0
```

## Explanation

$n=10, k=4, w=4$

There is no set of $4$ elements where the conditions are met.
```