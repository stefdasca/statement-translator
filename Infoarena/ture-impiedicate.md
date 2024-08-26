## Task

Miruna is learning chess. She has learned about rooks and understands that they can move only horizontally or vertically. She also knows that if another piece is in the path of a rook, it can be attacked. Miruna found the theory of rook movement too simple and imagined the following problem: On an $N * N$ chessboard, she randomly places $K$ rooks. She wants to move the rooks in such a way that, after the moves, no rook can attack another rook. After several attempts, the girl proposed to determine the minimum number of moves necessary to obtain the final arrangement of the rooks. Since Miruna's rooks are older and somewhat clumsy, they can only move one square (left, right, up, or down) in each move. A rook cannot jump over another rook and cannot leave the chessboard.

## Input data

In the input file `ture-impiedicate.in`, the first line will contain the values $N$ and $K$ as described in the problem statement. The next $K$ lines will contain 2 values $l_i$ and $c_i$, separated by a space, which represent the row and column where the rook is initially located.

## Output data

In the output file `ture-impiedicate.out`, the first line will contain the minimum number of (valid) moves required to obtain a configuration where no rook can attack another rook.

## Constraints and clarifications

$K \leq N$

$1 \leq c_i , l_i \leq N$

for any $i$ from $\{1, 2, \dots, K\}$

Subtasks

| Index | Points |
|-------|--------|
| 1 | 15 points, $N \leq 9$ |
| 2 | 15 points, $N \leq 100$ |
| 3 | 20 points, $N \leq 2\ 000$ |
| 4 | 50 points, $N \leq 100\ 000$, $K \leq 2\ 000$ |

## Example

`ture-impiedicate.in`
```
10 5
2 9
2 8
3 10
10 2
2 9
```

`ture-impiedicate.out`
```
5
```