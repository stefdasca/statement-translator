The sequence of natural numbers is generated, whose first terms are, in order:

$1$, $12$, $21$, $123$, $231$, $312$, $1234$, $2341$, $3412$, $4123$, $12345$, $23451$, ...

# Task

Deduce the rule by which the terms of the sequence are generated and write a program that reads the natural numbers $k$, $x$, $a$, and $b$ and determines:

1. the last digit of the sum of all terms of the sequence formed by at most $k$ digits;
2. the successor of term $x$ in the given sequence, where $x$ is a term of the sequence;
3. the number of terms in the sequence that have the most significant digit equal to $a$ and do not contain the digit $b$ in their writing.

# Input data

The input file `sir.in` contains a single line that contains the four natural numbers $k$, $x$, $a$, and $b$, separated by spaces.

# Output data

The output file `sir.out` will contain 3 lines:

* the first line will contain a natural number representing the last digit of the sum of all the terms of the sequence formed by at most $k$ digits;
* the second line will contain a natural number representing the successor of term $x$ in the given sequence;
* the third line will contain a natural number representing the number of terms in the sequence that have the most significant digit equal to $a$ and do not contain the digit $b$ in their writing.

# Constraints and clarifications

* The numbers $k$, $x$, $a$, and $b$ are non-null natural numbers
* $1 \leq k \leq 9$;
* $x$ is a term of the sequence from the statement and has a successor in the sequence
* the successor of term $x$ in the sequence is the term that immediately follows $x$ (for example, if $x = 2341$ then the successor of $x$ in the sequence is $3412$)
* $1 \leq x < 9 \cdot 10^8$;
* $1 \leq a, b \leq 9$; $a \neq b$;
* the most significant digit of a natural number is the first digit from its left-to-right writing (for example, the most significant digit of the number $32156$ is $3$)
* To solve requirement a) 30% of the score is awarded, for requirement b) 40% of the score is awarded, and for requirement c) 30% of the score is awarded.

# Example

`sir.in`
```
3 45123 3 6
```

`sir.out`
```
0
51234
3
```

## Explanation

The terms of the sequence formed by at most $k = 3$ digits are: $1$, $12$, $21$, $123$, $231$, $312$. Their sum being equal to $700$, the first line of the file `sir.out` will contain the digit $0$ (the last digit of the sum).

The successor of term $45123$ is $51234$, which will be written on the second line of the file `sir.out`.

There are $3$ numbers that start with the digit $3$ and do not contain the digit $6$, namely: $312$, $3412$, $34512$. Therefore, the number $3$ is written on the third line of the file `sir.out`.