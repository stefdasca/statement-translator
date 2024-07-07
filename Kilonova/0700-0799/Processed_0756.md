
Given $n$ natural numbers $x_1, x_2, \dots, x_n$. Large numbers can be formed by writing the numbers of a subarray consecutively without spaces between them.

# Task

Among all large numbers formed as mentioned above, the task is to determine the largest one that is a palindrome.

# Input data

The input file `mare.in` contains on the first line the number $n$, and on the second line the natural numbers $x_1, x_2, \dots, x_n$ separated by a space.

# Output data

The output file `mare.out` will contain on the first line the large number from the task.

# Constraints and clarifications

* $1 \leq n \leq 100$;
* $x_1, x_2, \dots, x_n$ are natural numbers with a maximum of 9 digits.
* By subarray of numbers in an array of numbers, we mean one or more numbers situated immediately one after another in the array.
* By palindromic number we mean a number which, read from left to right or from right to left, gives the same number.
* All tests used for evaluation contain at least one large number.

# Example

`mare.in`
```
9
80 1 23 2 1 401 10 4 900
```

`mare.out`
```
401104
```

## Explanation

The subarrays of numbers that give palindromic large numbers are: $(1)$, $(1, 23, 2, 1)$, $(2)$, $(1)$, $(401, 10, 4)$ and $(4)$.

These give us the large numbers $1$, $12321$, $2$, $1$, $401104$ and $4$. Among these, the largest is the penultimate one.
