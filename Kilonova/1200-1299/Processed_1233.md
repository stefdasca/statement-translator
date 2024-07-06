For a sequence $x_1, x_2, \dots, x_n$, we say that the element $x_k$ is visible from the left if for any $i$, $1 \leq i < k$ we have $x_i < x_k$. Similarly, we say that $x_k$ is visible from the right if for any $i$, $k < i \leq n$ we have $x_i < x_k$ (the first element is considered visible from the left, and the last from the right).

# Task

We consider the permutations of the set $\{1, 2, \dots, n\}$. Determine how many of these permutations have $p$ elements visible from the left and $q$ elements visible from the right.

# Input data

The input file `vizibil.in` contains natural numbers $n$, $p$, $q$, separated by a space, in the first line.

# Output data

The output file `vizibil.out` will contain the number of permutations that satisfy the condition from the statement modulo $997$, in the first line.

# Constraints and clarifications

* $2 < n < 101$
* $0 < p, q \leq n$

# Example

`vizibil.in`
```
4 2 3
```

`vizibil.out`
```
3
```

## Explanation

The permutations with two elements visible from the left and $3$ visible from the right are $(1, 4, 3, 2), (2, 4, 3, 1), (3, 4, 2, 1)$