
Andrei and his friends decided to play Remi, a game that contains multiple pieces of the same size, with each piece having a digit from $0$ to $9$ written on it. 
~[remi.png|align=right]
At the beginning of the game, all the pieces are in a bag from which each player will draw pieces in turn as follows: the first piece drawn will be named â€œJolly Jokerâ€ and will be kept to be later placed on the game board. The same player then draws, one by one, another $N$ pieces from the bag and arranges them from left to right on his game board, in the order in which he drew them. After all the players have arranged their pieces, the game begins with the following rules:

* The â€œJolly Jokerâ€ piece can be placed at any time and anywhere on the drawing player's game board.
* At most one of the $N$ pieces drawn after the â€œJolly Jokerâ€ and placed on the game board can be moved from its place and placed elsewhere on the same board.

The winner of the game is designated the one who can form, respecting the game's rules, the largest number, read from left to right with the digits written on the $N + 1$ pieces placed on his game board.

# Task

Knowing the pieces drawn by Andrei, help him build the number so that he has the greatest chance of winning the game.

# Input data

The input file `remi.in` contains:

* the first line contains a single digit representing the â€œJolly Jokerâ€ piece drawn by Andrei.
* the second line contains the natural number $N$, representing the number of pieces drawn afterward by Andrei.
* the third line contains $N$ digits separated by a space, representing the digits written on Andrei's pieces, in the order of their drawing and placing on the game board.

# Output data

The output file `remi.out` will contain the first line a single natural number, representing the largest number formed with Andrei's $N + 1$ game pieces, respecting the rules of the game.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$
* The numbers on the pieces are digits from $0$ to $9$

# Example

`remi.in`
```
3
5
4 2 7 0 4
```

`remi.out`
```
743204
```

## Explanation

The â€œJolly Jokerâ€ piece has the digit $3$ Andrei drew another $5$ pieces from the bag in the following order: $4, 2, 7, 0$ and $4$. From the five pieces drawn, the piece that changes position is the one containing the digit $7$. The largest number constructed by Andrei in the Remi game is: $743204$
