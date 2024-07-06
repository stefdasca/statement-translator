~[xy1.png|align=right]
One of the passions of the two brothers Rareș and Bogdan is inventing games. Their latest game is called *xy* and is played by two players who alternatively fill squares on a rectangular surface divided into $n \times m$ identical squares, as shown in the images beside. It is considered that the square in the top-left corner of the surface is positioned at row $1$ and column $1$, and the square in the bottom-right corner is positioned at row $n$ and column $m$.
A move is considered the stage in which one of the players fills at least one square on the rectangular surface. The moves are executed alternately, as follows:

* The first player chooses a square, fills it with the character `x`, and tries to draw the largest possible `X` centered on the chosen square, as in $Figure \\ 3$, where the chosen square is positioned at row $3$ and column $3$.
* The second player also chooses a square, fills it with the character `y`, and tries to draw the largest possible `Y` centered on the chosen square, as in $Figure \\ 4$, where the chosen square is positioned at row $3$ and column $3$.

The game board in the adjacent figures contains $6 \times 5$ squares positioned on $6$ rows and $5$ columns. The smallest `X`, respectively the largest, that can be drawn on this game board is the one from $Figure \\ 1$, respectively the one from $Figure \\ 3$, by filling the unfilled squares with the character `x`, which can be drawn anywhere suitable on the game board.
The smallest `Y`, respectively the largest, that can be drawn on this game board by filling the unfilled squares with the character `y`, is the one from $Figure \\ 2$, respectively the one from $Figure \\ 4$, which can be drawn anywhere suitable on the game board.
The game ends if one of the following situations arises:

* One of the players chooses as the center a square filled by any player on a previous move
* The player who needs to make the move fills just the chosen square as the center on the game board and cannot draw the X or Y
* All proposed moves have been carried out

Since the two children are brothers, they do not care who wins.

# Task

Write a program that reads three natural numbers $n$, $m$, $k$ and a sequence of $k$ moves that the two brothers wish to execute, alternately, in the given order, and then determine:

* the maximum number $a$ of squares filled during a move
* the number $b$ of squares left free after the end of the game
* the maximum number $c$ of squares filled which form a rectangular surface on the game board at the end of the game

# Input data

The input file `xy.in` contains on the first line three natural numbers $n$, $m$, and $k$, separated by a space, with the meaning from the statement. The next $k$ lines each contain two natural numbers $i$ and $j$, separated by a space, representing the row $i$ and column $j$ where the chosen square is positioned as the center for executing the proposed move.

# Output data

The output file `xy.out` will contain on the first line the three numbers determined by the program: $a$, $b$ and $c$, separated by a space, in this order, with the meaning from the statement.

# Constraints and clarifications

* $0 < n, m, i, j < 101$
* $0 < i \leq n$
* $0 < j \leq m$
* $0 < k < 10\ 000$
* $n, m, i, j, k$ are natural numbers
* Initially, all squares on the game board are unfilled
* Filling a square is done by writing the character `x` or `y` in it, the first player filling only with the character `x`, and the second player only with the character `y`
* Each player fills on the board first the chosen square as the center and then tries to draw their symbol
* During a move, when drawing an `X` or `Y`, players can use squares filled during a previous move without counting them in this move
* A rectangular surface formed by filled squares on the game board can consist of:
1. at least one filled square
2. multiple filled squares situated on the same row in consecutive columns
3. multiple filled squares situated on the same column in consecutive rows
4. multiple filled squares situated in consecutive rows and columns
* Correctly solving the first requirement grants $40\%$ of the score, for correctly solving the second requirement $30\%$ of the score, and for correctly solving the third requirement $30\%$ of the score.

# Example

`xy.in`
```
6 5 5
3 2
4 4
3 4
2 4
5 4
```

`xy.out`
```
5 17 9
```

## Explanation

In the first move, the first player draws an `X`, centered on row $3$ and column $2$, by filling $5$ squares with the character `x`.
In the second move, the second player draws a `Y` centered on row $4$ and column $4$, by filling $4$ squares with the character `y`.
In the third move, the first player draws an `X`, centered on row $3$ and column $4$, by filling only $3$ squares with the character `x$ because $2$ squares were used from the first move.
In the fourth move, the second player succeeds in filling with the character `y` only the chosen square as the center, situated on row $2$ and column $4$, and the game ends because the `Y` cannot be completed.
~[xy2.png|align=center]
The proposed fifth move is not carried out because the game has ended.