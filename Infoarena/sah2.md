## Chess2

Ana and Ion share a common passion for chess and play whenever they have free time. Being non-conformist individuals, they have ordered chessboards of different sizes and sets of special pieces. If they don't have time to finish a game, they leave the pieces as they are on the chessboard and continue the next day. This time, a problem arose - their son Ionel accidentally overturned the chessboard - and now they are trying to reconstruct the last configuration. Ion precisely remembers how the chessboard looked at the start of yesterday's game and the moves he made. Ana remembers that she played strangely - she moved the same piece, a rook, throughout the game. She doesn't recall the exact positions where she moved, but she remembers the directions in which the rook moved.

## Task

Write a program that determines the positions where Ana's moved rook could be at the end.

## Input data

The input file $sah.in$ contains on the first line two natural numbers separated by a space $X N$, representing the size of the chessboard and the number of pieces on the chessboard, respectively. The next $N$ lines contain information about the positions of the pieces on the board. Specifically, on line $i+1$ is the position of piece $i$ in the form of two natural numbers separated by a space $L C$, representing the row and column where the piece is located. The last position corresponds to the rook that Ana moves. On the next line, there is a natural number $Nr$, representing the number of moves made by Ion and Ana respectively. On each of the next $Nr$ lines, there is information about the moves made by Ion. Specifically, on line $N+2+j$ are written $3$ natural numbers separated by a space $i L_1 C_1$ signifying piece $i$ is moved to row $L_1$, column $C_1$. On the last line of the file, there is a sequence of $Nr$ characters from the set $\{'N', 'S', 'E', 'V'\}$ which represent the directions in which Ana moved the rook (the $i$-th character in this sequence corresponds to the $i$-th move).

## Output data

The output file $sah.out$ will contain on the first line a natural number $p$, representing the number of possible final positions. On the next $p$ lines, the possible final positions are written, one position per line. A position is described by two natural numbers separated by a space $L C$, meaning "row $L$ and column $C$ is a possible final position." The final positions will be written in the order of rows; if there are multiple final positions in the same row, they will be written in the order of columns.

## Constraints and clarifications

1 $\lt$ $X \leq 50$

1 $\lt$ $N \leq 1000$

0 $\lt$ $Nr \leq 1000$

The pieces are numbered from $1$ to $N$.

The rows of the chessboard are numbered from top to bottom from $1$ to $X$, and the columns are numbered from left to right from $1$ to $X$.

Ana and Ion move alternately, Ion was the first to move.

A rook can only be moved in 4 directions: north (coded $N$) - to a row with a smaller index, the same column; south (coded $S$) - to a row with a larger index, the same column; east (coded $E$) - to a column with a larger index and the same row; west (coded $V$) - to a column with a smaller index and the same row.

In one move, a piece must move from its current position.

## Example

$sah2.in$
```
5 8
2 2
3 2
4 3
5 4
5 3
5 2
4 4
4 3
4 2
4 5
3
1 1 2
2 5 1
SVNV
```

$sah2.out$
```
4
2 1
2 2
3 1
3 2
```