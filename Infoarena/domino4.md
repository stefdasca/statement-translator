## Task 

A chessboard with $m$ rows and $n$ columns is given, with $m \cdot n$ being an even number and $\frac{m \cdot n}{2}$ domino pieces each covering two adjacent squares on the chessboard. Each domino piece has two identical numbers (one in each square) from the set $\{1, 2, \dots, \frac{m \cdot n}{2}\}$ . No two domino pieces have the same numbers. The goal is to find a way to place all domino pieces on the chessboard such that: 
- no two pieces on the board overlap;
- any line parallel to the edges of the chessboard intersects the interior of at least one of the domino pieces.

Write a program that determines a way to place the domino pieces according to the given conditions. 

## Input data

The input file `domino4.in` contains the natural numbers $m$ and $n$, separated by a space, on the first line. 

## Output data

The output file `domino4.out` will contain $m$ rows, each row will contain $n$ numbers separated by a space, representing in the order of the rows, and in the same row in the order of the columns, the numbers written on the dominoes on the chessboard, if a solution exists. If no solution exists, the file `domino4.out` will contain the number $0$ on the first line. 

## Constraints and clarifications

$2 \leq m, n \leq 500$ 
$m \cdot n$ is an even number 

## Example

`domino4.in`
`
5 6
`

`domino4.out`
`
1 2 2 4 4 5
1 3 3 6 7 5
8 8 9 6 7 13
10 11 9 12 12 13
10 11 14 14 15 15
`
