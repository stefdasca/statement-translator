## Task

A rectangular hallway with dimensions $M*N$ is considered. In this hallway, there are several straight columns of negligible size. Determine the radius of the largest spherical ball that can traverse the hallway from the west end to the east end. For the ball, any starting point at the west end and any ending point at the east end can be chosen. The height of the corridor is always sufficiently large.

## Input data

The input file `hallway.in` contains two integers $M$ and $N$, separated by a single space, representing the dimensions of the corridor in the east-west and north-south directions, respectively. The second line contains a single number $K$, representing the number of columns in this hallway. Each of the next $K$ lines contains two integers, separated by a single space, which represent the coordinates at which a column is located.

## Output data

The output file `hallway.out` must contain a single number representing the radius of the largest spherical ball that can traverse the hallway from the west end to the east end.

## Constraints and clarifications

$1 \leq M, N, K \leq 1000$

The east-west direction is represented by the first coordinate

The determined radius of the ball must be written with 8 decimals, rounded at the last one.

## Example

`hallway.in`

```
5 2
1
1 1
```

`hallway.out`

```
0.50000000
```