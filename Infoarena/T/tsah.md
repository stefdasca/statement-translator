## Task

A chessboard is a binary matrix of dimensions $N \times N$, with rows and columns numbered from $1$ to $N$. Each position is either black if the sum of the row number and column number is even, or white otherwise. The figure below illustrates what a chessboard looks like for $N = 1$, $N = 2$, and $N = 3$. Given a binary matrix, find the dimension of the largest chessboard completely located inside the matrix, as well as the number of chessboards of maximum dimension (these boards may partially overlap).

## Input data

The first line of the input file `tsah.in` contains an integer $T$, representing the number of upcoming tests. Each test contains an integer $N$ on the first line, representing the number of rows and columns of the given matrix. The next $N$ lines describe the matrix: each line contains $N$ characters, which can be either '1' (representing a black square) or '0' (representing a white square). The matrix will contain at least one '1' character.

## Output data

For each of the $T$ tests, in the order from the input file, print to the output file `tsah.out` a line containing the dimension of the largest chessboard, followed by a space and the number of chessboards of maximum dimension.

## Constraints and clarifications

$1 \leq T \leq 6$  
$1 \leq N \leq 2000$

The input file will have a maximum of 16 MB.

## Example

`tsah.in`
```
1  
5  
00101  
11010  
00101  
01010  
11101  
```

`tsah.out`
```
3 3
```