## Line

A simple polygon is given, not necessarily convex.

## Task

There are $Q$ questions of the type: Is the point with coordinates $x$, $y$ located inside the polygon?

## Input data

The input file `dreapta.in` will contain on the first line the value $N$ representing the number of vertices of the polygon. The next $N$ lines will contain two real values each, representing the coordinates of the vertices of the polygon. It is guaranteed that any two adjacent points define an edge of the polygon. Also, the line connecting the first and the last point is an edge of the polygon. The next line will contain the natural number $Q$ representing the number of queries. The following $Q$ lines will contain two real values each, representing the coordinates of the points in the respective queries.

## Output data

The output file `dreapta.out` will contain $Q$ lines. The line with index $i$ will have the value $1$ if the point with index $i$ in the queries is inside the polygon, or the value $0$ otherwise.

## Constraints and clarifications

$1 \leq N \leq 100 \ 000$

$2 \leq Q \leq 100 \ 000$

$-10^9 \leq x , y \leq 10^9$, for all coordinates of the points in the input

It is guaranteed that all points in the queries will be on the same line.

To avoid precision errors or special cases, the following is guaranteed:

The line on which the queries are located will not intersect any polygon vertex.

No edge of the polygon will be parallel to the $Oy$ axis.

No point in the queries will be located on an edge of the polygon.

The line on which the queries are located is not parallel to the $Oy$ axis.

## Example

`dreapta.in`
```
5
3.0 1.0
1.0 4.0
3.0 5.0
5.0 5.0
4.0 2.0
3
3.0 4.0
5.0 6.0
3.5 4.5
```

`dreapta.out`
```
1
0
1
```