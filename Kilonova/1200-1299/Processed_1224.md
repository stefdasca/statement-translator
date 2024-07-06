For the final project at the end of 7th grade, Vivi prepared the game "four in a row". He created a game board with $26$ columns, which are labeled with the letters of the English alphabet: `A`, `B`, `C`, $\dots$, `Z`, and a number of $40$ rows. He assumed the existence of two players, one having only black tokens (denoted with `B` - "Black"), and the other having only red tokens (denoted with `R` - "Red"). The player with the red tokens starts. A move involves placing a token in a column of the board, with the token descending in the column until it reaches the first unoccupied position. The moves are given by a compact string of uppercase English letters. For example, the string `ABAC` means:

- The first player places the token (red) on column `A`; it descends to the base of column `A`
- The second player places the token (black) on column `B`; it descends to the base of column `B`
- Red goes next and places the token on column `A`; it descends above the previously placed token
- Black goes next and places the token on column `C`; it descends to the base of column `C`

The player who first manages to align at least four tokens of the same color in a row, column, or diagonal will win. At that moment, the game ends.

Example: consider that part of the board encoded from `A` to `G`, the red token (`R`) represented by and the black token (`B`) by the following three figures may represent configurations on the game board that can be reached through any sequence of moves.

~[plinie.png]

# Task

Write a program that, reading the sequence of moves, will determine who the winning player is, if they exist. It will display `R` if the winning player is the one with red tokens and `B` if the winning player is the one with black tokens.
The game may not have a winner for two reasons:
- The string of characters representing the moves does not lead to a winner: it will display `N` (Undecided);
- The string of characters is larger than allowed by the game board, and until the end, neither player won, in which case it will display `O` (Out).

# Input data

A match consists of four games. The first four lines of the input file `plinie.in` contain a sequence of moves formed by uppercase English letters, each line corresponding to a game. There are no separators between the letters.

# Output data

The output file `plinie.out` will contain four lines. On each of them, there is a character representing the result of the game described on the corresponding line from the input file. The characters can be:

* `R` - the player with red tokens wins;
* `B` - the player with black tokens wins;
* `N` - the string of characters does not lead to a winner, the game is undecided;
* `O` - the game board filled before the end of the string of moves, without any player achieving four in a row, column, or diagonal.

# Constraints and clarifications

* The game board has $40$ rows and $26$ columns.
* The string of characters based on which the moves are made has at most $1 \ 500$ characters.
* A game may end before all the given moves are performed.

# Example

`plinie.in`
```
DEDEAABCCBFGDE
DEDEAABCCBFGDEE
ABACADGE
ABC
```

`plinie.out`
```
N
R
B
N
```

## Explanation

See figure $1$
See figure $2$
See figure $3$