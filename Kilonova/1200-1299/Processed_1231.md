_Collapse_ is a very popular game. The game board is represented by a rectangular area on the screen, the area being divided into cells, organized in $N$ lines and $M$ columns. Each cell can contain a red piece (identified by the letter $R$), green (identified by the letter $V$), or blue (identified by the letter $A$).

The group of a piece consists of all the pieces that have the same color as the respective piece and can be reached by moving only on pieces of the same color as the respective piece. A move can be made in $4$ directions (up, down, left, or right). A group must contain at least two pieces.

By acting through a click on a piece, the entire group of pieces corresponding to that piece will disappear.

After the group of the piece on which we acted through a click has disappeared, the pieces on the board "collapse". The collapse is carried out by executing, in order, the following two operations:

1. First, all remaining pieces "fall" (are moved down), to fill the gaps in the columns; the order of the pieces in the columns is preserved.
2. If a column is completely emptied, it will be eliminated, moving the other columns to the left, as much as possible; the order of the columns is preserved.

~[joc.png]

The game ends when groups of pieces can no longer be formed on the game board.

Vasile has been playing this game for many years. He never plays randomly, always using the same strategy. At each step, Vasile clicks on a piece from the largest existing group on the game board. Even if there are multiple choices to select the piece, he will click on the piece located on the farthest left column. And if there are multiple choices to select a piece on the farthest left column, Vasile will always choose the one located on the lowest line.

# Task

Write a program to simulate the game and determine the number of clicks Vasile executes until the game ends.

# Input data

The input file `joc.in` contains on the first line two natural numbers separated by a space $N$, $M$, which represent the number of lines and respectively the number of columns on the game board. It follows by $N$ lines, each line containing $M$ characters from the set $\\{R, V, A\\}$.

# Output data

The output file `joc.out` will contain a single line on which it will be written the number of clicks that Vasile executes until the game ends.

# Constraints and clarifications

* $1 \leq N, M \leq 50$;

# Example 1

`joc.in`
```
3 4
AVVR
AAVV
AVRR
```

`joc.out`
```
3
```

# Example 2

`joc.in`
```
8 7
RRARVRV
RRRRVAV
VRRRVAR
VVRRAVV
VVRRAAA
AAARVVA
AAARVVR
ARRRVRR
```

`joc.out`
```
7
```
