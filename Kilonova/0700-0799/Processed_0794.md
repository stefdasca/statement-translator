Given a strictly positive rational number $q$, in the form of a decimal fraction.

# Task

Determine two natural numbers $a$ and $b$ such that $q = a / b$, and the absolute value of the difference between $a$ and $b$ is minimized.

# Input data

The file `numar.in` contains:

* The first line contains two natural values $ni$ and $nz$. $ni$ represents the number of digits that form the integer part of $q$, and $nz$ represents the number of digits that form the fractional part of $q$.
* The second line contains $ni$ digits that represent the integer part of $q$. There is a space character between every two digits.
* The third line contains $nz$ digits that represent the decimal part of $q$. There is a space character between every two digits.

# Output data

The file `numar.out` will contain:

* The first line contains a natural number $n_1$, which represents the number of digits from which the number $a$ is composed;
* The second line contains the digits of the number $a$, without spaces between them.
* The third line contains a natural number $n_2$, which represents the number of digits from which the number $b$ is composed;
* The fourth line contains the digits of the number $b$, without spaces between them.

# Constraints and clarifications

* $1 \leq ni, nz < 2 \ 000$.
* $1 \leq ni + nz \leq 2 \ 000$.
* The digits that form $q$ are those from the decimal system.
* For $20$% of the tests, $ni + nz \leq 9$; for another $15$% of the tests, $10 \leq ni + nz \leq 16$.

# Example 1

`numar.in`
```
1 3
0
3 7 5
```

`numar.out`
```
1
3
1
8
```

## Explanation

$q = 0.375 = 3 / 8$.

There are other pairs of natural values $x, y$ such that $x / y = 0.375$, but for any other pair, $|x-y| > |3-8|$.

# Example 2

`numar.in`
```
3 7
0 1 2
3 4 5 6 7 0 0
```

`numar.out`
```
7
1234567
6
100000
```

## Explanation

$q = 12.34567 = 1234567 / 100000$.