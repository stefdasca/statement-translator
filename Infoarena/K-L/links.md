# Links

Given $N$ points in the plane by their coordinates. Additionally, $Q$ pairs of points, different from the initially given ones, are provided.

## Task

Verify for each pair of points $(A, B)$ among the $Q$ pairs if there is a path that starts at $A$ and reaches $B$ by moving 1 step towards North, West, South, or East while avoiding any of the $N$ initially given points.

## Input data

The first line of the text file `links.in` contains the natural numbers $N$ and $Q$, separated by a space. The next $N$ rows contain two natural numbers each, separated by a space, representing the coordinates of the $N$ given points. The next $Q$ rows contain four natural numbers each, separated by a space, representing the coordinates of the $Q$ pairs of points for the requested verifications.

## Output data

On each of the first $Q$ lines of the output file `links.out`, there will be written one of the numbers $1$ (true) or $0$ (false), representing the answer to the corresponding verification, depending on whether there is a path or not between the points of the given pair in the query.

## Constraints and clarifications

$1 \leq N \leq 10^5$

$1 \leq Q \leq 10$

The coordinates of all given points are positive natural numbers less than $10\^9$

For $30\%$ of the tests, the coordinates of all given points will be positive natural numbers less than $10^3$

## Example

`links.in`

```
4 2
1 2
2 1
3 2
2 3
1 1 2 2
1 1 1 3
```

`links.out`

```
0
1
```

## Explanation

The point $(1,1)$ can only be reached by passing through $(2,3)$, $(2,1)$, $(1,2)$, $(3,2)$ which are the $4$ given points and thus need to be avoided. Therefore, it is not possible to reach from $(1,1)$ to $(2,2)$. The correct answer is $0$. From $(1,1)$ to $(1,3)$, it is possible to reach by the path: $(1,1)$, $(0,1)$, $(0,2)$, $(0,3)$, $(1,3)$. The correct answer is $1$.