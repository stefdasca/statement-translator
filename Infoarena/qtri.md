## Task

You are given $Q$ quadruples in the form $(A, B, C, D)$, where $A$, $B$, $C$, and $D$ are 4 points in the plane, with integer coordinates. Answer the following question for each quadruple: is point $D$ inside the triangle formed by points $A$, $B$, and $C$?

## Input data

The input file `qtri.in` contains the number $Q$ on the first line. Each of the following $Q$ lines contains $X_1$, $Y_1$, $X_2$, $Y_2$, $X_3$, $Y_3$, $X_4$, $Y_4$, the coordinates of the 4 points, where $X_1$, $Y_1$, $X_2$, $Y_2$, $X_3$, $Y_3$ represent the coordinates of the triangle.

## Output data

In the output file `qtri.out` you will print for each query the answer YES, if the point is inside, or NO otherwise.

## Constraints and clarifications

1 $\leq Q \leq 300\,000$

$-10\,000 \leq X, Y \leq 10\,000$

Any 3 points from a quadruple are non-collinear.

## Example

`qtri.in`

```
2
0 5 5 0 0 0 1 1
0 5 5 0 0 0 5 5
```

`qtri.out`

```
YES
NO
```