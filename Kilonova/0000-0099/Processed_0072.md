# Task

Miguel received a list with $N$ natural numbers. Each natural number has a "postal code" associated with it, which is equal to the sum of all previous numbers smaller than it. Miguel wants to find out the sum of the postal codes.

# Input data

The first line contains the number $N$ (the number of numbers), and the second line contains those $N$ numbers.

# Output data

The first line will contain the sum of all postal codes.

# Constraints and clarifications

* $1 \leq N$
* No given number exceeds $1000000$

# Example

`stdin`
```
5
1 4 3 5 3
```

`stdout`
```
11
```

# Explanation

The postal codes are $0, 1, 1, 8, 1$, and their sum is $11$.