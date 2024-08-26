Zero

We only consider $L$-digit numbers written in base $B$ ($2 \leq B < L \leq 20$), where the first digit (the most significant) is different from $0$.

## Task:

Given two numbers $P$ and $Q$ ($2 \leq P$, $Q \leq L-1$), the task is to find:
a) How many numbers exist with at most $P$ consecutive $0$ digits (zeroes).
b) How many numbers exist with at least $Q$ consecutive $0$ digits (zeroes).

## Input data

The first line of the input file `zero.in` contains the numbers $L$, $B$, $P$, and $Q$, separated by spaces.

## Output data

The first line of the output file `zero.out` contains the number required for point a), while the second line of the file will contain the number required for point b).

## Example:

`zero.in`
```
3 2 1 2
```

`zero.out`
```
3
1
```

For at most one zero digit, we have the numbers $101$, $110$, and $111$, and for at least $2$ consecutive zeroes we have the number $100$.