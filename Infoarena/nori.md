## Task

Since vacation has arrived, I am visiting my grandparents again, near the Danube. And because the rain is coming, with thunder and lightning, I hear the cannon strikes of the Bulgarian neighbors, who, in order to protect their cucumber crops from hail, need to disperse the threatening clouds. I now want to find out, for each possible direction of a strike, whether it hits any cloud. We consider that the clouds have a circular shape, and a cannon strike sends the projectile in the direction of a line. Formally, $N$ circles completely included in the first quadrant of an orthogonal coordinate system and $M$ half-lines starting from the origin and passing through the first quadrant are given. Determine, for each of the half-lines, if it intersects at least one circle.

## Input data

The file `nori.in` contains:
the first line contains $N$, the number of clouds;
each of the following $N$ lines contains 3 natural numbers separated by a space representing a circle (in order, the abscissa of the center, the ordinate of the center, the radius);
the next line contains $M$, the number of strikes;
each of the following $M$ lines contains 2 non-zero natural numbers separated by a space, $x$ and $y$ meaning: the strike starts from the origin of the orthogonal system in the direction of a line passing through the point of coordinates $(x, y)$.

## Output data

The first line of the file `nori.out` contains $M$ values 0 and 1, not separated by spaces. The $k$-th value is 1 if the $k$-th line from the input file does not intersect any circle and 0 if it intersects at least one circle.

## Constraints and clarifications

$1 \leq N, M \leq 100000$

The other values in the input file are non-zero positive numbers less than or equal to $10000$

The circles can intersect and can even be identical

The half-lines are not necessarily distinct and are infinite

A half-line intersects a circle if it has at least one common point with it.

## Example

nori.in
```
2
8 2 1
2 8 1
6
8 2
8 3
2 8
1 1
1 100
100 1
```

nori.out
```
000111
```