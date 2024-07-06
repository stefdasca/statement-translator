On a chessboard with $N$ rows and $N$ columns, there are $M$ bishops. As is known from the game of chess, bishops attack only diagonally.

A position on the chessboard is considered safe if it is not attacked by any bishops on the board.

# Task

Write a program to determine the number of safe positions on the chessboard.

# Input data

The input file `nebuni.in` contains on the first line the natural numbers $N \ M$, separated by a space, as explained in the problem statement. On the following $M$ lines, the positions (row and column, separated by a space) of the $M$ bishops are described, one bishop per line.

# Output data

The output file `nebuni.out` will contain a single line that contains a natural number representing the number of safe positions on the chessboard.

# Constraints and clarifications

* $1 \leq N \leq 10^6$
* $1 \leq M < 16 \ 500$
* Rows and columns are numbered from $1$ to $N$.
* For 50% of tests $N \leq 300$.
* For 60% of tests $M \leq 1 \ 000$.

# Example

`nebuni.in`
```
5 4
2 1
1 3
4 2
5 2
```

`nebuni.out`
```
6
```

## Explanation

On a $5 \times 5$ chessboard, there are $4$ bishops.

The positions attacked by the $4$ bishops are marked in grey.

~[nebuni.PNG|align=left|width=10cm]

