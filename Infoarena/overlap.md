# Overlap

Given $N$ points in a plane with integer coordinates $x_i$, $y_i$. These are rotated by $k*90$ degrees $(k = 0, 1, 2$ or $3)$ and/or translated, resulting in another $N$ points, which are pairwise different from the first ones.

## Task

Given $N$ (an even number) points, determine a division of them into two subsets of cardinality $\frac{N}{2}$ such that the second subset can be obtained from the first one through the described operations.

## Input data

The input file `overlap.in` contains:

- The first line contains $N$, the number of points.
- The next $N$ lines each contain a pair $x_i$, $y_i$ - the $i$-th line contains the coordinates of the $i$-th point.

## Output data

The output file `overlap.out` will contain $N$ lines. Each line will contain a single character $1$ or $2$ indicating that the points labeled with $1$ are part of the first set, and the points labeled with $2$ are part of the second set. If there are multiple solutions, any of them is acceptable; the existence of at least one solution is guaranteed.

## Constraints and clarifications

$1 \leq N \leq 800$

$0 \leq x_i, y_i \leq 100\ 000$

By "rotation," it is meant fixing an arbitrary point in the plane and rotating all initial points relative to it.

By "translation," it is meant choosing constant numbers $shift\_x$ and $shift\_y$, and transforming the coordinates $(P_{ix}, P_{iy})$ into $(P_{ix} + shift\_x, P_{iy} + shift\_y)$ for any point $i$.

## Example

`overlap.in`
```
6
5 5
9 1
6 1
3 2
6 3
3 5
```

`overlap.out`
```
1
2
2
1
2
1
```