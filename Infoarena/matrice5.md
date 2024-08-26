# Matrix5

You are given $4$ numbers $N$, $M$, $P$, $K$ and the task is to find out how many matrices with $N$ rows and $M$ columns with values between $1$ and $K*P$ exist such that the sum on any row and any column is a multiple of $K$. 

## Input data

The input file `matrice5.in` will contain on the first line a natural number $T$ representing the number of tests, and on the next $T$ lines, $4$ natural numbers $N$, $M$, $P$, $K$ with the meaning defined in the statement.

## Output data

The output file `matrice5.out` will contain $T$ lines. Line $i$ will contain the answer for test $i$ modulo $10007$.

## Constraints and clarifications

$1 \leq N \leq 1000$

$1 \leq M \leq 1000$

$2 \leq K \leq 1000$

$1 \leq P \leq 1000$

$1 \leq T \leq 100000$

## Example

`matrice5.in` 

```
4
2 3 1 9
3 2 4 3
2 4 6 2
5 5 3 4
```

`matrice5.out` 

```
81
6843
7534
7579
```