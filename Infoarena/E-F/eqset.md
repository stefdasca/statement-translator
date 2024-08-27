## Task

Given $X$ and $Y$ as two natural numbers, determine if $X$ and $Y$ have exactly the same prime factors.

## Input data

The input file `eqset.in` will contain the value $T$ on its first line, representing the number of tests in the input file. The next $T$ lines will each contain a pair of numbers $X$ $Y$.

## Output data

The output file `eqset.out` will contain $T$ lines, the $i$-th of which will contain the value $1$ if the answer for the $i$-th test from the input file is positive, and $0$ otherwise.

## Constraints and clarifications

$1 \leq T \leq 100\ 000$

$1 \leq X, Y \leq 10^{18}$

## Example

`eqset.in`

```
3
12 18
12 13
1 8
```

`eqset.out`

```
1
0
0
```