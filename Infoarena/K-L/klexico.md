## K-Lexicographic

Given a string $A$ of length $N$ with lowercase letters from the English alphabet and a number $K$, how many strings $B$ exist that satisfy the following properties:

- Have the same length $N$
- Are also composed of lowercase letters from the English alphabet
- For any $i,j$, $1 \leq i,j \leq N$ and $j - i + 1 == K$, the string $A[i\ldots j] < B[i\ldots j]$, where $A[i\ldots j]$ represents the substring formed by the elements from position $i$ to position $j$.

Two strings satisfy the property $A < B$ (string $A$ is less than another string $B$) if $A$ is strictly lexicographically smaller than $B$.

## Input data

The input file `klexico.in` will contain 2 natural numbers $N$ and $K$ on the first line. On the second line, the string $A$ will be present.

## Output data

The output file `klexico.out` will contain a single natural number representing the answer modulo $666013$.

## Constraints and clarifications

$1 \leq N \leq 100000$

$1 \leq K \leq N$

For tests worth 40 points $N \leq 1000$

## Example

`klexico.in`
```
5 2
zywxx
```

`klexico.out`
```
214
```