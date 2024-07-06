~[flori0.png|align=right]

For the upcoming spring, the company responsible for arranging the green space in the center of Slatina aims to plant rows of flowers arranged diagonally, with each plot having a different number of flowers. The irrigation of the flowers is done with a pump that moves around the green space, starting from the top right corner, moving counterclockwise. The rows are numbered with $1$, $2$, $3$, $\dots$ starting from the top right corner, following the pump movement direction. When watering a row of flowers, an amount of water equal to the number of flowers in that row is pumped.

The water flow in the pumping system can remain constant, can be increased, but cannot be decreased. A row of flowers can only be watered if it has a number of flowers greater than or equal to the last watered row, except for the first row chosen to be watered. Any row of flowers can be watered at most once, at either of its ends. The water stops upon returning to the starting corner.

# Task

Given a matrix with $n$ rows and $m$ columns, where each element represents the number of flowers in a plot, determine the maximum number of flowers that can be watered by a complete rotation of the pump around the green space. Among the determined solutions, find the one with the minimum number of rows with flowers, as well as the row indices of the watered rows, following the order in which they were watered.

# Input data

The input file `flori.in` contains:
* The first line contains the natural numbers $n$ and $m$ representing the number of rows and the number of columns of the matrix, respectively.
* Each of the next $n$ lines contains $m$ non-zero natural numbers separated by a space, representing the number of flowers in each plot of the respective row in the matrix.

# Output data

The output file `flori.out` will contain:
* The first line contains the maximum number of flowers that can be watered.
* The second line contains the minimum number of watered rows.
* The third line contains the indices of the watered rows in the order they were watered, separated by a space.

# Constraints and clarifications

* $0 < n,m \leq 900$;
* $0$ < number of flowers in a plot $\leq 60\ 000$
* For correctly solving the first task, $40\%$ of the score is awarded, and for correctly solving the first two tasks, $60\%$ of the score is awarded.

# Example

`flori.in`
```
5 6
2 1 3 5 2 3
3 4 5 6 4 3
2 3 6 3 4 9
1 2 7 2 5 1
10 5 14 10 10 3
```

`flori.out`
```
104
7
1 2 4 5 8 7 6
```

## Explanation

While moving along the first horizontal edge of the flower bed, rows $1$, $2$, $4$ and $5$ are watered, rows $8$ are watered while moving along the first vertical edge, and rows $7$ and $6$ are watered while moving along the bottom edge of the bed.

~[flori.png]