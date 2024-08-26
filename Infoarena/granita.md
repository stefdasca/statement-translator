# Border

At the border of state $A$ with state $B$, there are $N$ defense devices. For each device $k$, the operating interval $[A_k, B_k]$ is known (the border is considered to be a straight line, and each device covers a certain segment of this line). To reduce maintenance costs, the president of state $A$ has decided that some of the $N$ defense devices should be dismantled. Specifically, redundant devices will be dismantled. A device $i$ is redundant if there is at least one other device $j$ such that the interval $[A_i, B_i]$ is included in the interval $[A_j, B_j]$ (i.e., $A_j < A_i$ and $B_i < B_j$).

## Task

Determine how many of the $N$ defense devices are redundant.

## Input data

The first line of the input file `granita.in` contains the integer $N$, representing the number of defense devices. The next $N$ lines contain two integers, $a$ and $b$ ($a < b$), representing the endpoints of the intervals in which each device operates.

## Output data

The output file `granita.out` contains a single line that prints a single integer, representing the number of redundant devices.

## Constraints and clarifications

$1 \leq N \leq 16\,000$

$0 \leq A_i < B_i \leq 2\,000\,000\,000$

All numbers $A_i$ will be different from each other

All numbers $B_i$ will be different from each other

## Examples

`granita.in`

```
5
0 10
2 9
3 8
1 15
6 11
```

`granita.out`

```
3
```

## Explanation

The redundant devices are: the second, third, and fifth.