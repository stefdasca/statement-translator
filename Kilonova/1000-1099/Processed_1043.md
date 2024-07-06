For a non-zero natural number $X$, a proper divisor of $X$ is defined as a natural divisor of $X$ different from $1$ and $X$. For example, the proper divisors of $20$ are $2, 4, 5, 10$, and the number $20$ has $4$ proper divisors.

# Task
Write a program that solves the following problems:
1. Given a natural number $N$, determine the smallest number in the closed interval $[1, N]$ that has the maximum number of proper divisors.
2. Given three numbers $N$, $M$, and $T$, determine how many intervals of the form $[a, b]$ have the property that there are exactly $M$ natural numbers with $T$ proper divisors.

# Input data
The input file `numere.in` contains on the first line a natural number $P$ indicating which task needs to be solved.

If $P = 1$, then the second line contains a natural number $N$, representing the right end of the interval.

If $P = 2$, then the second line contains three numbers: a natural number $N$, a natural number $M$, and a natural number $T$ with the meaning described in the statement.

# Output data
If $P = 1$, then the output file `numere.out` will contain on a single line the smallest number determined which has the maximum number of proper divisors.

If $P = 2$, then the output file `numere.out` will contain on a single line the number of intervals determined that have the required property.

# Constraints and clarifications
* $1 \leq N \leq 100 \ 000$
* $1 \leq M \leq 100 \ 000$
* $1 \leq T \leq 100 \ 000$
* $1 \leq a \leq b \leq N$
* Proper solutions for Task 1 will be awarded $40$ points, and proper solutions for Task 2 will be awarded $60$ points.

# Example 1

`numere.in`
```
1 
20
```

`numere.out`
```
12
```

## Explanation

$12$ has $4$ proper divisors and is the smallest number with $4$ proper divisors in $[1, 20]$.

# Example 2

`numere.in`
```
2
10 3 2
```

`numere.out`
```
6
```

## Explanation

$[1,10]$, $[2,10]$, $[3,10]$, $[4,10]$, $[5,10]$, $[6,10]$ are the $6$ intervals in which there are exactly $3$ numbers with $2$ proper divisors ($6$, $8$, $10$ are the numbers with $2$ proper divisors).