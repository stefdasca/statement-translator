
A natural number is called palPow if its reversed form has strictly more positive divisors than the number itself. For example, $23$ is a palPow number because $23$ has two positive divisors $(1, 23)$ while its reversed form, $32$, has six positive divisors $(1, 2, 4, 8, 16, 32)$. The reversed form of a number is the value obtained by considering the digits of the number from right to left (for example, the reversed form of $675$ is $576$ and the reversed form of $20310$ is $1302$).

# Task

Given an array of $n$ natural numbers, determine how many palPow numbers are in the array as well as the smallest and largest palPow numbers in the array.

# Input data

The input file contains on the first line the number $n$ and on the second line $n$ natural numbers separated by spaces.

# Output data

The output file will contain on the first line three values separated by a space, representing in order, the number of palPow numbers, the smallest palPow number, and the largest palPow number from the given array.

# Constraints and clarifications

* $1 \leq n \leq 1\ 000$
* The numbers in the array are natural numbers at most equal to $10^9$
* The array contains at least one palPow number

# Example

`palpow.in`
```
6
13 23 231 408 48 36
```

`palpow.out`
```
3 23 231
```
