A natural number $N$ is given. We will denote by $P$ the set of prime numbers less than or equal to $N$. We aim to determine the largest sum of a subarray of $P$ containing $[card(P)/2]$ elements and the number of non-empty subsets of $P$, modulo $7919$.

# Task

Given $N$, it's required to:
1. find the largest sum of a subarray of $P$ with $[card(P)/2]$ elements;
2. find the number of non-empty subsets of $P$, modulo $7919$.

# Input data

The first and second lines of the input file `submultprime.in` contain two natural numbers, $C$ and $N$, representing the number of the task to be solved ($1$ or $2$), respectively the number from the statement.

# Output data

The first line of the output file `submultprime.out` will contain a single natural number corresponding to the solution of the task $C$ from the input file.

# Constraints and clarifications

* $1 \leq N \leq 1 \ 000 \ 000$;
* For a set $M$, $card(M)$ represents the number of elements of $M$.
* For the correct solution of task $1$, $20$ points will be awarded.
* For the correct solution of task $2$, $80$ points will be awarded.

# Example 1

`submultprime.in`
```
1
10
```

`submultprime.out`
```
12
```

## Explanation

$C = 1$. We get that $P = \{2, 3, 5, 7\}$, $card(P) = 4$. The largest sum for a subarray with two elements is $5 + 7 = 12$.

# Example 2


`submultprime.in`
```
2
10
```

`submultprime.out`
```
15
```

## Explanation

$C = 2$. The number of non-empty subsets of $P = \{2, 3, 5, 7\}$ is $15$.