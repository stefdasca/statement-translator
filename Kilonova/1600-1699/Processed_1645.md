It is well-known that the algorithm for computing the greatest common divisor (gcd) with Euclid's algorithm through repeated division. According to this algorithm, the gcd of two non-zero natural numbers $a$ and $b$ is calculated by keeping the remainder of the division and then repeating the division with the old divisor and the old remainder. The algorithm will terminate when the remainder of the division becomes zero. The greatest common divisor of the two numbers $a$ and $b$ will be the last divisor.

For the calculation of the greatest common divisor of the pair ($16$, $22$), the successive divisions will be performed as follows:

|Dividend|Divisor|Remainder|Step|
|---|---|---|---|
|$16$|$22$|$16$|Step $1$|
|$22$|$16$|$6$|Step $2$|
|$16$|$6$|$4$|Step $3$|
|$6$|$4$|$2$|Step $4$|
|$4$|$2$|$0$|Step $5$|

We will call an "operation" a division operation that intervenes in the calculation of gcd. It can be observed that to determine gcd($16$, $22$) = $2$, $5$ steps were necessary.

# Task

Given the value of a natural number $n$, write a program that determines a pair of natural numbers ($a$, $b$) less than or equal to $n$, whose gcd is obtained in a maximum number of steps. If there are multiple pairs ($x$, $y$) with this property, the smallest one will be displayed. We say that the pair ($a$, $b$) is smaller than ($x$, $y$), if $a < x$ or $a = x$ and $b < y$.

# Input data

The text file `euclid.in` contains a single natural number $n$.

# Output data

The text file `euclid.out` will contain on the first line the maximum number of steps determined. The second line will contain a natural number $a$ representing the first number of the minimum identified pair, and on the third line the number $b$ representing the second number of the pair will be written.

# Constraints and clarifications

* $4 \leq n \leq 10^{200}$;

# Example 1

`euclid.in`
```
8
```

`euclid.out`
```
5
5
8
```

## Explanation

The maximum number of steps for any pair of numbers less than or equal to $8$ is $5$. The pair ($5$, $8$) is the smallest with this property.

# Example 2

`euclid.in`
```
12345678910 
```

`euclid.out`
```
48
4807526976
7778742049
```

## Explanation

The maximum number of steps for any pair of numbers less than or equal to $12\ 345\ 678\ 910$ is $48$. The pair ($4\ 807\ 526\ 976$, $7\ 778\ 742\ 049$) is the smallest with this property.