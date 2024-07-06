```markdown
Chess is becoming more and more popular in IIOTLand and as a result, the government decided to organize a chess tournament in order to award the best chess players from the country. In order to find out more about the outcome of the tournament, you have been asked by the government to analyze the results of each game played.

In short, you are given the descriptions of each game, move by move, and you have to print the outcome of each game. The moves are noted according to the algebraic chess notation.

The description of each game contains the moves, which are given in the input as a string (the string contains spaces) and the moves are described one by one, the first part of the move representing the first player's move while the second part of the move represents the second player's move, unless the game is finished by the first player, in this case the second part doesn't exist.

It is known that all the games have been played until the very end (thus, there were no resigns) and that the game can be either won by one of the players, or result in a draw.

# Task

Determine the outcome of each game based on the given moves.

# Input data

The first line of the input contains $t$, the number of games played in the tournament. 

The next $t$ lines contain the strings representing the description of each game.

# Output data

The output will contain for each of the testcases a string, which is either "First", if the first player wins, "Second", if the second player wins, or "Draw", if the outcome is a draw.

# Constraints and clarifications

* $1 \leq t \leq 5\ 000$
* $1 \leq |s| \leq 5\ 000$

# Example

`stdin`
```
3
1. e4 c6 2. Nc3 d5 3. Nf3 dxe4 4. Nxe4 Nf6 5. Qe2 Nbd7 6. Nd6#
1. e4 e5 2. Nf3 Qf6 3. d4 exd4 4. Nxd4 Bc5 5. Nb3 Qxf2#
1. e4 b6 2. Qh5 Bb7 3. Nc3 Nc6 4. Bc4 g6 5. Qf3 Bg7 6. Qxf7#
```

`stdout`
```
First
Second
First
```
```