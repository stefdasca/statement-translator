# Suma6

Given two natural numbers $N$ and $S$ and an array of $N$ natural numbers $a_1, a_2, \dots, a_N$.

## Task

Answer $Q$ queries of the type $(L, R)$, for each query specifying the number of pairs $(i, j)$, $L \leq i < j \leq R$ with the property $a_i + a_j = S$.

## Input data

The input file `suma6.in` contains the natural numbers $N$ and $S$ on the first line. The 2nd line contains the values $a_1, a_2, \dots, a_N$ separated by exactly one space. The 3rd line contains $Q$, the number of queries, and on each of the following $Q$ lines, there are two numbers $L R$ separated by a space, corresponding to a query. 

## Output data

The output file `suma6.out` will contain $Q$ lines, on line $i$ will be the answer for the $i$-th query.

## Constraints and clarifications

$2 \leq N \leq 100\ 000$

$1 \leq Q \leq 200\ 000$

$0 \leq a_i \leq 1\ 000\ 000,$ $1 \leq i \leq N$

$1 \leq L \leq R \leq N$

$0 \leq S \leq 1\ 000\ 000$

## Example

`suma6.in`
```
10 10
1 4 8 9 6 1 10 4 12 1
5
1 4
1 10
5 6
4 6
1 5
```

`suma6.out`
```
0
1
3
0
1
```

## Explanation

For example, for the last query $1 6$, the 3 pairs are: $a_1 + a_4 = 10$; $a_2 + a_5 = 10$; $a_4 + a_6 = 10$.