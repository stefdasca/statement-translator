## Task

You are given $n$ lines and $m$ points in the plane. No point will be on any line. The lines divide the plane into regions. We say that two points are in the same region if there is no line separating them. You are required to display the number of groups of points, with each group containing all the points in the same region.

## Input data

The first line of the input file will contain $n$ and $m$ separated by a space. The next $n$ lines will contain 3 integers $a$, $b$, $c$ each, representing the coefficients of the line equation $ax + by + c = 0$. The next $m$ lines will contain two integers separated by space representing the coordinates of the points.

## Output data

The number of groups of points.

## Constraints

$1 \leq n, m \leq 1000$

The coordinates of the points and the coefficients of the lines will be between $-30000$ and $30000$.

## Example

`regiuni.in`

```
3 5
0 1 -1
1 0 -2
1 1 -6
1 3
1 4
3 2
5 3
6 3
```

`regiuni.out`

```
3
```

## Explanation

The first two points form a group, the next point forms another group, and the last 2 points form the third group.