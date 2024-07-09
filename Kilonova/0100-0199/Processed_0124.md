Let `x` be a natural number with exactly `n` digits written in base `10`.

# Task
Write a program that determines the smallest natural number strictly greater than `x`, which has the same digits as the number `x` and is a palindrome.

# Input data
The input file `nr.in` contains two lines. The first line contains `n`, the number of digits of the number `x`. The second line contains the `n` digits of `x`.

# Output data
The output file `nr.out` contains a single line that contains the smallest natural number strictly greater than `x`, which has the same digits as the number `x` and is a palindrome. If no such number exists, the first line of the output file will contain the value `0`.

# Constraints and clarifications
* `2 \leq n \leq 1\ 000`
* A number is called a palindrome if it reads the same from left to right as it does from right to left (for example, `1331, 12321`, etc).
* The first digit of a number must be non-zero.
* By the same digits, it is understood that each digit from `0` to `9` appears in the result the same number of times as in the number `x`.

# Examples

`nr.in`
```
5
12022
```

`nr.out`
```
0
```

`nr.in`
```
5
12200
```

`nr.out`
```
20102
```
