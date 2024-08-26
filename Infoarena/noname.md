## Noname

A natural number $N$ and $2$ permutations of length $N$: $P_1$ and $P_2$ are given. It is required to determine how many matrices with $N$ rows and $N$ columns exist filled with $0$s and $1$s which respect the property that on row $i$, the sum of the elements is equal to $P_1[i]$, and on column $i$ the sum of the elements is equal to $P_2[i]$. The answer must be determined modulo $666013$, and a solution must also be reconstructed.

## Input data

The input file `noname.in` will contain on the first line a natural number $N$. Line $2$ will contain $N$ elements representing the permutation $P_1$ and line $3$ will contain the permutation $P_2$.

## Output data

The output file `noname.out` will contain on the first line a natural number representing the answer modulo $666013$. On the next $N$ lines, $N$ numbers between $0$ and $1$ will be printed, representing a matrix that satisfies the given property.

## Constraints and clarifications

$1 \leq N \leq 1000$.

For the reconstruction of the solution, any matrix that satisfies the given property is acceptable.

## Example

`noname.in`

```
2
2 1
1 2
```

`noname.out`

```
1
1 1
0 1
```