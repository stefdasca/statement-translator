A little old man has $m$ grandchildren and a forest that he wants to divide into $m$ parts to clarify its situation through the will. The forest consists of $m \cdot n$ trees encoded by the numbers $1, 2, ..., m \cdot n$, for which the coordinates in the plane are known. To achieve the fairest possible division, the old man wants to determine $m$ disjoint areas in the form of convex polygons that each contain $n$ trees inside or on the boundary. The areas must have their vertices in trees from the forest. The codes of the trees on the border of each area will be written in the will to avoid any dispute among the grandchildren.

# Task

Write a program to determine a way to divide the forest under the previously specified constraints.

# Input data

The input file `testament.in` will contain on the first line the numbers $n$ and $m$, and on the next $m \leq n$ lines, the coordinates of the trees in the order of encoding: abscissa ordinate.

# Output data

The output file `testament.out` will contain $m$ lines, each of these lines containing: $k$ and $q$ followed by $k$ numbers separated by a space representing the codes of the trees that are the vertices of a forest area in the will in a counterclockwise direction, followed by $q$ numbers representing the codes of the trees that are inside or on the edge of the land surface, except for the vertices, for each grandchild. $k$ represents the number of vertices of the forest area and $q$ represents the number of trees inside the area.

# Constraints and clarifications

- $3 \leq n \leq 100$
- $1 \leq m \leq 100$
- The coordinates of the trees are integers with an absolute value $< 32 \ 000$.
- The counterclockwise direction is opposite to the direction of the clock hands.
- Two areas are disjoint if their interiors have an intersection equal to the empty set and their frontiers have an empty intersection. The trees have distinct positions.
- If there are multiple solutions, one of them will be displayed.

# Example

`testament.in`
```
4 2
6 1
4 8
2 1
3 9
2 6
6 6
3 20
0 10
```

`testament.out`
```
4 0 6 5 3 1
3 1 2 7 8 4
```

## Explanation

The first forest area has corners in trees $6$, $5$, $3$, $1$, and the second in trees $2$, $7$, $8$. The second forest area contains tree $4$ inside.