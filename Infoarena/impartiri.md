# Divisions

This problem was sponsored by IXIA in round 6! The participant who won the prize is Heidelbacher Andrei • a_h1926. Marian loves lines very much, so he drew a rectangle in the Cartesian plane, having the bottom-left corner at coordinates $(0, 0)$, and the top-right corner at coordinates $(N, M)$. He draws a number of lines (possibly $0$), but with the following properties:
- the lines are parallel either to the Ox axis or to the Oy axis;
- the lines pass only through points with integer coordinates;
- the lines must intersect the given rectangle in a finite and non-zero number of points;
- the lines drawn by Marian are not allowed to overlap, but only to intersect.

After finishing drawing the lines, Marian observes that the initial rectangle is divided into a number of smaller rectangles.

## Task

Determine in how many ways Marian can draw the lines with the given properties, so that the area of each smaller rectangle (inside the initial rectangle) is less than or equal to a natural number $K$. Since this number can be very large, only the remainder when divided by the number $2113$ is required.

## Input data

The input file `impartiri.in` contains on a single line $3$ natural numbers: $N$, $M$, and $K$, separated by a space, having the property described in the statement.

## Output data

The output file `impartiri.out` will contain on the first line a natural number that represents the number of ways Marian can draw the lines such that all constraints are respected, modulo $2113$.

## Constraints and clarifications

$2 \leq N$

$M \leq 3000$

$1 \leq K \leq N \times M$

A line is a segment with infinite length.
If a line overlaps a side of the rectangle, it is considered that the line intersects the rectangle in an infinite number of points.
Two ways of drawing lines are considered distinct if at the end (after the drawing process is finished) the content of the initial rectangle is different.

## Example

`impartiri.in`
```
3 2 2
```

`impartiri.out`
```
4
```

## Explanation

The valid ways in which Marian can draw the lines are as follows (the initial rectangle is represented in blue, and the drawn lines in red): Unfortunately, the area of all rectangles inside the initial rectangle must be at most $2$ (since $K = 2$), so only $4$ ways satisfy all requirements. If $K$ were equal to $6$, then the answer would be $8$.