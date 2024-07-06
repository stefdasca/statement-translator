A natural number with at least two digits is called accessible if it consists of consecutive digits in strictly increasing order. ($23$ and $6789$ are accessible numbers, while $7$, $2334$ and $654$ are not accessible numbers)

# Task

Write a program that reads the numbers $k, n$ and an array of $n$ natural numbers and displays:

1. The largest $3$ accessible numbers, not necessarily distinct, from the array of $n$ numbers;
2. How many of the numbers in the given array that are not accessible become accessible by removing exactly one digit;
3. The smallest and largest accessible number consisting of $k$ digits;
4. The number of even accessible numbers with $k$ digits and the number of odd accessible numbers with $k$ digits.

# Input data

The input file `accesibil.in` contains on the first line a natural number $p$. For all test cases, the number $p$ is a number from the set $\{1,2,3,4\}$. The second line of the input file contains $k$ and $n$, and on the third line contains $n$ natural numbers separated by a space.

# Output data

* If the value of $p$ is $1$, only point $1$ from the task will be solved. In this case, the output file `accesibil.out` will contain, in increasing order, separated by a space, the three largest accessible numbers among the $n$ numbers found on the third line of the file. It is guaranteed that for $p = 1$ there are at least three accessible numbers in the array of $n$ numbers.
* If the value of $p$ is $2$, only point $2$ from the task will be solved. In this case, the output file `accesibil.out` will contain the number of numbers in the given array that are not accessible but would become accessible if one digit is removed.
* If the value of $p$ is $3$, only point $3$ from the task will be solved. In this case, the output file `accesibil.out` will contain two values, separated by a space, representing the smallest accessible number with $k$ digits and the largest accessible number with $k$ digits. If the two numbers to be printed coincide, their common value will be printed only once.
* If the value of $p$ is $4$, only point $4$ from the task will be solved. In this case, the output file `accesibil.out` will contain two values representing the number of even accessible numbers with $k$ digits and the number of odd accessible numbers with $k$ digits, in this order, separated by a space.

# Constraints and clarifications

* $2 \leq k \leq 9$ and $3 \leq n \leq 100\ 000$;
* $0 \leq$ numbers in the array $\leq 2\ 000\ 000\ 000$;
* From the number $5073$, for example, by removing one digit, the numbers $507, 503, 573$ and $73$ can be obtained;
* To solve task points $1$ and $2$, the value of $k$ is not used, and to solve task points $3$ and $4$, the array of $n$ numbers is not used;
* Points awarded: $40$ points for task point $1$; $30$ points for task point $2$; 10 points for task point $3$; 10 points for task point $4$;

# Example 1

`accesibil.in`
```
1
3 8
6 12 235 5678 90 987 234 5678
```

`accesibil.out`
```
234 5678 5678
```

## Explanation

Accessible numbers are $12, 5678, 234$ and $5678$. The largest $3$ values, in increasing order: $234 \ 5678 \ 5678$ (since $p$ is $1$ only task point $1$ is solved)

# Example 2

`accesibil.in`
```
2
3 9
4 34 123 1238 301 689 4560 7023 1238
```

`accesibil.out`
```
5
```

## Explanation

If you remove one digit from $1238, 689, 4560, 7023, 1238$, they become accessible numbers (since $p$ is $2$ only task point $2$ is solved)

# Example 3

`accesibil.in`
```
3
4 3
12 345 67
```

`accesibil.out`
```
1234 6789
```

## Explanation

The smallest accessible number with $4$ digits is $1234$ and the largest is $6789$ (since $p$ is $3$ only task point $3$ is solved)

# Example 4

`accesibil.in`
```
4
9 3
12 345 67
```

`accesibil.out`
```
0 1
```

## Explanation

There is only one accessible number with $9$ odd digits, namely $123456789$ and no even number with $9$ digits (since $p$ is $4$ only task point $4$ is solved)