## Task

Given $N$ circles in the plane, find a rectangle with maximum area whose sides are parallel to the coordinate axes, and with the coordinates of the corners being natural numbers, such that:
$0 \leq x \leq L$, $0 \leq y \leq H$, where $x$ and $y$ represent the coordinates of the point,
no circle has more than one point in common with the area bounded by the rectangle.

## Input data

The first line of the input file `amax.in` contains the natural numbers $H$ and $L$.
The second line contains the natural number $N$.
The following $N$ lines contain 3 integers each, separated by a space: $x_i$, $y_i$, $r_i$, representing the coordinates of the center and the radius of each circle.

## Output data

In the output file `amax.out` print the maximum area of a rectangle that has the properties specified in the statement.

## Constraints and clarifications

$0 \leq H, L \leq 700$ 

$0 \leq x_i, y_i, r_i \leq 700$ 

$0 \leq N \leq 30$

## Example

`amax.in`

```
10 15
3
3 2 2
3 8 1
10 4 2
```

`amax.out`

```
44
```

## Explanation

The rectangle has the bottom-left corner at $(4,6)$ and the top-right corner at $(15,10)$.