```markdown
# Task

Consider an infinite 2D plane that contains all points with integer coordinates, from which the coordinate system has been removed (thus the coordinates of a point are no longer known, but it is still possible to calculate the distance between any $2$ points and differentiate the directions up-down and left-right). Initially, all points with integer coordinates in the plane are colored white. Then, a set consisting of at least $2$ points is selected, and the points in the set are colored black so that the following property exists: there are two black points at Manhattan distance $D$ and the Manhattan distance between any other $2$ black points does not exceed $D$. Determine how many different sets of points with this property can be selected. Two sets of points $A$ and $B$ are considered identical if they contain the same number of black points and if there exist two possible placements of the origin of the coordinate system so that the points in set $A$ and those in set $B$ have exactly the same coordinates (in other words, set $B$ can be obtained from set $A$ by translating all points horizontally and/or vertically). The Manhattan distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ is defined as $|x_1 - x_2| + |y_1 - y_2|$.

Given the value $D$, determine the number of sets that can be selected modulo $1 \ 000 \ 000 \ 007$ ($10^9+7$).

# Input data

The input file `dsets.in` contains on the first line the natural number $D$.

# Output data

The output file `dsets.out` will contain on the first line a single natural number representing the number of different sets modulo $1 \ 000 \ 000 \ 007$.

# Constraints and clarifications

* $1 \leq D \leq 1 \ 000 \ 000 \ 000$
* $65\%$ of the tests will have $D \leq 100 \ 000$

# Example 1

`dsets.in`
```
1
```

`dsets.out`
```
2
```

## Explanation

The two sets have the following structure:
1. Two points at a distance $1$ and having the same $x$ coordinate
2. Two points at a distance $1$ and having the same $y$ coordinate

# Example 2

`dsets.in`
```
2
```

`dsets.out`
```
21
```

# Example 3

`dsets.in`
```
3
```

`dsets.out`
```
280
```

# Example 4

`dsets.in`
```
4
```

`dsets.out`
```
8400
```

# Example 5

`dsets.in`
```
12345
```

`dsets.out`
```
290642959
```

# Example 6

`dsets.in`
```
1000000000
```

`dsets.out`
```
957938183
```
```