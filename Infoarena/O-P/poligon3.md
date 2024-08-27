# Polygon3

You are given $N$ points in the plane. Determine the convex polygon with the maximum area whose vertices are some of the $N$ points and which does not contain any of the given points in its interior.

## Input data

The input file `poligon3.in` contains the integer $N$ in the first line. The next $N$ lines each contain two integers $x$ and $y$ representing the coordinates of the points.

## Output data

The output file `poligon3.out` will contain a single real number with at least two decimal places representing the maximum area of a polygon that meets the task.

## Constraints

$1 \leq N \leq 500$  
$-15\ 000 \leq x$, $y \leq 15\ 000$  
There will be no 3 collinear points.  
A solution will be considered correct if it differs by at most $0.01$ from the correct result.  
For $20\%$ of the tests, $N \leq 15$.  
For $50\%$ of the tests, $N \leq 100$. 

## Example

`poligon3.in`  
`6`  
`1 0`  
`-2 3`  
`0 -2`  
`-5 -2`  
`-3 -1`  
`-3 3`  
`13.00`  

## Explanation

The $5$ points that form the convex polygon with the maximum area, in counterclockwise order, are: $3, 1, 2, 6, 5$.