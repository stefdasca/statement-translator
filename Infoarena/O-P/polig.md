## Task

Lucy really likes pink flowers and convex polygons. She knows the location of $N$ gardens (the gardens are represented as points in a plane) that contain many pink flowers, and she wants to visit some of these gardens riding her unicorn to see the maximum number of flowers. Between any two gardens, there is a single direct path formed by the segment that joins them. Another wish of hers is that the path taken should have the shape of a convex polygon. She will always start from her house, located at the origin of the plane (coordinate $(0, 0)$), and will return here at the end of the route. Determine the maximum number of flowers she can see.

## Input data

The input file `polig.in` contains:

- The first line contains $N$ with the meaning given in the statement.
- The next $N$ lines each contain three integers $x$, $y$, and $c$, where the line $i+1$ represents the coordinates and the number of flowers in garden $i$.

## Output data

The output file `polig.out` should contain a single number, the maximum number of flowers she can see.

## Constraints and clarifications

$1 \leq N \leq 100$

$-10000 \leq x_i \leq 10000$

$0 \leq y_i \leq 10000$

$0 \leq c_i \leq 10000$

A polygon is convex if it does not contain an angle with a measure strictly greater than $180$ degrees

Any three points are non-collinear

There are no two points that are collinear with the origin

At least $20 \%$ of the tests will have $N \leq 15$

## Example

`polig.in`

$7$

$-14$ $12$ $14$

$4$ $10$ $5$

$6$ $14$ $20$

$11$ $18$ $15$

$-8$ $13$ $16$

$-2$ $11$ $14$

$-4$ $11$ $1$

`polig.out`

$50$

## Explanation

Lucy starts from the coordinate $(0, 0)$, then visits gardens $3$, $5$, and $1$ in that order, and returns to the coordinate $(0, 0)$.