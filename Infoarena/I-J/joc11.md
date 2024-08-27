## Task

Determine which player has a sure winning strategy. A player has a sure winning strategy if he/she will win regardless of the opponent's moves.

## Input data

The input file $joc11.in$ contains on its first line a number $T$, the number of tests. The descriptions of the tests will be on the following lines. The first line of each test contains an integer $N$, the length of the side of the board.
Each of the next $N$ lines contains $N$ characters, without spaces between them. Each character is one of the following: $.$ (a white square), $\#$ (a black square), $A$ (the starting position of player $A$), $B$ (the starting position of player $B$). 

## Output data

In the output file $joc11.out$, for each test, print one line with one of the characters $A$ or $B$, indicating the player who has a sure winning strategy. 

## Constraints and clarifications

$1 \leq T \leq 6$

$2 \leq N \leq 300$

There will always be a path on white squares between the starting positions of the two players.

For 40$\%$ of the tests $N \leq 40$.

For 60$\%$ of the tests $N \leq 150$. 

## Example

`joc11.in`

`
1
5
.....
A....
..###
.#...
....B
`

`joc11.out`

`
A
`

## Explanation

There is a single path of length $7$ between the two players. If player $B$ does not choose the shortest path, then he will make more than $7$ moves, hence $A$ will win. If player $B$ does choose the shortest path, player $A$ will still skip over $B$ gaining a two-square advantage, thus winning.