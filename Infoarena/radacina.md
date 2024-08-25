## Task

Given a polynomial $P$ of odd degree $G$ and of the form $P(x) = A[G] * x^G + A[G - 1] * x^{G - 1} + \dots + A[1] * x^1 + A[0] * x^0$, find a root of it. A real number $x$ is called a root of the polynomial $P$ if and only if $P(x) = 0$.

## Input data

The input file `radacina.in` will contain on the first line the degree $G$ and on the next line $G + 1$ real numbers representing the coefficients $A[i]$, for $i$ from $0$ to $G$.

## Output data

The output file `radacina.out` will print on the first line a root of the polynomial.

## Constraints and clarifications

$1 \leq G \leq 7$

$-1\ 000\ 000\ 000 \leq A[i] \leq 1\ 000\ 000\ 000$

It is guaranteed that all solutions of the given polynomial are real and lie within the interval $(-20, 20)$.

A number $x$ will be considered correct if the absolute difference between $x$ and the actual root is less than $10^{-5}$.

## Example

`radacina.in`

```
3
-250 -100 2.5 1
```

`radacina.out`

```
10
```

## Explanation

$P(x) = 1 * x^3 + 2.5 * x^2 + (-100) * x^1 + (-250) * x^0$

This polynomial has 3 real roots: $10$, $-2.5$, and $-10$.