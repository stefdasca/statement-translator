# The Flip Game

Gigel discovered a new game called "Flip". It is played on a rectangular board of size $N \times M$ which contains integers. Each row and each column has a switch that changes the state of all elements in that row or column by multiplying them by $-1$. The goal of the game is that for a given configuration of the game board, to act on the rows and columns so as to obtain a board with the largest possible sum of elements.

## Task

Given a configuration for the "Flip" board, create a program that determines the maximum sum Gigel can obtain.

## Input data

The first line of the file `flip.in` contains two integers $N$ and $M$, separated by a space, representing the dimensions of the board. The next $N$ lines contain $M$ integers separated by spaces, describing the configuration of the game board.

## Output data

The first line of the file `flip.out` contains a number representing the maximum sum Gigel can obtain by switching the rows and columns of the game board.

## Constraints

$1 \leq N, M \leq 16$

The game board contains integers in the range $[-1\ 000\ 000, 1\ 000\ 000]$

## Example

`flip.in`
```
5 3
4 -2 2
3 -1 5
2 0 -3
4 1 -3
5 -3 2
```

`flip.out`
```
28
```

## Explanation

The second column and the third row are toggled.