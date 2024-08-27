## Task

Let $A$ be an $N \times N$ matrix with natural numbers. The permanent of the matrix is the sum of all products $A[1, p[1]] \times A[2, p[2]] \times \dots \times A[N, p[N]]$ for all possible permutations $p$ of the elements $\{1, 2, \dots, N\}$. For example, the permanent of a $2 \times 2$ matrix is: $P = A[1,1] \times A[2,2] + A[1,2] \times A[2,1]$. Given a matrix $A$, calculate its permanent modulo $9901$.

## Input data

The input file `matperm.in` contains the integer $N$ on the first line. The next $N$ lines contain $N$ values each, representing the elements of the matrix. All numbers on the same line are separated by a space.

## Output data

The output file `matperm.out` will contain a single number, the permanent modulo $9901$.

## Constraints and clarifications

$2 \leq N \leq 20$ 

$0 \leq A[i,j] \leq 10\ 000$ 

For 30% of the tests, $N \leq 10$ 

For 70% of the tests, $N \leq 16$

## Example

`matperm.in`

```
3
1 2 3
4 5 6
7 8 9
```

`matperm.out`

```
450
```