Regardless of the data encoding required to store the coordinates, $N$ domino pieces of different heights are placed at coordinates marked along a straight line drawn on a flat surface. By acting on one piece, it can topple to the left or right, creating a series of other pieces falling one over the other. A piece is toppled by another piece if it is touched in its fall, even if only at its base, making it possible for a smaller piece to topple a larger one if it is touched by the falling piece.

# Task:

Determine the maximum length of a series of toppled pieces obtained by acting on one piece in a certain direction. This is the longest horizontal length fully covered by toppled pieces.

# Input data

The input file `domino.in` contains on the first line $N$, the number of pieces, and on each of the next $N$ lines, the coordinate of the piece and its height, separated by a space.

# Output data

The output file `domino.out` contains on the first line a natural number representing the maximum length of the series of toppled pieces.

# Constraints and clarifications

* The surface is sufficiently large so that the pieces do not fall outside it.
* The number of pieces $N$ is a natural number in the interval [$1$ – $100$]
* The height of a piece is a natural number in the interval [$1$ – $1000$]

# Example 1

`domino.in`
```
5
40 1
8 2
30 4
1 6
4 11
```

`domino.out`
```
14
```

## Explanation

The length of the longest series of toppled pieces is equal to $14$ and is obtained by acting towards the right on the piece placed at coordinate $1$, which will topple the piece at coordinate $4$ and this one, in turn, the one at coordinate $8$.

# Example 2

`domino.in`
```
6
53 3
62 4
15 5
20 6
60 8
75 9
```

`domino.out`
```
12
```

## Explanation

The length of the longest series of toppled pieces is equal to $12$ and is obtained by acting towards the left on the piece placed at coordinate $62$, which will topple the piece at coordinate $60$ and this one, in turn, the one at coordinate $53$.