## Task

The Romanian word $“popeală”$ originates from the Romanian historical novel "Alexandru Lăpuşneanul" where the Prince of Moldova uses a series of terms to describe his future revenge on the usurpers. The term has recently been adopted, somewhat surprisingly, on the Romanian programming competition scene. It is used to describe situations when the committee makes life difficult for competitors in an unorthodox and (usually) involuntary manner: very strict time limits, erroneous tests, incorrect problems, stolen keyboards, and other mechanisms.

This problem refers to a “popeală”. We consider a programming contest with $N$ participants. The contest has only one problem with $T$ tests. The scientific committee wants to group the tests into at most $S$ subproblems. 

How subproblems work: Each test belongs to exactly one subproblem. A subproblem can contain any number of tests but at least one. If a participant fails at least one test of a subproblem, their score for that subproblem will be 0. Otherwise, the score for that subproblem will be equal to the sum of the point values of all the subproblem's tests. This is a common practice in programming contests, but now the committee wants to do this after the contest is over.

The committee knows which tests each participant solved correctly and wants to group the tests of each subproblem so as to minimize the total number of points obtained in the contest. Specifically, you are given an array of integers $Points[]$ of size $T$. $Points[i]$ will contain the point value of the $i$-th test. You also receive a two-dimensional array $Results[][]$ of size $N \times T$. $Results[i][j]$ will be equal to 1 if the $i$-th contestant solved the $j$-th test correctly. Otherwise, it will be 0.

The committee has already decided that all subproblems will contain consecutive tests. In other words, if tests $X$ and $Y$ are included in the same subproblem, then any test $Z$ with $X \leq Z \leq Y$ will be in the same subproblem.

You need to help the committee. They want to know, for each value $1 \leq K \leq S$, what is the minimum total number of points possible in the contest if the tests are grouped into exactly $K$ subproblems.

## Input data

The input file `popeala.in` will contain on the first line three positive integers $N$, $T$, and $S$, separated by space. The second line will contain $T$ integers, separated by space, representing the elements of the array $Points[]$. The following $N$ lines will each contain a binary string of length $T$, representing the elements of the matrix $Results[][]$.

## Output data

The output file `popeala.out` will contain $S$ lines. The $i$-th line must contain a single integer: the minimum total number of points that can be obtained in the contest by grouping the tests into $i$ subproblems.

## Constraints and clarifications

$1 \leq T \leq 20\ 000$

$1 \leq N \leq 50$

$1 \leq S \leq \min(50, T)$

$1 \leq Points[i] \leq 10\ 000$, for any $1 \leq i \leq T$.

It is guaranteed that $(Points(1) + Points(2) + \ldots + Points(T)) \times N \leq 2\ 000\ 000\ 000$ for all tests.

For tests worth 8 points, $T \leq 40$.

For other tests worth 9 points, $40 < T \leq 500$.

## Example

`popeala.in` 

```
2 3 3 
4 3 5 
101 
110 
```

`popeala.out` 

```
0 
8 
16 
```

## Explanation

We have $N = 2$ contestants, $T = 3$ tests and at most $S = 3$ which means that we need to calculate the minimum score for 1, 2, and respectively 3 subproblems. The array $Points[] = \{4, 3, 5\}$. In the case of a single subproblem, the total number of points that can be obtained is 0, because no contestant has solved all the cases correctly and all tests must be in the same subproblem. There are two ways to group the tests into two subproblems. One of them leads to a total of 12 points and the other to a total of 8 points. Since we are looking for the minimum value, we will choose the second one. There is also a single way to group the tests into three subproblems, which leads to a score of 16 points.