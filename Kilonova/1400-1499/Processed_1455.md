Mihai loves fun mathematics or maybe fun more than mathematics. To avoid homework, he invented the "smile" operation denoted by the symbol ☺, an operation that applies to non-zero natural numbers according to the examples below:
$6 \☺\ 4 = 210$
$9 \☺\ 2 = 711$
$8 \☺\ 5 = 313$
$7 \☺\ 6 = 113$
$6 \☺\ 6 = 12$
$6 \☺\ 10 = 416$
$43 \☺\ 1500 = 14571543$
$23 \☺\ 23 = 46$

The math teacher promised Mihai a grade of $10$ for the invention, only if he correctly determines the number of even divisors for the result obtained through the “smile� operation. Thus, Mihai received $N$ pairs of numbers ($a$, $b$) for which he needs to calculate $a \☺\ b$ and determine if the result obtained has even divisors.

# Task

Write a program that reads a natural number $N$ and $N$ pairs of natural numbers ($a$, $b$) and displays:

1. for each pair of numbers ($a$, $b$), the result $a \☺\ b$;
2. the smallest and the largest result $a \☺\ b$ that has no even divisors.

# Input data

The input file `inventie.in` contains on the first line a natural number $N$. Each of the following $N$ lines contains two natural numbers $a$, $b$ separated by a space.

# Output data

In the output file `inventie.out`:

* for each of the $N$ pairs ($a$, $b$), print the result $a \☺\ b$, each result on a separate line, in the order in which the pairs appear in the input file;
* if all $N$ results obtained have even divisors, print the value $0$ (zero) on line $N+1$;
* if at least one result is obtained without even divisors, then on line $N+1$ print the smallest result $a \☺\ b$ that has no even divisors, and on line $N+2$ print the largest result $a \☺\ b$ that has no even divisors. If only one result does not have even divisors, then this result will be written both on line $N+1$ and on line $N+2$.

# Constraints and clarifications

* $1 \leq N \leq 20$
* $a$ and $b$ are non-zero natural numbers with a maximum of $18$ digits each

# Example 1

`inventie.in`
```plaintext
8
6 4
9 2
8 5
7 6
6 6
6 10
43 1500
23 23
```

`inventie.out`
```plaintext
210
711
313
113
12
416
14571543
46
113
14571543
```

## Explanation

Using the “smile� operation, the values obtained in order are $210$, $711$, $313$, $113$, $12$, $416$, $14571543$, $46$. Among these, the numbers that do not have even divisors are $711$, $313$, $113$, $14571543$, with the smallest being $113$ and the largest $14571543$.

# Example 2

`inventie.in`
```plaintext
2
13 13
268 1244
```

`inventie.out`
```plaintext
26
9761512
0
```

## Explanation

Using the “smile� operation, the values obtained in order are $26$, $9761512$, both numbers having even divisors.
