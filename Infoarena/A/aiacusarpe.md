## Task

Recently, Bulanel discovered a new activity to pass the time: a variation of the classic Snake game. The game is based on a grid with $N$ rows and $M$ columns. Initially, the snake occupies a single cell, located at coordinates $(1, 1)$, i.e., in the top-left corner. At any moment, the snake can move one unit in one of the North, East, South, or West directions. At the start of the game, Bulanel sets a sequence of $T$ moves that the snake must perform. This sequence is fixed, cannot be changed later, and the snake cannot skip any moves. During the game, Bulanel has an infinite amount of apples that he can place at any moment in any of the free cells of the grid. When the head of the snake reaches a cell containing an apple, the snake will instantly grow in length by one unit, with its tail remaining in place during that move. The game ends in any of the following situations: The snake crashes into the wall surrounding the grid. The snake crashes into itself. Note: During a move, all cells of the snake move simultaneously. The snake performs all the moves from the sequence set by Bulanel. We define the score obtained as the length of the snake at the end of the game. Bulanel wants to place the apples in such a way as to obtain the highest possible score, regardless of whether the game ends before the snake finishes the sequence of moves.

## Input data

The input file `aiacusarpe.in` contains on the first line the values $N$, $M$, and $T$, separated by spaces. The second line contains $T$ characters from the set $\{N, E, S, W\}$, representing the sequence of moves.

## Output data

The output file `aiacusarpe.out` must contain a single value: the maximum score that can be obtained through the strategic placement of apples.

## Constraints

$3 \leq N, M \leq 1000$

$1 \leq T \leq N \cdot M$

For tests worth $20$ points,

$N, M \leq 10$ and $T \leq 15$.

For tests worth $50$ points,

$N, M \leq 100$ and $T \leq 2000$.

The problem will be evaluated on tests worth $90$ points.

## Example

`aiacusarpe.in`

```
3 4 6
ESSENV
```

`aiacusarpe.out`

```
6
```

## Explanation

We analyze two possible scenarios: After the first move of the snake, we place a single apple at coordinates $(2, 2)$. The snake executes all the moves from the given sequence and ends the game with a length of $2$. We place apples at coordinates $(1, 2)$, $(2, 2)$, $(3, 2)$, $(3, 3)$, $(2, 3)$. We can do this at the start of the game or sequentially, one apple at a time. Both approaches lead to the game ending when the snake crashes into itself on the last move, having a length of $6$. This is the maximum score that can be obtained.