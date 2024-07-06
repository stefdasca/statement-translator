Inspired by the classic Tic-Tac-Toe game (`X` and `0`), Teodora and Ștefan propose to play something similar, adding a few new rules to the classic game:

~[joc.png|align=right|width=13em]

- The game board is a square with side length $N$, which is divided into $N \cdot N$ cells, arranged in $N$ rows and $N$ columns; the cells of the square are numbered from $1$ to $N^2$ traversing the rows from top to bottom, and the columns from left to right;
- Teodora will mark the cells with `X` (the letter `X`), and Ștefan with `0` (the digit `0`);
- During a round, the children alternately mark one previously unmarked cell of the square;
- A round of the game is described by a sequence of exactly $N^2$ natural numbers representing the cells of the square, in the order in which they were successively marked by the two children;
- The game has $K$ rounds; the first is started by Teodora, the second by Ștefan, the third by Teodora, the fourth by Ștefan, and so on;
- A round is won by the player who first manages to completely mark a row, a column, the main diagonal, or one of the two parallel and **adjacent** semi-diagonals (Figure $1$), the secondary diagonal, or one of the two parallel and **adjacent** semi-diagonals (Figure $2$);
- A round ends without a winner if, after marking the $N^2$ cells, there is no row, column, diagonal, or semi-diagonal marked with the same symbol on the board.

# Task

Given the numbers $N, K$ and the $K$ sequences of numbers representing the rounds played, write a program that solves one of the following two tasks:
1. Determine how many rounds each child won.
2. Determine the highest number of marks made until a round is won.

# Input data

The input file `joc.in` contains on the first line a natural number $C$. For all tests, $C$ can only take the values $1$ or $2$. The second line contains two natural numbers $N$ and $K$, separated by a space, representing the size of the game board and the number of rounds played, respectively. On the following $K$ lines, the game rounds are described, one round per line of the file. Within the lines, the numbers are separated by a space.

# Output data

If the value of $C$ is $1$, only point $1$ of the task will be solved. In this case, the output file `joc.out` will contain on the first line two natural numbers $t$ and $s$, separated by a space, where $t$ represents the number of rounds won by Teodora and $s$ the number of rounds won by Ștefan.

If the value of $C$ is $2$, only point $2$ of the task will be solved. In this case, the output file `joc.out` will contain on the first line the highest number of marks made until a round is won.

# Constraints and clarifications

* $3 \leq N \leq 100$;
* $1 \leq K \leq 25$;
* In each game, at least one round is won.
* For a correct solution to the first task, $45$ points are awarded, and for a correct solution to the second task, $45$ points are awarded. $10$ points are awarded for participation.

# Example 1

`joc.in`
```
1
4 4
16 13 15 9 10 1 5 2 6 14 3 7 11 4 8 12
1 2 3 4 5 6 7 8 12 11 10 9 13 14 15 16
1 5 9 6 2 7 3 8 4 10 11 12 13 14 15 16
1 2 3 4 8 7 6 5 12 11 10 9 16 15 14 13
```

`joc.out`
```
2 1
```

## Explanation

The illustration of the game rounds until a winner is identified is as follows:

~[joc2.png|align=center|width=60em]

# Example 2

`joc.in`
```
2
4 4
16 13 15 9 10 1 5 2 6 14 3 7 11 4 8 12
1 2 3 4 5 6 7 8 12 11 10 9 13 14 15 16
1 5 9 6 2 7 3 8 4 10 11 12 13 14 15 16
1 2 3 4 8 7 6 5 12 11 10 9 16 15 14 13
```

`joc.out`
```
14
```

## Explanation

Only $3$ out of the $4$ rounds played were won. Until winning the first round, $7$ marks were made, in the second $14$, and in the third $8$. Therefore, the maximum number of marks made until winning a round is $14$.