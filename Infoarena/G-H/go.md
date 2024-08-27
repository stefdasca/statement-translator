Claudia plays GO against the computer. Her strategy is simple but effective: at each move, she will choose to place a piece in such a way as to capture as many of the opponent's pieces as possible. If there are multiple options, she will choose to place the piece as high as possible, and if there are still multiple options, she will place the piece as far to the left as possible. The GO game is played on a rectangular board with $N \times M$ cells arranged on $N$ rows and $M$ columns. The rules are: Players move alternately, placing one piece on an unoccupied cell of the board. All pieces of the same color that are adjacent horizontally or vertically form a group. Two pieces are adjacent if the two cells in which they are placed share a common side. If a player's move leads to the elimination of the liberties of a group of the opponent's pieces, those pieces are captured and removed from the board. The liberties of a group are all empty cells that are adjacent to at least one piece in the group. Given a configuration of the GO board, help Claudia choose the correct move to capture as many of the opponent's pieces as possible, under the conditions stated above.

## Task

## Input data

The first line of the file `go.in` contains two natural numbers $N$ and $M$ which represent the number of rows and columns of the game board, respectively. The next $N$ lines contain the current configuration of the game board ($0$ represents an unoccupied cell, $1$ - a piece of Claudia, $2$ - an opponent's piece).

## Output data

The file `go.out` must contain on the first line two numbers separated by a single space. These represent the row index and the column index, where the piece should be placed according to Claudia's strategy (rows and columns are numbered starting from $0$).

## Constraints

The input file contains a valid configuration (each group of pieces has at least one liberty, otherwise it would have already been captured). 

Also, there is at least one position on the game board where Claudia can place a piece.

$1 \leq N$

$1 \leq M \leq 1000$

## Example

`go.in` `go.out` 5 7 0 1 2 2 2 0 2 0 1 2 2 1 2 1 0 0 1 1 2 2 0 0 1 2 2 0 1 2 0 0 1 1 2 0 0 0 5 3 4 1 0 1 0 0 2 0 2 1 1 2 2 0 1

## Explanation

In the first example, by placing the piece at position $(0,5)$, Claudia will capture $6$ pieces (the group to the left of this piece formed by five values equal to $2$ and adjacent, plus the group formed by the piece at position $(0,6)$). Anywhere else she makes the move, Claudia will not be able to capture as many pieces.

In the second example, Claudia cannot capture more than $0$ pieces, wherever she places the new piece. Therefore, she will choose to place the piece on the highest row and as far to the left on that row as possible.