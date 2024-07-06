The king is known to move on the chessboard only to the neighboring squares in all 8 directions. In the figure below, we can see the possible movements of the king in one move. We call a path a succession of one or more such moves.

~[imag.png|align=center|width=20em]

# Task

Given the size $m \\times n$ of the chessboard, the initial position $(l_1, \\ c_1)$ and the final position $(l_2, \\ c_2)$ of the king's path, calculate the **number of distinct minimum paths** in which the king can travel.

# Input data

The input file `rege.in` contains on the first line the values $m$ and $n$ separated by a space, representing the size of the chessboard; on the second line, the numbers $l_1$ and $c_1$ separated by a space, representing the row and column of the king's initial position; and on the third line, the numbers $l_2$ and $c_2$ separated by a space, representing the king's final position.

# Output data

The output file `rege.out` will contain on the first line the number of distinct minimum paths modulo $666013$.

# Constraints and clarifications

* $1 < m, n, l_1, c_1, l_2, c_2 \\leq 1 \ 000$

# Example

`rege.in`
```
5 5
3 3
2 5
```

`rege.out`
```
2
```

## Explanation

1) $(3, 3) - (3, 4) - (2, 5)$
2) $(3, 3) - (2, 4) - (2, 5)$