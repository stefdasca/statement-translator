# Tri3

Given $K$ points with positive integer coordinates, and $M$ triangles, each with one vertex at the origin and the other two vertices at positive integer coordinates. Determine for each triangle if it has at least one of the given $K$ points inside it. None of the $K$ points lie on the edge of any triangle.

## Input data

The first line of the input file `tri3.in` contains $K$ and $M$. The next $K$ lines contain 2 integers $x$ and $y$, separated by a space, representing the coordinates of the points. The following $M$ lines contain 4 positive integers, separated by a space, $($$x_1$$, $y_1$$)$ and $($$x_2$$, $y_2$$)$, representing the other 2 vertices of the triangle, except for the one at the origin.

## Output data

The output file `tri3.out` contains exactly $M$ lines. Line $k$ contains the character $Y$ if the $k$-th triangle (in the order given in the input file) contains at least one point inside it, or $N$ otherwise.

## Constraints and clarifications

$1 \leq K, M \leq 100\ 000$

$1 \leq$ coordinates of the $K$ points $\leq 10^9$

$0 \leq$ coordinates of the triangle vertices $\leq 10^9$

The triangles are not degenerate (all have a non-zero area).

In 50% of the tests, all triangles have vertices at coordinates $x_1 = 0$ and $y_2 = 0$. This means that two of the triangle's edges lie on the coordinate axes.

## Example

`tri3.in`

```
4 3 
1 2 
1 3 
5 1 
5 3 
1 4 3 3 
2 2 4 1 
4 4 6 3 
```

`tri3.out`

```
Y 
N 
Y 
```

## Explanation

`tri3.in`

```
4 2 
1 2 
1 3 
5 1 
4 3 
0 2 1 0 
0 3 5 0 
```

`tri3.out`

```
N 
Y 
```