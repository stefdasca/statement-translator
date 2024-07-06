A natural number $n$ is called a **VIP** number if it consists of at least two digits, contains at least one odd digit and at least one even digit, and all odd digits are written before any even digits. (**VIP** = **V**alues **I**mpare **P**are). For example, $352, 7546$ are **VIP** numbers, while $35, 468, 5483, 387$ are not **VIP** numbers. A **VIP** **SEQUENCE** within a string of digits is a succession of digits (the ones on consecutive positions in the string) that form, in order, a **VIP** number.

# Task

Given a string of non-zero digits, determine:

1. The number of **VIP** SEQUENCES in the string.
2. The minimum length of a string of digits that contains the same number of **VIP** SEQUENCES as the given string and has all the odd digits before the even ones.
3. The sum of all numbers that can be formed such that each number contains all the distinct digits of the largest **VIP** number in the given string, with each digit used exactly once, and no other different digit.

# Input data

The file `evip.in` contains:
- On the first line, a natural number $c$ representing the task that needs to be solved ($1$, $2$ or $3$).
- The second line contains a string of non-zero digits, not separated by spaces, representing, in order, the elements of the string.

# Output data

If the task is $c=1$, then the file `evip.out` will contain on the first line a natural number representing the number of **VIP** SEQUENCES in the string.
If the task is $c=2$, then the file `evip.out` will contain on the first line a natural number representing the minimum length of a string of digits that contains the same number of **VIP** SEQUENCES as the given string and has all the odd digits before the even ones.
If the task is $c=3$, then the file `evip.out` will contain on the first line a natural number representing the sum of all numbers that can be formed such that each number contains all the distinct digits of the largest **VIP** number in the given string, with each digit used exactly once, and no other different digit.

# Constraints and clarifications

* The number of digits on the second line of the input file is at least $2$ and at most $10 \ 000$.
* The string contains at least one **VIP** SEQUENCE.
* For tests worth 30% of the score, the task is 1. For tests worth 30% of the score, the task is 2. For tests worth 40% of the score, the task is 3.

# Example 1

`evip.in`
```
1
413643623
```

`evip.out`
```
6
```

## Explanation

There are $6$ **VIP** SEQUENCES in the given string.

# Example 2

`evip.in`
```
2
413643623
```

`evip.out`
```
5
```

## Explanation

The given string contains $6$ **VIP** SEQUENCES. The smallest number of digits in a string that contains $6$ **VIP** SEQUENCES and has all odd digits before the even ones is $5$. An example of such a string is $13246$.

# Example 3

`evip.in`
```
3
413443623
```

`evip.out`
```
1776
```

## Explanation

The largest **VIP** number in the string is $1344$. The distinct digits of this number are ${1, 3, 4}$. The sum of all numbers that can be written, using each digit ${1, 3, 4}$ exactly once, and no other digit, is $1776$. $134 + 143 + 314 + 341 + 413 + 431 = 1776$.