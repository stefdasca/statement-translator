
A Texan has a pasture with the boundary in the form of a convex polygon. Since he has reached an age where he can no longer take the cattle to graze on his pasture, he decides to donate part of the pasture to the worthiest of his grandchildren. Thus, he provides them with the Cartesian coordinates of the pasture corners and asks them to find 3 positions on the pasture boundary where three poles can be placed, so that by connecting the 3 poles with barbed wire, an equilateral triangle is formed.

# Task

Write a program to help the grandchildren determine the positions of the $3$ poles.

# Input data

The input file `texan.in` contains:
* The first line contains the natural number $n$, which represents the number of corners of the pasture.
* The next $n$ lines contain a pair of real numbers, which represent the coordinates of the pasture corners separated by a space (in the order: abscissa ordinate). The corners of the pasture are specified in counterclockwise order.

# Output data

The output file `texan.out` will contain three lines. Each line contains the coordinates of one of the three poles (in the order: abscissa ordinate) separated by a space. These coordinates will be specified with $6$ decimal places (rounded).

# Constraints and clarifications

* $4 < n < 501$
* The coordinates of the pasture corners are rational numbers in the range $[-7\ 000, 7\ 000]$.
* For the evaluation, a solution is considered correct with a margin of error of $0.01$.
* If the solution is not unique, any valid solution will be displayed.
* In the test files, the distance between any two corners of the pasture is $\geq 1$.
* The side of the determined equilateral triangle must be > $0.1$. 
* For the test data, there is always a solution that meets the problem requirements.

# Example

`texan.in`
```
5
10 0
15 15
0 20.5
-10 15
0 0
```

`texan.out`
```
12.500000 7.500000
-3.150637 4.725956
2.272289 19.666827
```
