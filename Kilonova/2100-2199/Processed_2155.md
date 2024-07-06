# Task

Consider two distinct lines \( a \) and \( b \) parallel to the Ox axis. The distance between them is two units. On line \( a \), there are \( n_1 \) equidistant points, and on line \( b \), there are \( n_2 \) equidistant points. Known values are the abscissa of the leftmost point on line \( a \), the abscissa of the leftmost point on line \( b \), and the distance between two consecutive points on line \( a \), respectively on line \( b \).

Determine:
1) How many isosceles trapezoids, with one of the bases on line \( a \) and the other base on line \( b \), and with the vertices in the two sets of given points, can be formed? Rectangles will not be considered isosceles trapezoids!
2) What is the maximum area of one of the isosceles trapezoids determined in task 1)?

# Input data

The first line of the `trapeze.in` file contains three natural numbers \( x_1 \), \( d_1 \), \( n_1 \) with the following meanings:

* \( x_1 \) - the abscissa of the first point on line \( a \) (positive value);
* \( d_1 \) - the distance between two consecutive points on line \( a \);
* \( n_1 \) - the number of points on line \( a \);

The second line of the `trapeze.in` file contains three natural numbers \( x_2 \), \( d_2 \), \( n_2 \) with the following meanings:

* \( x_2 \) - the abscissa of the first point on line \( b \) (positive value);
* \( d_2 \) - the distance between two consecutive points on line \( b \);
* \( n_2 \) - the number of points on line \( b \);

# Output data

The `trapeze.out` file will contain:

* On the first line, a natural number representing the number of isosceles trapezoids.
* On the second line, a natural number representing the maximum area of one of the isosceles trapezoids.

# Constraints and clarifications

* \( d_1, d_2 \) are two non-zero natural numbers \( \leq 40\ 000 \)
* \( n_1, n_2 \) are two non-zero natural numbers \( \leq 500\ 000 \)
* The coordinates of the points are positive and do not exceed \( 2 \cdot 10^9 \).
* It is guaranteed that the points form at least one isosceles trapezoid

# Example 1

`trapeze.in`
```
7 2 5
7 3 5
```

`trapeze.out`
```
3
16
```

## Explanation

- Number of isosceles trapezoids.
- The largest area of one of these trapezoids (the one with vertices at the abscissas \( 11 \) and \( 15 \) on line a, respectively \( 7 \) and \( 19 \) on line b).

# Example 2

`trapeze.in`
```
7 8 15
7 10 16
```

`trapeze.out`
```
103
224
```

