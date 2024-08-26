## Task

Let $P$ be a permutation of order $N$. We define an inversion as a pair of indices $(i, j)$ with the property that $i < j$ and $P[i] > P[j]$. In this problem, you need to display a permutation of order $N$ with exactly $K$ inversions.

## Input data

The input file `invinv.in` will contain on its first line the value $T$, representing the number of tests in the input file. The next $T$ lines will each contain a pair of numbers $N$ and $K$.

## Output data

The output file `invinv.out` will contain $T$ lines. The $i$-th line will contain a permutation corresponding to the $i$-th test from the input file.

## Constraints and clarifications

$1 \leq N \leq 50\ 000$ 

$0 \leq K \leq N * (N - 1) / 2$ 

Any permutation of order $N$ with $K$ inversions is accepted.

It is guaranteed that the sum of the values of $N$ in an input file is at most equal to the value $600\ 000$.

Note that there is no explicit limitation for $T$.

## Example

`invinv.in`

```
3
1 0
4 1
4 6
```

`invinv.out`

```
1
1 3 2 4
4 3 2 1
```