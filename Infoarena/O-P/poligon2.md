# Polygon 2

Gigel drew a polygon (not necessarily convex and which may even self-intersect) with $N$ vertices on paper and marked the midpoint of each side. However, his brother erased the drawn polygon, leaving only the midpoints of the sides marked on the paper. Gigel would like to redraw the polygon as it was initially. The polygon's vertices are numbered from $1$ to $N$ in the order they appear along the polygon's contour. With this numbering of vertices, the sides are also numbered. Side $i$ $(1 \leq i \leq N)$ is the segment that connects vertices $i$ and $i + 1$. Side $N$ connects vertices $1$ and $N$.

## Task

Given the coordinates of the midpoints of a polygon's sides, determine the coordinates of its vertices.

## Input data

The first line of the input file `polygon2.in` contains the integer $N$, the number of sides (and vertices) of the polygon. The next $N$ lines contain two real numbers (with at most three decimals), separated by a space, $x$ and $y$, representing the coordinates of the midpoints of each side, in order, from $1$ to $N$.

## Output data

The output file `polygon2.out` will contain the message `fara solutie` (no solution) if Gigel marked the midpoints of the sides incorrectly and no polygon can be formed with the given midpoints of the sides. If there is at least one solution, you will print $N$ lines. Each line will contain two real numbers, displayed with three decimals, representing the coordinates $(x, y)$ of a vertex. The first line will contain the coordinates of the vertex numbered $1$, the second line, the coordinates of the vertex numbered $2$, and so on.

## Constraints and clarifications

$3 \leq N \leq 10\ 000$

The coordinates of the midpoints of the sides are in the interval $[0, 2\ 000\ 000\ 000]$.

If the problem admits at least one solution, with the coordinates of the vertices displayed in the output file, the coordinates of the midpoints of each side will be calculated. You will receive maximum points for the respective test if the difference between the given coordinates of the midpoints and those calculated from the output file is at most $0.001$ for any side. Otherwise, you will receive no points.

## Examples

`polygon2.in`
```
4
0 0
2 0
2 2
0 2
```

`polygon2.out`
```
-1.000 1.000
1.000 -1.000
3.000 1.000
1.000 3.000
```

`polygon2.in`
```
4
0 0
2 0
2 2
1 3
```

`polygon2.out`
```
fara solutie
```