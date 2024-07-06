Maia has just learned in school how to do additions with natural numbers having multiple digits. Because she likes mathematics very much, she started to write many natural numbers, with one or more digits, on a piece of paper and began to add them.

After a while, she got a bit bored and thought about finding the highest sum that could be obtained if the digits of the numbers on the sheet were shuffled. However, she has one wish: after shuffling the digits, the number of numbers with one digit, the number of numbers with two digits, and so on, remain the same.

# Task

Write a program that determines:

1) The maximum sum that can be obtained by shuffling the digits of the initial numbers.
2) A sequence of numbers for which the maximum sum is obtained, respecting the constraints described.

# Input data

The input file `cifre.in` contains the following:

The first line contains a natural number $n$ representing the number of numbers written by Maia on the sheet. The next $n$ lines contain the $n$ natural numbers initially written on the sheet, one number per line.

# Output data

The output file `cifre.out` will contain:

The first line contains a natural number $S$ representing the maximum sum obtained. The following $n$ lines will contain $n$ natural numbers, one number per line, representing a sequence of numbers for which the maximum sum is obtained, respecting the constraints described.

# Constraints and clarifications

* $2 \leq n \leq 100\ 000$
* The initial sequence numbers are non-negative and $\leq 2^{30}-1$.
* The numbers in the output sequence will not contain insignificant zeros.
* If there are multiple sequences for which the maximum sum is obtained according to the constraints described, any of them will be displayed.
* For correctly displaying the maximum sum, $40\%$ of the points are awarded, with the full score obtained by correctly solving both tasks.

# Example

`cifre.in`
```
8
3120
400
1000
50
1
0
37
60
```

`cifre.out`
```
14280
6410
500
10
20
10
0
7330
0
```

## Explanation

It is observed that in both the initial sequence and the final one, there are $2$ numbers with $4$ digits, one number with $3$ digits, $3$ numbers with two digits, and $2$ numbers with one digit.

Additionally, the numbers in the output sequence contain the same digits in total as the numbers in the input file.

The maximum sum that can be obtained is $14\ 280$.