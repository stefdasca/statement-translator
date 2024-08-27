## Task

Mikasa Ackerman gives Eren the following function $f(a,b) = a f(a, b - 1)$ for any $b > 1$. Knowing that $f(a,1) = a$, help Eren to calculate $f(a,b)$ modulo $p$ for three given numbers $a$, $b$, and $p$.

## Input data

The input file `ackermann.in` will contain on the first line a natural number $T$, representing the number of tests. On the following $T$ lines, there will be $3$ natural numbers $a$, $b$, and $p$.

## Output data

The output file `ackermann.out` will contain $T$ lines, with the answer to test $i$ on the $i$-th line. 

## Constraints and clarifications

$1 \leq T \leq 1\,000$

$1 \leq a, b, p \leq 1\,000\,000\,000$

$a$ is a prime number

$a > p$

## Example

`ackermann.in` 

```
3
3 2 10
2 3 7
2 4 666013
```

`ackermann.out` 

```
7
2
65536
```

Observations: 

In the example $p > a$.

The example is given just for better understanding. 

In the tests, $a > p$.