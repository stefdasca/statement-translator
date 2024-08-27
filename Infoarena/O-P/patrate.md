# Squares

Shepherd Ion wants to enclose his sheep in pens, and by a fortunate coincidence, his friend Vasile has a company that builds pens. Since Vasile is a good friend of Ion, he proposed to build the pens for free, provided that they have the lowest possible cost. Vasile accepts to build at most three pens in the shape of squares with sides parallel to the coordinate axes. These squares must contain within them all the sheep; for simplicity, we consider a sheep to be a point on the plane. To minimize the cost, the side of the largest pen must be as short as possible. The pens can intersect, and a point on the edge of the pen is considered to be inside.

## Task

Help Ion find a solution that will satisfy Vasile.

## Input data

In the input file `patrate.in`, the first line contains a natural number $n$ which represents the number of Ion's sheep, and the following $n$ lines contain the positions of the sheep, where each such line contains two integers $x, y$ separated by a single space which represents the position of a sheep (abscissa and ordinate).

## Output data

The output file `patrate.out` will contain a natural number which represents the minimum side length that the largest pen among the three can have, such that all the sheep are inside the three pens.

## Constraints and clarifications

$1 \leq n \leq 50000$  
The coordinates of the sheep are integers in the range $[0 50000]$

## Examples

`patrate.in`  
```
6
1 0
2 1
3 2
3 4
5 4
6 0
```

`patrate.out`  
```
2
```

## Explanations