## Competitive Programming Problem Statement: Minimum Effort Calculation

When bored, Costel invents logic games and tries to solve them. One day, Costel takes a rectangular board divided into $M \cdot N$ identical squares, similar to a chessboard, and places identical cubes on it such that each square of the board contains at least one cube and at most $10$ cubes stacked. Costel determines the minimum number of cubes placed on a position of the board, denoted with $MIN$.

He defines the notion of a move as follows: choose four adjacent squares that form a square composed of $2 \cdot 2$ squares and adjust the number of cubes on these positions so that each of the four squares has an equal number of cubes equal to $MIN$. The effort required to make the move is equal to $MAX - MIN$, where $MAX$ represents the maximum number of cubes found on one of the chosen four squares.

The goal of the game is to achieve the same number of cubes, equal to the value $MIN$, on each square of the board, performing a series of moves that require a minimum total effort. The total effort required to solve the game is equal to the sum of the efforts of the moves made.

# Task

Determine the minimum total effort required to solve the game.

# Input Data

The input file `joc.in` has the following structure:

* The first line contains two natural numbers $M$ and $N$, separated by a single space, representing the number of rows and the number of columns of the game board respectively.
* The next $M$ lines contain $N$ natural numbers each, separated by a space, representing the initial number of cubes on each square of the game board.

# Output Data

The output file `joc.out` will contain a single natural number representing the value of the minimum total effort.

# Constraints and Clarifications

* $M$ and $N$ are natural numbers greater than or equal to $2$ with the property that $4 \leq M \cdot N \leq 18$
* The number of cubes placed on a position of the board is a natural number between $1$ and $10$.

# Example

`joc.in`

```
3 4
2 3 2 2
2 4 3 2
3 2 4 2
```

`joc.out`

```
4
```

## Explanation

The minimum is $2$. An optimal sequence of moves could be:

Move $1$: Choose positions $(2, 2)$, $(2, 3)$, $(3, 2)$, and $(3, 3)$. The effort is $4 - 2 = 2$

Move $2$: Choose positions $(1, 1)$, $(1, 2)$, $(2, 1)$, and $(2, 2)$. The effort is $3 - 2 = 1$

Move $3$: Choose positions $(2, 1)$, $(2, 2)$, $(3, 1)$, and $(3, 2)$. The effort is $3 - 2 = 1$

The total effort is $4$.