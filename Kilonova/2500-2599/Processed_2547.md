# Task

A perfect number is a number whose sum of its divisors, excluding the number itself, is exactly the number itself.

Given a sequence with $N$ numbers, how many subsequences have a product that is a perfect number less than or equal to a given $X$?

# Input data

The first line contains two integers, $N$ and $X$.  
The second line contains the sequence of $N$ numbers.

# Output data

Print the answer modulo $10^9+7$.

# Constraints and clarifications

* $1 \\leq N \\leq 10^5$
* $1 \\leq X, v_i \\leq 10^9$

# Example

`stdin`
```
6 15
1 3 3 2 6 28
```

`stdout`
```
6
```

## Explanation

The subsequence containing the number $28$ is not counted because it is greater than $X$ even though it is a perfect number ($28=1+2+4+7+14$).  
All subsequences with a product of $6$ are considered valid because $6$ is a perfect number ($6=1+2+3$).