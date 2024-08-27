# Tri2

Little Gigel has marked $N$ points on a piece of paper, each having integer coordinates. Then he started drawing triangles, each with vertices in three different points out of the $N$ points. For each triangle drawn, Gigel would like to know how many of the $N-3$ remaining points lie strictly inside the triangle.

## Task

For each given triangle (through the indices of its 3 vertices), determine how many of the other points lie strictly inside the triangle.

## Input data

The first line of the input file `tri2.in` contains the integer $N$, representing the number of points marked by Gigel on the paper. Each of the next $N$ lines contains the coordinates of each point, in order, from the one numbered $1$ to the one numbered $N$. The coordinates are described by two integers $x$ and $y$, separated by a space. The next line contains the integer $M$ representing the number of triangles drawn by Gigel. Each of the following $M$ lines contains three integers $a$, $b$, and $c$, separated by spaces, representing the indices of three different points out of the $N$ points.

## Output data

In the output file `tri2.out` you will print $M$ lines. Each line will contain an integer, representing the number of points out of the remaining $N-3$ points that lie strictly inside the corresponding triangle (the first line will contain the answer corresponding to the first triangle described in the input file, the second line the answer corresponding to the second triangle, and so on).

## Constraints and clarifications

$3 \leq N \leq 1000$

$1 \leq M \leq 500\ 000$

Coordinates $x$ and $y$ are integers in the range $[0, 2\ 000\ 000\ 000]$

Any two points have distinct $x$ and $y$ coordinates

Any three points are non-collinear

If you want to use real numbers in your program, it is recommended to use the `long double` type for C/C++, or `extended` for Pascal. For testing the equality of two real numbers, it is recommended to use a precision of $10^{-14}$.

## Example

`tri2.in`

```
5
0 0
1 10
2 4
3 7
10 1
3
1 2 3
5 1 2
5 3 2
```

`tri2.out`

```
0
2
1
```