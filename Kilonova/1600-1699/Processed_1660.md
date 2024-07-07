
Given a natural number $a$ having $n$ digits.

# Task

Write a program that determines a natural number $x$ with the property that it is the smallest number greater than $a$, which has exactly the same digits as the number $a$.

# Input data

The input file `numar.in` contains two lines:

- the first line contains a natural number representing the value of $n$;
- the second line contains, without spaces between them, $n$ digits representing the number $a$.

# Output data

The output file `numar.out` will contain a single line that will contain the number $x$.

# Constraints and clarifications

* $1 \leq n \leq 5 \ 000 \ 000$;
* for $50\%$ of the tests, $n \leq 1 \ 000 \ 000$;
* there is a solution for all test cases.

# Example

`numar.in`
```
6
204924
```

`numar.out`
```
204942
```

## Explanation

There are several numbers formed from exactly the same digits as the number $204 \ 924$ that are greater than it. Among these, $204 \ 942$ is the smallest.
