
# Task

You are given $n$ numbers. Find how many **non-prime primes** exist in the given sequence.

A **non-prime prime** number is a number that has the property that all of its digits are prime numbers, but the number itself is not prime.

# Input data

The first line of the input file `neprim.in` contains $n$, the number of numbers in the sequence. The following line contains these $n$ numbers in the sequence, which are natural numbers with at most $9$ digits.

# Output data

The first line of the output file `neprim.out` will contain a single integer, the number of **non-prime primes** in the sequence.

# Constraints and clarifications

* $1 \leq n \leq 1000$;
* $1 \leq v_i < 10^9$;

# Example

`neprim.in`
```
6
34 23 130 325 777 120
```

`neprim.out`
```
2
```

## Explanation

The two non-prime prime numbers in the sequence are $325$ (it is divisible by $5$) and $777$ (it is divisible by $111$).
