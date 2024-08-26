# Circle

We consider $N$ circles in a plane. The task is to determine the number of finite regions into which the given circles divide the plane. 

## Input data

The input file `cerc.in` contains:
- The first line contains $N$.
- The next $N$ lines each contain three integers in the form $x_i$ $y_i$ and $r_i$, representing the coordinates of the center and the radius of the $i$-th circle.

## Output data

The output file `cerc.out` will contain the number of regions determined by the given circles.

## Constraints and clarifications

$1 \leq N \leq 200$ 

The coordinates of the circles are integers in the interval $[0, 10\ 000]$ 

The radii of the circles are integers in the interval $[1, 1\ 000]$

## Example

`cerc.in`
```
4
90 110 50
130 70 30
155 45 15
165 115 65
```

`cerc.out`
```
11
```