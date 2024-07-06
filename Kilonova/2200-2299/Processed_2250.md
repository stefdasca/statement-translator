# Task

JellyTheOctopus is ready to try today's puzzle from the New York Times! Just for him, the sudoku proposers have created a new difficulty level, "Impossible", alongside the well-known "Easy", "Medium" and "Hard".

The usual rules of Sudoku are as follows: a $9$ x $9$ board is given, divided into $9$ squares of $3$ x $3$. You must place the numbers from $1$ to $9$ on each row, column, and square so that each number appears only once. However, today's puzzle has some minor changes. Instead of a $9$ x $9$ puzzle, we have a $N$ x $N$ puzzle, divided into squares of $3$ x $3$ ($N$ is divisible by $3$).

Due to the new matrix structure, some numbers may already repeat on a row or column. However, the new numbers placed by Jelly must follow the usual rules mentioned above. You can see here an image with a regular Sudoku board.

~[sudoku.png|align=center]

As the name suggests, it's highly likely this puzzle is impossible to solve. Thus, Jelly has created a new challenge for himself. As we all know, $8$ is the luckiest number, and Jelly wants to find the "luck" of the grid. Given an $N$ x $N$ board, find all positions where Jelly can place a single $8$.

Jelly will write only one number. If he places $8$ in a different position, he will erase it from the grid before considering other positions where he can place $8$.

The luck of the grid is calculated as the number of positions where he can place a single $8$. Help Jelly find this number before NYT publishes their next Impossible Sudoku puzzle!

# Input data

The first line will contain $N$ and $M$, the number of already occupied positions.

The following lines will contain the coordinates where we have already placed numbers, along with the placed number.

# Output data

The first line will print the luck of the grid received by Jelly as part of today's Impossible Sudoku puzzle from the New York Times.

# Constraints and clarifications

* $3 \leq N \leq 2 \cdot 10^5$;
* $N$ is divisible by $3$;
* $0 \leq M \leq \min(2 \cdot 10^5, N^2)$;
* $0 \leq x, y < N$;
* $1 \leq digit \leq 9$;

|#|Points|Constraints|
|-|-|--------|
|0|0|Example|
|1|6|$M = 0$|
|2|22|$1 \leq n \leq 200$|
|3|35|$1 \leq n \leq 2 \ 000$|
|4|37|No additional constraints|

# Example

`stdin`
```
9 7
1 7 8
3 2 1
4 7 3
1 0 5
8 7 4
2 4 9
3 4 6
```

`stdout`
```
57
```

## Explanation

In the example sudoku, he cannot place an $8$ on the already filled squares, or any other square located on row $1$ or column $7$.