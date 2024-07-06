Sure, here is the translated text:
```markdown
Trio is a game containing $N$ pieces of the same shape, placed next to each other on a game board and numbered from left to right with values from $1$ to $N$. Each piece has three zones marked on it, and in each of them, a digit is written. It is considered that a piece on which the digits $\\text{C1}$, $\\text{C2}$, and $\\text{C3}$ are written in order from left to right has the following properties:

* it is *identical* to another piece if that piece contains exactly the same digits, in the same order as them or in reverse order. So, the piece $\\boxed{\\text{C1|C2|C3}}$ is identical to another piece of the form $\\boxed{\\text{C1|C2|C3}}$ and to a piece of the form $\\boxed{\\text{C3|C2|C1}}$.
* it is *friendly* with another piece if it contains exactly the same digits as the given piece, but not necessarily in the same order. So, the piece $\\boxed{\\text{C1|C2|C3}}$ is friendly with the pieces: $\\boxed{\\text{C1|C2|C3}}$, $\\boxed{\\text{C1|C3|C2}}$, $\\boxed{\\text{C2|C1|C3}}$, $\\boxed{\\text{C2|C3|C1}}$, $\\boxed{\\text{C3|C1|C2}}$ and $\\boxed{\\text{C3|C2|C1}}$. Note that two identical pieces are also friendly!

A group of friendly pieces consists of **all** the friendly pieces with each other present on the game board.

# Task
1) Choose a piece on the game board so that the number $M$ of pieces identical to it is the highest possible and display the determined number $M$;
2) Display the number of groups of friendly pieces present on the game board;
3) Display the maximum number of pieces in a sequence containing pieces placed next to each other on the game board, for which the first piece and the last piece in the sequence are friendly.

# Input data

The file `trio.in` contains:
- the first line contains a natural number $C$ which represents the task number and can have the values $1$, $2$ or $3$.
- the second line contains a natural number $N$ which represents the number of game pieces;
- the following $N$ lines contain three digits, separated by a space, which represent, in order, the digits written on a game piece. The pieces are given in the order of their numbering on the game board.

# Output data

The file `trio.out` will contain a single natural number on the first line that represents the result determined according to each task.

# Constraints and clarifications
* $2 \leq N \leq 100\ 000$;
* There are at least two identical pieces on the game board;
* A piece that is not friendly with any other piece on the game board forms a group by itself;
* For solving task 1, 20 points are awarded, for solving task 2, 30 points are awarded, and for solving task 3, 50 points are awarded.

# Example 1

`trio.in`
```
1
6
1 3 3
4 5 9
1 3 3
9 5 4
3 3 1
9 4 5
```

`trio.out`
```
2
```

## Explanation

~[ex1.png]

Task 1 is solved. By choosing any of the pieces $1$, $3$, or $5$, there are two identical pieces on the board with the chosen piece. By choosing any of the pieces $2$ or $4$, there is only one piece identical to the chosen piece. If we choose piece $6$, there are no identical pieces on the board.

# Example 2

`trio.in`
```
2
6
1 3 3
4 5 9
0 8 0
9 5 4
3 3 1
9 4 5
```

`trio.out`
```
3
```

## Explanation

~[ex2.png]

Task 2 is solved. Pieces $1$ and $5$ form a group of friendly pieces. Pieces $2$, $4$, and $6$ form another group. Piece $3$ forms a group by itself. In total, there are $3$ groups of friendly pieces on the board.

# Example 3

`trio.in`
```
3
6
1 3 3
4 5 9
0 8 0
9 5 4
3 3 1
9 4 5
```

`trio.out`
```
5
```

## Explanation

Task 3 is solved. We identify two sequences of maximum length, equal to $5$, for which the first and last pieces are friendly:

~[ex3_1.png]

~[ex3_2.png]

```

I have translated the text while preserving the formatting and additional instructions you provided. If there are any corrections or additions you would like, please let me know.