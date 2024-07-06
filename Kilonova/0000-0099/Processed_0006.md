We will form a sequence of points that are vertices with integer coordinates, in a grid. Every two consecutive points in the sequence define a vertical or horizontal segment of length $1$. We will call this sequence a "path". We consider such paths formed from $N$ segments that are "non-intersectable" (any two segments that are not consecutive on the path do not intersect and do not have common points). Also, we want the first segment on the path to connect the points with coordinates $(0,0)$ and $(1,0)$, and the first vertical segment to go upwards.

# Task

Write a program `trap` that calculates the total number of non-intersectable paths in a square grid obtained after $N$ steps that cannot be further extended because adding the next $(N+1)$-th segment will cause self-intersection.

# Input data

The first line contains an integer $N$.

# Output data

The first line contains an integer corresponding to the number of non-intersectable paths of length $N$ that cannot be extended.

# Constraints
- $1 \leq N \leq 26$

# Example

`stdin`
```
8
```

`stdout`
```
2
```

## Explanations

Two non-intersectable paths of length 8 are:

- $(0,0); (1,0); (2,0); (2,1); (2,2); (1,2); (0,2); (0,1); (1,1)$;
- $(0,0); (1,0); (1,1); (2,1); (3,1); (3,0); (3, -1); (2, -1); (2,0)$.

They are also drawn in the figures below:

~[1.png]

~[2.png]