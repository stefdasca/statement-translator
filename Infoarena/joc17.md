# Game17

We have a grid with $N$ rows and $M$ columns and two players who move alternately. A move consists of coloring one cell of the grid in red or blue, depending on the player making the move. On the first move, a player can color any uncolored cell. Afterwards, players are allowed to color only cells that are adjacent (sharing a side) to a previously colored cell in the same color. The player who cannot make a move loses the game. Determine the winner considering that both players play optimally.

## Input data

The input file joc17.in contains on the first line a natural number $T$ representing the number of tests. On each of the following lines, each test is described by a pair of two natural numbers $N$ and $M$, the number of rows and columns of the grid where the game is played.

## Output data

For each test in the input file, print to the output file joc17.out one line in the form `Case <t>: <result>` (without quotes) where $<t>$ is the test number (starting from 1), and $<result>$ will be replaced by the word "First" if the first player wins, or "Second" if the second player wins.

## Constraints and clarifications

$1 \leq T \leq 100$

$1 \leq N, M \leq 1000$

## Example

`joc17.in`

```
2
1 1
2 2
```

`joc17.out`

```
Case 1: First
Case 2: Second
```