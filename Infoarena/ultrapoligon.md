# Ultrapolygon

Given $N$ points that represent a convex polygon. A subpolygon is defined as the polygon determined by a subset of points of the initial polygon. A polygon is its own subpolygon. The task is to find double the sum of the areas of all the subpolygons of the given input polygon.

## Input data

The input file `ultrapoligon.in` will contain on the first line the number $N$, and on the next $N$ lines, there will be 2 numbers each representing the coordinates of the points.

## Output data

The output file `ultrapoligon.out` will contain double the sum of the areas of the subpolygons.

## Constraints

**ATTENTION!!!** Since it can be demonstrated that the answer is an integer, and large numbers are no longer fashionable, you are required to display the answer modulo $1.000.000.007$

All coordinates are integers ranging from $0$ to $10^9$

For 20 points, $N \leq 18$

For another 40 points, $N \leq 2.000$

For the remaining 40 points, $N \leq 100.000$

The points are given in the input in counterclockwise order

No 3 consecutive points are collinear

## Example

`ultrapoligon.in`

```
4
0 0
1 0
1 1
0 1
```

`ultrapoligon.out`

```
6
```

`14`

```
431
0
983
14
997
331
994
511
975
679
910
893
849
937
830
947
557
985
235
977
16
892
6
778
2
569
30
12
295591745`

## Explanation

In the first example our polygon is a square. Its subpolygons are:
The square $\{ (0,0), (1,0), (1,1), (0,1) \}$ with area $1$, and the triangles with area $0.5$:
$\{ (1,0), (1,1), (0,1) \}$
$\{ (0,0), (1,1), (0,1) \}$
$\{ (0,0), (1,0), (0,1) \}$
$\{ (0,0), (1,0), (1,1) \}$

Double the sum of the areas is $2 \cdot (1 + 0.5 \cdot 4) = 2 \cdot 3 = 6$

For the second example, you will have to take our word for it.