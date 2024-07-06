After graduating from college, Ionică became a construction engineer and wants to get a job in his hometown. After studying the job offers, he finds an engineer position at the City Hall. To occupy this position, he needs to pass a theoretical test. For this test, he must create a project to pave the town square.

The square has the shape of a rectangle and is drawn on a grid, so it can be represented as a two-dimensional array with $n$ rows and $p$ columns. Each element of the matrix corresponds to a square with a side length of $1 \\ \\text{m}$. Paving can be done using tiles of two types:
Type `F`:
~[pavare1.png|align=center]
Type `I`:
~[pavare2.png|align=center]
Notice that a type `F` tile is formed from $6$ squares with a side length of $1 \\ \\text{m}$, arranged in the shape of the letter `F` (thus covering an area of $6 \\ \\text{m} ^ 2$), while a type `I` tile is formed from two squares with a side length of $1 \\ \\text{m}$ (thus having an area of $2 \\ \\text{m} ^ 2$).
Paving the square means covering each $1 \\ \\text{m}$ side square of the square with exactly one tile. The tiles can be rotated and used on any side.
The constraint imposed by the mayor is that the area of the square paved with type `F` tiles must have the same area as that paved with type `I` tiles.
To visualize the paving method of the square, Ionică will number the tiles with consecutive natural numbers starting from $1$. The number associated with a tile will be written in each square of the square covered by that tile.

# Task

Write a program to determine a paving method for the square that respects the above conditions.

# Input data

The input file `pavare.in` will contain on the first line two natural numbers separated by space $n \\ p$ representing the number of rows and the number of columns of the matrix, respectively.

# Output data

The output file `pavare.out` will contain $n$ rows, each row containing $p$ natural numbers separated by a space. The values written in the output file are the numbers associated with the tiles that cover the $n \\times p$ squares of the square.

# Constraints and clarifications

* $3 \\leq n, p \\leq 150$
* The product $n \\cdot p$ is a multiple of $24$.
* The solution is not unique; any solution can be shown.

# Example

`pavare.in`
```
6 4
```

`pavare.out`
```
7 7 8 8
1 1 2 2
1 3 3 2
1 1 2 2
1 4 4 2
5 5 6 6
```

## Explanation

We paved a square with $6$ rows and $4$ columns, having an area of $24 \\ \\text{m} ^ 2$. For paving, $8$ tiles were used ($2$ type `F` tiles covering an area of $2 \\cdot 6 = 12 \\ \\text{m} ^ 2$ and $6$ type `I` tiles, covering the rest of the square, also having an area of $12 \\ \\text{m} ^ 2$). The output file corresponds to the paving:
~[pavare3.png|align=center]