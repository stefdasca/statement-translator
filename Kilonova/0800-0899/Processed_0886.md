
It is considered $N$ points in the plane, having natural number coordinates, relative to a Cartesian reference XOY, with any two points being distinct.

~[triunghiuri.png]

# Task

Given $N$ and the coordinates of the $N$ points, determine:

1. The maximum number of points that have the same abscissa.
2. The number of triangles that can be drawn respecting the following conditions:
   * All vertices are among the given points;
   * One side is parallel to OX;
   * **Do not** have sides parallel to OY;

# Input data

Input data is read from the file `triunghiuri.in`, which has the following structure:

The first line contains the number $p$, which indicates the task that needs to be solved ($p$ has the value $1$ or $2$);
The second line contains the natural number $N$, representing the number of given points;
The next $N$ lines contain two natural values $x \\ y$, separated by a space, representing the coordinates of the given points.

# Output data

The file `triunghiuri.out` will have the following structure:

If $p = 1$, write in the file, on the first line, the maximum number of points that have the same abscissa (task $1$).
If $p = 2$, write in the file, on the first line, the number of triangles that can be drawn respecting the given conditions, modulo $1 \\ 000 \\ 003$, that is, the remainder of the division of the number of triangles by $1 \\ 000 \\ 003$ (task $2$).

# Constraints and clarifications

* $3 \\leq N \\leq 100 \\ 000$;
* $0 \\leq x, y \\leq 1 000$;
* $25$ points are awarded for a correct solution to task $1$ and $65$ points for a correct solution to task $2$.

# Example 1

`triunghiuri.in`
```
1
5
2 1
1 4
3 4
3 2
6 4
```

`triunghiuri.out`
```
2
```

## Explanation

Task 1 is solved. There are a maximum of two points that have the same abscissa, ($3, 4$) and ($3, 2$).

# Example 2

`triunghiuri.in`
```
2
5
2 1
1 4
3 4
3 2
6 4
```

`triunghiuri.out`
```
4
```

## Explanation

Task $2$ is solved. Four triangles can be drawn that satisfy the conditions.
If we name the $5$ points in the file $A, B, C, D, E$ (as in the image),
then the $4$ triangles that satisfy the conditions are: $ABC$, $ACE$, $ABE$ and $BDE$.
```

Please double-check for potential grammar and/or syntax errors to ensure correctness.
