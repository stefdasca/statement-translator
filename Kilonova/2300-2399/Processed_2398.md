# Statement

Writing the names of localities on a map has always been an important problem for cartographers, because if some names overlap, the map would become unreadable.

The Cartesian coordinates of the points that mark the localities on the map are known. For each locality marked on the map, its name must be written. The name of a locality must be enclosed in a rectangle that meets the following conditions:
* it has sides parallel to the coordinate axes;
* the width of the rectangle is equal to three times the height of the rectangle;
* the point that marks the locality on the map should be placed in the top left corner of the rectangle.

The rectangles in which the localities’ names are written should all have the same dimensions.

# Task

Write a program that determines the maximum height of the rectangle that encloses the names of the localities, so that any two rectangles drawn on the map have an intersection area of $0$.

# Input data

The file `harta.in` contains on the first line a natural number $N$ representing the number of localities marked on the map. Each of the next $N$ lines contains two natural numbers $X \ Y$, representing the coordinates of the points (abscissa, ordinate) that mark the localities on the map.

# Output data

The file `harta.out` will contain a single line that contains a real number with $3$ decimals representing the maximum width of the rectangles that enclose the names of the localities, so that any two rectangles have an intersection area of $0$.

# Constraints and clarifications

* $1 < N \leq 1 \ 000 \ 000$;
* $0 \leq X, Y \leq 1 \ 000 \ 000$;
* Any two points on the map are distinct.
* The result will be considered correct if the absolute difference between the correct result and the one in the output file is $< 0.01$.

# Example 1

`harta.in`
```
5
1 1
6 5
18 3
9 9
16 15
```

`harta.out`
```
4.000
```

# Example 2


`harta.in`
```
10
26 77
12 37
14 18
19 96
71 95
91 9
98 43
66 77
2 75
94 91
```

`harta.out`
```
7.667
```