Ionel and Georgel are classmates and want to exchange files via email. Each of them archives their files with a password. Each child creates their password based on a sequence consisting of $N$ natural numbers.

The numbers in the sequence that are used to construct the passwords are **only** those divisible by the numbers in the set $\\{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15\\}$. The children count how many of the values in the sequence are divisible by each of these numbers.

The password used by Ionel is obtained by summing the number of values in the sequence that are divisible by the numbers in the set $\\{2, 3, 4, 5, 6, 7, 8, 9\\}$. The password used by Georgel is obtained by summing the number of values in the sequence that are divisible by the numbers in the set $\\{10, 11, 12, 13, 14, 15\\}$.

# Task

Write a program that reads the sequence of $N$ numbers and determines:

1. how many numbers in the sequence will not be used in constructing the passwords of the two children;
2. the password constructed by Ionel;
3. the password constructed by Georgel.

# Input data

The input file `cod.in` contains:

- the first line contains a natural number $P$. For all input tests, the number $P$ can have only the value $1$, $2$, or $3$.
- the second line contains the natural number $N$, and on the third line, $N$ natural numbers separated by the character `#`.

# Output data

If the value of $P$ is $1$, only point $1$ from the task will be resolved. In this case, the output file `cod.out` will contain the first line a non-zero natural number representing how many numbers in the sequence were not used in constructing the passwords or $0$ if no such numbers exist.

If the value of $P$ is $2$, only point $2$ from the task will be resolved. In this case, the output file `cod.out` will contain the first line a natural number representing the password constructed by Ionel.

If the value of $P$ is $3$, only point $3$ from the task will be resolved. In this case, the output file `cod.out` will contain the first line a natural number representing the password constructed by Georgel.

# Constraints and clarifications

* $0 < N \leq 100\ 000$
* $2 \leq$ the number of digits of a number $\leq 100$
* It is guaranteed that all the passwords obtained by the children are non-zero
* In the input file, the last number is not followed by the character `#`
* $16\%$ of the tests contain only numbers formed of at most $9$ digits
* For correctly solving task $1$ $20$ points are obtained, for correctly solving task $2$ $40$ points are obtained, and for correctly solving task $3$ $40$ points are obtained

# Example 1

`cod.in`
```
1
6
10#20#12#34#15#23
```

`cod.out`
```
1
```

## Explanation

Only the number $23$ is not divisible by any number in the set $\\{2, 3, ..., 15\\}$

# Example 2

`cod.in`
```
2
5
16#61#12#385#31
```

`cod.out`
```
9
```

## Explanation

For Ionel's password, we need to check the divisibility by the numbers $2, 3, 4, 5, 6, 7, 8, 9$. Two numbers are divisible by $2$ ($16$ and $12$), one number is divisible by $3$ ($12$), two numbers are divisible by $4$ ($16$ and $12$), one number is divisible by $5$ ($385$), one number is divisible by $6$ ($12$), one number is divisible $7$ ($385$), one number is divisible by $8$ ($16$). The password is $2 + 1 + 2 + 1 + 1 + 1 + 1 = 9$

# Example 3

`cod.in`
```
3
5
30#1100#11#85#121
```

`cod.out`
```
6
```

## Explanation

For Georgel's password, we need to check the divisibility by the numbers $10, 11, 12, 13, 14, 15$. Two numbers are divisible by $10$ ($30$ and $1100$), three numbers are divisible by $11$ ($1100$, $11$, and $121$), and one number is divisible by $15$ ($30$). The password is $2 + 3 + 1 = 6$