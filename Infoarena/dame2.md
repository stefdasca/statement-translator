## Queens 2

We have a chessboard $ ( 8 \times 8 )$ from which some squares have been destroyed. On the squares that are not destroyed, we need to place a minimal number of queens so that each square which is not destroyed is attacked, and any two queens do not attack each other. A queen attacks a square if it is on the same row, column, or diagonal (even if there are destroyed squares between them).

## Task

Calculate the minimum number of queens required and find a lexicographically minimal arrangement of these.

## Input data

The input file `dame2.in` will contain 8 lines with 8 characters each. Character $i$ on line $j$ will be $0$ if the square is not destroyed and $1$ otherwise.

## Output data

The first line of the output file `dame2.out` will contain $X$, the minimum number of queens required. The next line will contain $X$ pairs of numbers $a \ b$ indicating that a queen should be placed on row $a$ and column $b$.

## Constraints and clarifications

An arrangement $a 1 \ b 1 \ a 2 \ b 2 \ \dots \ a X \ b X$ is lexicographically smaller than $c 1 \ d 1 \ c 2 \ d 2 \ \dots \ c X \ d X$ if the string obtained by concatenation is lexicographically smaller.

The pairs will be separated by exactly one space.

If there is no solution, the output file will contain the number $0$ on the first line.

## Example

`dame2.in`
```
00000000  
00111111  
01011111  
01101111  
01110111  
01111011  
01111101  
00000000
```

`dame2.out`
```
2  
1 1  
8 2  
```

## Explanation

We place one queen on the first row and first column, and another queen on the last row and the second column.