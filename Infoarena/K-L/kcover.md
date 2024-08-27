## Task

You are given $N$ points on the $OX$ axis. The points are numbered from $1$ to $N$, and point $i$ is positioned at coordinate $x_i$. You need to place $K$ closed intervals on the $OX$ axis, such that each of the $N$ points is covered by at least one of the $K$ intervals (a point $i$ is covered by an interval $[a,b]$ if $a \leq x_i \leq b$). The aim is to minimize the sum of the lengths of the $K$ intervals.

## Input data

The first line of the input file `kcover.in` contains the integer number $T$, representing the number of tests that follow. Each test consists of 2 lines. The first line contains the integers $N$ and $K$, separated by a space. The second line contains the coordinates of the $N$ points, separated by spaces.

## Output data

For each of the $T$ tests in the input file, in the order given in the file, print a line in the output file `kcover.out` representing the minimum sum of the lengths of the $K$ intervals, such that each point is covered.

## Constraints and clarifications

$1 \leq T \leq 10$

$1 \leq K \leq N \leq 100\ 000$

$-2\ 000\ 000\ 000 \leq x_i \leq 2\ 000\ 000\ 000$

The length of a closed interval $[a,b]$ is equal to $b-a$.

## Example

`kcover.in`
```
6
6 1
2 4 1 8 3 6
6 2
2 4 1 8 3 6
6 3
2 4 1 8 3 6
6 4
2 4 1 8 3 6
6 5
2 4 1 8 3 6
6 6
2 4 1 8 3 6
7 5
3 2 1 0 7
```

`kcover.out`
```
1
3
6
5
4
2
7
```