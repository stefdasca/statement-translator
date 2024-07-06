Alex is a boy who loves to read and keeps track of how much he's read over the last $n$ days. More precisely, he has noted down how many pages he read each day. Even though his passion is literature, he also wants to improve his computer science skills. Alex has two questions about the sequence of the number of pages he read in the last $n$ days, but after spending a few days thinking about them, he realized they are too difficult for him. Help him find the answers!

# Task

Given the number $n$, the number $p$, and the sequence of values noted by Alex over the $n$ days, determine the answer to the following questions that are troubling Alex:

1. How many triplets of numbers in consecutive positions in the given sequence fulfill the condition that their greatest common divisor has at most $p$ natural divisors?
2. What is the maximum length of a subarray in the given sequence in which the greatest common divisor of any triplet of numbers in consecutive positions has at most $p$ natural divisors?

# Input data

The file `avid.in` contains on the first line a natural number $C$, with the value $1$ or $2$, representing the number of the question. The second line contains two natural numbers $n$ and $p$, in this order, with the meaning given in the statement. The third line of the file contains $n$ natural numbers representing the sequence of values noted over the $n$ days. The numbers on the same line of the file are separated by a space.

# Output data

The file `avid.out` will contain a single number, representing the answer for the given question, $C$.

# Constraints and clarifications

* $1 \le C \le 2$
* $3 \le n \le 1 \ 000 \ 000$
* $2 \le p \le 100$
* $1 \le a_i \le 5 \ 000 \ 000$, where $a_i$ is the number of pages read by Alex on day $i$ (Alex reads at an impressive speed)
* For the first task, it is guaranteed that there is at least one triplet with the indicated property.
* For the second task, it is guaranteed that there is at least one valid sequence with the indicated property.

| # | Points | Constraints |
| - | ------ | ------------|
|1|12|$C = 1$, $n \le 1 \ 000$|
|2|17|$C = 1$, $1 \ 000 \lt n \le 1 \ 000 \ 000$|
|3|29|$C = 2$, $n \le 1 \ 000$|
|4|42|$C = 2$, $1 \ 000 \lt n \le 1 \ 000 \ 000$|

# Example 1

`avid.in`
```
1
10 3
12 48 36 6 3 7 12 16 24 3
```
`avid.out`
```
6
```

## Explanation

$gcd(12, 48, 36) = 12$, which has $6$ natural divisors.

$gcd(48, 36, 6) = 6$, which has $4$ natural divisors.

$gcd(36, 6, 3) = 3$, which has $2$ natural divisors.

$gcd(6, 3, 7) = 1$, which has $1$ natural divisor.

$gcd(3, 7, 12) = 1$, which has $1$ natural divisor.

$gcd(7, 12, 16) = 1$, which has $1$ natural divisor.

$gcd(12, 16, 24) = 4$, which has $3$ natural divisors.

$gcd(16, 24, 3) = 1$, which has $1$ natural divisor.

Thus, $6$ out of the $8$ triplets have at most $p = 3$ natural divisors.

# Example 2

`avid.in`
```
2
7 2
12 48 36 6 3 7 12
```
`avid.out`
```
5
```

## Explanation

Since $p = 2$, the longest sequence is $36, 6, 3, 7, 12$.