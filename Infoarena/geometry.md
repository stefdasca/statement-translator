# Geometry

Ionut has $N$ segments in the $XY$ plane and would like to know how many pairs of these intersect. It is considered that two segments intersect even if they touch at a single point.

## Task

Help Ionut find the answer.

## Input data

The file `geometry.in` will contain on the first line an integer $N$, the number of segments, followed by $N$ lines in the form $X1, Y1, X2, Y2$, representing the coordinates of the endpoints for each of the segments.

## Output data

The file `geometry.out` will contain on the first line a single number, representing the number of pairs of segments that intersect.

## Constraints and clarifications

$0 < N \leq 500$

The coordinates of the segment endpoints are all integers between $-10\ 000$ and $10\ 000$.

## Example

`geometry.in`
```
3
-1 -1 1 1
0 -1 0 1
-1 0 1 0
```

`geometry.out`
```
3
```