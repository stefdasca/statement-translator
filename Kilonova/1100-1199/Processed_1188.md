Here is the translated problem statement:

# Task

Given a grid of size $M \times N$ with $K$ points placed on it.

Each point can be connected to its direct neighbor in up to eight directions ($N, NE, E, SE, S, SW, W, NW$).

# Task

Determine the quadrilaterals having vertices at the given points and edges formed by connections between two or more collinear points.

# Input data

Input file: `poligon.in`

* Line $1$: $M$, $N$, $K$, three non-zero natural numbers, separated by a space, representing the dimensions $M, N$ of the grid and the number of points $K$.
* Line $2$: $I_1$, $J_1$, $V_1$, three non-zero natural numbers, separated by a space, representing the coordinates of point $1$ and the directions to which it is connected to direct neighbors.
* Line $3$: $I_2$, $J_2$, $V_2$, three non-zero natural numbers, separated by a space, representing the coordinates of point $2$ and the directions to which it is connected to direct neighbors.

$\\ \\ \\ \\ \\ \\ldots$

* Line $K+1$: $I_k$, $J_k$, $V_k$, three non-zero natural numbers, separated by a space, representing the coordinates of point $K$ and the directions to which it is connected to direct neighbors.

The encoding of the directions is done by a number between $0$ and $255$. Its binary representation on $8$ digits represents, starting from left to right, the connections in the directions:

$N \\ NE \\ E \\ SE \\ S \\ SW \\ W \\ NW$

For example:

$1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 1 \\ 0 = 134$ thus connections towards $N$, $SW$, $W$ ($1$ – connection, $0$ – no connection)

# Output data

Output file: `poligon.out`

* Line $1$: $n_{pol}$, a natural number representing the number of quadrilaterals.

# Constraints and clarifications

* $1 < N, M \leq 100$
* $4 \leq K \leq 50$

# Example

`tablou.in`
```
4 4 9
1 1 24
2 1 184
2 2 43
2 3 22
3 1 136
3 2 213
3 4 5
4 1 192
4 3 65
```

`tablou.out`
```
6
```

## Explanation

~[Poza1.png|align=left]