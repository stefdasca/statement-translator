In the xOy plane, a rectangle with sides parallel to the coordinate axes is drawn. The coordinates of the lower-left and upper-right vertices of the rectangle are $(0, 0)$ and $(c, d)$. Let $P$ be the set of points located inside the rectangle, whose coordinates are natural numbers. By drawing a minimum number $m$ of straight line segments, the vertex with coordinates $(0, 0)$ is connected to each point in the set $P$. Thus, each point in $P$ will belong to the interior of a segment from the $m$ segments or will be an endpoint of a segment from the $m$ segments.

# Task

Write a program that reads the natural numbers $c$ and $d$, and determines the minimum number $m$ of drawn straight line segments.

# Input data

The input file `mins.in` contains a single line that contains two natural numbers $c$ and $d$, separated by a space.

# Output data

The output file `mins.out` will contain a single line that will contain a natural number representing the minimum number $m$ of drawn straight line segments.

# Constraints and clarifications

* $1 \leq c, d \leq 5 \ 000$
* $c$ and $d$ are non-zero natural numbers.

# Example

`mins.in`
```
4 3
```

`mins.out`
```
5
```

## Explanation

$c = 4$, $d = 3$.

The set $P$ of natural coordinate points located inside the rectangle consists of $6$ points: $\{P_1, P_2, P_3, P_4, P_5, P_6\}$. To connect the vertex $(0, 0)$, from the lower-left of the rectangle with the $6$ points, $m = 5$ segments are sufficient.

~[mins.png|width=30em]