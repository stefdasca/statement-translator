# Task

You are given a number $t$ and $t$ natural numbers. For each of them, find the answer to one of the following questions:

* $1 \\ n$: Determine if $n$ is prime or not. If it is, print `YES`, otherwise print `NO`.
* $2 \\ n$: Find how many divisors $n$ has – for example, if $n = 12$, print $6$ ($1$, $2$, $3$, $4$, $6$, $12$ are the divisors of $12$).
* $3 \\ n$: Find the number of prime divisors of $n$ – for example, if $n = 21$, print $2$.
* $4 \\ n$: Display the prime factorization of a number, each factor on a new line, in **ascending** order of the prime numbers – for example, if $n = 60$, display on $3$ different lines $2 \\ 2$, $3 \\ 1$, and $5 \\ 1$.

# Input data

The first line contains $t$, the number of tested numbers. The following $t$ numbers are pairs in the form $(type, n)$, where $type$ is a number between $1$ and $4$, and $n$ is between $1$ and $10^9$.

# Output data

For each of the $t$ questions, print the answer according to the format presented in the statement.

# Constraints and clarifications

* $1 \\leq t \\leq 1 \\ 000$
* $1 \\leq n \\leq 10^9$
* For tests worth $20$ points each, we will have only questions of type $1$, $2$, $3$, and $4$.

# Example

`stdin`
```
8
1 7
2 15
3 24
4 1000
1 5835834
2 7675774
3 30240
4 14400
```

`stdout`
```
YES
4
2
2 3
5 3
NO
8
4
2 6
3 2
5 2
```

## Explanation

$7$ is a prime number.  
The divisors of $15$ are $1$, $3$, $5$, $15$.  
The prime divisors of $24$ are $2$ and $3$.  
The prime factorization of $1000$ is $2^3 \\cdot 5^3$.