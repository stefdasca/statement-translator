# Drepte3

Given $N$ lines in a plane, consider $S$ to be the set of intersection points between any two lines.

## Task

Determine the minimum area of a rectangle, with sides parallel to the coordinate axes, that contains all points in the set $S$.

## Input data

The input file `drepte3.in` contains on the first line $N$, the number of lines. Each of the following $N$ lines contains 3 integers $a, b, c$, representing the coefficients of the line equation: $ax + by + c = 0$.

## Output data

The output file `drepte3.out` will contain a single real number representing the area of the required rectangle.

## Constraints and clarifications

$2 \leq N \leq 100\ 000$

$-10^5 \leq a, b, c \leq 10^5$

There will be no two parallel lines.

The result will be considered correct if it has an error of at most $10^{-5}$.

## Example

`drepte3.in`
```
3
1 -1 0
0 1 -2
1 0 -1
```

`drepte3.out`
```
1
```

## Explanation

The set $S = \{(1, 1), (1, 2), (2, 2)\}$. The minimum area of a rectangle with sides parallel to the coordinate axes that covers the three points in $S$ is $1$.