NrDivUnique

It is known that each number strictly greater than $1$ has at least $2$ divisors (1 and itself). We define a divisor of an interval $[A,B]$ as a number in the interval $[1,B]$ which is a divisor of at least one number in the interval $[A,B]$.

## Task

Consider $N$ intervals of two natural numbers $A_i$ and $B_i$. For each interval $i$, display the number of divisors.

## Input data

The input file `nrdivunique.in` contains on the first line the natural number $N$. The next $N$ lines contain the values of the $N$ intervals. Line $i+1$ contains the two natural numbers of interval $i$, $A_i$ and $B_i$ separated by a space.

## Output data

In the output file `nrdivunique.out` you will print $N$ lines, one for each interval. Line $i$ contains a single natural number, representing the number of divisors of interval $i$.

## Constraints and clarifications

$1 \leq N \leq 1\,000$

$2 \leq A \leq 1\,000\,000$

$A < B \leq 1\,000\,000\,000$

The interval $[A,B]$ is closed, so the values $A$ and $B$ will also be considered.

For $20\%$ of the tests $N \leq 100$ and $B \leq 500$

For another $30\%$ of the tests $N \leq 500$ and $B \leq 10\,000$

## Example

`nrdivunique.in`
```
2
2 3
5 7
```

`nrdivunique.out`
```
3
6
```

## Explanation

In the first interval, the divisors are: $1$, $2$, and $3$.

In the 2nd interval, the divisors are: $1$, $2$, $3$, $5$, $6$, and $7$.