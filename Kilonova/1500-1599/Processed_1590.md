Two kids want to play a game with two pawns and a board consisting of $N$ squares numbered from $1$ to $N$, arranged consecutively in a single line. The game has the following rules:

* The pawns are placed on the first square of the board (each child has their own pawn);
* The first child is the one who starts the game;
* The children take turns coming to the game board;
* Whoever is at their turn makes one or more moves forward according to the rule below, before yielding their turn to the other:
   * Calculate a value $X$ in the manner described below;
   * Move their pawn forward by $X$ positions and if the calculated value $X$ is $6$, they have the right to calculate another value of $X$, meaning another move, not yielding their turn to the other child yet, and if the value $X$ is different from $6$, they yield the turn;
* $X$ is calculated according to the rule:
   * If the move number is odd, then:
     $$
     X = (\text{move\_number} + ((\text{pawn\_position} + N) \mod 10)) \mod 6 + 1
     $$
   * If the move number is even, then:
     $$
     X = ((((\text{move\_number} + 1) \mod 5) + ((\text{pawn\_position} + N) \mod 10)) \mod 6) + 1
     $$
   where $N$ is the number of squares on the game board, $\text{move\_number}$ signifies the move count, $\text{mod}$ is the operation resulting in the remainder from the integer division of two numbers, and the resulting value, $X$, is one of the digits $1$, $2$, $3$, $4$, $5$, or $6$, as deduced from the above formulas.
* After advancing, if a pawn reaches a square currently occupied by the other pawn, it takes its place, and the pawn which was occupying the square is sent back to square number $1$ (this return to position $1$ is not counted as a move);
* If after advancing, a pawn would reach outside the game board, it is placed on square $N$ (the last square);
* The child who first reaches the pawn to square $N$ of the board wins, and the game ends.

# Task

Given the number $N$, determine:
* The number of divisors of $N$;
* The maximum number of occurrences of any calculated value during the game using the given formulas;
* The squares occupied, during the game, by the winning pawn in the order they were visited.

# Input data

The first line of the file `joc.in` contains two natural numbers, $C$ and $N$ separated by a space. If $C=1$, then only the first task is solved, if $C=2$, then only the second task is solved, and if $C=3$, then only the third task is solved.

# Output data

The file `joc.out` contains:
If $C=1$ or $C=2$, it contains a natural number representing the answer to the respective task. If $C=3$, it contains a series of natural numbers, separated by spaces, representing the answer to the third task.

# Constraints and clarifications

* $2 \leq N \leq 10 \ 000$;
* For tests worth $23$ points, $C=1$.
* For other tests worth $33$ points, $C=2$.
* For other tests worth $44$ points, $C=3$.
* It is guaranteed that there exists a winner.
* During the game, children can reach squares they have visited before.
* It is guaranteed that the number of squares occupied by children is less than $100 \ 000$.
* The problem does not follow finding any special properties for the sequences of values calculated using the given formulas.

# Example 1

`joc.in`
```
1 10
```

`joc.out`
```
4
```

## Explanation

$C=1$ so the first task is solved. $N=10$ has $4$ divisors.

# Example 2

`joc.in`
```
2 10
```

`joc.out`
```
2
```

## Explanation

- Both pawns are on square $1$. In the adjacent images, the first child has the red pawn and the second child has the green pawn.
~[joc-1.png|width=23em]
- The first child moves (their pawn is on square $1$); it is the first move (odd number); the digit for moving the pawn is calculated: $X = (1 + (1 + 10) \text{ mod } 10) \text{ mod } 6 + 1 = 3$; the first player moves the pawn from square $1$ to square $4$.
~[joc-2.png|width=23em]
- The second child moves (their pawn is on square $1$); it is the second move (even number); the digit for moving the pawn is calculated: $X = ((((2 + 1) \text{ mod } 5) + ((1+10) \text{ mod } 10)) \text{ mod } 6) + 1 = 5$; the second child moves the pawn from square $1$ to square $6$.
~[joc-3.png|width=23em]
- The first child moves (their pawn is on square $4$); it is the third move (odd number); the digit for moving the pawn is calculated: $X = (3 + (4 + 10) \text{ mod } 10) \text{ mod } 6 + 1 = 2$; the first child moves the pawn from square $4$ to square $6$; as the second child’s pawn is on square $6$, it is sent back to square $1$, so the second child’s pawn now occupies square $1$.
~[joc-4.png|width=23em]
- The second child moves (their pawn is on square $1$); it is the fourth move (even number); the digit for moving the pawn is calculated: $X = ((4 + 1) \text{ mod } 5 + (1 + 10) \text{ mod } 10) \text{ mod } 6 + 1 = 2$; the second child moves the pawn from square $1$ to square $3$.
~[joc-5.png|width=23em]
- The first child moves (their pawn is on square $6$); it is the fifth move (odd number); the digit for moving the pawn is calculated: $X = (5 + (6 + 10) \text{ mod } 10) \text{ mod } 6 + 1 = 6$; the first child moves the pawn from square $6$ to square $10$ (it should move to square $12$ which is outside the game board) the digit is $6$; the child is entitled to another move but has already reached the final square with the pawn and the game ends.
~[joc-6.png|width=23em]

The first child is the winner. The calculated digits were, in order, $3\ 5\ 2\ 2\ 6$, and the digit $2$ appeared the most, namely $2$ times.

# Example 3

`joc.in`
```
3 10
```

`joc.out`
```
1 4 6 10
```

## Explanation

$C = 3$ so the third task is solved. The first child is the winner, having occupied the squares in this order: $1\ 4\ 6\ 10$.