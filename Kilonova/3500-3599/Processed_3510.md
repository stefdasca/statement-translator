
# Task

A number $i$ is called a Sophie Germain number if $i$ is prime and $2 \cdot i + 1$ is also prime. This concept can be generalized as follows: $i$ is considered a $k$-Sophie Germain number if $i$ is prime and $i \cdot k + 1$ is also prime, for a non-zero natural number $k$, $k > 2$.

1. Given a non-zero natural number $n$, calculate how many Sophie Germain numbers exist between $1$ and $n$.
2. Given two non-zero natural numbers $n$ and $k$, calculate how many $k$-Sophie Germain numbers exist between $1$ and $n$. 

# Input data

The first line of the input file `sophie.in` contains a natural number $c$, which can only be $1$ or $2$, representing the number of the task to solve.

If the task is $c=1$, the second line contains a non-zero natural number $n$, with the meaning from the statement.
If the task is $c=2$, the second line contains two non-zero natural numbers $n$ and $k$, separated by a space, with the meaning from the statement.

# Output data

In the file `sophie.out` a natural number will be printed representing the required count.

# Constraints and clarifications

* $1 \leq n, k \leq 10^6$;
* For the first task ($c=1$) $40$ points are awarded.
* For the second task ($c=2$) $60$ points are awarded. Out of these, $15$ points are for when $k$ is odd. For another $15$ points, $n \cdot k \leq 10^6$.

# Example 1

`sophie.in`
```
1
10
```

`sophie.out`
```
3
```

## Explanation

The task is 1. The Sophie Germain numbers between $1$ and $10$ are: 
* $2$: $2$ is prime, and $2 \cdot 2 + 1 = 5$ and $5$ is prime.
* $3$: $3$ is prime, $3 \cdot 2 + 1 = 7$, and $7$ is prime.
* $5$: $5$ is prime, and $5 \cdot 2 + 1 = 11$, where $11$ is prime.

# Example 2

`sophie.in`
```
2
10 20
```

`sophie.out`
```
3
```

## Explanation

The task is 2. The only numbers that meet the criterion between $1$ and $10$ are: 
- $2$ ($2$ is prime and $2 \cdot 20 + 1 = 41$ is prime);
- $3$ ($3$ is prime and $61$ is a prime number);
- $5$ ($5$ is prime and $101$ is a prime number).
```
