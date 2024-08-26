# Farey Sequence

A Farey sequence of order $N$ is the sequence of all irreducible fractions $P / Q$ with $0 < P < Q \leq N$, arranged in increasing order. For example, the Farey sequence of order 5 is: $1 / 5 \ 1 / 4 \ 1 / 3 \ 2 / 5 \ 1 / 2 \ 3 / 5 \ 2 / 3 \ 3 / 4 \ 4 / 5$. We will number the fractions in the sequence starting from $1$. For example, the $6$-th fraction in the Farey sequence of order 5 is $3 / 5$.

## Task

Given $N$ and a number $K$, find the $K$-th fraction in a Farey sequence of order $N$.

## Input Data

The input file `farey.in` contains a single line with the numbers $N$ and $K$ separated by a space. $K$ will always be a valid index, meaning it will be at least $1$ and will not be greater than the number of fractions in the Farey sequence of order $N$.

## Output Data

The output file `farey.out` will contain a single line with two integers $P$ and $Q$ separated by a space. The fraction $P / Q$ must be the $K$-th fraction in the Farey sequence of order $N$. The fraction must be irreducible, meaning the greatest common divisor between $P$ and $Q$ must be $1$.

## Constraints and clarifications

$1 < N \leq 40\ 000$

40% of the tests will have $K \leq 50\ 000$

All test data used for evaluation will have $N \geq 10\ 000$

## Example

`farey.in`
```
5 6
```

`farey.out`
```
3 5
```

Friendly advice This is not a mathematics problem; only elementary mathematical knowledge is needed to solve it. Instead, you need to find an efficient algorithm to solve it.