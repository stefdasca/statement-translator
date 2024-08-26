## Task

Gigel and Ionel are playing a game. They have a pile containing $N$ objects and take turns making moves. The player whose turn it is can take from the pile a number of objects between $1$ and $min\{ K, the number of objects remaining in the pile \}$. The number of objects taken at each move is added to the total number of objects taken so far by that player. The winner of the game is the one who, when the pile is emptied, has an even number of objects (since the initial number of objects in the pile is odd, there will be a single winner). Gigel makes the first move. Given values $N$ and $K$, determine who will win the game, considering that both Gigel and Ionel use an optimal strategy.

## Input data

The first line of the input file `obj.in` contains the number $J$ of games to be described below. Each of the next $J$ lines contains two integers, separated by a space: $N$ and $K$.

## Output data

In the output file `obj.out` you will print $J$ lines. For each game described in the input file (in the order given in the file), you will print the character `G` if Gigel will win the game, or the character `I` if Ionel will win the game.

## Constraints

$1 \leq J \leq 30$

For each game:

$1 \leq N \leq 1\ 000\ 000\ 000$, $N$ odd

$1 \leq K \leq N$

For $50\%$ of tests $N \leq 20\ 000$ and $K \leq 100$

For $90\%$ of tests $N \leq 1\ 000\ 000$

## Example

`obj.in`

```
5
21 8
23 8
9 3
11 3
999999 12345
```

`obj.out`

```
I
G
I
G
G
```