Alinuța noticed that from the sequence of consecutive numbers $1, 2, 3, 4, 5, 6, 7, 8, 9, 10$, she can form sums of two terms such that the result is not divisible by a given value $k$. For example, for $k = 9$, she can consider the terms $1, 2, 3, 4, 9, 10$ because no matter how she forms sums with two terms, the result is not divisible by $9$.

# Task

Given two natural numbers $n$ and $k$, determine the maximum number of terms that can be taken from the sequence $1, 2, 3, \dots, n$, such that no matter how two distinct terms are chosen, their sum is not divisible by $k$.

# Input data

The input file `suma.in` contains a single line consisting of two values $n$ and $k$ separated by a space.

# Output data

The output file `suma.out` contains on the first line a single value representing the maximum number of terms that can be chosen from the $n$ terms with the property that the sum of any two numbers from the determined set is not divisible by $k$.

# Constraints and clarifications

* $0 \lt n \leq 2\ 000\ 000\ 000$
* $0 \lt k \leq 10\ 000$

# Example

`suma.in`
```
15 7
```

`suma.out`
```
8
```

## Explanation

The values can be chosen as:
${1, 2, 3, 7, 8, 9, 10, 15}$ or
${1, 4, 5, 7, 8, 11, 12, 15}$ etc.