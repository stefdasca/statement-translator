To convert a number from decimal to binary, we will repeatedly divide it by $2$ until we obtain a quotient of zero. Then we will collect the remainders from last to first. These remainders are the digits in the binary representation of the given number, from left to right. For example, $13_{(10)} = 1101_{(2)}$.

# Task

Write a program that, for a given array of $n$ natural numbers, solves the following tasks:
1) Determine the largest of the $n$ given numbers that has the maximum number of $1$s in its binary representation.
2) Determine the longest subarray of numbers that have an equal number of $1$s in their binary representations. If there are multiple such subarrays of maximum length, the leftmost will be chosen. A subarray is a subsequence of numbers that appear in consecutive positions in the initial array.

# Input data

The file `binar.in` contains on the first line the number $C$ representing the task ($1$ or $2$), on the second line the natural number $n$, and on the third line $n$ natural numbers separated by a space.

# Output data

If $C = 1$, then the first line of the output file `binar.out` will contain the number representing the answer to task $1$.
If $C = 2$, then the first line of the output file `binar.out` will contain, separated by a space, the maximum length of the determined subarray and the position of the first term in the subarray (considering that the first number of the $n$ given numbers is at position $1$).

# Constraints and clarifications

* $1 \leq n \leq 1\ 000\ 000$;
* The values in the input array are natural numbers of at most $9$ digits.
* For $30\%$ of the tests, the task will be $C=1$.

# Example 1

`binar.in`
```
1
7
16 12 3 5 14 13 11
```

`binar.out`
```
14
```

## Explanation

$16_{(10)}=10000_{(2)}$; $12_{(10)}=1100_{(2)}$; $3_{(10)}=11_{(2)}$; $5_{(10)}=101_{(2)}$; $14_{(10)}=1110_{(2)}$; $13_{(10)}=1101_{(2)}$; $11_{(10)}=1011_{(2)}$;
The largest number of $1$s in a binary representation is $3$; the largest number that has $3$ $1$s in its binary representation is $14$.

# Example 2

`binar.in`
```
2
7
16 12 3 5 14 13 11
```

`binar.out`
```
3 2
```

## Explanation

There are two subarrays of maximum length of numbers that have an equal number of $1$s in their binary representation: $12 \ 3 \ 5$ and $14 \ 13 \ 11$. We will choose the leftmost one, which has a length of $3$ and starts at position $2$.