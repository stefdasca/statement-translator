# Symmetries

Given two sets of $N$ points each in the plane, determine if by applying a series of geometric transformations to the first set, you can obtain the second set. The valid transformations are:
a) Translation - Two values $D_{x}$ and $D_{y}$ are fixed, and each point $(x,y)$ in the first set will be transformed into the point $(x+D_{x},y+D_{y})$.
b) Rotation - A center of rotation $(P,Q)$ and an angle $\alpha \in \{0,90,180,270\}$ are fixed. Each point in the first set will undergo a rotation of angle $\alpha$ around the center of rotation $(P,Q)$.

##  Task

Determine a sequence of translations and/or rotations to transform the first set of points into the second set.

##  Input data

The input file `symmetries.in` contains on the first line the natural number $N$ as described above. The following $2 \cdot N$ lines will each contain two numbers $x$ and $y$. The first $N$ pairs will represent the points of the first set, the rest will be the points of the second set.

##  Output data

The output file `symmetries.out` will contain on the first line the number $M$ of operations performed on the points of the first set. On the next $M$ lines, you must describe the $M$ operations performed in order in the following format:
`0 Dx Dy` - in the case of a translation operation
`1 P Q alpha` - in the case of a rotation operation
If the second set cannot result from the first set after $M$ operations, print $-1$.

##  Constraints

$$1 \leq N \leq 100\,000$$
$$1 \leq M \leq 100$$
$$-100\,000 \leq P, Q, D_{x}, D_{y} \leq 100\,000$$
$P$, $Q$, $D_{x}$, and $D_{y}$ are integers.
$$\alpha \in \{0, 90, 180, 270\}$$
The rotation is counterclockwise.
The points in the two sets have integer coordinates.
The coordinates of the points are within the range $[-100\,000 \dots 100\,000]$.
For $40\%$ of the tests, $N \leq 1\,000$.

##  Example

`symmetries.in`
```
2
-2 2
-1 2
1 -2
2 -2
3 1
0 0 90
1 0 0 270
1 0 0 180
2 -2 2
-1 2
1 -2
3 -2 -1
```