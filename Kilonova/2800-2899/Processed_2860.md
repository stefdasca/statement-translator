
With the help of three given digits $a$, $b$, $c$, where $a > 0$, the following sequence of numbers is constructed: $\overline{\text{a}}$, $\overline{\text{ab}}$, $\overline{\text{abc}}$, $\overline{\text{abca}}$, $\overline{\text{abcab}}$, $\overline{\text{abcabc}}$, $\dots$.

For example, for $a=1$, $b=3$, $c=7$, we can construct the sequence: $1$, $13$, $137$, $1371$, $13713$, $137137$, $1371371$, $13713713$, $\dots$.

# Task

Write a program that determines how many numbers divisible by $k$ can be found in the first $n$ terms of the given sequence.

# Input data

The input file `sirdivk.in` contains on the first line the numbers $a$, $b$, $c$, $n$, $k$.

# Output data

The output file `sirdivk.out` contains a single line which contains the number $nr$ of numbers divisible by $k$ among the first $n$ terms of the given sequence.

# Constraints and clarifications

* $1 < n < 1 \ 000$
* $2 \leq k < 32 \ 000$
* $1 \leq a \leq 9$
* $0 \leq b,c \leq 9$

# Example

`sirdivk.in`
```
7 2 1 8 3 
```

`sirdivk.out`
```
2
```

## Explanation

Among the first $8$ terms of the sequence: $7$, $72$, $721$, $7217$, $72172$, $721721$, $7217217$, $72172172$, $\dots$ there are two terms divisible by $3$.
