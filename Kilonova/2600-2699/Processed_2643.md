It is considered a natural number consisting of $n$ digits. By inserting $p$ `+` operators and $q$ `−` operators between the digits of the given number, an arithmetic expression is obtained. An operator can only be inserted between two digits, so no operator can be placed before the first digit of the number.

# Task

Write a program that, for a given number, determines the maximum value of an arithmetic expression that can be obtained by inserting $p$ `+` operators and $q$ `−` operators between the digits of the given number.

# Input data

The input file `expresie.in` contains on the first line the natural numbers $n \ p \ q$ separated by a space, with the meaning given in the statement. The second line contains a number consisting of $n$ digits.

# Output data

The output file `expresie.out` will contain a single line, which will contain the maximum value of an arithmetic expression that can be obtained by inserting $p$ `+` operators and $q$ `−` operators between the digits of the given number.

# Constraints and clarifications

* $2 \leq n \leq 1\ 000$
* $0 < p + q < n$
* The number read does not start with $0$.

|#|Score|Constraints|
|-|-|--------|
|1|6|$n \leq 18$ and $p + q = 1$|
|2|9|$n > 18$ and $p + q = 1$|
|3|26|The result has at most $18$ digits and $p + q > 1$|
|4|60|There are no additional constraints|

# Example

`expresie.in`
```
5 1 2
54321
```

`expresie.out`
```
54
```

## Explanation

$54 + 3 − 2 − 1 = 54$