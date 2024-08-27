## Joc3

Gigel and Andrei have $N$ bags with precious stones numbered from $1$ to $N$. Because they do not want to split the stones between themselves, they decided to play a game, and the winner would take all the stones. The game consists of alternately making moves. A move consists of selecting some stones from a bag $i$ $(1 \leq i < N)$ and moving them to bag $i+1$. The player who can no longer make a move (when all the stones are placed in the last bag) loses the game.

## Task

Knowing both the number of bags and their configuration, and the fact that Gigel will make the first move, determine if there is a winning strategy for him.

## Input data

The first line of the file `joc3.in` will contain $N$, the number of bags. The next $N$ lines will contain the number of precious stones in bag $i$.

## Output data

If Gigel does not have a winning strategy, the output file `joc3.out` will contain the value $-1$. Otherwise, print on the first line the numbers $p$ and $q$ that encode the initial move Gigel should make to win the game ($p$ is the number of the bag, and $q$ is the number of stones). If there are multiple initial moves that could lead to a certain win, print the move with the smallest $p$. If there are still ties, print the move with the smallest $q$.

## Constraints and clarifications

$1 \leq N \leq 100000$

$0 \leq$ number of stones in a bag $\leq 10000$

## Examples

`joc3.in`

```
5
2
5
4
3
1
```

`joc3.out`

```
2 2
```

## Explanation

By making this move, Gigel will win if he continues to play perfectly. There is no other move with a smaller $p$ or $q$.

`joc3.in`

```
5
0
0
0
0
10000
```

`joc3.out`

```
-1
```

## Explanation

Since all the stones are placed in the last bag, Gigel cannot make any move.