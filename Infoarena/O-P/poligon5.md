# Polygon5

Mitruţ, the Puss in Boots, has a magical garden in the shape of a convex polygon with vertices having integer coordinates. However, because he sleeps too much, he doesn't have time to take care of the whole garden. Therefore, he wants to give up some parts of the garden but wants the new garden to still respect certain conditions:
- it must be a convex polygon with vertices having integer coordinates
- it must have the same number of vertices as the initial polygon
- it must fit within the initial polygon but should not have common vertices with it
- each side of the given polygon must contain exactly one vertex of the new polygon
- it must have the minimum possible perimeter

## Task

Determine the minimum perimeter for Mitruţ's new magical garden. Mitruţ provides you with $T$ such tests to ensure he's not fooled on April 1st.

## Input data

The first line of the input file `poligon5.in` contains the number $T$ of tests in the file. 
The first line of each test contains the number $N$ of vertices of the initial polygon. The next $N$ lines contain two integers $x_i$ and $y_i$ representing the coordinates of the vertices of a polygon. The vertices are given in a clockwise direction.

## Output data

The output file `poligon5.out` contains $T$ integers. Each line $i$ contains the number $P_i$, representing the minimum perimeter of the polygon required by test $i$.

## Constraints and clarifications

$3 \leq N \leq 200$ <br>
$1 \leq T \leq 10$ <br>
$-10\ 000 \leq x_i, y_i \leq 10\ 000$ <br>
The number of points with integer coordinates on the contour of the polygon will not exceed 200. <br>
For simplicity, we will consider that the distance between any two points is the square of the Euclidean distance. So, for two points with coordinates $(x_i, y_i)$ and $(x_j, y_j)$, 
the distance is $(x_i - x_j)^2 + (y_i - y_j)^2$. <br>
It is guaranteed that each side of the initial polygon has at least one point with integer coordinates. <br>
For 10% of the tests, each side of the initial polygon will have exactly one point with integer coordinates. <br>
For another 20% of the tests, the number of points with integer coordinates on any side does not exceed 3, and $N \leq 12$ and $T \leq 5$. 

## Example

`poligon5.in` 
```
1
7
9 0
2 7
0 13
3 16
11 16
16 11
14 5
```

`poligon5.out`
```
268
```

## Explanation

In total, we have 25 points with integer coordinates on the contour of the polygon. From these, the chosen vertices for the new polygon are: $(5, 4)$, $(1, 10)$, $(2, 15)$, $(7, 16)$, $(13, 14)$, $(15, 8)$, $(13, 4)$.