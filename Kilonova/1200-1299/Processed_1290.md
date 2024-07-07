
Consider the series of natural numbers: $1, \\ 3, \\ 5, \\ 7, \\ 9, \\ 11, \\ 13, \\ 15, \\ 17, \\ 19, \\ 21, \\dots$

The numbers in the series are grouped so that the first group, numbered $1$, consists of the first number in the series ($1$), the second group, numbered $2$, consists of the next two numbers in the series ($3$, $5$), the third group, numbered $3$, consists of the next three numbers in the series ($7$, $9$, $11$), $\\dots$, the $n$-th group in the series, numbered $n$, consists of the next $n$ numbers in the series, etc.

# Task

Determine the rule by which the terms of the series are generated and write a program that reads the natural numbers $p$, $n$ and $k$ and determines:

1. the index of the number in the series that has the value $p$;
2. the largest natural palindrome number that can be obtained using the digits of all the numbers in the $n$-th group of the given series, not necessarily all these digits;
3. the index of the group with the property that the sum of all the numbers contained in it is equal to the number $k$, if there exists such a group.

# Input data

The input file `sir.in` contains a single line that contains, in this order, three natural numbers $p$, $n$ and $k$, separated by a space.

# Output data

The output file `sir.out` will contain $3$ lines. The first line will contain a natural value representing the index of the number in the series that has the value $p$. The second line will contain the largest natural palindrome number that can be obtained using the digits of all the numbers in the $n$-th group of the given series, not necessarily all these digits. The third line will contain the index of the group with the property that the sum of all the numbers contained in it is equal to the number $k$; if there is no such group, the number $0$ will be written.

# Constraints and clarifications

* The numbers $p$, $n$ and $k$ are natural
* $1 \\leq p \\leq 2 \\ 000 \\ 001$, $p$ is a natural **odd** number
* $1 \\leq n \\leq 50$
* $1 \\leq k \\leq 2 \\ 000 \\ 000 \\ 000$
* A natural number is a palindrome if it is equal to the number obtained by writing its digits in reverse order
* For solving task $1$, $40\\%$ of the score is awarded, for task $2$, $30\\%$ of the score, and for task $3$, $30\\%$ of the score.

# Example

`sir.in`
```
19 5 125
```

`sir.out`
```
10
22922
5
```

## Explanation

1. In the series, the value $19$ appears at position $10$, these $10$ terms being: $1$, $3$, $5$, $7$, $9$, $11$, $13$, $15$, $17$, $19$. The determined position is $10$, a value that will be written on the first line of the file `sir.out`
2. The numbers in the 5th group are written using $1$ digit of $1$, $5$ digits of $2$, $1$ of $3$, $1$ of $5$, $1$ of $7$, $1$ of $9$. The largest palindrome that can be written with these digits is $22 \\ 922$, a value that is written on the second line of the file.
3. Group $5$ has a sum equal to $k (21 + 23 + 25 + 27 + 29 = 125)$.
