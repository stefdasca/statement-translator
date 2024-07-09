Consider $N$ segments in a plane identified by the coordinates of their endpoints. All segments are closed, meaning each also contains the two points considered as its endpoints. We assume that at point $O(0,0)$ which is the origin of the orthogonal axis system $XOY$, there is a laser that can transmit a beam of light to any point with a positive ordinate $(\geq 0)$. The beam can be represented in the plane as a ray with the endpoint at the origin of the axes. However, if the beam of light meets a segment, it obstructs it, meaning it prevents it from passing beyond that point. We consider that each segment has an associated cost for drawing it in the plane.

# Task

Determine the minimum total cost of the segments that can be chosen to obstruct any beam of light that would leave the origin towards a point with a positive ordinate.

# Input data

The input file `laser.in` contains the first line the natural number $N$ of segments. The following $N$ lines contain five integers $x1, y1, x2, y2$ cost, separated by a space. The first four numbers represent the coordinates of the endpoints of each segment, in the order of the abscissa and the ordinate, and the last number on the line represents the cost of the segment.

# Output data

The output file `laser.out` will contain a number representing the determined minimum cost or $-1$ if no solution exists.

# Constraints and clarifications

* $1 \leq N \leq 5 \ 000$
* $-10^9 \leq$ abscissae of points $\leq 10^9$
* $0 \leq$ ordinates of points $\leq 10^9$
* $0 \leq$ costs of segments $\leq 10^9$
* It is guaranteed that point $O(0,0)$ is not on any of the $N$ segments
* Evaluation will use input files worth $30$ points where all segments have a cost equal to $1$

# Example 1

`laser.in`
```
4
2 3 5 0 2
2 3 -4 4 1
-2 4 -5 0 1
6 0 -14 1 8
```

`laser.out`
```
4
```

## Explanation

The segments with the minimum total cost $[(-5, 0), (-2,4)], [(-4, 4), (2,3)]$ and $[(2, 3), (5,0)]$ were chosen. The segments $[(-5, 0), (-2,4)]$ and $[(-14, 1), (6,0)]$ obstruct any beam but have a higher total cost.

# Example 2

`laser.in`
```
4
-1 3 1 3 1
-2 0 -1 1 1
2 0 1 1 1
1 1 -1 1 1
```

`laser.out`
```
3
```

## Explanation

The chosen segments are: $[(-2, 0), (-1,1)], [(-1, 1), (1,1)], [(1, 1), (2,0)]$.

# Example 3

`laser.in`
```
3
-1 3 1 3 1
-2 0 -1 1 4
2 0 1 1 5
```

`laser.out`
```
-1
```

## Explanation

No segments exist that meet the requirements.