
Zăhărel drew $N$ points on a piece of paper. Curious by nature, he chose another $M$ points on the OX axis and wondered for each of the $M$ points on the OX axis which of the $N$ points is the closest (located at the minimum distance). It is considered that the distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ is $(x_1 - x_2)^2 + (y_1 - y_2)^2$.

# Task

Write a program for Zăhărel that determines for each of the $M$ points on the OX axis the distance to the nearest point among the $N$ drawn on the paper.

# Input data

The input file `puncte.in` contains the natural numbers $N$ and $M$ separated by spaces on the first line. Each of the next $N$ lines contains a pair of non-zero natural numbers $x \\ y$, separated by spaces, representing the coordinates of the $N$ points (in ascending order by the x-coordinate, then by the y-coordinate if x-coordinates are equal). Each of the next $M$ lines contains a natural number $x$, representing the x-coordinates (coordinates on the OX axis) of the $M$ points.

# Output data

The output file `puncte.out` will contain $M$ lines. On the $i^{th}$ line, it will contain a natural number representing the distance to the nearest point among the $N$ on the paper for the $i^{th}$ point on the OX axis (considering the order of the points in the input file).

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $1 \leq M \leq 200\ 000$
* All coordinates in the input file are natural numbers in the range $[1, 10^9]$
* The $N$ points in the input file are sorted in ascending order by the x-coordinate, and if two points have the same x-coordinate, they are sorted in ascending order by the y-coordinate.
* For $50\%$ of the tests, $N \geq 90\ 000$ and $M \geq 150\ 000$.

# Example

`puncte.in`
```
3 2
1 1 
5 1
10 2
2
7
```

`puncte.out`
```
2 
5
```

## Explanation

Three points are drawn on the paper, with coordinates $(1,1)$, $(5,1)$, and $(10,2)$. There are 2 points on the OX axis, with x-coordinates $2$ and $7$ respectively.
The minimum distance from the point on the OX axis with x-coordinate $2$ is $2$ (the nearest point is the one with coordinates $(1,1)$).
The minimum distance from the point on the OX axis with x-coordinate $7$ is $5$ (the nearest point is the one with coordinates $(5,1)$).

~[puncte.png]
```
