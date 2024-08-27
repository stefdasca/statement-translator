Dreptunghi2

Given $N$ points in a plane with known coordinates $(x_i , y_i)$ with integer values. A rectangle encloses these points if all points are inside the rectangle or on its sides. Determine the minimum area of ​​a rectangle that encloses all $N$ points and has its sides parallel to either the first or the second bisector of the coordinate axes. The first bisector of the coordinate axes is the line that has the equation $x - y = 0$ and the second bisector is the line with the equation $x + y = 0$ .

## Input data

The input file `dreptunghi2.in` contains on the first line the number of tests $T$. Next, follows a description of each test as follows: The first line contains the natural number $N$ and on the next $N$ lines two integer numbers $x_i$ $y_i$ separated by space.

## Output data

The output file `dreptunghi2.out` contains a single number, the minimum area of ​​a rectangle that meets the restrictions rounded to the first $3$ decimal places. If all points are on a line segment, we consider a degenerate rectangle with area $0$ $($print $0.000)$.

## Constraints and clarifications

$1 \leq N \leq 10^{5}$

$-10^{4} \leq x_i, y_i \leq 10^{4}$

The input file will contain a maximum of $10$ tests.

## Example

`dreptunghi2.in`
```
1
6
1 1
-2 1
1 4
-1 3
3 0
-2 5
```
`dreptunghi2.out`
```
30.000
```

## Explanation

The coordinates of the vertices of the rectangle are : $(1, -2), (4, 1), (-1, 6), (-4, 3)$