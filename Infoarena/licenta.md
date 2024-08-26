## Task

In her final year of university, Mihaela decides to finish her thesis titled 'The minimal polynomial of a root of order $O$ in an algebraic extension of degree $G$'. Because her work has produced results related to the existence of Martians, she wishes to meet with her advisor, the dean. Unfortunately, time is not on her side. Mihaela has a set of intervals $S$ of size $N$ during which she can come to the university. The dean is a very busy person like Mihaela, so he has a set of intervals $T$ of size $M$ during which he is in his office. Mihaela needs exactly $K$ minutes to explain the ideas in her thesis to her advisor. Since our heroine is working on the conjecture $P=NP$, she asks you to find a time interval of exactly $K$ seconds such that she is at the university and her advisor is in his office. If there are multiple solutions of the form $[X, Y]$, she wants you to display the interval with the minimum $X$. If there is no solution, then display $-1$ on the first line.

## Input data

The input file `licenta.in` contains on the first line the natural number $K$ specified in the statement. 

The second line contains a single natural number $N$ representing the size of the set $S$. 

The following $N$ lines contain $2$ natural numbers separated by a space: $XS[i]$, $YS[i]$ specifying the intervals of minutes during which Mihaela is at the university. The intervals are pairwise disjoint. 

The next line contains the natural number $M$. 

The following $M$ lines contain $2$ natural numbers separated by a space: $XT[j]$, $YT[j]$ specifying the intervals of minutes during which the professor is in his office. The intervals are pairwise disjoint. 

## Output data

The first line contains $2$ natural numbers separated by a space $X$, $Y$, representing the time interval during which Mihaela meets the Dean. 

## Constraints and clarifications

$1 \leq K < 10^9$

$1 \leq N \leq 10^5$

$0 \leq XS[i] < YS[i] < 10^9$ for any $1 \leq i \leq N$

$1 \leq M \leq 10^5$

$0 \leq XT[j] < YT[j] < 10^9$ for any $1 \leq j \leq M$

For $40$ points 

$1 \leq N * M \leq 5 \cdot 10^6$

To get $100$ points, you need to do it for the watch.

## Example

`licenta.in`

```
4
2
1 10
11 13
2
2 4
5 12
```

`licenta.out`

```
5 9
```

## Explanation

Mihaela can be at the university during the intervals $[1, 10]$; $[11, 13]$. 

The dean is in his office during the intervals $[2, 4]$; $[5, 12]$. 

It can be observed that if Mihaela meets starting from minute $5$, she manages to explain her entire thesis for $4$ minutes. Therefore, the solution is the interval $[5, 9]$.