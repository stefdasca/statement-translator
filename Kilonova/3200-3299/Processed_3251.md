Sure, here is the translated text:

---

"Chess speaks for itself"

A year ago, Ernest challenged the grandmaster Carlos Magnussen to a game of chess. To counter Carlos's experience, Ernest chose to significantly change the rules from the classic game of chess and train exclusively with these new rules.

The rules of the game are as follows:
- The game is played on an $8 \times 8$ board. The rows are numbered from bottom to top, from $1$ to $8$. Specifically, the $1$st row of the matrix corresponds to the $8$th row of the game board, and vice versa.
- A game will be played only with pawns of both colors; there will be no other pieces on the board. **There can be more than $8$ pawns of a particular color**.
- The pawns move as in normal chess, and the moves alternate between the two players. White pawns advance from bottom to top, and black pawns from top to bottom (see the example for details).
- Just like in chess, white pawns starting from the second row (of the board) can advance two squares at the first move if there is no other pawn in their path. The same applies to black pawns on the seventh row.

Ernest has extensively studied [Anarchy Chess](https://www.reddit.com/r/AnarchyChess/) and knows that en passant is always **forced**. Knowing he is to move, he wonders how many different moves he can make such that Carlos Magnussen will be forced to play en passant.

~[gif_ep.gif|align=center|width=25%]

# Task
Given a configuration of the chessboard and the color Ernest is playing with, knowing he is to move, help him find the number of moves he can make so that on the next move Carlos Magnussen is forced to play en passant.

# Input data
The first line will contain a character `W` or `B`, indicating that Ernest is playing with the white or black pieces, respectively.

The next $8$ lines will contain $8$ characters each, representing the board configuration. The $j$-th character of the $i$-th line will be `.` if there is no pawn on this position, `W` if there is a white pawn, or `B` if there is a black pawn.

# Output data

The first line will contain a single integer, the number of ways Ernest can move a pawn, forcing his opponent to play en passant.

# Constraints and clarifications
* It is guaranteed that there will be no pawns on the first or last row.
* It is possible that Ernest has no available move that forces an en passant in the given configuration.

# Example 1

`stdin`
```
W
........
...B.B..
........
....W...
.B.B....
........
..W.....
........
```

`stdout`
```
1
```

# Example 2

`stdin`
```
B
........
...B.B..
........
....W...
.B.B....
........
..W.....
........
```

`stdout`
```
2
```

## Explanation
In both examples, the initial chessboard looks as follows:
~[ep2.png|width=25%]

If Ernest plays with the white pieces, he can make only one move:
~[ep3.png|width=25%]

If he plays with the black pieces, he has two move options:
~[ep4.png|width=25%]
~[ep1.png|width=25%]
