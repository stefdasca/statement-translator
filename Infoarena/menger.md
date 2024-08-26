# Menger

We have a fractal cube positioned with one corner at the origin of the coordinate system, and all other corners at non-negative coordinates. The cube is constructed as follows: 

- The cube of degree $0$ is the unit cube.
- The cube of degree $n+1$ is the set $(x, y, z)$ in $\mathbb{R}^3$ with the property that there exist $i$, $j$, $k$ in $\{0, 1, 2\}$ such that $(3x-i, 3y-j, 3z-k)$ is part of the cube of degree $n$, and at least one of $i$, $j$, $k$ is $1$.

Cubes of degrees $0$, $1$, $2$, $3$ are illustrated to scale in the image below. 

We want to calculate the volume of the intersection of such a cube with a rectangular parallelepiped, having edges parallel to the axes of the coordinate system, with known corners.

## Input data

The input file `menger.in` contains on the first line the number of tests $T$. Each test contains two lines. The first line contains the degree $G$ of the cube. The next line contains $6$ numbers, which represent the coordinates of the points that define a diagonal of the rectangular parallelepiped: $(X1, Y1, Z1)$ and $(X2, Y2, Z2)$, in this order.

## Output data

The output file `menger.out` contains $T$ lines. Each line contains in order the volume of the intersection of the two geometric bodies.

## Constraints and clarifications

$T = 20$ 

$0 \leq G \leq 5$

$0 \leq X1 \leq X2 \leq 10^3$ 

$0 \leq Y1 \leq Y2 \leq 10^3$ 

$0 \leq Z1 \leq Z2 \leq 10^3$ 

## Example

`menger.in`
```
1
0
0 0 0 2 3 4
```

`menger.out`
```
1
```

## Explanation

The input file contains $1$ test. The cube of degree $0$ has a volume of $1$ and occupies the space between $(0, 0, 0)$ and $(1, 1, 1)$. Part of the parallelepiped occupies the same space between $(0, 0, 0)$ and $(1, 1, 1)$, with a volume of $1$. The output file contains $1$ line with this volume.