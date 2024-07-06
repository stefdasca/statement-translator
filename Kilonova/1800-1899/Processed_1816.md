In anticipation of the great confrontation with the Turks, the Moldovan soldiers are training their minds by playing a team game called "_Bârligă!_" A team has $N$ players, numbered from $1$ to $N$, in the order they are seated. Each player receives a plank painted on one side red, and on the other side yellow. On each plank, all natural numbers from $1$ to $V$ are written, each number appearing only once; some numbers are written on the red side, and the others are written on the yellow side of the plank. At the beginning of the game, all planks are placed with the red side up. When the first player shouts "_Bârligă!_", every player in the team can decide whether to leave their plank with the red side up or to flip it (to "bârlige") with the yellow side up. The score obtained by the team is equal to the number of distinct visible values at the end.

# Task

Write a program that knows $N$, the number of players in the team, as well as the values written on the red side of the plank received by each player, and determines the maximum score the team can achieve, as well as the player numbers who need to flip their planks to the yellow side up, to obtain this maximum score.

# Input data

The input file `barliga.in` contains on the first line the natural numbers $N$ and $V$, with the meaning as described. On the following $N$ lines are the pieces of information about the planks of the $N$ players, in the order from $1$ to $N$. The line describing a plank has the form $nr \ r_1 \ r_2 \dots \ r_{nr}$, meaning: "on the red side of the plank are written $nr$ distinct natural numbers between $1$ and $V$; these are $r_1$, $r_2$, $...$, $r_{nr}$".

# Output data

The output file `barliga.out` will contain on the first line a natural number representing the maximum score the team can achieve. On the second line, it will contain a natural number $T$, representing the number of players who need to flip their plank to the yellow side up, followed by $T$ distinct natural numbers between $1$ and $N$, representing the player numbers who need to flip their plank to the yellow side up.

# Constraints and clarifications

* $2 \le N \le 16$
* $3 \le V \le 80\ 000$
* The values on the same line in the input file or in the output file are separated by a single space.
* If there are multiple solutions for the team to achieve the maximum score, any of them will be displayed.
* The score on the test is obtained if both the maximum score and a way to achieve the maximum score are displayed correctly.
* For tests worth $8$ points, $N \leq 6$ and $V \leq 100$
* For tests worth $18$ points, $10 \leq N \leq 12$ and $V \leq 4500$
* For tests worth $74$ points, there are no other constraints.

# Example

`barliga.in`
```
2 10
3 7 5 10
4 1 5 10 2
```

`barliga.out`
```
9
1 1
```

## Explanation

There are two planks, with each containing natural numbers from $1$ to $10$.

On plank $1$, the red side has $3$ values $(7, 5, 10)$, and the other $7$ values are written on the yellow side $(1, 2, 3, 4, 6, 8, 9)$.

On plank $2$, the red side has $4$ values $(1, 5, 10, 2)$, and the other $6$ values are written on the yellow side $(3, 4, 6, 7, 8, 9)$.

The maximum score that can be obtained is $9$.

One way to obtain the maximum score is by flipping plank number $1$ to the yellow side up. Thus, the numbers $1, 2, 3, 4, 6, 8, 9$ become visible on plank $1$, and the numbers $1, 2, 5, 10$ remain visible on plank $2$, totaling $9$ distinct numbers.