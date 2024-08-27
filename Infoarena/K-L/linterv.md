## Task

Lengths of Intervals

You are given $N$ intervals $[A_i, B_i]$ $(1 \leq i \leq N)$. Calculate the sum of the lengths of all intervals. Overlapping intervals should be counted only once.

## Input data

The input file `linterv.in` will contain multiple test cases. The first line contains $T$, the number of test cases. The first line of each test case contains $N$ - the number of intervals, followed by $N$ lines each containing two numbers $A_i$ and $B_i$ - the endpoints of the intervals.

## Output data

The output file `linterv.out` will contain $T$ lines, each containing a single number $x$ - the calculated sum.

## Constraints

$1 \leq N \leq 5000$

$-1000000 \leq A_i \leq B_i \leq 1000000$

$1 \leq T \leq 75$

## Example

`linterv.in`

```
1
6
-5 5
0 3
2 8
10 13
11 15
100 100
```

`linterv.out`

```
18
```