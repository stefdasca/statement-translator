## Task

There are $N$ points given in the plane. Calculate how many convex quadrilaterals with vertices at the given points exist.

## Input data

The input file `patrulatere.in` contains on the first line the natural number $N$. Each of the following $N$ lines will contain two integers representing the coordinates of a point.

## Output data

The output file `patrulatere.out` should contain on the first line the required number.

## Constraints and clarifications

$1 \leq N \leq 256$

The coordinates of the points will be within the closed interval $[-10^9, 10^9]$

There will be no two points with the same coordinates

There will not be 3 or more collinear points

For $30\%$ of the test cases used for input $N \leq 64$.

## Example

`patrulatere.in`
```
5
3 8
7 4
10 7
6 9
9 7
```

`patrulatere.out`
```
3
```