## Task

Given a chessboard of size $N \times N$. On this board, some squares are free, while others are blocked. Determine the maximum number of queens that can be placed on the chessboard such that no two queens attack each other. A queen can only be placed on a free square. Two queens attack each other if they are on the same row, column, or diagonal, and all the squares between the two queens (on the respective row, column, or diagonal) are free. Let $Q$ be the maximum number of queens that can be placed on the board. In addition, you need to determine the number of ways to place the $Q$ queens on the board.

## Input data

The first line of the input file `regine2.in` contains the integer $T$, representing the number of tests. The following lines contain the descriptions of the $T$ tests. The first line within each test contains the integer $N$, representing the size of the chessboard. The next $N$ lines contain $N$ characters each, representing the description of each row of the chessboard. The character '.' represents a free square, and the character '#' represents a blocked square.

## Output data

For each test, print to the output file `regine2.out` one line containing 2 integers: $Q$ and $P$. $Q$ represents the maximum number of queens that can be placed on the respective chessboard, and $P$ represents the number of ways to place $Q$ queens on the chessboard.

## Constraints

$1 \leq T \leq 30$ 

$1 \leq N \leq 8$ 

## Example

`regine2.in`
```
3
1
.
1
#
4
.#..
##..
.#.#
.#.#
```

`regine2.out`
```
1 1
0 1
4 6
```