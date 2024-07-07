
A sequence of natural numbers is generated whose first terms are, in this order:

$1$, $2$, $3$, $5$, $8$, $3$, $1$, $4$, $5$, $9$, $4$, $3$, $7$, $0$, $7$, $7$, $4$,...

# Task

Deduce the rule by which the terms of the sequence are generated and write a program that reads the natural numbers $n$, $k$ and $p$ and determines:

1. the sum of all prime numbers among the first $n$ terms of the sequence from the statement;
2. the number of occurrences of the digit $k$ among the first $n$ terms of the sequence from the statement;
3. the $p$-th term of the sequence from the statement.

# Input data

The file `nr.in` contains a single line containing three natural numbers $n$, $k$, and $p$, separated by a space.

# Output data

The output file `nr.out` will contain $3$ lines:

1. The first line will contain a natural number representing the sum of all prime numbers among the first $n$ terms of the sequence from the statement.
2. The second line will contain the number of occurrences of the digit $k$ among the first $n$ terms of the sequence from the statement.
3. The third line will print the $p$-th term of the sequence from the statement.

# Constraints and clarifications

* $3 \leq n \leq 100$;
* $0 \leq k \leq 9$;
* $1 \leq p \leq 2\ 000\ 000\ 000$;
* For solving requirement 1), 40% of the points are awarded, for requirement 2) 20% of the points, and for requirement 3) 40% of the points.
* For tests worth $50$ points, $p \leq 10\ 000\ 000$.

# Example

`nr.in`
```
19 5 26
```

`nr.out`
```
47
3
8
```

## Explanation

The first $19$ terms of the sequence are: $1$, $2$, $3$, $5$, $8$, $3$, $1$, $4$, $5$, $9$, $4$, $3$, $7$, $0$, $7$, $7$, $4$, $1$, $5$. The prime numbers that appear among these terms are $2$, $3$, $5$, $3$, $5$, $3$, $7$, $7$, $7$, $5$, their sum being $47$. The value $47$ is written on the first line of the file `nr.out`.

On the second line of the file `nr.out` the number $3$ is written, because there are $3$ terms equal to $k$ among the first $n = 19$ terms of the sequence.

On the last line of the file the number $8$ is written, because the $p$-th term of the sequence is $8$.

```
