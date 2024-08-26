# Drum6

We all know how much Trăncănici loves to talk. So much so, that the night before, he had a very strange dream... He found himself in the cell $(1, 1)$ of a matrix with $N$ rows and $M$ columns. Each cell in the matrix contains a lowercase letter from the English alphabet. In his dream, he had quite a difficult mission. Starting from cell $(1, 1)$, he had to reach cell $(N, M)$ in the matrix, moving only right or down at each step. Because there are so many such paths and Moş Ene realizes that Trăncănici will talk a lot thinking about all possibilities, the dream asks him to choose the lexicographically smallest path.

## Input data

The input file `drum6.in` contains on the first line two natural numbers $N$ and $M$, representing the dimensions of the matrix. Each of the next $N$ lines contains $M$ characters (lowercase letters of the English alphabet), representing the content of the matrix.

## Output data

The output file `drum6.out` will contain a sequence formed of $N + M - 1$ characters, representing the lexicographically smallest path from cell $(1, 1)$ to cell $(N, M)$ of the matrix.

## Constraints

$1 \leq N, M \leq 1000$

## Example

`drum6.in`
```
5 5
abfsd
asfkg
mcxjf
sdgjg
sdgkj
```

`drum6.out`
```
aamcddgkj
```