Two natural numbers $a$ and $b$ with a maximum of $9$ digits are given.

# Task

1. Determine the distinct digits common to the numbers $a$ and $b$.
2. Display the largest number formed from all the digits of $a$ and $b$.

# Input data

From the input file `cifre.in`, the first line contains the values $a$ and $b$ separated by a space.

# Output data

The output data is printed in the output file `cifre.out` on exactly two lines. The answer to the first task will be printed on the first line of the file, with the digits written in strictly increasing order and separated by exactly one space. The answer to the second task will be printed on the second line. In case the two numbers have no common digits, the first line of the output file will contain the value $-1$.

# Constraints and clarifications

* $1 \leq a, b < 10^9$;
* $50\%$ of the score is awarded for the first task and the full score for both tasks solved correctly.

# Example

`cifre.in`
```
2115 29025
```

`cifre.out`
```
2 5
955222110
```