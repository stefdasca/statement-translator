
$N$ points in 3D space are given by their coordinates. We want to place two cubes with sides parallel to the coordinate axes, such that each point lies on one of the faces or inside at least one of the cubes. Additionally, the side of the cube with the maximum side length among the two must be minimal.

# Task
Write a program to determine the side of the cube with the maximum side length for two cubes that cover the set of points under the conditions given above.

# Input data
The first line of the file `cuburi.in` will contain ten natural numbers $N$, $A_x$, $B_x$, $C_x$, $A_y$, $B_y$, $C_y$, $A_z$, $B_z$, $C_z$. The coordinates of the $N$ points are generated according to the following rules:

- $X_1 = 1, X_i = (X_{i-1} \cdot A_x + B_x \cdot i)$ mod $C_x$, for $i = 2 \dots n$
- $Y_1 = 1, Y_i = (Y_{i-1} \cdot A_y + B_y \cdot i)$ mod $C_y$, for $i = 2 \dots n$
- $Z_1 = 1, Z_i = (Z_{i-1} \cdot A_z + B_z \cdot i)$ mod $C_z$, for $i = 2 \dots n$

The $i$-th point has coordinates $(X_i, Y_i, Z_i)$.

# Output data
The file `cuburi.out` will contain a single natural number representing the side of the cube with the maximum side length.

# Constraints and clarifications
- $1 \leq N \leq 2 \cdot 10^{6}$
- $1 \leq A_x, A_y, A_z \leq 1\ 000$
- $1 \leq B_x, B_y, B_z \leq 10^{10}$
- $2 \leq C_x, C_y, C_z \leq 10^{15}$
- A point on the face of the cube (including on an edge or at a corner of the cube) is considered to be inside the cube
- For a number of tests worth $30$ points $N \leq 100$ and $C_x, C_y, C_z \leq 20$
- For a number of tests worth $70$ points $N \leq 10^{5}$

# Example
`cuburi.in`
```
6 2 3 10 3 1 9 5 7 8
```
`cuburi.out`
```
5
```
# Explanation
The 6 points have the following coordinates: $(1,1,1)$, $(8,5,3)$, $(5,0,4)$, $(2,4,0)$, $(9,8,3)$, $(6,3,1)$. One possible solution is to place the first cube such that two opposite corners have coordinates $(0, 0, 0)$ and $(5,5,5)$ and the second cube to have two opposite corners at coordinates $(6,3,1)$ and $(11,8,6)$.
