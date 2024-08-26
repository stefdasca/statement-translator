Segmente2

Vlad drew $N$ points on a plane, at integer coordinates, numbered in order from $0$ to $N-1$. He wants to draw $K$ distinct segments with each having endpoints in $2$ out of the $N$ points, such that the sum of the lengths of the $K$ segments is minimal. Your task now is to determine the minimum total length of the $K$ segments, as well as the points that belong to at least one segment, regardless of how Vlad draws those $K$ segments.

## Task

## Input data

The input file `segmente2.in` contains on the first line $2$ natural numbers $N$ and $K$, and on the next $N$ lines contains two integers $X_i$, $Y_i$ representing the coordinates of each point.

## Output data

In the output file `segmente2.out` you will print on the first line the minimum total length of the $K$ segments, with a precision of $5$ decimal places. Then, separately, print on each line and in ascending order the indices of the points that will belong to at least one of the $K$ segments, regardless of how they are drawn (If we remove any of these points, then it would no longer be possible to obtain an equally good solution with the remaining points).

## Constraints and clarifications

$2 \leq N \leq 5000$

$1 \leq K \leq \frac{N (N+1)}{2}$

$1 \leq K \leq 100$

all coordinates are integers in the range $[-10^9$, $10^9]$

the coordinates of the points are not necessarily distinct

## Example

`segmente2.in`
```
6 3
1 2
4 5
2 3
1 1
8 8
7 4
```

`segmente2.out`
```
4.65028
0
2
3
```