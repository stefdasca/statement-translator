Irinuca has discovered a new computer game. On the screen, $n$ colored balls are placed in a line. The colors of the balls are encoded with natural numbers. A subsequence of adjacent balls all having the same color is called a sequence. A sequence will contain the maximum number of adjacent balls having the same color. The length of a sequence is equal to the number of balls it is composed of.

Irinuca has a special bow. By shooting an arrow at one of the balls, if it is part of a sequence of length at least $3$, the entire sequence will be eliminated, and the balls to the right of the sequence will shift left to fill the "gap" left by the eliminated balls. If there are two sequences of the same color immediately to the left and right of the eliminated sequence, and the sequence obtained by merging these sequences has a length of at least $3$, it will be eliminated as well. The process continues until the sequences to the left and right of an eliminated sequence have different colors or until the length of the sequence obtained by merging is less than $3$ or until there are no more balls to the left or right of an eliminated sequence or until all the balls on the screen are eliminated.

The goal of the game is to eliminate as many balls as possible from the screen. Since Irinuca is still not very good at this game, she has established a strategy. She will always shoot an arrow at a ball that is part of the longest sequence on the screen. If there are multiple such sequences, she will choose the leftmost sequence of maximum length. If all the sequences on the screen have lengths less than $3$, Irinuca will no longer be able to eliminate any of them and the game ends.

**For example**, if the initial sequence of balls is
`5 1 3 3 2 2 2 2 3 1 1 5 6 4 4 4 4 7`
Irinuca will act on a ball of color $2$. After elimination, the sequence of balls obtained is
`5 1 3 3 3 1 1 5 6 4 4 4 4 7`
from which the sequence of balls of color $3$ is also eliminated, obtaining the sequence of balls
`5 1 1 1 5 6 4 4 4 4 7`
from which the sequence of color $1$ is also eliminated.
`5 5 6 4 4 4 4 7`
Since the sequence of balls of color $5$ is not long enough, it will not be eliminated. Now Irinuca shoots at a ball of color $4$ and obtains
`5 5 6 7`
but since the sequences to the left and right of the eliminated sequence are of different colors, no more sequences will be eliminated. The game ends because there are no more sequences of length at least $3$ to shoot at.

# Task
Knowing the number of balls and the colors of each ball on the screen, determine:
1. The number of sequences of balls that were initially on the screen.
2. The number of balls that remain uneliminated on the screen and the colors of the remaining balls in order on the screen at the end of the game.

# Input data
The input file `arc.in` contains on the first line a natural number $V$. For all input tests, the number $V$ can have only the value $1$ or $2$.
The second line contains a natural number $n$ representing the number of balls, and the third line contains $n$ natural numbers $c_1$, $c_2$, $\\dots$, $c_n$ separated by spaces, representing the colors of the $n$ balls on the screen.

# Output data
If the value of $V$ is $1$, **only point 1** of the task will be solved.
In this case, the output file `arc.out` will contain a single natural number $n_1$, representing the number of sequences of balls initially on the screen.

If the value of $V$ is $2$, **only point 2** of the task will be solved.
In this case, the output file `arc.out` will contain on the first line a single natural number $n_2$, representing the number of balls that remain uneliminated on the screen at the end of the game, and on the next $n_2$ lines a number that represents the colors of the uneliminated balls in order at the end of the game.

If at the end of the game no uneliminated balls remain, the output file will contain the value $0$ on its first line.

# Constraints and clarifications
- $1 \\leq n \\leq 10\\ 000$
- $1 \\leq c_1, c_2, \\dots, c_n \\leq 100\\ 000$
- For correctly solving point 1, 20 points are awarded, and for point 2, 80 points are awarded.

# Example 1
`arc.in`
```
1
18
5 1 3 3 2 2 2 2 3 1 1 5 6 4 4 4 4 7
```
`arc.out`
```
10
```

## Explanation

**$V = 1$, so only point 1 is solved for this test.**
The sequences are $(5)$, $(1)$, $(3,3)$, $(2,2,2,2)$, $(3)$, $(1,1)$, $(5)$, $(6)$, $(4,4,4,4)$, $(7)$.

# Example 2

`arc.in`
```
2
18
5 1 3 3 2 2 2 2 3 1 1 5 6 4 4 4 4 7
```
`arc.out`
```
4
5
5
6
7
```

## Explanation
**$V = 2$, so only point 2 is solved for this test.**

# Example 3

`arc.in`
```
2
15
1 2 2 2 2 1 1 3 3 3 4 4 4 4 3
```
`arc.out`
```
0
```

## Explanation
**$V = 2$, so only point 2 is solved for this test.**