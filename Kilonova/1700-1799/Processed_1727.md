Gigel imagines the world in 2D, i.e., represented in the Cartesian coordinate system XOY. Each person from his group of $N$ friends is represented in the plane by a point identified by its abscissa and ordinate. In his 2D world, it rains like in England, and the raindrops fall parallel to the OY axis from an infinite height.

To protect his friends from the rain, he proposes to build shields which he will represent on the map as line segments.

# Task

Knowing that he can only draw segments of equal lengths on the map, determine what is the minimum length of a segment such that by drawing at most $K$ segments, all his $N$ friends are protected from the rain.

# Input data

The input file `2d.in` contains:
- the first line contains the natural numbers $N$ and $K$;
- the next $N$ lines contain pairs of real numbers $x, y$, each with exactly three decimals, representing the abscissa and ordinate of the point corresponding to each of Gigel's friends;

# Output data

The output file `2d.out` will contain on the first line a single real number **with three decimals**, representing the minimum length of one of the segments drawn by Gigel.

# Constraints and clarifications

* $1 \leq K < N \leq 200\ 000$
* $-1\ 000\ 000 \leq x,y \leq 1\ 000\ 000$
* The minimum length of a segment Gigel will draw is $1$
* The result will be displayed with an error of at most $10^{-3}$
* A segment drawn between points $(x_1, y_1)$ and $(x_2, y_2)$ protects all points on the segment and the half-plane "below" the line passing through these points and which have the abscissas in the closed interval $[x_1, x_2]$.
* It is recommended to improve execution time for reading the data

# Example

`2d.in`
```
5 3
-5.000 1.000
-2.000 3.000
3.000 2.000
3.000 -2.000
1.000 2.000
```

`2d.out`
```
2.000
```

## Explanation

One possible way to draw the segments would be:

~[2d.png]