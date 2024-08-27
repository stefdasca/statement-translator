# Popandai2

The ground squirrels on the "cheerful meadow" have escaped the eagle attack and now must hide from the wolves in their burrows. These burrows can be identified by points with integer coordinates in the plane and are arranged at the corners of a convex polygon. To be protected from wolf attacks, the ground squirrels want to establish as large a safety perimeter as possible, where they can move freely. This perimeter will be in the shape of a quadrilateral and will have its vertices located at four of the $N$ points representing the burrows.

## Task

Help the ground squirrels determine the area of the maximum quadrilateral that satisfies the conditions mentioned!

## Input data

The input file `popandai2.in` contains on the first line an integer $N$, representing the number of burrows. The next $N$ lines each contain two integers $(X_i, Y_i)$ (separated by a space) representing the coordinates of the $i^{th}$ burrow. These coordinates will be given in counterclockwise order.

## Output data

The output file `popandai2.out` should contain a single real number with exactly one decimal place representing the maximum area of the desired quadrilateral.

## Constraints and clarifications

$4 \leq N \leq 1000$

$1 \leq X_i, Y_i \leq 30000$

For $60\%$ of the score, solve the problem for the case $3 \leq N \leq 300$

## Example

`popandai2.in`
```
7
3 2
6 1
9 3
8 7
6 9
3 8
2 4
```

`popandai2.out`
```
28.5
```