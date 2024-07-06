Sure, here is the translated problem statement:

---

Jerry the mouse is (once again?) in the labyrinth. The labyrinth can be encoded as a matrix with $n$ rows and $m$ columns consisting of $n \cdot m$ identical square cells. The rows are numbered from $1$ to $n$, and the columns from $1$ to $m$. The labyrinth is made up of free cells and cells occupied by the walls of the labyrinth.

At the initial moment, Jerry is in a certain free cell and his mission is to reach another specified free cell. The mouse can move from the current cell to any of the four cells sharing a side with it and cannot exit the labyrinth. It is possible that he cannot reach the final position from the initial position through free cells only. In this situation, he needs to break the wall in certain cells. Jerry has prepared dynamite for this purpose, since he does not think it is optimal to gnaw through the wall with his teeth.

# Task

Knowing the dimensions $n$ and $m$ of the labyrinth, the coordinates of the starting cell and the destination cell, as well as the coordinates of the cells occupied by walls, determine the minimum number of occupied cells that Jerry needs to dynamite to reach his destination.

# Input data

The input file `labir.in` contains on the first line two natural numbers $n$ and $m$ separated by a space, representing the number of rows and the number of columns of the matrix encoding the labyrinth. The second line contains four natural numbers $x_i$, $y_i$, $x_f$, $y_f$ separated by a space, representing the starting position and the destination position. The third line contains a natural number $k$, representing the number of occupied cells. On each of the next $k$ lines, there will be found two numbers $x$ and $y$ separated by a space, representing the row and column of an occupied cell.

# Output data

The first line of the file `labir.out` will contain a single natural number $D$, representing the minimum number of cells that Jerry needs to dynamite to reach his destination.

# Constraints and clarifications

* $2 \leq n, m \leq 5 \ 000$
* $1 \leq k \leq 50 \ 000$
* It is guaranteed that for all tests there are at least $\\frac{n}{2}$ rows and/or $\\frac{m}{2}$ columns made only of unoccupied cells.
* For $30\%$ of the tests $n, m \leq 1 \ 000$

# Example

`labir.in`
```
7 8
1 1 7 8
6
2 1
1 2
3 1
6 7
6 8
6 2
```

`labir.out`
```
1
```

## Explanation

~[labir.png]

The occupied cells have been colored gray. The mouse starts from the cell marked with $P$ and arrives in the cell $S$. For this, he dynamites the cell $(1, 2)$ and reaches $S$ by dynamiting a minimum number $D = 1$ of occupied cells.

---

Please let me know if you need further assistance or if any modifications are required.