# Tri

Given a triangle $ABC$ positioned such that vertex $B$ is at the origin (coordinate point $0$ and $0$), vertex $C$ is on the $OX$ axis and has a positive $x$ coordinate, and vertex $A$ has both coordinates positive. Inside this triangle, there are $N$ points ($N$ divisible by 3).

## Task

Determine a point denoted as $G$ that lies inside the triangle $ABC$ and satisfies the condition that inside or on the contour of each of the triangles $ABG$, $BCG$, and $CAG$, there is exactly one-third of the $N$ points. If any of the $N$ points lie on one of the segments $AG$, $BG$, or $CG$, it will be considered as belonging to only one of the two triangles that share the respective segment, and you may choose to which of the two triangles it belongs.

## Input data

The first line of the file `tri.in` contains $6$ integer values representing: the first two are the coordinates of vertex $A$, the next two are the coordinates of point $B$ (both being $0$), and the last two are the coordinates of point $C$ (the second value in this pair is $0$).

The second line contains the natural number $N$.

Each of the following $N$ lines contains two integer values representing the coordinates of each of the $N$ points located inside the triangle $ABC$.

## Output data

The first line of the file `tri.out` contains two real numerical values representing the coordinates of point $G$.

The second line prints $N/3$ pairs of integer values separated by at least one space representing the coordinates of the points located inside or on the contour of the triangle $BCG$.

The third line prints $N/3$ pairs of integer values separated by at least one space representing the coordinates of the points located inside or on the contour of the triangle $ABG$.

The fourth line prints $N/3$ pairs of integer values separated by at least one space representing the coordinates of the points located inside or on the contour of the triangle $ACG$.

## Constraints and clarifications

$2 < N \leq 10000$

The coordinates for the vertices of the triangle and for each point inside the triangle are non-negative integers $\leq 1\ 000\ 000$

In each pair representing the coordinates of a point, the first value represents the abscissa and the second the ordinate

The coordinates of point $G$ will be displayed with at least $8$ exact decimal places

Any two of these points are not collinear with one of the vertices $A$, $B$, or $C$

## Example

`tri.in` `tri.out`

```
5 5 0 0 10 0
6
8 1
3 0
3 2
1 1
1 3
2 9
1 6
1 1
1 3.636364 1.590909
3 0  6 1  3 2  1 1
8 1  9 1
```