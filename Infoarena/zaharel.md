# Zaharel

Zaharel is a great enthusiast of colors, so he took a math sheet with $N$ rows and $N$ columns and drew $M$ red or blue dots in the cells of the math sheet, in different positions. After drawing the points, he noticed that there is at least one red point on each row and at least one blue point on each column. Thus, he posed the following problem: can he construct two polygons (not necessarily convex) that have the same number of vertices, one polygon having only red dots as vertices and the other having only blue dots as vertices, such that the centroids of the two polygons coincide? Zaharel is not a picky boy, so he doesn't mind if the two polygons intersect or if one is inside the other! The only conditions that need to be respected are listed above. The centroid of a polygon with vertices $(x_{0},y_{0}), (x_{1},y_{1}), \dots, (x_{n},y_{n})$ is considered to be the point with coordinates $\left(\frac{x_{0} + x_{1} + \dots + x_{n}}{n+1}, \frac{y_{0} + y_{1} + \dots + y_{n}}{n+1}\right) .$

## Task

Write a program that determines the two polygons for a math sheet drawn as described above by Zaharel.

## Input data

The first line of the file zaharel.in contains the natural numbers $N$ and $M$. 
The next $M$ lines are of the form $i \ j \ c$ where $i$ and $j$ are natural numbers representing the row and column of a dot, respectively, and $c$ is a character representing the color ($R$ for red and $A$ for blue). 

## Output data

The first line of the output file zaharel.out should contain a number representing how many vertices each polygon has. 
The next line should contain the points describing the polygon with red dots as vertices, in any order.
The third line should contain the points describing the polygon with blue dots as vertices, in any order.

## Constraints and clarifications

$6 \leq N \leq 1000$ 

$2N \leq M \leq 100000$ 

If there is no solution, -1 will be printed in the output file.

If there are multiple solutions, only one should be printed.

The resulting polygons must have at least 2 vertices.

## Example

`zaharel.in`
```
6 12
1 3 R
2 4 R
3 1 R
4 6 R
5 2 R
6 4 R
2 1 A
4 2 A
3 3 A
1 4 A
6 5 A
6 6 A
```

`zaharel.out`
```
3
1 3
2 4
3 1
1 1
4 2
1 3
```