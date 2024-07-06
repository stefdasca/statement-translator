Be $N$ a natural number.

We define an ordered multiplicative partition of the number $N$ as writing $N$ as the product of one or more different divisors of $N$, each different from $1$.

Examples:
* The $4$ partitions of the number $N = 8$ are: $8$, $2 \times 4$, $4 \times 2$, $2 \times 2 \times 2$
* The $8$ partitions of the number $N = 12$ are: $12$, $2 \times 6$, $6 \times 2$, $3 \times 4$, $4 \times 3$, $2 \times 2 \times 3$, $2 \times 3 \times 2$, $3 \times 2 \times 2$

# Task

Write a program that reads $T$ natural numbers $X_i$, $1 \leq i \leq T$, and determines the number of ordered multiplicative partitions of each number $X_i$, $1 \leq i \leq T$.

# Input data

The input file `pmo.in` contains:
* The first line contains the natural number $T$
* The second line contains $T$ natural numbers $X_i$, $1 \leq i \leq T$, separated by a space

# Output data

The output file `pmo.out` will contain, on line $i$, the number of ordered multiplicative partitions of the number $X_i$, $1 \leq i \leq T$.

# Constraints and clarifications

* $1 \leq T \leq 30\ 000$
* $2 \leq X_i \leq 10^9$ for $1 \leq i \leq T$

|#|Score|Constraints|
|-|-|-|
|1|12|$T \leq 1\ 000$ and all numbers are powers of a prime number|
|2|20|$T \leq 100$ and $2 \leq X_i \leq 15\ 000$ for $1 \leq i \leq T$|
|3|68|No additional constraints.|

# Example 1

`pmo.in`
```
4
2 8 12 10
```

`pmo.out`
```
1
4
8
3
```

## Explanation

The numbers $2$, $8$, $12$, $10$ have $1$, $4$, $8$, and $3$ ordered multiplicative partitions, respectively.

# Example 2

`pmo.in`
```
2
123456 987654
```

`pmo.out`
```
2496
75
```

## Explanation

The numbers $123\ 456$ and $987\ 654$ have $2\ 496$ and $75$ ordered multiplicative partitions, respectively.