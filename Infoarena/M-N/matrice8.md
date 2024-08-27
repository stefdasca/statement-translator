## Task

Aurel has a binary matrix with $N$ rows and $M$ columns. He can cut the matrix into two along a row or column. Aurel wants to repeat the cutting process on the resulting matrices until all obtained matrices are uniform. A matrix is uniform if it contains only $0$s or only $1$s. Help Aurel determine the minimum number of cuts required to obtain only uniform matrices.

## Input data

The input file `matrice8.in` will contain on the first line $T$, the number of tests. Each test will contain on its first line two natural numbers, $N$ and $M$, having the significance from the statement. On the following $N$ lines, there will be $M$ digits from the set ${0, 1}$, representing Aurel's matrix.

## Output data

The output file `matrice8.out` will contain $T$ lines, with the number of minimum cuts for test $i$ on line $i$.

## Constraints and Clarifications

$T = 10$

$1 \leq N$

$M \leq 30$

## Example

`matrice8.in`

```
2
5 6
000000
000000
000111
000111
000000
2 3
000
011
```

`matrice8.out`

```
3
2
```