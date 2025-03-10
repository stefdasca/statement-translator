# Task

Little Gates is becoming more and more skilled with prime numbers, so the mathematics teacher proposes the following game: consider a number constructed by concatenating the first $k$ prime numbers in their increasing order. Help him win the game by solving the following tasks:

1. How many odd numbers were concatenated to the sequence?
2. What is the sum of the numbers that were concatenated?
3. The digits of the number formed from concatenating the primes are numbered starting from $1$. For $p$ positions given by the teacher, Little Gates needs to determine the prime number from which each digit at these positions originates.

# Input data

The first line of the input file `joc.in` contains the number $c$, which can only be $1$, $2$, or $3$, corresponding to the task that needs to be solved.

If the task is $1$ or $2$, the second line of the file `joc.in` contains a non-zero natural number $k$, representing the number of prime numbers that are concatenated.

If the task is $3$, the second line contains two non-zero natural numbers, $k$ – the number of prime numbers to be concatenated, and $p$ – the number of positions given by the teacher, separated by a space. The third line contains $p$ natural numbers, each representing a position $poz$ in the number formed by concatenating the $k$ prime numbers.

# Output data

If the task is $c=1$, the first line of the file `joc.out` contains a number corresponding to the answer to task $1$.
If the task is $c=2$, the first line of the file `joc.out` contains a number corresponding to the answer to task $2$.
If the task is $c=3$, the file `joc.out` will contain on the first line $p$ numbers separated by spaces, each number representing the prime number from which the digit at position $poz$ originates, according to the task.

# Constraints and clarifications

* $1 \leq k < 50 \ 000$;
* $1 \leq p \leq 100 \ 000$;
* $1 \leq $ poz $\leq$ the length of the formed number;
* For $15$ points, the task is $c=1$;
* For another $25$ points, the task is $c=2$;
* For another $60$ points, the task is $c=3$. Among these, for $30$ points $k \leq 1 \ 000$;
* It is guaranteed that there always exists a solution.

# Example 1

`joc.in`
```
1
3
```

`joc.out`
```
2
```

## Explanation

The task is $1$, $k=3$, therefore the first $3$ prime numbers ($2$, $3$, and $5$) are concatenated. Among these, two are odd.

# Example 2

`joc.in`
```
2
3
```

`joc.out`
```
10
```

## Explanation

The task is $2$, $k=3$, therefore the first $3$ prime numbers ($2$, $3$, and $5$) are concatenated. Their sum is: $2+3+5=10$

# Example 3

`joc.in`
```
3
5 3
1 5 6
```

`joc.out`
```
2 11 11
```

## Explanation

The task is $3$, $k=5$, $p=3$.
The first $5$ prime numbers are: $2$, $3$, $5$, $7$, $11$.
The constructed number is: `235711`.
* The digit at position $1$ is $2$, which originates from $2$.
* The digit at position $5$ is $1$, which originates from $11$.
* The digit at position $6$ is $1$ and originates from $11$.

# Example 4

`joc.in`
```
3
6 2 
8 3
```

`joc.out`
```
13 5
```

## Explanation

The task is $3$, $k=6$, $p=2$.
The first $6$ prime numbers are: $2$, $3$, $5$, $7$, $11$, and $13$.
The constructed number is: `23571113`.
* The digit at position $8$ is $3$, which originates from $13$.
* The digit at position $3$ is $5$, which originates from $5$.