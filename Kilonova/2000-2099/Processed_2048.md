```markdown
# Task

Did you think you would get away without a chess problem? You thought wrong!

There is a standard-sized chessboard ($8$ rows and $8$ columns), where the pieces are denoted by `*` (asterisk), and the empty spaces are denoted by `.` (dot). 

To teach students how to use the queen's maximum potential, the chess teacher has shown the students various ways to place the queen on the board on an empty space to attack as many pieces as possible. 

Now you have been given the task to find the maximum number of pieces that can be attacked simultaneously for different configurations. 

The queen moves in a row, column, and both diagonals until she encounters either a piece or the edge of the board. 

# Input data

The first line contains $t$, the number of tests. 

The next $8 \cdot t$ lines contain the chessboards, where pieces are denoted by `*` (asterisk), and empty spaces are denoted by `.` (dot). 

# Output data

For each of the $t$ lines, print the answer for the respective test. 

# Constraints and clarifications

* $t \leq 100$

# Example

`stdin`
```
2
**......
....*...
..*....*
*....*..
..*..*..
.....*..
...*..**
**......
.....*..
........
.....*..
..*.....
....*...
........
.*....*.
........
```

`stdout`
```
7
4
```

## Explanation

For the first test, placing the queen on $(2, 1)$ allows attacking $4$ pieces.

The optimal answer is $7$, by placing the queen on square $(5, 5)$.
```