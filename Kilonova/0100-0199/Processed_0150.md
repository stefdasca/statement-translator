# Task
Given a convex polygon with `N` sides, `N - 1` moves will be made. A move consists in selecting two neighboring points `A` and `B` on the polygon and moving point `A` to `B` (see figure). The cost of the move is equal to the Euclidean distance between `A` and `B`. After the move, point `A` is assimilated by `B`, and the process is repeated on the new polygon. We are asked to find the minimum total cost of a sequence of `N - 1` moves that reduces the polygon to a single point, as well as a way to achieve this cost.

~[enunt_poligon.jpg]

# Task
Given `T` convex polygons, determine:
1. The minimum cost `ans` of a sequence of moves that reduces the polygon to a single point;
2. A sequence of minimum-cost moves.

# Input data
The input file `poligon.in` contains on the first line an integer `p`, representing the number of the task to be solved.
The second line of the input file will contain `T`, representing the number of polygons to be read. Then, the `T` tests follow. Each test has the following structure:
- on the first line, a natural number `N`, representing the number of sides of the polygon;
- on the next `N` lines, `2` integers `x` and `y`, separated by a space, representing the coordinates of the vertices of the current polygon. The vertices are given in a trigonometric order.

# Output data
The output file `poligon.out` will contain, depending on the value of `p`, the following information:
1. If `p = 1`, solve only task `1`. For each of the `T` tests, print a real number `ans` on a line, meaning indicated in the statement.
2. If `p = 2`, solve only task `2`. For each of the `T` tests, print `N-1` lines, each of the form `A B`, representing the moves in the order in which they are made.

# Constraints and clarifications
* `1 \leq T \leq 5`
* `1 \leq N \leq 2000`
* For all polygon vertices `-1 000 000 \leq x, y \leq 1 000 000`
* There will not be `2` vertices of the polygon located at the same coordinates.
* The polygon is not necessarily strictly convex. In other words, there can be any number of consecutive collinear vertices.
* For tests worth `5` points, `N \leq 7`;
* For other tests worth `10` points, `N \leq 15`;
* For other tests worth `15` points, `N \leq 50`;
* For other tests worth `15` points, `N \leq 100`;
* For other tests worth `15` points, `N \leq 500`;
* For other tests worth `40` points, `N \leq 2000`;
* For solving task `1`, `80%` of the test score is awarded.
* For solving task `2`, `20%` of the test score is awarded.
* The value of `ans` is considered correct if it differs from the correct answer by a maximum of $10^{-6}$.
* **ATTENTION!** After a move `A B` (where vertex `A` has been assimilated by vertex `B`), a move of the form `A C` or `C A` will be considered invalid.

# Example

`poligon.in`
```
1
2
4
0 0
1 0
1 1
0 1
5
0 0
8 0
8 10
4 20
0 10
```

`poligon.out`
```
3
36.770329614269
```

Explanation
---
In this case `p = 1`, so only task `1` will be solved.
The file contains `T = 2` polygons.
The vertices of the first polygon are `(0, 0), (1, 0), (1, 1), (0, 1)`. The minimum cost associated with a sequence of minimum-cost moves is `3`.

The vertices of the second polygon are `(0, 0), (8, 0), (8, 10), (4, 20), (0, 10)`. The minimum cost associated with a sequence of minimum-cost moves is `36.770329614269`.

`poligon.in`
```
2
2
4
0 0
1 0
1 1
0 1
5
0 0
8 0
8 10
4 20
0 10
```

`poligon.out`
```
3 2
4 1
2 1
4 3
5 3
3 2
2 1
```

Explanation
---
In this case `p = 2`, so only task `2` will be solved.
The file contains `T = 2` polygons.
The vertices of the first polygon are `(0, 0), (1, 0), (1, 1), (0, 1)`. The minimum cost associated with a sequence of minimum-cost moves is `3`. A sequence of minimum-cost moves is:
```
3 2
4 1
2 1
```
The vertices of the second polygon are `(0, 0), (8, 0), (8, 10), (4, 20), (0, 10)`. The minimum cost associated with a sequence of minimum-cost moves is `36.770329614269`. A sequence of minimum-cost moves is:
```
4 3
5 3
3 2
2 1
```