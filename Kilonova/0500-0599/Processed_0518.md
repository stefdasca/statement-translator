In the first quadrant of the Cartesian system, we define a *zone* denoted by `Z(x, y, u, v)` as a set of lattice points belonging to a rectangle defined by two diagonally opposite points `(x, y)` and `(u, v)` with `x \leq u` and `y \leq v`. In particular, a zone can contain the points of a segment when `x = u` or `y = v`. Also, a zone can consist of a single point when `x = u` and `y = v`.

A *path* between two lattice points is defined as a minimum number of horizontal or vertical segments of length `1` that connect the two points.

~[manhattan.jpg]

# Task
Given two zones `Z1(a, b, c, d)` and `Z2(e, f, g, h)` that do not intersect at any point, calculate the number of distinct paths modulo `666013` that start in zone `Z1` and end in zone `Z2`.

# Example
For the zones `Z1(1, 1, 1, 2)` and `Z2(2, 2, 3, 2)` there are `7` distinct paths.

~[manhattan2.jpg]

# Input data
The input file `manhattan.in` contains on the first line eight natural numbers `a, b, c, d, e, f, g, h` with the above-mentioned significance.

# Output data
The file `manhattan.out` will contain on the first line the number of distinct paths modulo `666013`.

# Constraints and clarifications
* The coordinates of the zones are natural numbers less than or equal to `100\ 000`.
* For tests worth `10` points the coordinates of the zones are less than or equal to `30`.
* For tests worth `30` points the coordinates of the zones are less than or equal to `300`.
* For tests worth `50` points the coordinates of the zones are less than or equal to `1\ 000`.
* For tests worth `50` points the projections on the Ox and Oy axes of the zones are disjoint.

# Examples
`manhattan.in`
```
1 1 1 2 2 2 3 2 
```
`manhattan.out`
```
7
```

`manhattan.in`
```
1 1 2 2 2 3 3 4 
```
`manhattan.out`
```
53 
```

`manhattan.in`
```
8 4 13 7 2 3 6 8 
```
`manhattan.out`
```
44702 
```

`manhattan.in`
```
80 40 130 70 20 30 60 80
```
`manhattan.out`
```
145267 
```
Explanations
---

For the first example: study the example above
For the second example: the number of distinct paths is `53`
For the third example: the number of distinct paths modulo `666013` is `44702`
For the last example: the number of distinct paths modulo `666013` is `145267`