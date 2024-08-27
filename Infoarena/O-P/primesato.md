# Primesato

Primesato is completely obsessed with prime numbers, and thus she created the following problem: given three numbers $N$, $M$, and $K$. How many sequences $S$ of $N$ integers between 1 and $K$ exist such that all prime length subarrays of $S$ have even sums? The answer is required modulo $M$.

## Task

## Input data

The input file `primesato.in` will contain, on the first line, the number $T$ of tests in the file. The following $T$ lines will contain the descriptions of the $T$ tests, i.e., the numbers $N$, $M$, $K$, as described in the statement.

## Output data

The output file `primesato.out` will contain $T$ lines, each with the answer for each test, in order.

## Constraints

$1 \leq T \leq 100\ 000$

$1 \leq N, K \leq 10^{18}$

$1 \leq M \leq 10^9$

## Example

`primesato.in`
```
3
3 100 2
23 23 23
14343 23512 43646
1 11 6111
```

`primesato.out`
```
```