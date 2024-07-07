
There are $N$ colored points in a plane. They are identified by their integer coordinates on the OX and OY axes. Each point has an associated natural number between $1$ and $C$ representing its color code. A rectangle is called *correct* if it simultaneously meets the following conditions:

* all four vertices are among the given N points;
* its sides are parallel to the OX and OY axes;
* its vertices are colored in the same color.

# Task

Determine the maximum number of *correct* rectangles that can be formed with the $N$ points in the plane.

# Input data

The first line of the text file `dreptc.in` contains two numbers $N, MaxC$ representing the number of points in the plane and the number of colors associated with the points. On the next $N$ lines, we read three numbers $x \\ y \\ c$ representing in order the coordinate on the OX axis (abscissa), the coordinate on the OY axis (ordinate), and the color code associated with the point.

# Output data

The first line of the text file `dreptc.out` will contain a single number representing the maximum number of correct rectangles.

# Constraints and clarifications

* $1 \\leq N \\leq 1 \\ 000$;
* $1 \\leq C \\leq 5$;
* $-1 \\ 000 \\leq x, y \\leq 1 \\ 000$;
* There are no two points with the same coordinates;
* $40$% of tests will have $N \\leq 100$;

# Example

`dreptc.in`
```
9 2
3 10 1
3 8 2
3 6 1
3 4 1
3 0 1
6 0 1
6 4 1
6 8 2
6 10 1
```

`dreptc.out`
```
3
```

## Explanation

The vertices of the three correct rectangles are:

$(3, 0), (3, 4), (6, 4), (6, 0)$
$(3, 0), (3,10), (6,10), (6, 0)$
$(3, 6), (3,10), (6,10), (6, 4)$
