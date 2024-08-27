# Go2

Claudia, bored of playing Go, starts asking herself various questions about the game. With artistic inclinations and a vivid imagination, she wonders about the number of rectangular boards of size $N \times M$ in the game of GO such that each position on the board has among its neighbors (up, down, left, right) an even number of pieces (no distinction is made between the pieces of the first player and the pieces of the second player). Later, she wondered how many such boards exist such that certain positions on the boards are occupied and certain positions are free. The problem proved too difficult for Claudia, so she asks you to solve it. Since this number can be very large, she asks you to display the remainder of its division by $1\,000\,000\,007$.

## Input data

The input file `go2.in` will contain the following:

- The first line will contain 2 natural numbers $N$ and $M$ representing the number of rows and columns of the board, respectively.
- The next $N$ lines will contain $M$ characters each. If character $j$ on line $i$ is $0$, then the board must not have any pieces on this position at the end, if it is $1$, then the board must have exactly one piece on this position at the end, and if it is $?$ then the board may or may not have a piece on this position at the end.

## Output data

The output file `go2.out` must contain exactly one number representing the number of boards with $N$ rows and $M$ columns that meet the conditions in the problem statement and in the input file.

## Constraints and clarifications

$$1 \leq N, M \leq 100$$

At a position $(i, j)$ there can be at most one piece.

Neighbors of a position $(i, j)$ are $(i - 1, j)$, $(i, j - 1)$, $(i + 1, j)$, and $(i, j + 1)$.

## Example

`go2.in`
```
3 3 
??? 
101 
??? 
```

`go2.out`
```
2 
```

`go2.in`
```
2 2 
11 
0? 
```

`go2.out`
```
0 
```

## Explanation

For the first case, the solutions are:
```
010 101 010 
and 
111 101 111
```