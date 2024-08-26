## Subpermutations

Let $P$ be a permutation of length $N$. We say that another permutation $R$ (of length $M \leq N$) is a subpermutation of $P$ at position $i$ ($i \leq N - M + 1$) if for any $j$ and $k$ between $1$ and $M$ with $j ≠ k$ and $R[j] < R[k]$ then $P[j + i - 1] < P[k + i - 1]$. For example, the permutation $1$ $2$ is a subpermutation of $1$ $3$ $2$ $4$ at positions $1$ and $3$. You are given a permutation $P$ and you are required for each permutation $R$ that appears at least once as a subpermutation in $P$ to count its frequency of occurrences in $P$. For simplicity, you are asked for the sum of the squares of these numbers.

## Input data

The input file `subpermutari.in` will contain on the first line $N$, the size of permutation $P$. The next line will contain $N$ distinct values between $1$ and $N$, separated by space, the elements of the permutation.

## Output data

The output file `subpermutari.out` must contain a single number, the one required in the task.

## Constraints

$1 \leq N \leq 2000$

## Example

`subpermutari.in`
```
4 
1 3 2 4
```
`subpermutari.out`
```
24
```

## Explanation

The following subpermutations appear in $P$:
- $1 \rightarrow$ at positions $1$ $2$ $3$ and $4$
- $1$ $2 \rightarrow$ at positions $1$ and $3$
- $2$ $1 \rightarrow$ at position $2$
- $1$ $3$ $2 \rightarrow$ at position $1$
- $2$ $1$ $3 \rightarrow$ at position $2$
- $1$ $3$ $2$ $4 \rightarrow$ at position $1$

The number of occurrences of these subpermutations is $4$, $2$, $1$, $1$, $1$, and $1$. The answer is $4 \cdot 4 + 2 \cdot 2 + 1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1 + 1 \cdot 1 = 24$.