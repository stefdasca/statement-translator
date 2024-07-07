
Sudoku is a game that takes place on a square board consisting of $9$ rows and $9$ columns. Each cell must contain a value between $1$ and $9$. Typically, some of the cell values are given, and we need to fill in the rest so that:

* Each row contains exactly one occurrence of every number from $1$ to $9$.
* Each column contains exactly one occurrence of every number from $1$ to $9$.
* Each of the $9$ square submatrices $3 \times 3$ (highlighted in the example below) contains every number from $1$ to $9$.

~[sudoku.png|align=center]

# Task

In this problem, we do not need to complete any board. Instead, we are given already completed boards and we need to decide if they are correct according to the rules of the game stated above.

# Input data

The input file `sudoku.in` contains a value $N$ on the first line, representing the number of game boards we need to verify.
Further, there are $N$ matrices $9 \times 9$. Each is given by $9$ rows with $9$ values on each, separated by space. There is a blank line between any two matrices.

# Output data

The output file `sudoku.out` contains, on a single line, $N$ values which can be $1$ or $0$ and are not separated by spaces.
For a board, in the order from the input file, print $1$ if it is correctly completed and $0$ otherwise.

# Constraints and clarifications

* $2 \leq N \leq 20$
* The values in the matrices are natural numbers between $1$ and $9$.

# Example

`sudoku.in`
```
2
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8 9

6 8 2 1 9 4 3 5 7
7 3 1 5 6 8 9 2 4
4 9 5 7 2 3 8 6 1
8 2 7 9 3 5 1 4 6
5 1 9 6 4 7 2 8 3
3 6 4 2 8 1 5 7 9
9 5 6 4 1 2 7 3 8
2 4 8 3 7 9 6 1 5
1 7 3 8 5 6 4 9 2
```

`sudoku.out`
```
01
```
