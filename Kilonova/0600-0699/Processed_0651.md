Here is the translated text:

Given an array $a_1, a_2, \dots, a_n$ of non-zero natural numbers.

# Task

Determine the answer for one of the following tasks:

1. The greatest common divisor of all $n$ numbers.
2. The greatest common divisor that can be obtained by choosing exactly $n - 1$ elements from the array.
3. The greatest common divisor that can be obtained by choosing exactly $n - 2$ elements from the array.

# Input data

The input file `cmmdc.in` contains on the first line a natural number $T$ representing the required task ($1$, $2$, or $3$), the second line contains the non-zero natural number $n$, and on the next $n$ lines, there are, one per line, the $n$ elements of the array.

# Output data

The output file `cmmdc.out` will contain the answer for the required task.

# Constraints and clarifications

* $2 \leq a_i \leq 2^{63} - 1$ for any $1 \leq i \leq n$ (the numbers are of type `long long`)

|#|Score|Constraints|
|-|-|--------|
|1|16|$T = 1$, $3 \leq n \leq 100\,000$ and $a_i \leq 50\,000\,000$, for $1 \leq i \leq n$|
|2|20|$T = 1$ and $3 \leq n \leq 100\,000$|
|3|21|$T = 2$ and $3 \leq n \leq 3\,000$|
|4|21|$T = 2$ and $3 \leq n \leq 100\,000$|
|5|12|$T = 3$ and $3 \leq n \leq 300$|
|6|10|$T = 3$ and $3 \leq n \leq 2\,000$|

# Example 1

`cmmdc.in`
```
1
5
48
40
20
16
80
```

`cmmdc.out`
```
4
```

## Explanation

$T = 1$, so it requires determining the greatest common divisor of five numbers: $48$, $40$, $20$, $16$, and $80$.

The answer is $4$.

# Example 2

`cmmdc.in`
```
2
5
48
40
20
16
80
```

`cmmdc.out`
```
8
```

## Explanation

$T = 2$, so solve task $2$.

By removing number $20$, $n - 1 = 4$ numbers remain, and $\\text{gcd}(16, 48, 40, 80) = 8$, which is the maximum possible.

# Example 3

`cmmdc.in`
```
3
5
48
40
20
16
80
```

`cmmdc.out`
```
20
```

## Explanation

$T = 3$, so solve task $3$.

By removing the numbers $16$ and $48$, $n - 2 = 3$ numbers remain, and $\\text{gcd}(40, 20, 80) = 20$, which is the maximum possible.