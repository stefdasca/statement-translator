# Petrick

This problem is named Petrick – and this should not be confused with the name of the author. Petrick refers to "trick," a synonym for the Romanian phrases "pe șmecherie" or "pe barosaneală." The real trick is to see if you, an amazing chess player, can win against your opponent in a single move (remember, you are talented!). Formally, you are given a chessboard without pawns, with $N$ pieces on it, and you need to see if the white can checkmate the black king with one piece move. Note that the state of the chessboard can be generated in a hypothetical chess game, according to the well-known rules of chess.

Here follows a short description of the game of chess. Chess is a game played on a square board of $8 \times 8$, with different pieces. The pieces are kings, queens, bishops, knights, or rooks. Each piece can be black or white, and each piece can be in only one cell. There cannot be more than one piece in a cell. Each piece can move to other cells depending on its type; specifically:

- The king can move to any adjacent cell (vertical, horizontal, or diagonal).
- The rook can move orthogonally up, down, left, or right for any distance, as long as it doesn't "jump over" other pieces.
- The bishop can move diagonally for any distance, as long as it doesn't "jump over" other pieces.
- The queen can make any move that a bishop or a rook can do.
- The knight can move orthogonally up, down, left, or right for two cells, followed immediately by an additional move of one cell perpendicular to the last move (in the shape of a capital $L$); the knight can "jump over" other pieces.

There is exactly one king of each color. There are at most two rooks, bishops, and knights of each color. If there are two bishops of the same color, then it is guaranteed that the sum of the parities of the positions of the cells on which they are located is different. A piece cannot move to a cell that contains a piece of the same color. If a piece moves into a cell where there is a piece of the opposite color, then the piece that was initially in the cell is taken out of the game. We say that a color is in check if and only if a piece of the opposite color could move into the cell containing the king of that color. A piece is not allowed to make an invalid move. We say that a color is in checkmate if and only if it is in check and cannot make any valid moves.

Now, you need to find out if white can make a valid move that puts black in checkmate.

## Input data

The input file `petrick.in` will contain $N$, the number of pieces. The following $N$ lines will each contain a string from the set $\{ \text{king} , \text{rook} , \text{queen} , \text{bishop} , \text{knight} \}$, a string from the set $\{ \text{black} , \text{white} \}$, and two integers from the set $\{ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 \}$, which indicate the position of the piece on the board. The first string indicates the type of piece, while the second indicates which player owns the piece. 

## Output data

The output file `petrick.out` must contain a string that describes whether you will win in the next move or not. This string will be `Checkmate!` if you will win in the next move or `Bad Luck!` otherwise.

## Constraints and clarifications

$1 \leq N \leq 16$ 

The time limit for this problem has been reduced from 1 second to 0.01 seconds to protect the evaluator.

## Example

`petrick.in`

```
4 
king white 1 1 
rook white 7 6 
queen white 4 5 
king black 8 8 
```

`petrick.out`

```
Checkmate!
```

## Explanation

There is at least one move that allows white to checkmate the black king.