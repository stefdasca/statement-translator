Redu

Rebeca has a character string $S$ of even length $N$, which contains lowercase letters of the English alphabet. Rebeca can perform any number of reduction operations on the string. A reduction operation consists of choosing two consecutive characters $x$ and $y$ (i.e., they appear one after the other) and removing them from the string; the two possibly remaining strings are then rejoined. Each operation has a cost that depends on the chosen pair $(x, y)$, determined by the matrix $C$ with 26 rows and 26 columns where $C[x][y]$ equals the cost of removing the pair $(x, y)$. Rebeca wants to reduce the entire string with the minimum possible total cost.

## Input data

The input file `redu.in` will contain on the first line the number $N$ representing the length of the string $S$. The second line will contain the string $S$. The following 26 lines will contain 26 space-separated numbers representing the matrix $C$. The $i$-th row and $j$-th column represent the cost of an operation $(x, y)$ where $x$ is the $i$-th lowercase letter of the English alphabet and $y$ is the $j$-th lowercase letter of the English alphabet.

## Output data

In the output file `redu.out` you will print a single number representing the minimum total cost with which Rebeca can reduce the entire string $S$.

## Constraints and clarifications

$1 \leq N \leq 500$

$N$ is even

$0 \leq C[i][j] \leq 10000$

## Example

`redu.in`  
`4`  
`acab`  
`4 2 3 5 9 1 6 9 2 4 1 3 7 8 8 4 7 3 9 6 3 4 5 6 3 9 1`  
`5 0 3 7 7 9 9 4 0 2 1 0 4 5 1 9 4 2 8 8 1 3 8 7 7 1 4`  
`5 6 3 8 3 6 1 0 5 1 9 9 1 2 0 3 8 6 5 8 0 9 6 1 0 1 9`  
`0 0 1 6 5 9 0 4 3 8 7 5 3 0 7 2 4 1 5 7 9 3 2 7 5 3 5`  
`6 6 7 5 8 7 9 4 3 0 6 9 3 4 6 9 9 7 8 4 1 9 9 8 8 2 3`  
`6 7 8 3 6 4 0 1 2 0 2 9 5 3 5 4 8 2 2 9 1 9 7 5 2 6 6`  
`1 5 0 6 3 0 4 8 6 1 1 9 5 1 2 4 8 7 0 4 5 2 6 5 5 8 2`  
`3 0 1 9 3 8 0 9 1 2 6 1 8 9 2 9 4 3 1 9 1 8 1 5 6 3 4`  
`1 0 2 5 3 2 6 3 8 4 5 9 7 7 7 9 7 6 1 6 1 7 0 2 0 0 3`  
`8 6 8 2 9 8 6 7 2 0 3 7 8 0 4 8 9 3 5 0 0 4 4 8 5 3 0`  
`9 3 1 2 1 9 2 5 9 0 1 6 4 2 1 1 2 3 7 2 5 0 0 5 2 4 1`  
`1 9 4 1 8 8 4 2 1 4 4 9 5 6 2 3 1 6 6 4 9 2 2 1 7 4 1`  
`4 7 7 6 8 8 0 1 8 0 8 0 4 2 6 3 9 3 7 2 6 4 0 2 3 2 6`  
`6 1 1 0 6 8 7 4 8 6 6 1 4 7 9 7 3 1 5 6 2 8 3 6 6 9 7`  
`9 2 1 5 1 3 8 1 9 6 0 3 6 8 9 8 5 8 7 2 1 1 7 9 5 8 5`  
`2 6 4 9 5 9 0 3 0 5 1 3 6 0 5 9 6 4 1 6 9 1 6 3 5 7 2`  
`4 2 2 1 6 9 6 5 6 7 8 1 9 5 3 2 2 5 7 3 3 1 4 0 2 8 8`  
`7 3 5 0 9 9 2 3 8 3 1 3 0 8 3 1 7 9 6 9 3 3 8 6 7 2 3`  
`9 4 1 7 2 6 4 4 7 5 8 0 3 2 1 9 4 9 4 5 6 5 4 7 8 7 8`  
`5 6 0 8 5 6 1 4 0 7 0 4 4 6 3 5 1 7 6 0 1 8 5 8 6 0 2`  
`4 1 2 4 6 8 4 6 6 0 7 2 3 4 3 7 0 1 2 5 2 9 4 5 2 2 0`  
`1 8 2 5 4 3 9 8 1 0 4 7 8 7 4 0 0 0 5 7 1 6 2 8 1 3 2`  
`6 6 6 8 9 7 0 6 1 6 6 2 9 6 6 7 4 3 3 6 3 4 2 3 7 0 7`  
`5 1 0 0 7 8 6 5 9 3 8 6 7 6 4 9 5 0 7 4 6 1 8 2 6 4 4`  
`1 3 7 8 0 8 1 0 6 1 9 3 1 2 1 9 1 7 3 2 3 5 0 9 1 3 9`  
`5 3`

## Explanation

Rebeca will perform the operation $a\ c\ a\ b$ with the cost $C[3][1] = 1 $, and the remaining string will be $ab$. Then she will perform the operation $a\ b$ with the cost $C[1][2] = 2$, to reduce the entire string. The total cost equals $3$.