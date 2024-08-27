# Remainders

Given $N$ distinct prime numbers $p_1$, $p_2$, $\dots$, $p_N$ and $N$ distinct remainders $r_1$, $r_2$, $\dots$, $r_N$.

## Task

Find the smallest non-negative number $X$ such that $X \mod p_k = r_k$, for any $k$ from $1$ to $N$.

## Input data

The first line of the input file `resturi.in` contains $T$, the number of tests. The following lines contain the description of the $T$ tests. Each test begins with a line that contains $N$. The following lines contain $2$ integers each, $p_k$ and $r_k$.

## Output data

For each test, print a single line in the output file `resturi.out` that contains the number $X$.

## Constraints and clarifications

$N \leq 30$

$1 < p_k < 1000$

$0 \leq r_k \leq p_k - 1$, for $k$ from $1$ to $N$

$a \mod b$ represents the remainder of the division of the number $a$ by $b$

## Example

`resturi.in`

$3$

$1$

$2 \ 1$

$2$

$2 \ 0$

$3 \ 1$

$3$

$5 \ 4$

$11 \ 3$

$19 \ 8$

$1 \ 4$

`resturi.out`

$179$