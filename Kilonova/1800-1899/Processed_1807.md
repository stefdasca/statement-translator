Fie $D$, $K$ și $P$ trei numere naturale.

# Task

Determine the number of natural numbers, denoted by $T$, having the following properties:

* have exactly $D$ divisors;
* the prime factor decomposition of these numbers contains exactly $K$ prime numbers;
* all prime factors in the decomposition of the numbers are less than or equal to $P$.

# Input data

The input file `divizori.in` contains on the first line the numbers $D$, $K$ and $P$ with the above meaning, separated by a space.

# Output data

The output file `divizori.out` will contain on the first line the remainder of the division of the number $T$ by $3 \ 000 \ 017$.

# Constraints and clarifications

* $2 \leq D \leq 10^{14}$
* $1 \leq K \leq 10^2$
* $2 \leq P \leq 10^6$

# Example 1

`divizori.in`
```
6 2 5
```

`divizori.out`
```
6
```

## Explanation

$D = 6$, $K = 2$, $P = 5$  
There are $T = 6$ numbers with exactly $6$ divisors that contain in their prime factorization exactly $2$ prime numbers less than or equal to $5$: $2^1 3^2$, $2^1 5^2$, $2^2 3^1$, $2^2 5^1$, $3^1 5^2$, $3^2 5^1$.

# Example 2

`divizori.in`
```
18 3 10
```

`divizori.out`
```
12
```

## Explanation

$D = 18$, $K = 3$, $P = 10$  
There are $T = 12$ numbers with exactly $18$ divisors that contain in their prime factorization $3$ prime numbers less than or equal to $10$: $2^2 3^2 5^1$, $2^2 3^1 5^2$, $2^1 3^2 5^2$, $2^2 3^2 7^1$, $2^2 3^1 7^2$, $2^1 3^2 7^2$, $2^2 5^2 7^1$, $2^2 5^1 7^2$, $2^1 5^2 7^2$, $3^2 5^2 7^1$, $3^2 5^1 7^2$, $3^1 5^2 7^2$.

# Example 3

`divizori.in`
```
10 8 17
```

`divizori.out`
```
0
```

## Explanation

$D = 10$, $K = 8$, $P = 17$  
There are no numbers with exactly $10$ divisors that contain in their prime factorization exactly $8$ prime numbers $\\leq 17$ because there are only $7$ prime numbers less than or equal to $17$.