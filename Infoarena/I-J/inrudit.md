## Related

Two numbers are considered related if they are formed from exactly the same digits.

## Task

Given a number $X$, find the $K$-th related number greater than it.

## Input data

The input file `inrudit.in` contains two lines. The first line contains the number $K$, and the next line contains the number $X$.

## Output data

The output file `inrudit.out` will contain the $K$-th related number with $X$, greater than it. If there is no such number, print $-1$.

## Constraints and clarifications

The number $X$ has at most $1000$ digits

$K \leq 10^9$

For $15\%$ of the tests $K \leq 100$ and $X \leq 10^9$

For $25\%$ of the tests $K = 1$

For $45\%$ of the tests $K \leq 10^6$

## Example

`inrudit.in`
```
1
13
```

`inrudit.out`
```
31
```