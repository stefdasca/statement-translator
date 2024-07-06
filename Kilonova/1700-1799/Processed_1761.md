```
Ionică and Gigel are playing a game with $N$ pieces numbered from $1$ to $N$, which are placed in some order on a board in the form of a sequence. Gigel arranges the pieces on the board and Ionică has to guess their order using as few questions as possible. In one question, Ionică specifies a number of positions on the board where he wants to know the pieces. Gigel responds by specifying the set of values placed at those positions, but does not tell which value corresponds to which position. The positions of the board are numbered from $1$ to $N$.

# Task

Given the number $N$ of pieces, determine the minimum number of questions needed to identify the order of the pieces on the board, no matter what the order is.

# Input data

In the file `game.in`, the first line contains the non-zero natural number $N$.

# Output data

In the file `game.out`, the first line contains a number $K$ representing the minimum number of determined questions. The following $K$ lines in the file encode the questions. Each question contains a string of distinct natural numbers, representing the positions targeted in the current question. Each of these $K$ lines ends with the value $0$. The numbers in a line are separated by a space.

The problem allows multiple solutions. In the output file, the order of writing the positions within a question does not matter.

# Constraints and clarifications

* $1 \leq N \leq 450\ 000$;

# Example

`game.in`
```
5
```

`game.out`
```
3
2 3 0
4 3 0
5 0
```

## Explanation

The first and second questions surely determine the value of the piece at position $3$.
Knowing this value and the answer to the first question, it is possible to establish exactly which piece is at position $2$.
Similarly, based on the answer to the second question, it is possible to determine the value of the piece at position $4$.
After the first two questions, the pieces at the first and last positions remain undecided.
The last question determines the value of the piece at position $5$, so implicitly the value of the piece at the first position can also be determined.
```