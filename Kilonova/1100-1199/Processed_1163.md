Some natural numbers consist only of distinct non-zero digits. Among these, some, called circular numbers, have the following property: starting from the first digit and counting to the right, digit by digit, as many digits as indicated by the digit itself, a new digit is determined. By proceeding in the same way for this and for all subsequent ones, we will return to the first digit. If all the digits have been visited exactly once, the number is called circular.

For example, the number $1\ 894\ 256$ is circular because:

* It has only distinct digits
* It does not contain the digit $0$
* Starting from $1$, we obtain, in sequence: $8, 9, 2, 6, 5, 4, 1$

# Task

Write a program that, for a given $N$, determines how many circular numbers are less than or equal to $N$, as well as the largest circular number less than or equal to $N$.

# Input data

The input file `circular.in` contains the natural number $N$.

# Output data

The output file `circular.out` contains a single line, which contains the number of circular numbers less than $N$ and the required maximum circular number, separated by a space.

If there is no circular number less than $N$, the output file will contain the two values $0$ separated by a space.

# Constraints and clarifications

* $10 \leq n < 10\ 000\ 000$

# Example

`circular.in`
```
1894250
```

`circular.out`
```
347 1849625
```

# Explanation

There are $347$ circular numbers less than $1\ 894\ 250$, the largest of these being $1\ 849\ 625$