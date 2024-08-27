# Intervale2

Since he was not well-behaved during his computer science class, Andrei received an additional problem. Unable to solve it himself, he thought of asking for your help. Given an array $A$ made up of $N$ distinct numbers, find how many numbers in $A$ that are between positions $P[i]$ and $i$ (inclusive) are strictly greater than $A[i]$ for each $i$ from $1$ to $N$.

## Input data

The input file `intervale2.in` contains on the first line the number of elements, $N$. On the next 2 lines, there will be $N$ numbers each representing the array $A$ and $P$ respectively.

## Output data

The output file `intervale2.out` will print on the first line $N$ values representing the answers for each position.

## Constraints and clarifications

$1 \leq N \leq 100\ 000$

$-2\ 000\ 000\ 000 \leq A[i] \leq 2\ 000\ 000\ 000$

$1 \leq P[i] \leq i$

## Example

`intervale2.in`
```
5
6 9 8 15 7
1 1 2 1 2
```

`intervale2.out`
```
0 0 1 0 3
```

## Explanation

The intervals of interest are, in order: $[1, 1]$, $[1, 2]$, $[2, 3]$, $[1, 4]$, $[2, 5]$.