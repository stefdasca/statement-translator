## Task

Zaharel and Nargy have recently bought a tobacco plantation of size $N \times N$ meters. After a complex analysis, they calculated the productivity for each $1 \times 1$ meter piece, that is, the amount of tobacco they get in a day by planting tobacco on that piece. To increase productivity, they want to analyze only certain square pieces from the entire plantation. For this, they have asked $M$ questions in the form: "Which is the $1 \times 1$ piece with the maximum productivity in a square with the top-left corner at row $i$ and column $j$ and side length $k$?". Write a program to help them answer these questions.

## Input data

The first line of the file `plantatie.in` will contain the natural numbers $N$ and $M$ separated by a space. The next $N$ lines contain $N$ natural numbers each, separated by spaces, representing the productivity of the $1 \times 1$ pieces in the plantation. The following $M$ lines contain triplets of numbers $i$ $j$ $k$, representing the questions they have.

## Output data

The output file `plantatie.out` contains $M$ lines, representing the answers to the questions, in the order of the input file.

## Constraints

$1 \leq N \leq 500$

$1 \leq M \leq 75000$

The productivity of a piece from the plantation is a natural number in the interval $[0, 1000000000]$

The rows and columns of the plantation are numbered from $1$ to $N$

All questions will represent squares fully inside the plantation

## Example

`plantatie.in`
```
8 3
7 8 0 0 0 0 5 5
0 0 0 0 0 0 5 5
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 1 2 3 4
0 0 0 0 5 6 7 8
0 0 0 0 9 10 11 12
1 1 1 1
14 15 16 17
1 1 8
4 5 3
2 2 6
```

`plantatie.out`
```
17
7
11
```