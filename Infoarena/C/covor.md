# Carpet

Miruna has a square matrix of size $N$ with elements from the set $\{0, 1\}$. She wants to know how many submatrices that contain only $0$ exist.

## Input data

The input file `covor.in` will contain on the first line the number $N$, having the significance from the statement. The next $N$ lines will contain $N$ numbers from the set $\{0, 1\}$ without spaces in between, representing the matrix.

## Output data

In the output file `covor.out` you will print a single number, representing the number of submatrices that meet the condition from the statement.

## Constraints and clarifications

$1 \leq N \leq 2\,000$

For 50$\%$ of tests $N \leq 400$

A submatrix represents the two-dimensional extension of the subarray and not the subsequence.

## Example

`covor.in`

```
5
00100
00001
11000
00010
10000
```

`covor.out`

```
57
```