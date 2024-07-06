Maria received a puzzle box for her birthday, containing pieces labeled with natural numbers. To solve it, she needs to stick together as many pieces as possible in the order they are drawn from the box, forming groups of pieces.

Two puzzle pieces can be stuck together if the numbers on their labels have at least three digits in common. When two pieces are stuck together, a group is formed with a number label obtained by concatenating the first four digits of the first piece's label with the last four digits of the second piece's label (if the labels don't have at least four digits, only the existing digits are used without adding others). A piece can be stuck to another piece or an existing group of pieces (if it exists), or it can form a group on its own.

For example, if the labels have the numbers $133454$ and $3523143$, they can be stuck together because they share five digits (one digit $1$, two digits $3$, one digit $4$, and one digit $5$). As a result of sticking, a group is formed with the label $13343143$.

To solve the puzzle, Maria draws pieces one by one from the box. If a piece can be stuck to the last formed group, she sticks it and updates the group's label; otherwise, she puts aside that group and starts forming a new group with the drawn piece.

After forming the groups, Maria chooses group labels in the following order: first, she chooses the label with the maximum number of distinct digits. If there are multiple, she chooses the one with the smallest value. Among the remaining labels, she chooses the next label following the same rule. She continues this process until she has chosen $K$ labels.

# Task

Knowing the $N$ natural numbers found on the labels of the puzzle pieces in the order they are drawn from the box, determine:

1. The number of groups Maria obtains after solving the puzzle;
2. The $K$ numbers on the labels of the groups chosen by Maria.

# Input data

In the file `puzzle.in` the first line contains, separated by a space, $C$, $N$, and $K$, where $C$ represents the task to be solved, $N$ the number of pieces in the game, $K$ the number of values required for task $2$. On the next line, separated by a space, are the $N$ numbers on the labels of the puzzle pieces, in the order they are drawn from the box.

# Output data

If the task is $1$, the output file `puzzle.out` will contain on the first line a natural number $G$, representing the number of groups obtained after completing the game.

If the task is $2$, on the first line of the output file `puzzle.out` will be written, separated by a space, the $K$ numbers on the labels of the groups chosen by Maria.

# Constraints and clarifications

* $1 \leq C \leq 2$
* $1 \leq N \leq 100 \ 000$
* $1 \leq K \leq 10$
* The numbers on the labels of the pieces are natural numbers with at most nine digits;
* For all test data, a solution exists.

| # | Score | Constraints |
|---|-------|-------------|
| 1 | 53    | $C = 1$     |
| 2 | 7     | $C = 2$, $K = 1$ |
| 3 | 13    | $C = 2$, $K = 2$ |
| 4 | 27    | $C = 2$, $K > 2$ |

# Example 1

`puzzle.in`
```
1 6 1
13345 23143 4343 784532 432 7826
```

`puzzle.out`
```
2
```

## Explanation

The piece with the label $13345$ can be stuck with the piece with the label $23143$, thus obtaining a group with the label $13343143$ which can be stuck with the piece with the label $4343$ obtaining $13344343$ that can no longer be stuck with the next piece with the label $784532$, but this piece will be stuck with the piece labeled $432$ and we obtain $7845432$ which can then be stuck with the piece $7826$ forming the second group with the label $78457826$.

# Example 2

`puzzle.in`
```
2 6 1
13345 23143 4343 784532 432 7826
```

`puzzle.out`
```
78457826
```

## Explanation

After grouping the pieces, we obtain two groups labeled $13344343$ and respectively $78457826$. Among these, $78457826$ has $6$ distinct digits, while $13344343$ has only $3$ distinct digits. Therefore, the desired value is $78457826$.