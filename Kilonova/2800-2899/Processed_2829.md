> "What's even better than soup?
> Only kebab and shawarma�

After a stormy night at the "La Regele" club, Țil and Rose head towards Siclam to eat. Unfortunately, after finding out that Cristi's menu is not being served that night, Rose decides that the best option is to get a schnitzel as big as a tractor's wheel. Since Țil is highly educated at top universities, he asks for $N$ schnitzels as big as tractor wheels. As tractor wheels are not always equal in size, the schnitzels can have different diameters. Since Rose also has to feed Lion, he will eat every second schnitzel, and Țil will eat every third schnitzel. The story continues through a night full of adventures. In order not to bore you with the details, we will get to the point.

We are given a sequence $a_1, \dots , a_N$ consisting of non-negative numbers. In this sequence, a game will be played between two players, let's call them $T$ and $R$, where $T$ moves first and the players alternate turns. Each player has a pawn placed at a position in the sequence $a$, with the two positions being distinct. On a move, $T$ can move his pawn from position $i$ to one of the positions $i \pm 2$, and $R$ from position $i$ to one of the positions $i \pm 3$. Players can also choose not to move their pawn in a turn, thus skipping their move. A position $1 \leq i \leq N$ is considered captured by a player if the player's pawn has been at that position at any point in the game. A move by a player is valid only if the position to which the pawn moves remains within the interval $[1, N]$ and has not already been captured by the other player. The game ends after a total of $10^{100}$ moves.

At the end of the game, a player’s score is the sum of the values associated with the positions he has captured. The player with the highest score wins, and in the event of a tie, $R$ wins. We will assume that both players play optimally, meaning if they have a strategy that guarantees them the win, they will execute it.

# Task

You are given $Q$ queries of the form $(l, r)$. For each query, compute the number of pairs $(i, j)$ with $i \ne j$ such that $l \leq i, j \leq r$ and $T$ would win if his pawn started at position $i$ and $R$'s pawn started at position $j$. **Note:** both $i < j$ and $i > j$ are considered.

# Input data

The first line of the input contains the integer $N$. The second line of the input contains $N$ non-negative numbers $a_1, \dots , a_N$ representing the game board. The third line of the input contains the integer $Q$. The next $Q$ lines each contain two integers $l, r$ representing the data for a query.

# Output data

The output will contain $Q$ lines, each containing the answer to a query, in the order of the input.

# Constraints and clarifications

* $3 \leq N \leq 500 \ 000$
* $1 \leq Q \leq 500 \ 000$
* $0 \leq a_i \leq 1 \ 000 \ 000 \ 000$ for $1 \leq i \leq N$

| # | Score | Constraints          |
| - | ------ | ------------------- |
| 1 | 17     | $1 \leq N \leq 300$  |
| 2 | 12     | $1 \leq N \leq 5 \ 000$     |
| 3 | 33     | $1 \leq Q \leq 100$     |
| 4 | 10     | $1 \leq Q \leq 100 \ 000$     |
| 5 | 28     | No additional constraints.     |

# Examples

`stdin`
```
7
1 2 3 4 5 6 7
4
1 7
1 5
2 3
4 7
```

`stdout`
```
27
12
1
8
```

## Explanation

For the third query, we have $l = 2, r = 3$. In this case, $T$ wins if his pawn starts at position $3$ and $R$'s pawn starts at position $2$.

For the fourth query, we have $l = 4, r = 7$. In this case, $T$ wins if the initial positions of the pawns $(t, c)$ are among the set $\{(4, 5), (5, 4), (4, 7), (7, 4), (5, 6), (6, 5), (6, 7), (7, 6)\}$.