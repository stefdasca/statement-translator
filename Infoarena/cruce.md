## Cross

A matrix $N \times M$ containing only lowercase English letters is given. Calculate how many palindrome crosses exist. A palindrome cross with the center $(x, y)$ and arms of lengths $K_1$ and $K_2$ $(K_1, K_2 \geq 1)$ is formed by the cells $(x-K_1, y)$, $(x-K_1+1, y)$, $\dots$, $(x+K_1, y)$ vertically and $(x, y-K_2)$, $(x, y-K_2+1)$, $\dots$, $(x, y+K_2)$ horizontally. Furthermore, $(x-K_1, y)$, $(x-K_1+1, y)$, $\dots$, $(x+K_1, y)$, and $(x, y-K_2)$, $(x, y-K_2+1)$, $\dots$, $(x, y+K_2)$ must be palindromes. A sequence is called a palindrome if it reads the same from left to right as it does from right to left.

## Input data

The input file `cruce.in` contains 2 numbers $N$ and $M$ on the first line. The next $N$ lines contain $M$ characters (without spaces between them) on each line.

## Output data

The output file `cruce.out` should contain a single natural number representing the number of palindrome crosses in the given matrix.

## Constraints

$1 \leq N, M \leq 100$

## Example

`cruce.in`
```
3 4
abcc
cccc
bbca
```

`cruce.out`
```
2
```

## Explanation

One cross is centered at $(2,2)$ and the second at $(2,3)$.