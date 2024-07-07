
Two horizontal parallel rays denoted as $a$ and $b$ are considered. Each of them has the left end positioned on the $\\text{Oy}$ axis. The distance between them is **two** units.
On ray $a$, there are $n_1$ points, and on ray $b$, there are $n_2$ points. For each of these points, the distance from the $\\text{Oy}$ axis is known.

# Task

Determine:

1. How many right trapezoids can be formed, with one of the bases on ray $a$, the other base on ray $b$, and the vertices in the two given sets of points?
2. What is the largest area of one of these trapezoids?

# Input data

The input file `trapeze.in` has the following content:
* The first line contains a natural number $n_1$, with the significance from the statement.
* The second line contains $n_1$ values separated by spaces. Each of these represents the distance from one of the $n_1$ points located on ray $a$ to the $\\text{Oy}$ axis.
* The third line contains a natural number $n_2$, with the significance from the statement.
* The fourth line contains $n_2$ values separated by spaces. Each of these represents the distance from one of the $n_2$ points located on ray $b$ to the $\\text{Oy}$ axis.

# Output data

The output file `trapeze.out` will contain two lines:
* The first line will contain a natural number representing the answer to request $1$.
* The second line will contain a natural number representing the answer to request $2$.

# Constraints and clarifications

* A trapezoid is a quadrilateral with two parallel sides called bases and the other two sides non-parallel. Rectangles, squares, parallelograms, and rhombuses **are NOT** trapezoids!
* A right trapezoid is a trapezoid in which the bases are perpendicular to one of the non-parallel sides.
* The area of a right trapezoid is equal to the product of the sum of the bases and the length of the perpendicular side divided by $2$;
* $2 \\leq n_1, n_2 \\leq 100\ 000$;
* The values on the second line and the fourth line do not exceed $1$ billion;
* The values on the second line and the fourth line are given in **ascending order**;
* It is guaranteed that the given points form at least one right trapezoid;
* For the correct solution of the first request, $50\\%$ of the score of a test is awarded; for the correct solution of both requests, $100\\%$ of the score of the test is awarded.
* $50\\%$ of the total score is awarded for correctly solving tests where $n_1$ and $n_2 \\leq 200$.

# Example

`trapeze.in` 
```
4
1 3 6 9
5
2 3 4 6 10
```

`trapeze.out`
```
12
13
```

## Explanation

On ray $a$, there are $4$ points at distances $1$, $3$, $6$, and $9$ from $\\text{Oy}$.
On ray $b$, there are $5$ points at distances $2$, $3$, $4$, $6$, and $10$ from $\\text{Oy}$.
The number of right trapezoids with one base on ray $a$ and the other base on ray $b$ is $12$, and the largest area of one such trapezoid is $13$.
