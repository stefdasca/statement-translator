```markdown
Consider a sequence consisting of $N+2$ binary digits, which contains at least one digit $1$ and at least three digits $0$; the first and the last digits of the sequence are $0$.
We define a __1-sequence__ as a succession made only of digits $1$, found in consecutive positions in this sequence, delimited by a digit $0$.
Corina constructs such a sequence, in which the number of digits $1$ in each __1-sequence__ is between two given natural numbers, $p$ and $q$ ($p \leq q$).

# Task

Write a program that determines a natural number $K$, equal to the remainder of the division by $666013$ of the number of distinct sequences of the type constructed by Corina.

# Input data

The input file `unuzero.in` contains on the first line the natural number $N$, and on the second line the natural numbers $p$ and $q$ ($p \leq q$), separated by a space.

# Output data

The output file `unuzero.out` will contain on the first line the requested natural number $K$.

# Constraints and clarifications

* $1 \leq p \leq q < N < 1 \ 000 \ 000$
* For $20$% of the tests $N \leq 25$, and for another $40$% of the tests $25 < N \leq 1 \ 000$.

# Example

`unuzero.in`
```
5
2 3
```

`unuzero.out`
```
8
```

# Explanation

$$
0 \ 0 \ 0 \ 0 \ 1 \ 1 \ 0 \\
0 \ 0 \ 0 \ 1 \ 1 \ 0 \ 0 \\
0 \ 0 \ 0 \ 1 \ 1 \ 1 \ 0 \\
0 \ 0 \ 1 \ 1 \ 0 \ 0 \ 0 \\
0 \ 0 \ 1 \ 1 \ 1 \ 0 \ 0 \\
0 \ 1 \ 1 \ 0 \ 0 \ 0 \ 0 \\
0 \ 1 \ 1 \ 0 \ 1 \ 1 \ 0 \\
0 \ 1 \ 1 \ 1 \ 0 \ 0 \ 0
$$
```