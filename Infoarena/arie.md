## Task

Two convex polygons with $N$ and $M$ vertices respectively are given. Determine the area of the intersection of the two polygons.

## Input data

The first line of the file `arie.in` contains the integer $N$, representing the number of vertices of the first polygon. The next $N$ lines contain two integers each, separated by a space, representing the $x$ and $y$ coordinates of the vertices of the first polygon. The vertices of the polygon are given in either clockwise or counterclockwise order. The following line contains the integer $M$, representing the number of vertices of the second polygon. The next $M$ lines contain two integers each, separated by a space, representing the $x$ and $y$ coordinates of the vertices of the second polygon. The vertices of the polygon are given in either clockwise or counterclockwise order.

## Output data

In the file `arie.out`, print the area of the intersection of the two polygons, rounded to 3 decimal places.

## Constraints and clarifications

$3 \leq N \leq 20$

$3 \leq M \leq 20$

$-50 \leq x$ coordinate of any vertex of a polygon $\leq 50$

$-50 \leq y$ coordinate of any vertex of a polygon $\leq 50$

For those surprised by the small input limits and the large time limit: often (TopCoder, ACM, etc.) a program with suboptimal complexity, but written quickly and clearly, is preferred over one with optimal complexity, whose writing duration is long and in which there is a high chance of having bugs!

## Example

`arie.in`

```
4 
-2 -2 
2 -2 
2 2 
-2 2 
3 
0 3 
3 0 
0 -3 
```

`arie.out`

```
7.000
```