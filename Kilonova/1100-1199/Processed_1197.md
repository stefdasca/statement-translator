Ionel has a mathematics problem to solve, which involves calculating an expression containing parentheses, addition, subtraction, multiplication, and division with natural numbers. The issue is that Ionel does not feel like calculating, so he started playing with all the numbers in the expression: he separated them into their component digits and, because he heard about palindromic numbers from a colleague who knew some computer science, he tried to write the largest number possible with the digits he has, which is also a palindrome. Because the game seemed too simple, he decided that if he uses a digit, he should use it as many times as it appears in the arithmetic expression.

# Task

Given the digits from the expression, determine the largest palindromic number that can be formed according to the above rule. A number is a palindrome if reading it from left to right has the same value as reading it from right to left (example: $17271$).

# Input data

The input file `palindrom.in` contains the following:

- The first line contains $n$, the number of digits of the number.
- The next $n$ lines contain each digit of the number.

# Output data

The output file `palindrom.out` should contain a single integer, which is the largest palindromic number that can be formed according to the above rule.

# Constraints and clarifications

* $1 \leq n \leq 10 \ 000$

# Example 1

`palindrom.in`
```
4
2
4
5
2
```

`palindrom.out`
```
252
```

# Example 2

`palindrom.in`
```
7
2 
2 
3 
5 
3 
3 
2
```

`palindrom.out`
```
333
```
