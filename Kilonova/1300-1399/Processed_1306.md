For a game design competition, Gigel wants to build a game. The game involves $n$ contestants numbered from $1$ to $n$.

Each contestant has a sequence of $m$ rooms at their disposal, numbered from $1$ to $m$. The goal of the game is to find a hidden treasure in one of these rooms.

Each room contains a code, a natural number that is either $0$ or has at least $2$ digits. The last digit indicates the number of penalty stages, i.e., the number of stages during which the contestant is not allowed to leave the room. The number obtained by removing the last digit of the code indicates the number of the room to which the contestant will move in the next stage or after the penalty expires. There are two exceptions to this coding rule: the number $9\ 999$ encodes a room containing a treasure, and the number $0$ encodes a room containing a trap.

In stage $1$, each player enters room $1$ in their sequence of rooms. Depending on the code found in the room, the following situations are possible:

* The found code is $9\ 999$, which means that the player is the winner and the game ends at the end of this stage.
* The found code is $0$, which leads to their elimination from the game.
* For other codes, after the penalty stages, the player moves to the room indicated by the code. For example, upon encountering the code $157$, after completing the $7$ penalty stages, the player will move to room $15$.

The transition from one stage to another occurs simultaneously for all contestants.

# Task

Given the number $n$ of contestants, the number $m$ of rooms allocated to each contestant, and the codes in the $n \cdot m$ rooms, determine the winner of the game, the room where the treasure was found, the number of stages passed until the winner finds the treasure, and the number of contestants eliminated from the game by that stage (inclusive).

# Input data

The first line of the input file `joc.in` contains two natural numbers $n$ and $m$, separated by a space, representing the number of contestants and the number of rooms, respectively.
The next $n$ lines contain $m$ natural numbers each, separated by a space, representing the codes in each room.

# Output data

The first line of the output file `joc.out` will contain four natural numbers separated by a space, representing the winner's index, the room number where the treasure was found, the stage number in which the winner succeeded, and the number of contestants eliminated from the game.

# Constraints and clarifications

* $1 \leq n \leq 400$
* $1 \leq m \leq 900$
* For all input tests, it is guaranteed that there is exactly one winner.

# Example

`joc.in`
```
4 8
0 9999 41 50 61 70 80 30
30 80 60 60 9999 21 40 50
20 30 40 50 61 71 81 9999
20 30 50 0 61 71 9999 41
```

`joc.out`
```
2 5 7 1
```

# Explanation

The second player wins after $7$ stages, and the room where the treasure is found is room $5$. In $7$ stages, one player was eliminated, specifically the first contestant.

The rooms the winner goes through until the end are:

$1 \rightarrow 3 \rightarrow 6 \rightarrow 2 \rightarrow 8 \rightarrow 5$