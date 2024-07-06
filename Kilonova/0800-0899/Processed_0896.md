Mihai received a puzzle game for his birthday. The game has $N$ pieces made by gluing together $1 \times 1$ blocks (illustrated in the figures below as `X`); we will call these blocks simply `X`s from now on. The following rules are followed to make a piece:

* The `X`s are stacked on top of each other, forming columns that can have different heights, then the columns are aligned at the bottom and glued together, one after the other, from left to right;
* A column can have at most $9$ `X`s;
* All pieces have the same number of columns.

~[puzzle.jpg|align=center]

In figures $1, 2, 3, 4$ there are puzzle pieces that follow the described rules, and in figure $5$ and figure $6$, there **are NOT** puzzle pieces, because they cannot be obtained by gluing columns of $X`s one after the other from left to right.
Being young, Mihai cannot solve the puzzle, but he can do one single operation: he chooses two pieces and joins them by their top sides, flipping one of the pieces upside-down (without rotating it or flipping it left-right). If as a result of this operation he obtains a rectangle consisting of complete columns of `X`s, all columns having the same height, he is satisfied. For example, the piece from figure $1$ and the one from figure $2$ can be joined as described.
In figure $7$, the piece from figure $2$ is flipped upside-down. In figure $8$, the rectangle obtained from the piece from figure $1$ and the piece from figure $2$ flipped upside-down is illustrated.
Note that if we rotated the piece from figure $4$, we could join it with the piece from figure $1$, but rotation is not allowed.
We will encode a piece by a natural number, each digit in the number representing (from left to right) how many `X`s are on the corresponding column of the piece.
For example:
- the piece from figure $1$ is encoded as $4232$;
- the piece from figure $2$ is encoded as $1323$;
- the piece from figure $3$ is encoded as $4444$;
- the piece from figure $4$ is encoded as $3231$.

# Task

Determine the number of ways Mihai can choose two pieces out of the $N$ to perform the described operation.

# Input data

The input file `puzzle.in` contains:
* on the first line a natural number $N$ representing the number of pieces in the game. 
* on the second line, $N$ natural numbers, separated by a single space, representing the encodings of the $N$ pieces.

# Output data

The output file `puzzle.out` will contain:
* a single line which will contain the requested number.

# Constraints and clarifications

* $2 \leq N \leq 10^5$;
* The numbers representing the encodings of the pieces have the same number of digits (at most $5$) and do not contain the digit $0$.
* In an operation it does not matter which of the pieces is flipped, therefore the pair formed by piece $a$ and piece $b$ is considered the same as the pair formed by piece $b$ and piece $a$.
* The rectangle obtained as a result of an operation can have a height greater than $9$.
* For tests worth $30$ points $N \leq 1 \ 000$.

# Example

`puzzle.in`
```
5
222 432 234 123 111
```

`puzzle.out`
```
3
```

## Explanation

There are $3$ pairs of pieces that can be joined: piece $1$ with piece $5$, piece $2$ with piece $3$, piece $2$ with piece $4$. Pieces $3$ and $4$ could be joined correctly if one of them was flipped left-right or rotated, but this is not allowed.