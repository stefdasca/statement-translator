## Task

Let $N$ be any natural number less than or equal to $2\ 000\ 000\ 000$. We define $f(x)$ as $x^2$ if $x$ is positive and $-x^2$ if $x$ is negative. The task is to find three integers $X$, $Y$, and $Z$ such that $f(X) + f(Y) + f(Z) = N$.

## Input data

The input file `triplet.in` will contain a single natural number $N$ on the first and only line.

## Output data

The output file `triplet.out` must contain a single line with exactly 3 integers $X$, $Y$, and $Z$.

## Constraints and clarifications

$1 \leq N \leq 2\ 000\ 000\ 000$

$-2\ 000\ 000\ 000 \leq X$

$Y$

$Z \leq 2\ 000\ 000\ 000$

## Example

`triplet.in`
```
21
```

`triplet.out`
```
4 -2 3
```

## Explanation

$16 - 4 + 9 = 21$