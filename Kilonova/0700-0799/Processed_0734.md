In the latest adaptation of the famous Shakespearean play, Romeo and Juliet live in a modern city, communicate via email, and even learn to program. In a poignant sequence, their inner struggles are depicted as they unsuccessfully try to write a program to determine an optimal meeting point.

They analyzed the city map and represented it as a matrix with $n$ rows and $m$ columns, where zones that can be traversed (safe streets) are marked with spaces and zones that cannot be traversed are marked with `X`. In the matrix, they also marked the location of Romeo's house with `R` and Juliet's house with `J`.

They can only move through zones marked with spaces, from their current position to any of the 8 adjacent positions (horizontally, vertically, or diagonally).

Since Romeo does not like to wait and will not appreciate being kept waiting, they decided that they need to choose a meeting point that both can reach at the same time, starting from their respective homes. Estimating the time required to reach the meeting point by the number of elements in the matrix that constitute the shortest path from home to the meeting point, and considering there may be multiple possible meeting points, they wish to choose the one for which the travel time is minimized.

# Task

Write a program to determine a position on the map where Romeo and Juliet can arrive at the same time. If there are multiple solutions, the program should determine a solution for which the time is minimal.

# Input data

The input file `rj.in` contains:
* The first line contains the natural numbers `N M`, representing the number of rows and columns in the matrix, separated by a space.
* Each of the next $N$ lines contain $M$ characters (which can only be `R`, `J`, `X` or space) representing the matrix.

# Output data

The output file `rj.out` will contain a single line with three natural numbers separated by a space `tmin x y`, with the following meaning:
* `x y` represents the meeting point ($x$ – the row number, $y$ – the column number);
* `tmin` is the minimal time in which Romeo (and Juliet) reaches the meeting point.

# Constraints and clarifications

* $2 \leq N, M \leq 100$;
* The rows and columns of the matrix are numbered starting from 1.
* For the test data, there is always a solution.

# Example

`rj.in`
```
5 8
XXR  XXX
 X  X  X
J X X  X
      XX
XXX XXXX
```

`rj.out`
```
4 4 4
```

## Explanation

Romeo's path can be:
$(1,3), (2,4), (3,4), (4,4)$
So the time required for Romeo to reach the meeting point from home is $4$.

Juliet's path can be:
$(3,1), (4,2), (4,3), (4,4)$.
The time required for Juliet to reach the meeting point is also $4$.
Moreover, $4$ is the closest point to them with this property.