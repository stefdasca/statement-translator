# Aurel

Aurel would like to know how many golden arrays exist. A golden array has the following properties:
- It has length $N$
- It is strictly increasing
- The sum of its elements is $S$
- It contains only positive natural numbers

## Input data

The input file `aurel.in` contains on the first line the number of tests $T$. Each of the following lines contains the numbers $N$ and $S$, separated by a space.

## Output data

The output file `aurel.out` contains $T$ lines. Each line contains the required number modulo $666013$ for the respective test.

## Constraints

$T = 5$

$1 \leq N \leq 100$

$1 \leq S \leq 100000$

## Example

`aurel.in`

2

1 1

3 8

`aurel.out`

1

2

## Explanation

For the first test, the array $1$ can be formed. For the second test, the arrays $1, 2, 5$ and $1, 3, 4$ can be formed.