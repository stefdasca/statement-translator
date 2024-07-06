Mădălina is crazy about geometry problems. This time she has $N$ points with real coordinates in a plane and wants to cover the points with circles that have their centers on the OX axis (the x-axis) such that the sum of the areas of the circles is minimized.

# Task

Given the coordinates of the $N$ points in the plane, find a coverage of these points with circles that have their centers on the OX axis such that the sum of the areas of the circles is minimized.

# Input data

The first line of the input file `acerc.in` will contain the natural number $N$. The following lines will each contain two real numbers $X$ and $Y$, representing the coordinates of the points.

# Output data

The first line of the output file `acerc.out` will contain a single number representing the minimum sum of the areas of the circles that satisfy the condition from the task.

# Constraints and clarifications

* $1 \leq N \leq 300$
* The values of the coordinates of the points will be in the interval $[-10\ 000, 10\ 000]$
* A circle covers all points in the plane that are at a distance less than or equal to the radius of the circle from its center
* For $40\%$ of the tests, $N \leq 50$
* For $70\%$ of the tests, $N \leq 100$
* The maximum difference by which the final result can vary from the correct one is $0.001$

# Example

`acerc.in`
```
7
0 2
1 1
1 3
4 0
3.9 2
8 4
7 4
```

`acerc.out`
```
79.6208
```

## Explanation

The 7 points will be covered with two circles: one with its center at the point $(0, 1)$ and radius equal to $3$ and one with its center at the point $(0, 7.41341)$ and radius equal to $4.04278$.