~[zar1.png|align=right]
Maria received a game as a gift. The game has a board in the form of a rectangular grid made up of $1$-by-$1$ squares arranged in $L$ rows and $C$ columns. The squares contain the first $L \times C$ natural numbers starting from $1$, representing codes. The encoding is done as follows: it starts with the value $1$ in the square at the bottom-left, continues with the values $2, 3, ..., C$ from left to right, continues on the next row from right to left, and so on. In this way, the last square will always be encoded with the value $L \times C$, as shown in the example on the right.

The game involves placing a token in the bottom-left corner and the token has to be moved beyond the square encoded with the value $L \times C$ by making moves. To make a move, the player first rolls a die. If the die shows the value $Z$ and the token is in the square with code $P$, the token will be moved to the square with code $P + Z$. If $P + Z > L \times C$, the game ends. Otherwise, there may be situations where the token will not necessarily stay in the new position, as some positions on the grid have indicators specifying where the token that has just arrived at that position should be moved.

~[zar2.png|align=right]
A square can contain at most one indicator. There are $9$ types of indicators: for the first $8$ types, it is specified how many positions the token will be placed from the current position, respectively: on the same row to the right $(1)$, diagonally towards the upper-right $(2)$, on the same column upwards $(3)$, diagonally towards the upper-left $(4)$, on the same row to the left $(5)$, diagonally towards the bottom-left $(6)$, on the same column downwards $(7)$, diagonally towards the bottom-right $(8)$. Indicator type $9$ specifies the code of a square where the token will be placed.

When applying an indicator, the following rules are respected:
a) if the token goes off the board, this indicator will be ignored, and the token will remain in place (the game cannot end this way).
b) if it lands on a square containing another indicator, that indicator will not be considered.

# Task

Given, in order, the $K$ values obtained from the dice rolls, determine if the game can end. If affirmative, display the number of dice rolls after which the game ends. If not, display the position of the token after the $K$ moves.

# Input data

The input file `zar.in` contains on the first line two numbers $L$ and $C$ representing the number of rows and the number of columns of the game board. The second line contains a natural number $I$ representing the number of squares with indicators. On the following $I$ lines, there are $3$ natural numbers separated by a space, describing each indicator. The first number is the code of the square where the indicator is placed, the second number is the type of indicator. If the type of indicator is $9$, the third number signifies the code of the square where the token will be sent. If the second number is from the set $\\{1, 2, 3, 4, 5, 6, 7, 8\\}$, the third number represents the number of positions on the board over which the token will be moved in the specified direction. On the next line, there is a natural number $K$ representing the number of dice rolls. The following line contains $K$ natural numbers separated by a space, representing, in order, the values obtained after each roll.

# Output data

The output file `zar.out` will contain on the first line two natural numbers separated by a space. If the game ends, the first value will be $1$, and the second will represent the number of moves after which it ended. If the game does not end, the first value will be $2$, and the second the code of the square where the token remained.

# Constraints and clarifications

* $1 \leq L, C \leq 50$
* $0 \leq I \leq L \times C$
* $1 \leq K \leq 1 \ 000$
* The values obtained in the dice rolls are numbers from the set $\\{1, 2, 3, 4, 5, 6\\}$
* The number of positions the token can move for an indicator type from $1$ to $8$ is a non-zero integer $\leq 50$

# Example

`zar.in`
```
3 4
4
3 2 1
8 1 1
7 1 2
9 9 11
4
2 1 2 2
```

`zar.out`
```
2 11
```

## Explanation

Initially, the token is in square $1$. After the first move, it reaches square $5$ (the die shows $2$ and the token would reach square $3$ but the indicator there sends it to square $5$). After the second move, the token reaches square $6$ (the die sends it there and no indicator is encountered). After the third move, the token reaches square $7$ (the die sends it to $8$, and the indicator there sends it to $7$ – now the indicator in $7$ is not considered). After the $4$th move, the token reaches square $11$ (after the die roll, it should go to $9$ and the indicator there sends it to $11$).