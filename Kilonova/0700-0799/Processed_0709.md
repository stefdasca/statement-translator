A triangulation of a convex polygon is a set of diagonals of the polygon that do not intersect within the polygon except at vertices and divide the entire surface of the polygon into triangles.

# Task

Given a polygon with $n$ vertices labeled $1, 2, ..., n$, generate all distinct triangulations of the polygon. Two triangulations are distinct if they differ by at least one diagonal.

# Input data

In the text file `triang.in`, the first line contains a single natural number representing the value of $n$.

# Output data

In the text file `triang.out`, write:

- the first line contains the number of distinct triangulations;
- each of the following lines contains the code of a triangulation, in any order. The code is formed using the diagonals that compose the triangulation. A diagonal is specified by two numbers representing the two vertices that define it.
$$\text{code = } \prod {( \min(d_1,d_2)\cdot 137+\max(d_1,d_2) )} \text{ mod } (10^9+7)$$, where $d_1$ and $d_2$ are the vertices of a diagonal in the decomposition, and the product is taken over all diagonals in the decomposition (consider $1$ for the empty set).

# Constraints and clarifications

* $1 \leq n \leq 16$
* $20\\%$ of the score is awarded for the number of distinct triangulations
* The statement and restrictions have been modified

# Example

`triang.in`
```
5
```

`triang.out`
```
5
19740
77562
116064
58240
39198
```

## Explanations
~[triang.png]

The decompositions are:
$(1,3), (1,4)$
$(2,4), (2,5)$
$(5,2), (5,3)$
$(3,5), (3,1)$
$(4,2), (1,4)$

$$ (137 \cdot 1 + 3) \cdot (137 \cdot 1 + 4) \text{ modulo } 10^9+7 = 19740$$