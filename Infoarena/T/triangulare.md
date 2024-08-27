## Task

Petrica has now moved on to geometry. A polygon is called simple if the polygon does not self-intersect or, more rigorously, if any two sides have in common at most their vertices. Any simple polygon with $N$ vertices can be triangulated, or divided into triangles, by drawing $N - 3$ segments between its vertices, provided that these segments, together with the sides of the polygon, do not intersect each other, except at the vertices they have in common. For a given simple polygon, you need to triangulate it.

## Input data

The input file `triangulare.in` contains a natural number $T$ on the first line representing the number of tests. Each test will contain on its first line a natural number $N$ representing the number of vertices of the polygon. On the following $N$ lines, there are two integers, $x$ and $y$, representing the coordinates of the points.

## Output data

In the output file `triangulare.out`, the answers for the $T$ tests will be printed. A test consists of $N - 3$ lines, each line containing two numbers, $a$ and $b$ representing the indices of the two vertices that form the respective segment. The list of segments must be sorted in ascending order by the value of $a$, and in case of equality, in ascending order by the value of $b$.

## Constraints and clarifications

$T = 5$

$4 \leq N \leq 50$

The coordinates are integers in the range $[-10^3, 10^3]$

The indices are numbered from $0$.

ATTENTION! In case there are multiple triangulations, you should print the triangulation that provides the lexicographically smallest list.

For example, if a valid triangulation provides the list $0 2, 0 3, 2 4$ and a second valid triangulation is the list $0 2, 0 4, 1 3$, then the first one will be printed because it is lexicographically smaller.

## Example

`triangulare.in`
```
3
4
0 0
5 0
5 5
0 5
4
0 0
5 0
5 5
3 2
5
0 5
5 3
2 5
5 5
0 0
```

`triangulare.out`
```
0 2
1 3
1 3
1 4
```

## Explanation

For the first test, it is observed that we have a square, and any diagonal of it is good, but we choose the one that gives us the lexicographically smallest, namely the segment $0 2$.

In the case of the second test, since the polygon is no longer a square, the only possible solution is the segment $1 3$.

The answer for the last test is again unique, and the list consists of the segments $1 3$ and $1 4$.