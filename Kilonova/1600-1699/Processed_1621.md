
A colony of $N$ ants has started to systematically explore the territory around the anthill. The ants move only to the right or down. This part of the territory has been divided into areas arranged in rows and columns in the form of a matrix with $NX$ rows and $NY$ columns.

The ants begin their exploration one by one from the top-left cell of the matrix. They move alternately: the first to the right, the second down, the third again to the right, and so on. They proceed in the same manner in each cell of the matrix they reach, guided by the pheromones left by the other ants. Thus, the first ant to reach a cell continues its path to the right cell, the second ant that reaches the same cell goes down, the third again to the right, and so on. The ants move in this way until they exit the matrix.

# Task

What area of the matrix remains unexplored if $N$ ants start from the anthill.

# Input data

The input file `explorare.in` contains on the first line the natural number $N$. The second line of the file contains two natural numbers representing $NX$ and $NY$.

# Output data

The output file `explorare.out` will contain a natural number representing the area of the territory that remains unexplored.

# Constraints and clarifications

* $1 \leq N \leq 10^9$
* $1 \leq NX, NY \leq 10^5$

# Example

`explorare.in`
```
4
5 6
```

`explorare.out`
```
7
```

## Explanation

The file will contain the number $7$, this being the number of cells not visited by any of the $4$ ants. The paths followed by the ants are the following:

~[explorare.png]
```
