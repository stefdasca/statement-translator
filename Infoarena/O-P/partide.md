## Task

N friends passionate about chess met up and, since they only had one chessboard, they decided to play using the following system. In the first game, two of them play (as you know, the game of chess is played by two). Then, after each game played, the winner "stays at the table". That is, the one who won stays to play the next game with one of the other friends (possibly, if the other friends do not mind, they could play even against the one they have just defeated). Knowing how many games each of the $N$ friends played (both won and lost), determine a possible order of the games played, along with the result of each one.

## Input data

The input file `partide.in` contains on the first line the integer number $N$, representing the number of friends. On the next line, it contains $N$ integers, greater than or equal to $0$, representing the number of games played by each of them. The first number corresponds to the games played by the first friend, the second corresponds to the games played by the second friend, and so on.

## Output data

The output file `partide.out` will contain on the first line the number $M$ of games played in total. On the next $M$ lines, it will contain two distinct integers $a$ and $b$, from the interval $[1, N]$, separated by a space. Their meaning is that in the respective game, friends $a$ and $b$ played. The winner of the game will be printed before the loser. For each game from $2$ to $M$, one of the players (the current winner or loser) must be the winner of the previous game.

## Constraints and clarifications

$2 \leq N \leq 100$  
The total number of games played will not exceed $10 \ 000$.   
The result of any game will not be a draw.   
For the test cases used in evaluation, there will be at least one possibility for playing the games.

## Example

`partide.in` 
```
4 
2 4 1 5
```

`partide.out`
```
6 
4 3 
4 1 
2 4 
2 1 
4 2 
2 4
```