PermutariAB

Consider two permutations $A$ and $B$ of the set ${1, 2, \dots, N}$. By one operation, you can select two adjacent elements from $B$ and swap them (i.e. $\text{swap}(B[i], B[i + 1])$ for $1 \leq i < N$). Determine the minimum number of operations needed to transform $B$ into $A$.

## Task

## Input data

The input file `permutariab.in` contains on the first line the natural number $N$. The second line contains $N$ natural numbers, separated by a space, representing permutation $A$. The third line also contains $N$ natural numbers, separated by a space, representing permutation $B$.

## Output data

The output file `permutariab.out` contains on the first line the natural number $X$, representing the minimum number of operations needed to transform $B$ into $A$.

## Constraints

$1 \leq N \leq 100\ 000$

For 70% of the score, $1 \leq N \leq 1\ 000$

## Example

`permutariab.in`

```
6
2 1 3 4 5 6
1 3 4 5 6 2
```

`permutariab.out`

```
5
```

`permutariab.in`

```
10
1 5 2 3 4 6 9 10 7 8
3 9 5 1 2 7 8 10 4 6
```

`permutariab.out`

```
17
```

## Explanation

In the first example, you swap $2$ with $6$, then $2$ with $5$, then $2$ with $4$, then $2$ with $3$, and finally $2$ with $1$.