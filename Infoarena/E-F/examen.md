## Task

Passing an exam is like crossing a zebra crossing, First you look left and right. During an exam, $N$ students are seated at a circular table. They have to solve a single problem. After many calculations, everyone has come to their own result. Of course, no one is sure whether this result is correct or not. Thus, instinct made everyone look to the left and right. Instead of recording their own result, they recorded the sum of the results of their two neighbors. In the last minute, a huge wave of conscience struck them all at once. Quickly they realized that they won't get anywhere in life by cheating and finally decided to write down their own result. The problem is that everyone lost the rough draft with the initial result. The only information they have available is the sum of the results of their two neighbors. Help the students follow the right path by reconstructing the initial results.

## Input data

The input file `examen.in` will contain a natural number $N$, the number of students. The next line contains $N$ values, the $i$-th representing the information of the $i$-th student.

## Output data

The output file `examen.out` will contain on a single line $N$ natural numbers representing the initial results of the $N$ students. If the solution is not unique, print $-1$.

## Constraints and clarifications

$4 \leq N \leq 100\ 000$

The initial results are integers in the range $[-1\ 000\ 000\ 000, 1\ 000\ 000\ 000]$

The neighbors of student $1$ are $2$ and $N$.

The neighbors of student $N$ are $1$ and $N - 1$.

It is guaranteed that there is at least one configuration of the initial results that satisfies the input conditions.

## Example

`examen.in`
```
5
6 13 11 10 10
```

`examen.out`
```
4 5 9 6 1
```