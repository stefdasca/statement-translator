Maria spends the last days of her Christmas vacation in Brașov, in April. She is so eager for the snow to melt that she already imagines herself playing in a green area, shaped like a polygon with $N$ vertices. Maria, passionate about mathematics, represents this polygon in the Cartesian coordinate system. She is very curious how many lattice points are inside the polygon, as well as on its edges. A lattice point is a point $(x,y)$ with the property that $x$ and $y$ are natural numbers. Considering this problem way too easy for her level, she wants to complicate it by assigning each lattice point of the form $(x,y)$ a cost equal to the sum of its coordinates, $x+y$. Now, pleased with what she has achieved, she asks you to find out the sum of the costs of the lattice points located inside and on the edges of the polygon.

# Task

Given a polygon with $N$ vertices in counterclockwise order, you are asked to find out the sum of the coordinates of the lattice points located inside and on its boundary.

# Input data

The input file `camp.in` contains on the first line a natural number $N$, representing the number of vertices of the polygon. The following $N$ lines will each contain exactly two natural values separated by a space, representing the vertices of the polygon, given in counterclockwise order.

# Output data

The output file `camp.out` will contain on the first line the required natural number.

# Constraints and clarifications

* $3 \leq N \leq 100\ 000$;
* For any point $(x,y)$ in the input file it is guaranteed that $1 \leq x, y \leq 100\ 000$;
* It is guaranteed that the polygon in the input file is convex;
* For tests worth $25$ points, $N \leq 50$ and $x,y \leq 100$;
* For tests worth another $25$ points, $N \leq 500$ and $x,y \leq 1000$;

# Example

`camp.in`
```
3
5 1
6 6
1 5
```

`camp.out`
```
122
```

## Explanation

~[Capture.JPG|align=right|width=auto]
The sum of the costs of the 16 lattice points that are inside or on the edges of the triangle with vertices at coordinates $(5,1)$, $(6,6)$ and $(1,5)$ is $122$.