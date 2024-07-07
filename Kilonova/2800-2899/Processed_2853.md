Gigel has learned a new word at school: *palindrome*. He now knows that a palindrome is a construction made up of letters and/or digits that looks the same whether read from the beginning to the end or from the end to the beginning. For example, the numbers $2552$ and $12321$ have the palindrome property. Because Gigel likes to play with numbers, he poses the following problem: given a natural number, can its digits be rearranged to form a palindrome? If yes, what is the maximum palindrome number that can be obtained?

# Task

Given a natural number $n$, determine the largest palindrome number that can be obtained by rearranging the digits of the number $n$.

# Input data

The input file `palindrom.in` contains on the first line the natural number $n$.

# Output data

The output file `palindrom.out` contains on the first line the largest palindrome number that can be obtained by rearranging the digits of the number $n$.

# Constraints and clarifications

* $1 \leq n < 2^{31}$
* For the test data, a solution always exists.

# Example

`palindrom.in`
```
3121321
```

`palindrom.out`
```
3211123
