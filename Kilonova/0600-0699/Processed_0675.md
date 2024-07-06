# Task

We define a **power** as a natural number $P$ with the property that there exist other two natural numbers $A > 1$ and $B > 1$ such that $P = A^B$. Examples of powers: $8 = 2^3$; $625 = 5^4$; $7776 = 6^5$.

# Task

Given $N$ a natural number and $V$ an array of $N$ natural numbers $V = (V_1, V_2, \ldots, V_N)$.

Write a program that determines a natural number $X$ with the property that the numbers in $(X \cdot V_1, X \cdot V_2, \ldots, X \cdot V_N)$ become **simultaneously** powers.

# Input data

The input file `powall.in` contains in the first line a natural number $N$, and in the second line $N$ natural numbers $V_i$, $1 \leq i \leq N$, separated by a space.

# Output data

The output file is `powall.out`.

The desired number $X$ will be written in the output file decomposed into prime factors as follows:

* The first line will contain a number $F$, representing the number of prime factors of $X$.
* On each of the following $F$ lines, a pair of natural numbers $B$ and $E$ ($B > 1$ and $E > 0$, where $B$ represents a prime factor and $E$ represents the exponent of $B$ in the prime factorization of $X$) will be written, separated by a space.

# Constraints and clarifications

* $2 \leq N \leq 10$
* $2 \leq V_i < 10^{12}$, $1 \leq i \leq N$
* The order of writing the pairs $(B, E)$ is not important;
* Only pairs $(B, E)$ for which $B$ is a prime factor of the factorization of at least one of the numbers $V_i$, $1 \leq i \leq N$ are accepted;
* Any two pairs $(B, E)$ must have distinct $B$ values.
* Only solutions for which both values $(B, E) \leq 2^{60}$ are accepted;
* It is guaranteed that a solution exists.

# Example

`powall.in`
```
3
2 3 6
```

`powall.out`
```
2
2 9
3 14
```

## Explanation

$N = 3$ and $V = (2, 3, 6)$

A possible solution is $X = 2448880128 = 2^9 \cdot 3^{14}$.

$X \cdot V = (2^{10} \cdot 3^{14}, 2^9 \cdot 3^{15}, 2^{10} \cdot 3^{15}) = ((2^5 \cdot 3^7)^2, (2^3 \cdot 3^5)^3, (2^2 \cdot 3^3)^5)$.