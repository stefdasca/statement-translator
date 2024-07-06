Ionică received a game made of triangular pieces of different sizes and a magnetic surface on which they can be placed from his father for his birthday. On the magnetic surface, a right triangle with the lengths of the legs $a$ and $b$ respectively and a coordinate system $xOy$ with the origin in the right angle of the triangle is drawn, with the semi-axis $[Ox$ along the leg of length $a$, and the semi-axis $[Oy$ along the leg of length $b$. At one point, Ionică places $n$ pieces on the magnetic board, for which the coordinates of their vertices are known. Ionică's father wants to check if the pieces on the board form a **partition** of the drawn right triangle, that is if the following conditions are satisfied:
- there are no overlapping pieces;
- the pieces cover the entire drawn portion (in the shape of a right triangle);
- there are no portions of pieces outside the drawn triangle.

# Task

Check if the pieces placed on the magnetic board form a **partition** of the right triangle drawn on the magnetic board.

# Input data

The input file `part.in` contains on the first line a natural number $k$, representing the number of data sets in the file. Followed by $k$ groups of lines, one group for each data set. The group of lines corresponding to a set consists of a line with the numbers $a$, $b$, $n$ separated by a space and $n$ lines with six integers each separated by spaces representing the coordinates of the vertices (x-coordinate and y-coordinate) of the $n$ pieces, one piece per line.

# Output data

In the file `part.out` there will be $k$ lines, one line for each data set. On line $i$ ($i = 1, 2, \ldots, k$) print $1$ if the triangles in data set $i$ form a **partition** of the triangle drawn on the magnetic board, or $0$ otherwise.

# Constraints and clarifications

* $1 \leq n \leq 150$
* $1 \leq k \leq 10$
* $a$, $b$ are integers between $[0, 31\000]$
* The coordinates of the vertices of the pieces are integers between $[0, 31\000]$.

# Example

`part.in`
```
2
20 10 4
0 5 0 10 10 5
0 0 10 5 0 5
0 0 10 0 10 5
10 0 20 0 10 5
20 10 2
0 0 0 10 10 5
0 0 20 0 20 10
```

`part.out`
```
1
0
```

## Explanation

Figure for data set $1$

~[part1.png]

Figure for data set $2$

~[part2.png]