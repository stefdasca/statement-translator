# Argintolac and Bronzolac compete in a game on a board with $N$ rows and $M$ columns that contain obstacles.

The game unfolds as follows:
* Dealer Nitsoc chooses a *nonempty* string $S$ that only contains the letters `U`, `D`, `L`, `R`.
* Argintolac chooses a free cell (one that does not contain an obstacle) on the board and places a robot in it.
* Bronzolac rearranges (or does not) the characters of the string $S$.
* The robot follows the path described by the string given by Bronzolac, moving at step $i$ to the adjacent cell in the direction represented by the character $S_i$ (`U` - up, `D` - down, `L` - left, `R` - right).
* Argintolac wins if the robot reaches the final cell unscathed (it does not leave the board and does not hit any obstacle along the way), otherwise, Bronzolac wins.

Before the game starts, dealer Nitsoc receives a favor from Argintolac and wonders how many strings $S$ he can initially choose such that Argintolac wins. *Being very competitive, both Argintolac and Bronzolac play optimally*. Since Nitsoc has spent the last 5 years at Master...Club, he is not able to solve the problem alone, so he asks for your help. The answer should be displayed modulo $10^9 + 7$.

# Task

# Input data
The first row contains 2 positive integers $N$ and $M$, representing the number of rows and the number of columns of the board.
The next $N$ rows describe the configuration of the board, row $i$ containing $M$ characters of type `.` (representing a free cell) or `#` (representing a cell that contains an obstacle).

# Output data
Print on the first row an integer representing the number of nonempty strings $S$ that can be initially chosen such that Argintolac wins, modulo $10^9 + 7$.

# Constraints and clarifications
* $1 \leq N, M \leq 2000$
* The board contains at least one free cell.

## Subtask 1 (29 points)
* $N = 1$

## Subtask 2 (8 points)
* $1 \leq N, M \leq 3$

## Subtask 3 (13 points)
* $1 \leq N, M \leq 10$

## Subtask 4 (9 points)
* $1 \leq N, M \leq 50$

## Subtask 5 (11 points)
* $1 \leq N, M \leq 150$

## Subtask 6 (16 points)
* $1 \leq N, M \leq 1\ 000$

## Subtask 7 (14 points)
* No additional constraints

# Examples

`stdin`
```text
2 4
##..
.##.
```

`stdout`
```
4
```

`stdin`
```
2 2
..
..
```

`stdout`
```
12
```

`stdin`
```text
4 4
....
.#..
....
#...
```

`stdout`
```
148
