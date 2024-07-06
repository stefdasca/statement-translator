```markdown
Ștefan is playing a game using a chessboard of size $N$ by $M$ squares. The board consists of free spaces (`.`), but also spaces occupied by enemy pieces: Queens (`R`, $9$ points), Rooks (`T`, $5$ points), Knights (`C`, $3$ points), and Bishops (`N`, $3$ points). He wants to find out the highest score a pawn can achieve when placed on the first row of this chessboard if the score of a pawn is the sum of the points of the captured pieces.

A pawn can move in 2 ways on a chessboard:
1. By one square forward, only if the square in front of it is free;
2. By one square diagonally forward-left or forward-right, only if the square it is moving to contains an enemy piece. That piece will be captured and its points will be added to the pawn’s score.

# Task

Given the size and configuration of the chessboard, find the maximum score a pawn placed on the first row of this chessboard can achieve. It is guaranteed that no enemy piece blocks starting positions.

# Input data

The input file `scor-pion.in` contains in the first line two integers, $N$ and $M$, the dimensions of the chessboard.
Each of the next $N$ lines contains a string of $M$ characters representing a row of the chessboard. It is guaranteed that the first row (the lowest one) is completely free.

# Output data

The output file `scor-pion.out` will contain a single integer, the highest score a pawn can achieve when placed on the chessboard.

# Constraints and clarifications

* $5 \leq N, M \leq 500$;
* The board consists only of the characters `.`, `R`, `T`, `C`, `N`;
* It is guaranteed that the first row of the board (the lowest one) is completely free;

|#|Points|Constraints|
|-|-|--------|
|1|10|There is only one enemy piece on the board|
|2|11|All enemy pieces are placed on the same row|
|3|12|Each row is either completely free or filled with only one type of piece|
|4|13|All enemy pieces are placed on the same diagonal, starting either from the top-left corner or from the top-right corner, with no free spaces between them|
|5|14|All enemy pieces are placed in an X-shaped pattern, meaning two diagonals intersecting (the four lines starting from the center of the X can be of different lengths, but there will be no free spaces between the pieces on them)|
|6|40|No additional constraints|

# Example 1

`scor-pion.in`
```
5 5
.....
..R..
....C
.T..N
.....
```

`scor-pion.out`
```
14
```

## Explanation

This score can be achieved by placing the pawn in the 3rd column, that is, on the square with coordinates $\{5, 3\}$.
After capturing the rook at position $\{4, 2\}$, its score goes to $5$ points, then it can move forward and capture the queen at position $\{2, 3\}$, reaching a total score of $5 + 9 = 14$ points.
The path taken by the pawn is: $\{5, 3\}$ -> $\{4, 2\}$ -> $\{3, 2\}$ -> $\{2, 3\}$.
```

Double-checking the grammar and syntax, everything looks accurate according to the provided guidelines.
```