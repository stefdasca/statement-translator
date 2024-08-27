# Pawns

We consider a board divided into multiple cells that contain pawns. The cells are connected by arrows, and moving from any cell in the direction indicated by the arrows, we will never return to the starting cell. Thus, there are cells from which no arrows leave and cells into which no arrows arrive. We consider two players. Each player can move, when it's their turn, a pawn from the cell it is in to a cell indicated by an arrow. The player who cannot move when it's their turn loses the game. At the beginning of a game, the first move is made by player $1$.

## Task

Determine if player $1$ has a winning strategy.

## Input data

The input file `pawns.in` contains on the first line two integers $n$ and $m$, separated by a single space, which represent the number of cells on the board and the number of arrows, respectively. On each of the next $m$ lines there are two integers $x$ and $y$, separated by a single space, indicating that there is an arrow from cell $x$ to cell $y$. On the next line there is a number $t$ which represents the number of games to be played. On each of the next $t$ lines there are $n$ integers, separated by spaces, which represent the number of pawns in each cell for a specific game.

## Output data

The output file `pawns.out` must contain $t$ lines. Each of the $t$ lines will contain the value $0$ if for a configuration player $1$ does not have a winning strategy, and the value $1$ otherwise.

## Constraints and clarifications

$1 \leq n, m \leq 500$

$1 \leq t \leq 15$

The number of pawns in a cell will not exceed the value $500$

The cells are numbered from $1$ to $n$

## Example

`pawns.in`

```
3 3
1 2
1 3
2 3
2
1 0 0
2 2 2
```

`pawns.out`

```
1
0
```