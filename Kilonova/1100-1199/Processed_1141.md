In the kingdom of XLand, cities were surrounded by walls in the shape of convex polygons. The emperor ordered the construction of a direct road between the capital and a given city. Each end of the road can be any point located on the wall of the city or the capital. The length of the road is the distance between its endpoints.

# Task

Determine the shortest road between the capital and the given city.

# Input data

Input file: `drum.in`

* Line 1: $K_1$ - a non-zero natural number representing the number of vertices of the capital's walls;
* Line 2: $x_1$, $y_1$, $x_2$, $y_2$, $\\dots$, $x_{K_1}$, $y_{K_1}$, $K_1$ pairs of integer numbers, separated by a space, representing the coordinates of the vertices of the capital's walls;
* Line 3: $K_2$, a non-zero natural number representing the number of vertices of the given city's walls;
* Line 4: $x_1$, $y_1$, $x_2$, $y_2$, $\\dots$, $x_{K_2}$, $y_{K_2}$, $K_2$ pairs of integer numbers, separated by a space, representing the coordinates of the vertices of this city.

# Output data

The first line of the output file `drum.out` should contain four real numbers truncated to $4$ decimal places ($x_1$, $y_1$, $x_2$, $y_2$), separated by a space, representing the endpoints of the respective connecting road.

# Constraints and clarifications

* $2 \leq K_1, K_2 \leq 20$
* The coordinates of the vertices of the walls surrounding the city and the capital are integers belonging to the interval $[-100, 100]$ and are given either in clockwise order or in counter-clockwise order.
* The capital and the city do not share any common points (they have no common interior points and no common points on their respective walls).
* If there are multiple solutions, any of them can be displayed.

# Example

`drum.in`
```
4
3 4 3 2 5 2 5 4
4
8 3 8 6 11 6 11 3
```

`drum.out`
```
5.0000 3.5000 8.0000 3.5000
```