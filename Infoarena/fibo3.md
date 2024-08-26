# Fibo3

Consider the Fibonacci sequence: $F_0 = 1, F_1 = 1, F_2 = 2, F_3 = 3, F_4 = 5$ etc. We will cover all lattice points with non-negative coordinates as follows: If for a point $P(x,y)$, $x+y$ is a Fibonacci number, then we associate the value $1$ with $P$. If for a point $P(x,y)$, $x+y$ is not a Fibonacci number, then we associate the value $0$ with $P$.

## Task

Answer $N$ queries of the form: Given a rectangle $D(x_1, y_1, x_2, y_2)$, what is the sum of the values associated with the points in the plane contained by the rectangle $D$?

## Input data

The input file `fibo3.in` contains on the first line the number $N$ of queries. The next $N$ lines will each contain four natural numbers representing a query rectangle.

## Output data

The output file `fibo3.out` will contain $N$ natural numbers, each on a separate line, the number on line $K$ being the answer to the $K$-th query.

## Constraints and clarifications

$1 \leq N \leq 100000$

$0 \leq x_1 \leq x_2 \leq 10^{15}$

$0 \leq y_1 \leq y_2 \leq 10^{15}$

A point $P(x,y)$ is called a lattice point if $x$ and $y$ are integers.

The Fibonacci sequence is determined by the recurrence $F_N = F_{N-1} + F_{N-2}$

For 30% of the tests, the coordinates of the rectangles do not exceed $1000$.

## Example

`fibo3.in`

```
2
0 0 1 1
1 0 1 2
```

`fibo3.out`

```
3
3
```