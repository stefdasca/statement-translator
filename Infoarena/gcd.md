## Task

Given $2$ natural numbers $N$ and $M$, determine the greatest common divisor of $N_{secondary} = 2^N - 1$ and $M_{secondary} = 2^M - 1$. The answer must be displayed modulo $P$.

## Input data

The input file `gcd.in` will contain on the first line a natural number $T$, representing the number of tests. On the next $T$ lines, there will be $3$ natural numbers $N$, $M$, and $P$.

## Output data

The output file `gcd.out` will contain $T$ lines, each line containing the answer for the $i^{th}$ test.

## Constraints and clarifications

$1 \leq N, M, P \leq 1\ 000\ 000\ 000$

$1 \leq T \leq 100\ 000$

## Example

`gcd.in`
`
2
2 3 100
2 4 100
`

`gcd.out`
`
1
3
`

## Explanation

The greatest common divisor of $3$ and $7$ is $1$
and the greatest common divisor of $3$ and $15$ is $3$.