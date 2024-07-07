
Let's consider a game board consisting of $N \times N$ squares organized in the form of a matrix with $N$ rows and $N$ columns. In each square, a natural number is written. At the start of the game, there is a pawn in the upper-left corner of the board. This pawn must reach the lower-right corner of the board. In one move, the pawn can move from its current position $(x, y)$ either to the square below $(x+1, y)$ (same column, next row) or to the square to the right of its position $(x, y+1)$ (same row, next column), but it cannot be placed in a square that contains the value $0$. The path of a pawn consists of all the squares through which the pawn passes to get from the upper-left corner to the lower-right corner of the board. The cost of a path is defined as the product of the numbers in the squares on the path. The cost of a path is optimal if the number of zeros at the end of its writing in base $10$ is minimal.

# Task

Write a program that determines the number of zeros at the end of the optimal cost.

# Input data

The input file `zero.in` contains the first line with the natural number $N$ representing the size of the game board. Each of the following $N$ lines contains $N$ natural numbers separated by a space representing the game board.

# Output data

The output file `zero.out` will contain a single line which will print the number of zeros at the end of the optimal cost.

# Constraints and clarifications

* $1 \leq N \leq 500$
* The game board contains natural numbers less than or equal to $1 \ 000 \ 000$.
* For the test data, there is always a solution.

# Example

`zero.in`
```
4 
1 3 0 0 
0 8 2 25 
6 5 0 5 
0 15 7 4
```

`zero.out`
```
2
```

## Explanation

The optimal path goes through $1, 3, 8, 5, 15, 7, 4$. 
The product of the elements on this path ends with two zeros. 
Another solution to reach the lower-right corner would have been $1, 3, 8, 2, 25, 5, 4$, but the number of zeros at the end of the product of the elements on this path is $3$.
