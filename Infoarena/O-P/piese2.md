# Piese2

Miruna and Aglaia received a game with colored pieces from their parents for St. Nicholas. The game consists of $K$ red pieces, $K$ blue pieces, and a game board of size $1 \times N$. The rules of the game are as follows: At the beginning, the pieces are placed on the board so that there are no $2$ pieces on the same column, and any $2$ consecutive pieces are colored differently. The first piece must be red. The two girls will take turns making moves until one of them can no longer make a move, at which point she loses the game. Miruna can only move red pieces, while Aglaia can only move blue pieces. A move consists of choosing a piece and moving it one column to the right or left if it does not leave the board and if the respective location is not occupied by another piece. Miruna makes the first move. The girls are very intelligent, so they will always play optimally. For an initial configuration of the pieces, you will have to determine who will win the game.

## Input data

The input file `piese2.in` contains the first line with $3$ natural numbers $T$, $N$, and $K$, representing the number of tests that will follow, the size of the game board, and the number of pieces of a certain color. The following $T$ lines will contain $2K$ natural numbers. These will be distinct and given in ascending order. They will represent the initial positions of the pieces.

## Output data

In the output file `piese2.out` you will print $T$ lines, on the $i^{th}$ line containing the name of the winning girl for the game number $i$.

## Constraints

$1 \leq T \leq 10$

$2 \leq N \leq 10^9$

$1 \leq K \leq 10^5$

$2K \leq N$

For $20\%$ of the tests $N \leq 10$

## Example

`piese2.in`
```
2
4
1
1 3
1 4
```

`piese2.out`
```
Miruna
Aglaia
```

## Explanation

We have a board of length $4$, and one piece of each color. In the first game, Miruna moves to $2$, Aglaia moves to $4$, Miruna moves to $3$, and wins. In the second game, Miruna moves to $2$, Aglaia moves to $3$, Miruna moves to $1$, Aglaia moves to $2$, and wins.