The text has been converted into an English-language competitive programming problem statement according to the given specifications. Here is the translated version:

---

At a bank, there are $n$ safes, whose secret access codes are natural numbers (let's denote the sequence of access codes by $s_1, s_2, \dots, s_n$). Due to an incident, some codes similar to the secret codes became public (let's denote the sequence of similar codes by $c_1, c_2, \dots, c_p$). To increase the security of the safes, it was decided to modify the codes $s_1, s_2, \dots, s_n$, using the codes $c_1, c_2, \dots, c_p$, in the following way.

For each code $s_i$, an associated code from the sequence $c_k$ is determined as follows:
- The code $s_i$ can be associated with the code $c_k$ if at least half of the digits of $s_i$ are contained in $c_k$ in case the number of digits of $s_i$ is even; and at least half +1 of the digits of $s_i$ are contained in $c_k$ if the number of digits of $s_i$ is odd.
- If there are multiple codes from the sequence $c$ that can be associated with a code $s_i$, the code that contains the largest number of common digits with $s_i$ will be chosen.
- If there are multiple codes $c_k$ with the same maximum number of common digits with the code $s_i$, the first one among them (the one with the smallest index) will be chosen.

The code $s_i$ is transformed into a new natural number $t_i$, obtained as follows:
- All common digits with the chosen $c_k$ are removed from $s_i$;
- The largest number is formed with all remaining digits after removal and this will be $t_i$; if the obtained $t_i$ is smaller than $12\ 345$, it is added to the number $12\ 345$.

# Task

Write a program that determines the sequence of codes $t$, obtained by transforming the initial codes $s$, based on the sequence $c$.

# Input data

The input file `cod.in` contains:
- The first line contains the numbers $n$ and $p$ separated by a space.
- The second line contains $n$ numbers representing the codes in the sequence $s$.
- The third line contains $p$ numbers representing the codes in the sequence $c$.

# Output data

The output file `cod.out` contains on a single line the sequence of numbers $t_1, t_2, \dots, t_n$ separated by a space.

# Constraints and clarifications

* $1 < n, p \leq 100$
* The codes in the sequence $s$ are distinct and each code contains at least $5$ distinct digits.
* $12\ 345 \leq s_i, c_k \leq 2\ 100\ 000\ 000$

# Example

`cod.in`
```
4 5
134925 32960 18542 195633
305285 3067583 20375 29785 213198
```

`cod.out`
```
12399 12441 12386 12436
```

