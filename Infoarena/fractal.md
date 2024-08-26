# Fractal

Hilbert found a curve that can pass through every point in space. This curve is based on a recursive construction. We call the Hilbert curve of order $K$ the curve that, following these rules, passes through each node of a grid of $2^K \times 2^K$ nodes and passes through neighboring nodes of the grid. The Hilbert curve of order 1 is a simple curve:
The transitions from a curve of order $x$ to a curve of order $x+1$ will be described in the following images:
Order 1 $\rightarrow$ Order 2
Order 2 $\rightarrow$ Order 3
Order 3 $\rightarrow$ Order 4
Order 4 $\rightarrow$ Order 5
We are given as input from the file fractal.in the numbers $K$, $x$, and $y$, where $K$ is the order of a curve, and $x$ and $y$ are integer coordinates inside a square of size $2^K \times 2^K$. 

## Task

You are required to write to the output file fractal.out the number of steps it takes to reach the coordinates $(x,y)$ if the points in the square are traversed in the order given by the Hilbert curve of order $K$. 

## Constraints

$1 \leq k \leq 15$

$1 \leq x,y \leq 2^K$

Coordinates $x$ and $y$ are between $1$ and $2^K$ inclusive ($x$ represents the column, $y$ the row), and the top-left corner has coordinates $(1,1)$.

## Examples

`fractal.in`
```
1 1 1
```

`fractal.out`
```
0
```

`fractal.in`
```
3 2 3
```

`fractal.out`
```
13
```

`fractal.in`
```
2 4 1
```

`fractal.out`
```
15
```