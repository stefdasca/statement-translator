The specific characteristic of the islands in the Maldives archipelago (Indian Ocean) is that all its $N$ islands are shaped like a triangle. The location of these islands uses the Cartesian coordinates of their three vertices.
The administration of these islands wants to install a radio-transmission device on the water or on an island, at a point having natural number coordinates $(x_D, y_D)$, which transmits signals only in horizontal and vertical directions simultaneously, with the following properties:
* denoting with $\text{NRO}$ the number of islands that the signal reaches horizontally and with $\text{NRV}$ the number of islands that the signal reaches vertically, the sum $\text{NRO} + \text{NRV}$ must be maximal;
* if there are multiple points with the previous property, then the point with the smallest lexicographical order will be chosen.

# Task

Write a program that, knowing the number of islands $N$ and the Cartesian coordinates of their vertices, determines the coordinates $x_D$ and $y_D$ with the properties from the statement.

# Input data

The input file `dispozitiv.in` contains on the first line the number $N$, as described above, and on the next $N$ lines each having six numbers representing the coordinates of the vertices of the islands $(x_1 \ y_1 \ x_2 \ y_2 \ x_3 \ y_3)$.

# Output data

The output file `dispozitiv.out` will contain on the first line the coordinates $x_D$ and $y_D$ with the property from the statement, separated by a space.

# Constraints and clarifications

* $1 \leq N \leq 10\ 000$
* The coordinates of the vertices of the islands are natural numbers $\leq 10^9$
* Any two islands do not have common points
* The point with coordinates $(x_1, y_1)$ is less than the point with coordinates $(x_2, y_2)$, if $x_1 \lt x_2$ or ($x_1 = x_2$ and $y_1 \lt y_2$)
* The scores of the tests in the contest were lost, so some sources may get different scores from those in the contest.

# Example

`dispozitiv.in`
```
6
0 7 4 7 1 10
5 1 6 1 6 2
2 3 2 4 4 4
2 0 1 2 4 2
6 7 7 7 6 10
5 0 7 0 7 1
```

`dispozitiv.out`
```
2 1
```

## Explanation

Code the islands with $1, 2, \dots, 6$, and island $i$ will have the coordinates of the vertices on line $i + 1$.
The parallels to the $ \text{Ox}$ and $\text{Oy}$ axes through the coordinate point $(2, 1)$ intersect a number of $\text{NRO} = 3$ triangles, namely: $4, 2, 6$ horizontally and intersect a number of $\text{NRV} = 3$ triangles: $4, 3, 1$ vertically. $\text{NRO} + \text{NRV}$ is maximal.
There are also other points with the same property but larger in lexicographical order, such as the point with coordinates $(6, 1)$. 

