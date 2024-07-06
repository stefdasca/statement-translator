Here is the translated statement:

---

A number is called a **palindrome** if its first digit is equal to its last digit, its second digit is equal to its second last digit, and so on. For example, the numbers $1221$, $505$, and $7$ are palindromes, while $500$, $1410$, and $2424$ are not palindromes.

Similarly, a number is called an **almost palindrome** if it has the same pairs of identical digits as a palindrome, except for one pair where the digits differ. For example, the numbers $500$, $1411$, $2444$, $1220$, $53625$, $14$, and $4014$ are almost palindromes (with the non-identical digit pair highlighted), while $1221$, $1410$, $6$, $505$, $22$, and $512125$ are not almost palindromes because they are either palindromes or have too many pairs of different digits.

We also define the **associated palindrome** of a number $x$ as the smallest palindrome $p$ that is strictly larger than $x$ ($p > x$). For example, the associated palindrome of $5442$ is $5445$, the associated palindrome of $2445$ is $2552$, the associated palindrome of $545$ is $555$, the associated palindrome of $39995$ is $40004$, the associated palindrome of $500$ is $505$, and the associated palindrome of $512125$ is $512215$.

# Task

Write a program that, reading a non-zero natural number $n$ and then an array of $n$ natural numbers, determines:

1. How many of the $n$ numbers are palindromes;
2. How many of the $n$ numbers are almost palindromes;
3. The associated palindromes for the $n$ numbers read.

# Input data

The input file `palindrom.in` contains on the first line a number $C$. For all tests, $C$ can only take the values $1$, $2$, or $3$. The second line contains the number $n$, and the third line contains the $n$ natural numbers separated by a space.

# Output data

The output file `palindrom.out`:

* if $C = 1$, will contain a single natural number representing the number of palindromes in the array;
* if $C = 2$, will contain the number of numbers in the array that are almost palindromes;
* if $C = 3$, will contain the associated palindromes for the $n$ numbers in the array, separated by a space.

# Constraints and clarifications

* $1 \leq n \leq 10 \ 000$;
* $1 \leq$ the numbers in the array $\leq 2 \cdot 10^9$;
* A correct solution for the first task is awarded $20$ points.
* A correct solution for the second task is awarded $30$ points.
* A correct solution for the third task is awarded $50$ points.

# Example 1

`palindrom.in`
```
1
7
1221 500 53635 505 7 4004 1410
```

`palindrom.out`
```
5
```

## Explanation

Explanation: The $5$ palindromes are $1221$, $53635$, $505$, $7$, and $4004$ ($C$ being $1$, only the first task is solved).

# Example 2

`palindrom.in`
```
2
4
5442 2445 545 39995
```

`palindrom.out`
```
3
```

## Explanation

Explanation: The $3$ almost palindromes are $5442$, $2445$ and $39995$ ($C$ being $2$, only the second task is solved).

# Example 3

`palindrom.in`
```
3
11
6 1411 2444 1221 505 1220 53625 14 4014 1410 22
```

`palindrom.out`
```
7 1441 2552 1331 515 1221 53635 22 4114 1441 33
```

## Explanation

Explanation: The associated palindrome of $6$ is $7$, $1411$ is $1441$, $2444$ is $2552$, etc. ($C$ being $3$, only the third task is solved).

---

Please review the English translation for accuracy and error correction.