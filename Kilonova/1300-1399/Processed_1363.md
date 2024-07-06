~[joc.png|align=right]
Rareș and Bogdan want to exercise outdoors, so they came up with a new game. On the football field, they drew a circular track and divided it into $n$ equal sectors, as shown in the adjacent image (where $n = 16$). They labeled the $n$ sectors with distinct numbers from $1$ to $n$, in a clockwise direction.
They decided that the game would be played as follows:

* Both will start in the sector numbered $1$, back to back, so that Bogdan will move in a clockwise direction, and Rareș in the opposite direction.
* Through simultaneous jumps to certain sectors, the children will move on the track in opposite directions and will make an equal number of jumps.
* A jump by Bogdan will result in moving from the current sector, in a clockwise direction, advancing by $x$ sectors on the track. For example, if $n = 16$ and $x = 2$, then starting from sector $1$, Bogdan will move by successive jumps, in this order, to the sectors labeled: $3, 5, 7, 9, \dots$
* A jump by Rareș will result in moving from the current sector, in a counterclockwise direction, advancing by $y$ sectors on the track. For example, if $n = 16$ and $y = 3$, then starting from sector $1$, Rareș will move by successive jumps, in this order, to the sectors: $14, 11, 8, 5, \dots$
* The game ends when the two children reach the same sector on the track as a result of their jumps or if one of the two children reaches the same sector for the second time.

# Task

Write a program that reads the three non-zero natural numbers $n$, $x$, and $y$, and then determines:
a) the number $t$ of sectors on the track through which neither of the two children pass as a result of the jumps made until the end of the game
b) the number $s$ of jumps made by each child until the end of the game
c) the labels $b$ and $r$ of the sectors where the two children end up at the end of the game (Bogdan ends up at the end of the game in the sector labeled $b$, and Rareș in the sector labeled $r$).

# Input data

The input file `joc.in` contains on the first line three natural numbers $n$, $x$, and $y$, separated by a space, with the significance given in the problem statement.

# Output data

The output file `joc.out` will contain on the first line the four natural numbers determined by the program: $t$, $s$, $b$, and $r$, separated by a space, in this order, with the significance given in the problem statement.

# Constraints and clarifications

* $16 \leq n \leq 40\ 000$
* $1 \leq x < n$
* $1 \leq y < n$
* for correct solving of the first task, $20\%$ of the score is awarded, for correct solving of the second task $40\%$ of the score is awarded, and for correct solving of the third task $40\%$ of the score is awarded ($20\%$ for correctly determining the value $b$, and $20\%$ for correctly determining the value $r$).

# Example 1

`joc.in`
```
16 2 3
```

`joc.out`
```
4 8 1 9
```

## Explanation

The two children, performing simultaneous jumps, pass until the end of the game, through the sectors:

| Bogdan | Rareș |
| ------ | ----- |
| 1 | 1 |
| 3 | 14 |
| 5 | 11 |
| 7 | 8 |
| 9 | 5 |
| 11 | 2 |
| 13 | 15 |
| 15 | 12 |
| 1 | 9 |

The game ends after $s = 8$ jumps because Bogdan reaches the sector labeled $b = 1$ again. At the end of the game, Rareș is in the sector labeled $r = 9$. The two children did not pass through $t = 4$ sectors whose labels are: $4$, $6$, $10$, $16$.

# Example 2

`joc.in`
```
16 6 2
```

`joc.out`
```
12 2 13 13
```

## Explanation

The two children, performing simultaneous jumps, pass until the end of the game, through the sectors:

| Bogdan | Rareș |
| ------ | ----- |
| 1 | 1 |
| 15 | 7 |
| 13 | 13 |

The game ends after $s = 2$ jumps because Bogdan and Rareș both reach the sector labeled $b = r = 13$. The two children did not pass through $t = 12$ sectors whose labels are: $2$, $3$, $4$, $5$, $6$, $8$, $9$, $10$, $11$, $12$, $14$, $16$.