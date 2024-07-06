```markdown
Domino is a game that uses $N$ special, rectangular pieces. Each piece has a digit from $1$ to $9$ inscribed on the first and second half.

During the game, the $N$ pieces are placed on the game board such that all digits are aligned horizontally, and the player can act upon a piece in two ways:
* REMOVE — the piece is taken off the game board;
* ROTATE — the piece is rotated $180^{\circ}$, maintaining its relative order with respect to the other pieces.

For example,

~[domino.png|width=35em]

# Task

Knowing that during the game at most $K_1$ ROTATIONS and exactly $K_2$ REMOVALS of pieces can be performed, determine the largest possible number that can be formed by writing, from left to right, the digits on the pieces remaining on the board after performing the allowed operations.

# Input data

The input file `domino.in` contains:
* The first line contains three natural numbers $N$, $K_1$, and $K_2$, in this order, separated by a space, having the meaning explained in the statement;
* The following $N$ lines contain two digits separated by a space, representing the digits inscribed on the domino pieces, in the order they are placed on the board, from left to right.

# Output data

The output file `domino.out` will contain a single natural number on the first line, representing the largest number determined according to the problem's requirements.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$
* $0 \leq K_1, K_2 \leq N$
* $0 < K_1 + K_2 \leq N$

# Example

`domino.in`
```
6 2 3
2 5
7 8
2 5
8 1
1 3
7 4
```

`domino.out`
```
878174
```

## Explanation

There are $6$ game pieces, and at most $2$ ROTATIONS and exactly $3$ REMOVALS can be performed. The pieces are placed on the game board as follows:

~[domino2.png|width=40em]

To obtain the largest possible number, proceed as follows:

~[domino3.png|width=40em]

Thus, we get the largest possible number: $878\ 174$.
```