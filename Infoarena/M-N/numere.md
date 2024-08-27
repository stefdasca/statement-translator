## Task

When they were younger, Mars and Mugurel liked to play with numbers. Thus, they invented the following game: Two players play with two positive numbers. Players take turns making moves, and the player who makes the last move wins. A move consists of subtracting from the larger number a strictly positive multiple of the smaller number, provided that this multiple is less than or equal to the larger number. In other words, assuming the two numbers are $X$ and $Y$ and $X \geq Y$, a move consists of subtracting any number of the form $K \cdot Y$ $(K \geq 1)$ from the number $X$, provided $K \cdot Y \leq X$. The game ends when one of the numbers becomes equal to $0$. Write a program that decides which of the two players will win the game, considering that both players play optimally.

## Input data

The first line of the file `numere.in` contains the number $T$ of games described below. Each of the next $T$ lines contain $2$ integers $X$ and $Y$, separated by a space, representing the initial values of the two numbers.

## Output data

In the file `numere.out` you will contain $T$ lines. Each line will contain the winner of the corresponding game from the input file. You will print $1$, if the first player (the one who makes the first move) will win, and $2$ if the second player will win.

## Constraints and clarifications

$1 \leq T \leq 20$

$1 \leq X,Y \leq 10^9$

## Example

`numere.in`
```
5
1 19
19 1
27 33
333333333 273333333
9997 19999
```

`numere.out`
```
1
1
2
2
1
```