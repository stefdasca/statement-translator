# Trapezoid

Zaharel is a student who gets bored quickly at school. One sunny day, when he didn't feel like listening to his math teacher, he started drawing points on a math sheet. He drew $N$ such points and then asked himself the following question: how many trapezoids can be formed with vertices at these points? A trapezoid is a convex quadrilateral with at least two parallel sides.

## Task

Help Zaharel determine how many trapezoids he can form with the $N$ points on the math sheet.

## Input data

The first line of the input file `trapez.in` contains the natural number $N$. The following $N$ lines contain pairs of natural numbers representing the coordinates of the points.

## Output data

The first line of the output file `trapez.out` will contain the number of trapezoids that can be formed.

## Constraints and clarifications

$4 \leq N \leq 1\ 000$

The coordinates of the points are integers in the range $[0, 2\ 000\ 000\ 000]$

Any three points are non-collinear

Parallelograms should be counted twice as they are trapezoids in two orientations

Try to avoid using real numbers in the implementation because they can cause precision errors

## Example

`trapez.in`

```
5
0 0
0 1
1 4
2 0
3 1
```

`trapez.out`

```
1
```