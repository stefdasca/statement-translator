## Task

Karina has a math sheet on which a Cartesian coordinate system is drawn. She draws $N$ points with integer coordinates and $M$ lines. Karina knows that any line divides the plane into two half-planes. She is curious about how the lines divide the points into two parts. Thus, she wants to know how many points are on one side of each line and how many points are on the other side. Specifically, for each line, she defines $N_1$ and $N_2$ as the number of points on one side and the other side of the line, respectively. Karina wants to find $\min(N_1, N_2)$ and $\max(N_1, N_2)$. If a point lies exactly on the line, it is not considered to be on either side of the line (it is not counted).

## Input data

The input file `dsip.in` will contain on the first line the numbers $N$ and $M$ representing the number of points in the plane and the number of lines, respectively. The next $N$ lines will contain 2 integers each, representing the coordinates of the points. The next $M$ lines will contain 4 integers $x_1, y_1, x_2$, and $y_2$ representing two points through which the respective line passes.

## Output data

The output file `dsip.out` will contain $M$ lines, each containing two numbers $\min(N_1, N_2)$ and $\max(N_1, N_2)$ representing the answer for each line in the order in which they appear in the input file.

## Constraints and clarifications

$1 \leq N \leq 2000$

$1 \leq M \leq 200000$

Any 3 points from the $N$ are non-collinear.

All coordinates in the input file will be between $0$ and $5000$

Note: it is recommended to avoid using floating-point data types.

## Example

`dsip.in`
```
5 6
4 7
8 6
4 6
7 3
3 2
2 4
7 4
4 1
4 4
5 2
6 5
2 1
5 4
8 2
3 7
3 3
4 2
2 3
1 2
2 3
2 2
1 2
1 4
```
`dsip.out`
```
...
```

## Explanations

...