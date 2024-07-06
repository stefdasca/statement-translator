Let's perform the translation as specified:

---

Let $N$ be a natural number. We define a two-line partition of the number $N$ as being two non-empty sequences of natural numbers $a_1, a_2, \ldots, a_k$ and $b_1, b_2, \ldots, b_p$ ($k \geq p$), with the properties:

* $a_1 > a_2 > \ldots > a_p > \ldots > a_k$
* $b_1 > b_2 > \ldots > b_p$
* $b_1 \leq a_1$, $b_2 \leq a_2$, $\ldots$, $b_p \leq a_p$
* $a_1 + a_2 + \ldots + a_k + b_1 + b_2 + \ldots + b_p = N$

Example:

The $7$ two-line partitions of the number $N = 6$ are:

~[pdl.png]

# Task

Write a program that reads the natural number $N$ and determines the number $P$ of two-line partitions of the natural number $N$.

# Input data

The input file `pdl.in` contains on the first line the natural number $N$.

# Output data

The output file `pdl.out` will contain on the first line the remainder of the division of the number $P$ by $3\ 000\ 017$.

# Constraints and clarifications

* $1 \leq N \leq 2\ 000$
* a sequence of numbers is non-empty if it contains at least one element


# Example

`pdl.in`
```
6
```

`pdl.out`
```
7
```

## Explanation

$N = 6$
There are $7$ two-line partitions according to the example above.