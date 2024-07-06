A sequence of natural numbers is generated with the first terms being, in this order:
$1$, $20$, $21$, $300$, $301$, $320$, $321$, $4000$, $4001$, $4020$, $4021$, $4300$, $401$, $4320$, $4321$, $50000$, $\dots$

# Task

Determine the rule by which the terms of the sequence are generated and write a program that reads the natural numbers $k$, $n$, and $x$ and determines:
1. the number of terms in the sequence that have the first digit (the most significant digit) equal to $k$;
2. the $n$-th term of the sequence from the statement;
3. the largest term of the sequence less than or equal to $x$.

# Input data

The input file `nr.in` contains a single line that contains three natural numbers $k$, $n$, and $x$, separated by a space.

# Output data

The output file `nr.out` will contain $3$ lines:

* the first line will contain a natural number representing the number of terms in the sequence that have the first digit (the most significant digit) equal to $k$;
* the second line will contain a natural number representing the $n$-th term of the sequence from the statement;
* the third line will contain a natural number representing the largest term of the sequence less than or equal to $x$.

# Constraints and clarifications

* $1 \leq k \leq 9$
* $3 \leq n \leq 511$
* $1 \leq x \leq 2 \ 000 \ 000 \ 000$
* Solving task 1 will grant $30\%$ of the score, solving task 2 will grant $30\%$ of the score, and solving task 3 will grant $40\%$ of the score.

# Example

`nr.in`
```
4 19 57890
```

`nr.out`
```
8
50021
54321
```

## Explanation

The first line of the file `nr.out` contains the number $8$, because there are $8$ terms in the sequence with the first digit equal to $k = 4$.

The second line of the file contains the number $50021$, because the $n$-th term ($n = 19$) in the sequence is $50 \ 021$.

The numbers $54 \ 321$ and $600 \ 000$ are two consecutive terms in the sequence mentioned in the statement, and $54 \ 321 \leq 57 \ 890 < 600 \ 000$. Therefore, the number $54 \ 321$ is written on the last line of the file `nr.out`.