It is considered a chessboard in the form of a matrix with $M$ rows and $N$ columns containing the characters `.` and `#`. The cells containing `#` are considered forbidden and rooks cannot be placed on them. Forbidden cells do not block the attacks of the rooks.

# Task

Calculate $X$, the number of ways to place the rooks in non-forbidden cells, such that no two rooks are placed on the same row or on the same column. Since this number can be very large, determine $X$ modulo $1\ 000\ 003$.

# Input data

The input file `rooks.in` contains on the first line the numbers $M$ and $N$, and on each of the following $M$ lines there are $N$ characters `.` or `#`. Note, the characters on a line are **not** separated by space.

# Output data

The output file `rooks.out` contains a single natural number, the number $X$ modulo $1\ 000\ 003$.

# Constraints and clarifications

* $1 \leq M, N \leq 1\ 000$;
* There will be at most $17$ forbidden cells.

# Example

`rooks.in`
```
3 3
..#
##.
#.#
```

`rooks.out`
```
10
```

## Explanation

There is one solution with zero rooks, four solutions with one rook, four solutions with two rooks, and one solution with three rooks.

~[rooks.png]