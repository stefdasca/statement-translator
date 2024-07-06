Ana and Bogdan have invented a new game, named Strips. It is a strategy and memory training game because it is played on a board that is not visible to both players during the game.

The game board is a white strip of $N$ cm in length, with positions marked every 1 cm. The positions are numbered from $0$ to $N - 1$, with position $0$ at the beginning of the board (left end) and position $N - 1$ at the end of the board (right end).

At the beginning of the game, each player has $Nr$ colored strips, all of the same length $L$ cm. Ana's strips are red, while Bogdan's strips are green.

Players take turns alternately, with Ana going first. On their turn, the player selects a position on the game board, and if the position is valid, a strip of the player's color will be placed on the board, with the left end of the strip fixed at the chosen position. If the position is not valid, the move will not be executed, and the player will receive 1 penalty point and lose the strip that should have been placed on the board at that position (it is removed from the game).

A position is considered valid if a strip of length $L$ can be placed on the game board with the left end of the strip fixed at the specified position such that the strip is entirely on the game board, without overlapping or touching an area colored in the opponent's color.

The game ends when the players run out of strips. Each player aims to obtain an area on the board of the longest possible length colored in their color. An area on the board consists of consecutive positions, all colored in the same color.

# Task

Write a program that reads the length of the game board, the number of colored strips each player has at the start of the game, the length of the strips, and the positions specified by the players during the game, and solves the following two tasks:

* Determine the number of penalty points for each of the two players.
* Determine the maximum length of an area on the board colored in each player's color at the end of the game.

# Input data

The input file `strips.in` contains on the first line a natural number $C$ representing the task to be solved ($1$ or $2$). The second line contains three natural numbers separated by a space $N \\ Nr \\ L$, with the meanings given in the statement. The other lines of the input file contain in order the positions specified by the players during the game, one position per line.

# Output data

The output file `strips.out` will contain a single line with two natural numbers $rezA$ and $rezB$, separated by a single space. If $C = 1$ then $rezA$ is the number of penalty points accumulated by Ana, and $rezB$ is the number of penalty points accumulated by Bogdan. If $C = 2$ then $rezA$ is the maximum length of a red area at the end of the game, and $rezB$ is the maximum length of a green area at the end of the game.

# Constraints and clarifications

* $1 \\leq N \\leq 1 \ 000 \ 000 \ 000$;
* $1 \\leq Nr \\leq 50 \ 000$;
* $1 \\leq L \\leq 20 \ 000$;
* It is guaranteed that for the test data at the end of the game, for each of the two players, the number of disjoint areas on the game board colored in the player's color is $\\leq 5 \ 000$.
* Positions are natural numbers less than $N$.
* Being beginners, Ana and Bogdan still do not play optimally.
* For tests worth $50$ points the task is 1.
* For tests worth $40$ points $1 \\leq N \\leq 1 \ 000 \ 000$; $1 \\leq L \\leq 1 \\ 000$; and $1 \\leq Nr \\leq 1 \ 000$.

# Example 1

`strips.in`
```
1
20 4 3
9
15
2
13
5
17
0
12
```

`strips.out`
```
0 1
```

# Example 2

`strips.in`
```
2
20 4 3
9
15
2
13
5
17
0
12
```

`strips.out`
```
8 7
```

## Explanation

The game board is $20$ cm long, and the positions are numbered from $0$ to $19$. Each player has $4$ strips of length $3$.

In the first move, Ana places a red strip on positions $9, 10, 11$.
In the second move, Bogdan places a green strip on positions $15, 16, 17$.
In the third move, Ana places a red strip on positions $2, 3, 4$.
In the fourth move, Bogdan places a green strip on positions $13, 14, 15$.
In the fifth move, Ana places a red strip on positions $5, 6, 7$.
In the sixth move, Bogdan places a green strip on positions $17, 18, 19$.
In the seventh move, Ana places a red strip on positions $0, 1, 2$.
In the eighth move, Bogdan chooses an invalid position (because it touches a red area), so the move will not be executed (he gets $1$ penalty point).
The game board at the end of the game will look like this:

~[strips.png]