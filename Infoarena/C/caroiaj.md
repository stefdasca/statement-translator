## Task

Serban and Teodora are playing a game on a square board with $N \times N$ cells. On each cell of the board, there is a colored token with a number written on it, so that, when viewed from above, the board looks like a grid. A move consists of choosing a token from one of the $2 \times N - 1$ main diagonals, provided that no other token from that diagonal has been chosen up to the moment of the move. The game begins. The two take alternate turns. Their grandfather, remembering that they will participate in the National Informatics Contest "Adolescent Grigore Moisil," motivates them to work as a team so that at the end of the $2 \times N - 1$ moves, different tokens have been chosen (considering the tokens chosen by Serban and Teodora). Two tokens are considered different if the numbers on them differ. For $T$ grids, indicate if the two can make moves such that at the end all chosen tokens are different. If there is a solution, a method of choosing should be displayed.

## Input data

The input file `caroiaj.in` will contain on the first line a natural number $T$, representing the number of grids. The next line contains a natural number $N$, representing the side of the grid. The following $N$ lines contain $N$ numbers, with line $i + 1$ representing the $i$-th line of the grid. This configuration is repeated $T$ times.

## Output data

The output file `caroiaj.out` will contain $T$ lines. The $i$-th line represents the answer for test $i$. If there is a solution, the message "DA" will be displayed, followed by $2 \times N - 1$ numbers, representing the numbers chosen from each diagonal. The first main diagonal is considered to be the bottom-left corner of the grid, and the last main diagonal is considered to be the top-right corner of the grid. If there is no solution for test $i$, then line $i$ will contain the message "Bunicul este dezamagit!".

## Constraints and clarifications

For all test evaluations,
$T = 44$.
$1 \leq N \leq 300$.
The numbers in the matrix are between $1$ and $10^9$. If there is a solution, the numbers corresponding to the chosen tokens will be displayed in ascending order of the main diagonals on which they are located. If there are multiple solutions, any of them can be displayed.

## Example

`caroiaj.in` 
```
1
3
1 2 3
4 5 6
7 8 9
```

`caroiaj.out` 
```
DA 7 4 1 2 3
```

## Explanation

We have the matrix 
```
1 2 3
4 5 6
7 8 9
```
From the main diagonal with order number 1, Teodora chooses the token with the number 7
From the main diagonal with order number 2, Serban chooses the token with the number 4
From the main diagonal with order number 3, Teodora chooses the token with the number 1
From the main diagonal with order number 4, Serban chooses the token with the number 2
From the main diagonal with order number 5, Teodora chooses the token with the number 3