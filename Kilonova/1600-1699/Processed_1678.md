~[smin.png|align=right]

Ana has a new game. On a square board there is a grid made up of square cells of size $1$. In any of the corners of any cell, Ana can stick a peg perpendicular to the board. After placing $n$ pegs, Ana takes from a box (with a sufficiently large number of circular elastic strings) one string with which she surrounds three or more pegs. Each string is well stretched and forms a polygonal contour on the board.

In the adjacent figure, a string is used that forms a polygonal contour with $4$ sides which surround $5$ of the $8$ pegs on the board. The game ends when enough strings have been placed so that all the pegs on the board are on the edge or inside at least one of the polygonal contours formed. The goal of the game is that the placement of the strings is done conveniently so that the total area of the formed polygonal contours is minimized.

~[smin2.png]

# Task

Given the coordinates of the $n$ pegs ($x_1$, $y_1$), ($x_2$, $y_2$), $\dots$, ($x_n$, $y_n$) measured from one of the grid corners, Ana wants to find the minimum sum of the areas of the polygonal contours formed by conveniently placing the strings, so that each peg is inside or on the contour of at least one such polygon.

# Input data

In the file `smin.in`, the first line contains the natural number $n$. Each of the next $n$ lines contains two natural numbers: $x \\ y$.

# Output data

In the file `smin.out`, the number $s$, representing the minimum sum of the areas of the convex polygons covering all the given points, will be printed.

# Constraints and clarifications

* $3 \leq n \leq 17$
* $0 \leq x, y \leq 100$
* Input data will not contain three pegs placed in collinear points on the board.
* The requested sum is obtained by summing the areas of all polygons, regardless of whether some polygons overlap or not.
* The absolute difference between the real value of $s$ and the displayed value is less than $0.001$.

# Example 1

`smin.in`
```
4
0 2
0 4
4 4
4 2
```

`smin.out`
```
8.000
```

## Explanation

The minimum area is the rectangle from the first figure, with the four pegs at the corners. A single elastic string is used.

# Example 2

`smin.in`
```
4
0 2
2 4
3 4
4 1
```

`smin.out`
```
2.500
```

## Explanation

The minimum area is the sum of the areas of the two triangles bounded by two elastic strings from the second figure.

