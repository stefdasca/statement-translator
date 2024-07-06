In the wake of the recent spectacular 3-0 victory of Romania's national football team against Ukraine, coach Fisu' lu' Tasu' has already begun preparations for the next match with Belgium. As the match approaches, the coach has a problem with forming the team and needs your help. As a reward for solving this problem, Fisu' lu' Tasu' promises you 3 points in the match with Belgium.

# Task

Fisu' lu' Tasu' has $N$ players available to choose the first 11 of Romania's national team. For each player, the positions they can play on the field are known, in the form of an 11-digit binary string. A $1$ at a certain position in the string indicates that the player can play on that position, and a $0$ indicates that they cannot play on that position. Field players cannot stay in goal, and goalkeepers cannot play on the field (the first position in the string is associated with the goalkeeper). Fisu' lu' Tasu' asks you to calculate the number of ways he can choose the first 11, modulo $10^9 + 7$.

# Input data

The first line of the input file `primul-11.in` contains a natural number, $N$.
The next $N$ lines contain $N$ binary strings of 11 digits each, the $i$-th string representing the positions in which player $i$ can play.

# Output data

The single line of the output file `primul-11.out` will contain a single natural number representing the number of ways Fisu' lu' Tasu' can choose the first 11, modulo $10^9 + 7$.

# Constraints and clarifications

* $1 \leq N \leq 1\ 000$;
* A football team (the first 11) is made up of one goalkeeper and 10 field players.
* The first position in the players' strings is associated with the goalkeeper.
* In a valid way to choose the first 11, there is one player in each field position.
* Two teams are different if there is a position among the 11 where the players in the two teams are different.

| # | Points | Constraints |
| - | - | ------------ |
| 1 | 0 | The example below. |
| 2 | 7 | Each player can play in at most one position. |
| 3 | 11 | $N=11$ |
| 4 | 32 | $N \leq 100$ |
| 5 | 50 | $N \leq 1\ 000$ |

# Example

`primul-11.in`
```
12
10000000000
10000000000
00001100000
00001010000
00000110000
01000000000
00110000000
00010001000
00000001000
00000000010
00000000100
00000000001
```

`primul-11.out`
```
4
```

## Explanation

There are 4 ways to choose the first 11. Based on the player IDs, they can be:
* $1$, $6$, $7$, $8$, $3$, $5$, $4$, $9$, $11$, $10$, $12$;
* $1$, $6$, $7$, $8$, $4$, $3$, $5$, $9$, $11$, $10$, $12$;
* $2$, $6$, $7$, $8$, $3$, $5$, $4$, $9$, $11$, $10$, $12$;
* $2$, $6$, $7$, $8$, $4$, $3$, $5$, $9$, $11$, $10$, $12$.

The $i$-th number in the teams above represents the ID of the player in position $i$.