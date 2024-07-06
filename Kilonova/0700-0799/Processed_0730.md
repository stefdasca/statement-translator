# The game "Don't Get Mad, Brother!"

The game "Don’t Get Mad, Brother!" is played by two players. On a circular track with $n$ numbered squares from $1$ to $n$, following the clockwise direction, there are values of $0, 1$, and $10$ written on them. Each of the two players will have a pawn and will take turns, starting from square $1$. Player $1$ starts the game. Each player will move their pawn according to the value obtained by rolling a die, accumulating or losing points depending on the square they reach. Each player reads the die value when it is their turn.

The game has the following rules:
1. The winner can be:
   - The player who first reaches square $1$ again, regardless of the score (except if their score is $0$).
   - If the series of die rolls finishes, it means the players got bored, and the one who has accumulated more points wins. If they have equal points, the player standing on the higher numbered square wins.
2. After rolling the die, the player moves their pawn by the number of squares indicated by the die, in the clockwise direction, starting the count with the next square from their current position. The first square does not contain the value $0$ (zero).
3. After the move, the following situations can occur:
   - They land on a square with the value $0$ (zero) – the player is penalized, loses all accumulated points, and resumes the game from position $1$.
   - They land on a square with the value $10$ – receives a bonus of $10$ points.
   - They land on a square with the value $1$ – receives $1$ point.
   - They land on a square where the other pawn is (except square $1$ when they win) – the player who arrives last is penalized, loses all points, and resumes the game from square $1$.

# Task

Determine the winning player, the positions of each player on the circle, and the score of each player.

# Input data

In the file `joc.in`, the following data is given:
- The first line contains the number $n$ of squares in the circle.
- The second line contains a sequence of $n$ values ($0, 1$ or $10$), separated by space, representing the value of each square.
- The third line contains the number of die rolls.
- The fourth line contains a sequence of integer values between $1$ and $6$, separated by space, representing the die rolls.

# Output data

The file `joc.out` will contain $3$ lines with the following information:
- The first line contains the winning player.
- The second line contains the position and score of player number $1$.
- The third line contains the position and score of player number $2$.

# Constraints and clarifications

* $7 \leq n \leq 100$;

# Example 1

`joc.in`
```
10
1 1 1 1 1 10 0 1 1 0
8
3 6 2 4 1 3 5 3
```

`joc.out`
```
2
6 10
1 3
```

# Example 2

`joc.in`
```
7
1 1 0 10 1 10 1
16
6 4 2 4 6 2 1 3 5 6 3 3 2 1 4 5
```

`joc.out`
```
1
1 3
1 0
```

# Example 3

`joc.in`
```
12
1 10 1 1 0 10 1 1 1 10 0 1
4
5 6 3 3
```

`joc.out`
```
2
9 11
10 11
```

