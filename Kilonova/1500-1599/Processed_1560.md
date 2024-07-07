The provided statement in Romanian has been translated according to your specifications. Here is the English version:

```markdown
We define a **right polygon** as a polygon with consecutive sides that are perpendicular and the lengths of the sides are non-zero natural numbers. A right polygon with $n$ sides is described by a sequence of $n$ non-zero integers in which the lengths of the sides are given by the absolute value of the numbers in the sequence, and the sign indicates the position of the sides, with a positive number indicating a side to the right or up from the end of the previous side, and a negative number indicating a side down or to the left from the end of the previous side; for example, the sequence $1,1,-1,-1$ represents a square with side $1$ (first side to the right, second up, third to the left, fourth down). We will consider the sides to be either horizontal or vertical, with the first side listed being horizontally to the right if the number is positive, or to the left if the number is negative.

# Task

Given one or more sequences of non-zero integers:
1. Determine for each whether it represents a right polygon.
2. Knowing that the given sequences represent right polygons, determine the area of each.

# Input data

The file `drept.in` contains on the first line, separated by space, a natural number $C$ and a natural number $T$. The following $2 \cdot T$ lines will describe the tests, two lines for each test. The first line corresponding to a test contains a natural number $n$, and the second line a sequence of $n$ integers, separated by a space.

# Output data

The file `drept.out` will contain on a single line the results corresponding to the $T$ tests, separated by a space. If $C=1$, for each sequence the result is $1$, if it represents a right polygon, or $0$ otherwise. If $C=2$, for each sequence the result is the area of the corresponding right polygon.

# Constraints and clarifications

* $1 \leq T \leq 10$;
* $4 \leq n \leq 100$;
* For tests worth $45$ points $C=1$, for the remaining $55$ points $C=2$;
* For tests worth $30$ points $C=1$ and the numbers describing the figure are non-zero integers belonging to the interval $[-100,100]$;
* For the other $15$ points and $C=1$ the numbers describing the figure are non-zero integers belonging to the interval $[-10^9,10^9]$;
* For tests worth $33$ points it is guaranteed that we have $C=2$ and the intersection between any horizontal line and the polygon is either empty or consists of a single segment.
* For the tests where the value of $C$ is $2$, the numbers in the sequence describing the polygon are non-zero integers from the interval $[-100, 100]$ and it is guaranteed that these sequences represent right polygons.
* In a right polygon, the sides do not have common points except at the ends of adjacent sides.
* The first and last sides of a right polygon are perpendicular.

# Example 1

`drept.in`
```
1 2
8
5 3 -3 -1 2 -1 -4 -1
8
-2 1 3 1 -4 -3 2 1
```

`drept.out`
```
1 0
```

## Explanation

The sequences describe the following figures:

~[drept.png]

# Example 2

`drept.in`
```
2 2
8
5 3 -3 -1 2 -1 -4 -1
4
1 1 -1 -1
```

`drept.out`
```
9 1
```
```
