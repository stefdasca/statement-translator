# Archipelago

One late evening, $K$ friends discovered a new game called Archipelago. The game is played on a large map that contains several islands, some of which are connected by bridges. For convenience, the islands are numbered from $1$ to $N$. An archipelago is a group of islands where you can reach any island from any other island using the existing bridges. The game is played in rounds, and in each round, the player whose turn it is chooses an archipelago to conquer. Once an archipelago is conquered by a player, it remains under that player's control until the end of the game. The game ends when there are no archipelagos left to conquer. At the end of the game, all friends are curious to find out their respective scores. Each player's score is given by the number of islands they conquered during the rounds. The order of the players is agreed upon by the friends and is given to you.

## Input data

The input file `arhipelag.in` contains on the first line the number $T$ of test cases. The first line of each test contains $3$ numbers $N$, $M$, and $K$, where $N$ represents the number of islands, $M$ represents the number of bridges, and $K$ represents the number of friends. On the next $M$ lines, there is one pair of integers representing $2$ islands connected by a bridge. On the last line of a test, the order of the players is given.

## Output data

In the output file `arhipelag.out`, you will print in order for each test case one line in the format "Case $<t>$: $<x1>$ $<x2>$ $\dots$ $<xK>$" (without quotes) where $<t>$ is the test number, $<x1>$ is the score of player number $1$, $<x2>$ is the score of player number $2$, $\dots$, $<xK>$ is the score of player number $K$.

## Constraints and clarifications

$T = 5$

$1 \leq N, M \leq 100\ 000$

$1 \leq K \leq 100$

Between $2$ islands there can be multiple bridges.

## Example

`arhipelag.in`
```
2
5 2 2
1 3
2 4
2
1 11
1 4
9 5
4 2
1 3
```

`arhipelag.out`
```
Case 1: 2 3
Case 2: 2 3 2 4
```

## Explanation

For the first game, player $2$ conquers the archipelago formed by island $5$, then player $1$ takes the archipelago formed by islands $1$ and $3$, and finally, player $2$ takes the archipelago formed by islands $2$ and $4$. At the end of the game, player $1$ has a score of $2$ (because they own $2$ islands), and player $2$ has a score of $3$ (they own the remaining $3$ islands).