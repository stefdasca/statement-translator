The text provided in Romanian is translated into English below while preserving the specified formatting, mathematical values, variable names, and custom image format:

---

Consider a one-dimensional array $x$ with $n$ components of distinct natural numbers, each at most $32\ 000$.

# Task

Write a program that constructs the array $y$ with elements from the set $\{1, 2, \dots, n\}$ such that for any natural numbers $i, j$ with the property that $1 \leq i \leq n$, $1 \leq j \leq n$ and $x_i < x_j$, we have $y_i < y_j$.

# Input data

The input file `siruri.in` will contain:

* the first line will contain the number $n$
* the second line will contain the components of the array $x$ separated by a space

# Output data

The output file `siruri.out` will contain the first line with the components of the array $y$ separated by a space.

# Constraints and clarifications

* $1 \leq n \leq 100$;
* The components of the array $x$ are natural numbers each at most $32\ 000$.

# Example

`siruri.in`
```
6
12 3 7 16 10 1
```

`siruri.out`
```
5 2 3 6 4 1
```
---

Please double check for grammar and syntax issues according to the rules of English language.