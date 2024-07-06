A natural number $x$ is called *freaky* if and only if it has an odd number of non-null natural divisors. For example, $10$ is not freaky because it has $4$ divisors ($1$, $2$, $5$, $10$), but $9$ is freaky because it has $3$ divisors ($1$, $3$, $9$).

A natural number $x$ is called a *didivisor* of a natural number $y$ if and only if it satisfies the following two properties:
* $x$ is *freaky*;
* $y$ is divisible by $x$.

# Task

Given $n$ and an array $a_1, a_2, \dots, a_n$, for each $i$ from $1$ to $n$, display the number of *didivisors* of $a_i$.

# Input data

The first line of the input file ```didivizori.in``` contains the number $n$. The second line contains the array $a_1, a_2, \dots, a_n$.

# Output data

Print the answer for each $i$ from $1$ to $n$ in the output file ```didivizori.out```.

# Constraints and clarifications

* $1 \leq n \leq 100$
* $1 \leq a_i \leq 10^9$

|#|Points|Constraints|
|-|-|--------|
|1|30|$a_i \leq 10$|
|2|30|$a_i \leq 1\ 000$|
|3|40|No additional constraints|

# Example

`didivizori.in`
```
11
1 2 3 4 5 6 7 8 9 10 16
```

`didivizori.out`
```
1 1 1 2 1 1 1 2 2 1 3
```

## Explanation

The only didivisor of $1$ is $1$. We can check that it meets both properties.

The only didivisor of $2$ and $3$ is $1$.

The didivisors of $4$ are $1$, $4$.

The didivisors of $8$ are $1$, $4$.

The didivisors of $9$ are $1$, $9$.

The didivisors of $16$ are $1$, $4$, $16$.