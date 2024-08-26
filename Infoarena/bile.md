# Balls

## Task

On a square board divided into $N \times N$ squares ($N$ rows and $N$ columns), there are $N \times N$ balls (one in each square of the board). Gigel likes balls a lot, so he takes, in turn, one ball from the board until there are no balls left on the board. Gigel is also a very curious boy. He noticed that balls can be divided into connected components as follows: each ball is part of exactly one connected component if 2 balls are neighbors horizontally or vertically, then they are part of the same connected component (i.e., if one is immediately above, below, to the right or to the left of the other). The size of a connected component is equal to the number of balls that are part of that connected component. After each ball is taken, Gigel wants to know the maximum value among the sizes of the connected components of the remaining balls.

## Input Data

The first line of the file `bile.in` contains the integer $N$, representing the number of rows and columns of the board. The following $N^2$ lines contain 2 integers $L$ and $C$, separated by a space, representing the row and column where the ball that Gigel takes is located. The coordinates of the balls are given in the order in which the balls are taken from the board.

## Output Data

The file `bile.out` will contain $N^2$ lines. Each line will contain the maximum size required after each ball is taken from the board.

## Constraints and clarifications

$1 \leq N \leq 250$

## Example

`bile.in`
```
3
2 1
2 2
3 3
1 3
1 2
2 3
3 1
1 1
```

`bile.out`
```
8
7
4
2
2
2
1
1
0
```