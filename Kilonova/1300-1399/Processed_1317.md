At the beginning of April, a new version of the well-known game $\\text{TETRIS}$ was launched. An avid player, Nicușor, is eager to play this game and therefore reads the rules carefully:

* The game takes place on a rectangular surface, divided into $m \times n$ identical squares with a side length of $1 \\text{cm}$, arranged in $m$ rows and $n$ columns.
* The player has $s$ pieces at their disposal, each piece being a square with a side length of $1 \\text{cm}$ on which a natural number not exceeding $9$ is inscribed, representing the value of the piece.
* Initially, all $s$ pieces are arranged in a sequence, outside the playing area.
* We call a tower a sequence of pieces placed in the same column, one on top of the other, with the last piece placed in the column being the top of the tower; the height of a tower represents the number of pieces that make up the tower.
* The game starts with the placement of the first piece from the sequence on the playing area in the square at the bottom-left corner.
* Next, attempts are made to place the other pieces, in the order in which they appear in the sequence, according to the following rules:
    * Search for, on the playing area, from left to right, the first tower of height strictly less than $m$ which has the most pieces on top with the same value as the piece to be added.
        * If such a tower exists, the piece will be placed on top of it.
        * If such a tower does not exist, search for, on the playing area, from left to right, the first tower containing the fewest pieces. The piece will be placed on top of this tower only if the number of pieces that make up the tower is strictly less than $m$.
* If, immediately after adding a piece, a tower containing $3$ pieces with the same value on top is obtained, then all $3$ pieces are removed from the playing area.
* The game ends when there are no more free spaces on the playing area or when the sequence of pieces is finished.

**Example**. If the surface has the configuration from $\\text{Fig}. 1$ and the piece with value $6$ needs to be added, then it will be placed on top of the 3rd tower, above the piece with number $9$, obtaining the configuration from $\\text{Fig}. 2$; if the value of the piece to be placed is $1$, then it will be placed above the first tower containing two values $1 \\ (\\text{Fig}. 3)$ on top, after which the $3$ pieces with the value $1$ are removed from the playing area $(\\text{Fig}. 4)$. 
~[tetris1.png|align=center]

# Task

Write a program that determines, for a given playing area and a given sequence of pieces, the number $p$ of pieces placed on the playing area, the number $t$ of pieces on the surface at the end of the game, and the number $h$ of pieces in the highest tower present on the playing area during the game.

# Input data

The input file `tetris.in` contains on the first line three natural numbers, $m$, $n$, and $s$ separated by a space. The next line contains the sequence of $s$ non-zero digits separated by a space, representing the values of the $s$ pieces, in the order in which they will be added to the playing area.

# Output data

The output file `tetris.out` contains on the first line the number $p$, the second line contains the number $t$, and the third line contains the number $h$.

# Constraints and clarifications

* $1 \\leq m \\leq 1 \\ 000$
* $1 \\leq n \\leq 9$
* $1 \\leq s \\leq 100 \\ 000$
* More pieces are not placed on the surface at the same time.
* $20\\%$ of the score is awarded for determining the value of $p$ and $40\\%$ of the score for determining each of the values of $h$ and $t$.

# Example

`tetris.in`
```
4 2 8
1 2 2 1 2 4 5 4
```

`tetris.out`
```
8
5
3
```

## Explanation

Adding the pieces modifies the playing area as follows:
~[tetris2.png|align=center]