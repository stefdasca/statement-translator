# Split3

Tassadar was playing "Slice It!" on his phone and came up with the idea to create a problem for Algoritmiada. If you manage to solve the problem, he will reward you with $100$ points. A convex polygon with $N$ vertices and a point $Q$ located on its edge are given. You are asked to find two lines that meet the following properties:
1. The first line passes through point $Q$.
2. The two lines split the polygon into four regions of equal area.

## Input data

The input file `split3.in` contains on the first line the natural number $N$ as described in the statement. The next $N$ lines will contain two real numbers $x_i$ and $y_i$ representing the coordinates of the polygon vertices, in counterclockwise order. On the next line, there will be two real numbers $x$ and $y$ representing the coordinates of point $Q$.

## Output data

In the output file `split3.out` you will display on a single line, separated by spaces, the real numbers $a_1$, $b_1$, $c_1$, $a_2$, $b_2$, $c_2$ representing the coefficients of the equations of the two lines. The equation of a line is $a \cdot x + b \cdot y + c = 0$.

## Constraints

$3 \leq N \leq 50000$

All coordinates are real numbers with up to $9$ decimal places in the interval $[-10^3, 10^3]$.

An error of at most $10^{-2}$ will be accepted, meaning that the difference between the largest and smallest areas of the four polygon regions should be at most $10^{-2}$.

It is recommended to output the numbers in the output file with $9$ decimal places.

It is recommended to use a precision of at least $10^{-6}$ when comparing real numbers.

For $30\%$ of the tests, the polygon will be regular.

## Example

`split3.in`

```
4
1.0 1.0
3.0 1.0
3.0 3.0
1.0 3.0
2.0 1.0
```

`split3.out`

```
-1.0 0.0 2.0 0.0 1.0 -2.0
```