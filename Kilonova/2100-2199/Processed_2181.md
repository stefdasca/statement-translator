To avoid boring the contestants with overly long and complicated statements, the committee presents you with the following problem. Given $N$ points on a plane with integer coordinates, cover the points with a minimum number of broken lines, each line satisfying the following requirements:

* A broken line must start from a point with integer coordinates.
* At each step, the line must be extended from the current point $(x, y)$ to one of the 3 points: $(x-1,y+1)$, $(x,y+1)$, $(x+1,y+1)$.

# Task
Determine the minimum number of broken lines that cover all given points.

# Input data

The input file `linii.in` contains:

* The first line contains a natural number $N$, representing the number of points.
* The next $N$ lines each contain two integers $X$ and $Y$, separated by a space, representing the coordinates of a point.

# Output data

The output file `linii.out` will contain the first line, a natural number representing the minimum number of broken lines that cover all $N$ points.

# Constraints and clarifications

* $1 \leq N \leq 300\ 000$
* The coordinates of the $N$ points are integers in the range $[0, 100\ 000\ 000]$
* The points are not necessarily distinct; if there are multiple coinciding points, they are considered simultaneously covered by the same broken line.

# Example

`linii.in`
```
5
1 1
6 4
3 3
3 5
5 2
```

`linii.out`
```
2
```

## Explanation

~[linii.png]