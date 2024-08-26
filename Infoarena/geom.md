Here's the translated statement:

Geometry

There are $N$ points in the plane.

## Task

Determine the minimum distance between two parallel lines that contain at least $K$ points between them.

## Input data

The input file `geom.in` will contain on the first line two integers $N$ and $K$ representing the number of points in the plane, and the number of points that must be found between the two lines, respectively. On the next $N$ lines, there will be two integers, separated by a space, $X$ and $Y$ which represent the coordinates of a point in the plane.

## Output data

The output file `geom.out` will contain on the first line a single real number $D$ with exactly three decimal places, which represents the minimum distance between two parallel lines that satisfy the conditions in the statement.

## Constraints and clarifications

1 $\leq$ $N$ $\leq$ 300

1 $\leq$ $K$ $\leq$ $N$

## Example

`geom.in`
```
5 4
0 0
1 0
0 1
1 1
1000 0
```

`geom.out`
```
1.000
```