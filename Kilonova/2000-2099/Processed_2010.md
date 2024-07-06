Princess Rafaela, known for her green eyes, has decided it's time to relinquish the kingdom's problems and play. Thus, she has $N$ point-shaped balls (represented by $N$ points in the Cartesian plane) and $Q$ lines passing through the origin of the coordinate system. For each of the $Q$ lines, the question is which would be the first ball among the $N$ to hit the line if the balls started to fall simultaneously (perpendicular to the Ox axis, with the same speed).

# Task

Given $N$ points in the plane and $Q$ lines (queries), Rafaela wonders what the minimum distance (on the Oy axis) from the points to each line is. You must display in the output file the answer for each of the $Q$ lines.

# Input data

The input file `ydist.in` contains on the first line two natural numbers $N$ and $Q$, separated by a space, representing the number of points in the plane and the number of query lines, respectively. On the next $N$ lines, there are two natural numbers $x$ and $y$, separated by a space, representing the coordinates of the points in the Cartesian plane. On the next $Q$ lines, there are two natural numbers $a$ and $b$, separated by a space, representing the coordinates of the second point through which the query line passes (the first being $(0, 0)$, the second $(a, b)$).

# Output data

The output file `ydist.out` will contain $Q$ lines, each containing a single real number, representing the minimum distance (on the Oy axis) from the points to the respective query line.

# Constraints and clarifications

* $1 \leq N \leq 100\ 000$
* $1 \leq Q \leq 100\ 000$
* The coordinates $x$ and $y$ of all points in the input file are in the range $[1, 1\ 000\ 000]$.
* The result is considered correct if the absolute value of the difference between it and the committee's result is less than $0.00001$.
* It is guaranteed that there is at least one ball above each line.

# Example

`ydist.in`
```
7 3
14 20
4 4
6 6
7 15
5 2
1 20
19 16
5 18
2 4
17 6
```

`ydist.out`
```
16.4
1
0.235294117647059
```

## Explanation

The first query line is: $(0, 0) \rightarrow (5, 18)$, and the minimum distance (on the Oy axis) is given by the point: $(1, 20)$.

The second query line is: $(0, 0) \rightarrow (2, 4)$, and the minimum distance (on the Oy axis) is given by the point: $(7, 15)$.

The third query line is: $(0, 0) \rightarrow (17, 6)$, and the minimum distance (on the Oy axis) is given by the point: $(5, 2)$.