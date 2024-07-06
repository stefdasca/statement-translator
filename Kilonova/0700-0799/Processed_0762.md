Dexter inherited a fabulous fortune, but it is locked in a safe. His uncle, the one who left him the fortune, wanted to put him to the test as follows: he filled a very large box with balls on which natural numbers from the set $\{0, 1, 2, \dots, 99\}$ are written. On each ball, only one number is written. Dexter has to form pairs of balls that have the same number written on them. In the end, a few balls without a pair will remain. The access code to the safe is formed from the numbers left on the balls without a pair, arranged in ascending order and without any space between them.

# Task

Write a program that provides the access code to the safe.

# Input data

The input file `cod.in` contains on the first line the natural number \( n \), representing the number of balls in the box. On the next line of the file are the \( n \) numbers written on the balls, separated by a space.

# Output data

The output file `cod.out` will contain on the first line the numbers that make up the code, in ascending order and without spaces between them.

# Constraints and clarifications

* \( 1 \leq n \leq 90\ 000 \);

# Example

`cod.in`
```
10
11 3 11 11 12 2 11 12 3 11
```

`cod.out`
```
211
```

## Explanation

The pairs of balls that can be formed are: $(11, 11); (3, 3); (12, 12); (11, 11)$, and the remaining balls are those with the numbers $11$ and $2$. These numbers, written in ascending order and without spaces between them, give us the code $211$.

