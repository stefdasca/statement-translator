Maria is passionate about mathematics. She is particularly interested in elements of the Fibonacci sequence and wants to study the properties of these elements. She recently wrote down the Fibonacci numbers: $1, 1, 2, 3, 5, 8, 13, \dots$ and noticed that one element, the number $5$, can be written as the sum of two other Fibonacci numbers squared, $5 = 1 ^ 2 + 2 ^ 2$, and another Fibonacci number, the number $144$, can be written as the difference of two other Fibonacci numbers squared, $144 = 13 ^ 2 - 5 ^ 2$.

Maria was delighted with the results she obtained and would like to find other elements of the sequence that can be written as a sum or as a difference of two other Fibonacci numbers squared.

# Task

Help Maria decide about an arbitrary Fibonacci element if it can be written as a sum or difference of two distinct Fibonacci numbers squared. Given the large values of Fibonacci numbers, compute the remainder of their division by $46337$.

# Input data

The input file `fibo.in` contains a single natural number $n$, representing the sequence number of the $n$-th Fibonacci number $(3 \lt n \lt 25\ 000)$.

# Output data

If the problem has a solution, the output file `fibo.out` will contain $5$ lines:
* The first line of the file will contain the value $1$ or $0$, depending on whether the $n$-th Fibonacci number can be written as a sum or as a difference of two other Fibonacci numbers squared.
* The second line of the output file will contain two natural numbers $i$ and $j \ (0 \lt i \lt j)$ separated by a space, representing the sequence numbers of the two required Fibonacci elements $(f_n = f_j ^ 2 \pm f_i ^ 2)$.
* The third line of the output file will contain the remainder of the division of the $i$-th Fibonacci number by $46337$.
* The fourth line of the output file will contain the remainder of the division of the $j$-th Fibonacci number by $46337$.
* The fifth line of the output file will contain the remainder of the division of the $n$-th Fibonacci number by $46337$.
If the problem has no solution, the output file will contain the value $-1$ on its first line.

# Constraints and clarifications

* $3 \lt n \lt 25\ 000$
* The indices of the Fibonacci numbers start from $1$: $f_1 = 1, f_2 = 1, f_3 = 2, \dots$
* There can be multiple solutions, in which case any of them are accepted.

# Example 1

`fibo.in`
```
5
```

`fibo.out`
```
1
1 3
1
2
5
```

## Explanation

$1$ - it is a sum
using elements $f_1$ and $f_3$
$f_1 \mod 46337 = 1$
$f_3 \mod 46337 = 2$
$f_5 \mod 46337 = 5$
since $f_5 = f_1 ^ 2 + f_3 ^ 2 = 1 ^ 2 + 2 ^ 2 = 1 + 4 = 5$

# Example 2

`fibo.in`
```
5
```

`fibo.out`
```
0
3 4
2
3
5
```

## Explanation

$0$ – it is a difference
using elements $f_3$ and $f_4$
$f_3 \mod 46337 = 2$
$f_4 \mod 46337 = 3$
$f_5 \mod 46337 = 5$
since $f_5 = f_4 ^ 2 - f_3 ^ 2 = 3 ^ 2 - 2 ^ 2 = 9 - 4 = 5$

# Example 3

`fibo.in`
```
12
```

`fibo.out`
```
0
5 7
5
13
144
```

## Explanation

$0$ – it is a difference
using elements $f_5$ and $f_7$
$f_5 \mod 46337 = 5$
$f_7 \mod 46337 = 13$
$f_{12} \mod 46337 = 144$
since $f_{12} = f_7 ^ 2 - f_5 ^ 2 = 13 ^ 2 - 5 ^ 2 = 169 - 25 = 144