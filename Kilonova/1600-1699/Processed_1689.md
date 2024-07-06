Here is the translated statement:

Fibonacci sequence, defined by $F_1$ = $1$, $F_2$ = $1$ and the recurrence relation $F_k$ = $F_{k-1}$ + $F_{k-2}$, $k \geq 3$. Consider a natural number $N$ and an array $A_1$, $A_2$, $\dots$, $A_N$ of $N$ distinct natural numbers. Additionally, consider a natural number $T$.

# Task

Write a program to determine a value $D$ which represents the number of terms in the Fibonacci sequence $F_1$, $F_2$, $\dots$, $F_T$ that are divisible by **at least one** of the numbers $A_1$, $A_2$, $\dots$, $A_N$.

# Input data

The input file `fibodiv.in` contains in the first line the numbers $N$ and $T$ separated by a space, and in the second line $N$ natural numbers, $A_1$, $A_2$, $\dots$, $A_N$, separated by a space.

# Output data

The output file `fibodiv.out` will contain in the first line the natural number $D$, with the above-mentioned meaning.

# Constraints and clarifications

* $1 \leq N \leq 15$
* $2 \leq T \leq 10^{18}$
* $2 \leq A_i \leq 50$, $1 \leq i \leq N$

# Example

`fibodiv.in`
```
3 20
3 6 10
```

`fibodiv.out`
```
6
```

## Explanation

$N = 3$; $T = 20$; $A_1$ = $3$, $A_2$ = $6$, $A_3$ = $10$

The first $20$ terms of the Fibonacci sequence are: $1$, $1$, $2$, $3$, $5$, $8$, $13$, $21$, $34$, $55$, $89$, $144$, $233$, $377$, $610$, $987$, $1 \ 597$, $2 \ 584$, $4 \ 181$, $6 \ 765$. Among these, there are 6 terms divisible by at least one of the numbers $3$, $6$, $10$ namely: $3$, $21$, $144$, $610$, $987$, $6 \ 765$.