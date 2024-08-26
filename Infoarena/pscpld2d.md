# PScPld2D

Given a square matrix of size $N$ which contains lowercase letters of the Latin alphabet, the task is to calculate how many odd-sized palindromic submatrices exist in the given matrix.

## Input data

The input file `pscpld2d.in` contains on the first line the number $N$ as described in the statement. On the following $N$ lines, each line will contain $N$ characters, representing the content of the matrix.

## Output data

In the output file `pscpld2d.out` you will print the requested number on the first line.

## Constraints

$1 \leq N \leq 1000$  
A matrix is palindromic if all its rows are palindromes and all its columns are palindromes.

## Example

`pscpld2d.in`  
```
5
isxsi
kowok
arura
kowok
isxsi
```

`pscpld2d.out`  
```
27
```