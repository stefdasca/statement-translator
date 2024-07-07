A swampy area has a rectangular shape with $n_l$ rows and $n_c$ columns. It is made up of cells with a unit side. Some of these represent land, while others represent water, with land coded as $0$ and water as $1$. The goal is to find a path from the north shore to the south shore, passing only through land. Water cells can be transformed into land by dropping a pontoon (a raft) the size of a cell onto a water cell. Since parachuting is dangerous, we want to minimize the number of parachuting operations. Movement can be made one cell at a time on the row, column, or diagonally.

# Task:

Write a program that determines the minimum number of pontoons and their coordinates.

# Input data:

The file `lac.in` has the following structure:

* the first line contains two natural numbers $n_l$ and $n_c$ separated by a space, representing the number of rows and columns of the area;
* the next $n_l$ lines contain $n_c$ binary values separated by spaces, representing the configuration of the area ($0$ for land and $1$ for water).

# Output data

The file `lac.out` will contain the following structure:
* the first line contains a natural number $min$, which represents the required number of pontoons.
* the following $min$ lines contain two natural numbers separated by a space, representing the coordinates of the $min$ pontoons (row and column).

# Constraints and clarifications

* $1 \leq n_l \leq 100$
* $1 \leq n_c \leq 100$
* The solution with the minimum number of pontoons is not unique.
* If there are multiple solutions, only one will be displayed.
* Row and column numbering starts with value $1$.

# Example

`lac.in`
```
8 9
0 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 
1 0 1 1 1 0 1 1 1
1 1 0 0 1 1 0 1 1
1 1 1 1 1 1 1 0 1
1 1 1 1 1 1 1 1 0
1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 0 1 1
```

`lac.out`
```
2
4 5
7 8
