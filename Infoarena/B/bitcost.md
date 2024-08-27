## Task

You are given an array with $K$ integers, the $i$-th number representing the cost of the $i$-th least significant bit. We define the cost of a number $x$ as the sum of the costs of the $1$ bits in the binary representation of the number $x$. For example, if we have the array $[3, -2, 7]$, the cost of the number $6(110)$ is $-2 + 7 = 5$, and the cost of the number $3(011)$ is $3 - 2 = 1$. $M$ queries of the type $a, b$ are given: what is the maximum cost of a number in the interval $[a, b]$?

## Input data

The input file `bitcost.in` will contain two natural numbers $K$ and $M$ on the first line. The second line will contain $K$ numbers representing the bit costs. The next $M$ lines will contain $2$ numbers $a, b$ representing the queries.

## Output data

The output file `bitcost.out` will contain $M$ lines, with the answer for query $i$ on the $i$-th line.

## Constraints and clarifications

$1 \leq K \leq 60$

$1 \leq M \leq 100\ 000$

$1 \leq a \leq b \leq 2^K - 1$

The costs are integers in the interval $[-1\ 000\ 000, +1\ 000\ 000]$

## Example

`bitcost.in`

```
3 2
3 -2 7
1 7
2 4
```

`bitcost.out`

```
10
7
```