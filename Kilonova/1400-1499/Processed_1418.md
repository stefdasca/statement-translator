
A non-zero natural number $n$ is called *balanced* if in its prime factorization the sum of the bases is equal to the sum of the exponents.

For example, the numbers $72 = 2^3 \cdot 3^2$, $5760 = 2^7 \cdot 3^2 \cdot 5^1$ are *balanced*.

# Task

Write a program that reads two non-zero natural numbers $a$ and $b$ and determines all *balanced* numbers in the closed interval $[a, b]$.

For example, if $a=2$ and $b=99$, the *balanced* numbers between $2$ and $99$ are $4, 27, 48$ and $72$.

# Input data

The input file `cumpanit.in` contains on the first line the non-zero natural numbers $a$ and $b$ separated by exactly one space, as mentioned above.

# Output data

The output file `cumpanit.out` will contain the sought numbers, written in **increasing** order, one on each line.

# Constraints and clarifications

* $2 \leq a \leq b \leq 10^{14}$
* For $25\%$ of the tests, it is guaranteed that $2 \leq a \leq b \leq 10^6$

# Example
`cumpanit.in`
```
2 99
```
`cumpanit.out`
```
4
27
48
72
```
