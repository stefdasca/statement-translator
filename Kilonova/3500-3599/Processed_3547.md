# Task

You are given a number $n$ and a sequence of $n$ natural values. Determine how many of the $n$ values have an even number of divisors.

# Input data

The file `divpar.in` contains on the first line the value $n$ and on the second line the $n$ given values, separated by space.

# Output data

The file `divpar.out` contains the required value.

# Constraints and clarifications

* $1 \leq n \leq 1 \ 000$;
* The $n$ given numbers are non-zero natural numbers with a maximum of $8$ digits.

# Example

`divpar.in`
```
7
1 2 6 4 1 2 2
```

`divpar.out`
```
4
```

## Explanation

The number $2$ has two divisors ($1$ and itself) while the number $6$ has $4$ divisors ($1$, $2$, $3$, $6$). The other three numbers have an odd number of divisors.