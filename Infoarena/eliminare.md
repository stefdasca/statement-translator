# Elimination

Consider a sequence of $n$ natural numbers $x_1, x_2, \dots, x_n$ on which $m$ elimination operations are successively performed. An elimination operation consists of choosing two indices $i, j$ $(1 \leq i \leq j \leq$ number of elements in the sequence$)$ and eliminating the largest element in the subarray $x_i, x_{i+1}, \dots, x_j$. If there are multiple elements with the maximum value, the one with the smallest index will be eliminated. After each elimination, the sequence elements are renumbered (the indices of the elements after the eliminated one are decremented by $1$).

## Task

Determine the subsequence remaining after the $m$ elimination operations.

## Input data

The first line of the input file `eliminare.in` contains two natural numbers separated by a space $n m$, representing the number of elements in the initial sequence and the number of elimination operations, respectively. On the next $n$ lines, the numbers of the initial sequence are written, one per line. Each of the last $m$ lines contains two natural numbers separated by a space $i j$ representing the indices between which an elimination operation is executed. More precisely, on line $1+n+k$ $(1 \leq k \leq m)$, the interval corresponding to the $k$th elimination $(1 \leq i \leq j \leq n-k+1)$ is written.

## Output data

The output file `eliminare.out` will contain the $n-m$ remaining numbers, respecting the initial order, one number per line.

## Constraints and clarifications

$2 \leq n \leq 1\ 000\ 000$

$1 \leq m \leq \min(n-1, 500\ 000)$

The terms of the sequence are non-zero natural numbers less than or equal to $300\ 000$

## Example

`eliminare.in`
```
8 5
3
7
2
5
8
5
9
4
2 5
6 6
3 6
2 5
1 2
```

`eliminare.out`
```
4
2
5
4
```