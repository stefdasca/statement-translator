Andrei is very good at geometry and that's why he invents all kinds of games that he tests with Alexandru, his desk mate. To prepare the new game with three levels, Andrei draws the xOy Cartesian coordinate system and several distinct points on graph paper. Each drawn point has both the abscissa $x$ and ordinate $y$ as integer numbers.

At the first level, Alexandru determines the maximum number of points (among those drawn) located on one of the axes of the Cartesian coordinate system or on a line parallel to one of the two axes.

At the second level, Alexandru considers all the drawn points whose abscissa $x$ and ordinate $y$ satisfy at least one of the relations $x = y$ or $x + y = 0$, and then calculates how many distinct lines pass through at least two of these points.

At the third level, Alexandru counts and deletes the points every 3rd one (the 1st, the 4th, the 7th, etc.), starting from the leftmost drawn point and continuing to the right. If two or more points have the same abscissa, he counts them from bottom to top (starting from the point with the smallest ordinate). When he reaches the rightmost point, he continues with the leftmost remaining point.

Alexandru stops counting and deleting when there is only one drawn point left on the paper.

~[puncte.png]

# Task

Write a program that reads the non-zero natural number $N$, then the $2 \cdot N$ integer numbers representing the coordinates of the $N$ points, and determines:

- $NRP$, the maximum number of points (among those drawn) located on one of the axes of the Cartesian coordinate system or on a line parallel to one of the two axes;
- $NRD$, the number of distinct lines that pass through at least two of the drawn points whose abscissa $x$ and ordinate $y$ satisfy at least one of the relations $x = y$ or $x + y = 0$;
- $XP$ representing the abscissa of the point remaining on the paper at the end of the third level of the game.

# Input data

The input file `puncte.in` contains the number $N$ of points on the first line, and on each of the following $N$ lines, two integers separated by a space representing, in order, the abscissa and ordinate of a point in the plane.

# Output data

The output file `puncte.out` will contain on the first line the natural number $NRP$, on the second line the natural number $NRD$, and on the third line the integer representing the coordinate $XP$.

# Constraints and clarifications

- $5 \leq N \leq 250\ 000$;
- The coordinates of the points are integers with at most $3$ digits;
- $20$% of the score will be awarded for the correct solution of point (a), $20$% for the correct solution of point (b), and $60$% for the correct solution of point (c).

# Example

`puncte.in`
```
5
-1 5
0 0
2 2
-3 3
2 -2
```

`puncte.out`
```
2
4
-1
```

## Explanation

a) There are at most $2$ points on a line parallel to one of the two axes or on axes

~[puncte1.png]

b) There are $4$ distinct lines that connect at least two of the points ($0,0$), ($2,2$), ($-3,3$) and ($2,-2$)

~[puncte2.png]

c) The points are deleted, in order, with coordinates: ($-3,3$), ($2,-2$), ($0,0$), ($2,2$). The remaining point has coordinates ($-1,5$)
