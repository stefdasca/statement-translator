# Camera

Zebu recently bought a new plot of land where he wants to expand his chicken business, but he is very worried about thieves that could affect the wellbeing of his business. A friend who recently visited the States gave him a very advanced video camera as a gift, which has the ability to film with a 360-degree angle. Zebu is very happy with this acquisition, which he can use immediately to monitor the newly purchased plot. However, the camera cannot supervise the entire plot if it is placed at just any point, and Zebu is curious about the area where the camera can be positioned so that all points of the plot can be monitored. We can model the plot as a polygon with $N$ vertices, and the camera as a point inside this polygon.

## Task:

Determine the area where the camera can be placed!

## Input data:

The file `camera.in` will contain a line with an integer representing the value of $N$. The next $N$ lines will contain two integers separated by a single space, with the $i+1$-th line containing the coordinates of the $i$-th vertex.

## Output data:

The file `camera.out` will contain a single real number with two decimal places representing the area where the camera can be placed.

## Constraints and clarifications:

$3 \leq N \leq 2000$

$-100000 \leq x_i, y_i \leq 100000$, $(x_i, y_i)$ are the coordinates of the polygon vertices.

For 20% of the tests, the edges of the plot will be parallel to the coordinate axes.

Two real numbers are considered equal if the difference between them is at most $10^{-6}$.

A result will be considered correct if the difference between it and the result returned by the official solution is $\leq 0.01$.

## Example:

`camera.in`
9
5 1
5 2
1 3
3 4
2 8
5 5
9 6
7 3
9 2

`camera.out`
2.86

## Explanation