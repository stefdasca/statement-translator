In *Hogwarts* there is a chessboard with $N$ rows and $M$ columns. *Harry Potter* has found $T$ rooks placed by *Hagrid*, each of which guards the row and the column on which it is placed. He needs to place *safely* $K$ pawns on the board, meaning that none of them should be attacked by any rook. The chessboard in *Hogwarts* is special because multiple pawns can be placed in the same cell simultaneously!

# Task

Knowing all these rules, help *Harry Potter* determine the number of ways to place **all** $K$ pawns safely on the chessboard.

# Input data

The input file `potter.in` contains on the first line four non-zero natural numbers $N, M, T, K$ separated by spaces, with the meanings described above, and on the next $T$ lines, pairs $(i, j)$ representing the row and the column where each rook is placed.

# Output data

The output file `potter.out` contains a single number, representing the remainder of the division by $10^9+7$ of the number of distinct ways to position **all** $K$ pawns.

# Constraints and clarifications

* $1 \leq N, M \leq 2 \ 000$
* $1 \leq K \leq 100 \ 000$
* $1 \leq T \leq N \cdot M$
* Two arrangements are distinct if there is at least one cell with a different number of pawns.

|#|Points|Constraints|
|-|-|--------|
|1|9|$K = 1$|
|2|12|$K = 2$|
|3|19|$1 \leq N \cdot M \leq 25, 1 \leq K \leq 10$|
|4|23|$1 \leq N, M \leq 100$|
|5|37|No additional constraints|

# Example

`potter.in`
```
2 3 1 3
1 1
```

`potter.out`
```
4
```

## Explanation

On the board, *Harry Potter* can place the three pawns safely in the cells $(2,2)$ and $(2,3)$. In each of these cells, he can place $0$, $1$, $2$, or $3$ pawns.