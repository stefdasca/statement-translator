# Local Transport in the City of ISANOTOB

Local transport in the city of ISANOTOB is optimally solved with the help of minibuses. The routes have been designed in such a way that two minibuses do not share any common road segment, except for intersections. Any route can be represented as a segment or a polyline made up of several perpendicular segments. The polyline can be open or closed.

The routes are stored on a rectangular map made up of $n \cdot m$ identical squares. These squares are denoted by $a_{i, j}$. We will also assign a coordinate system to the map with $n \cdot m$ points, with the Ox coordinate axis oriented to the right, and the Oy axis oriented downwards. At the intersection of the axes is the point with coordinates $(0,0)$, so the bottom-right corner of each square $a_{i, j}$ has coordinates $(i,j)$.

Two routes can intersect, but **cannot have any common segment**. In figure $1$, on a map of dimensions $4 \cdot 3$, we see four routes:

1. The first route, drawn with a double line, starts from the point with coordinates $(1,2)$ and arrives at the point with coordinates $(1,2)$. This is a closed route (cycle). It would be equally correct if the starting point were $(2,2)$ and the stopping point $(2,2)$; the map would not change.
2. The second route, drawn with a triple line, starts from the point with coordinates $(3,1)$ and ends at the point with coordinates $(3,3)$.
3. The third route, drawn with a dotted line, has the starting and ending points at the coordinates $(4,1)$ and $(2,2)$, respectively.
4. The fourth route, drawn with a dashed line, has the starting and ending points at the coordinates $(4,1)$ and $(2,2)$, respectively.

Next, we are interested in the segments on the map without knowing which route they belong to. That’s why we will draw all the routes with a thick line. This map is stored as a matrix of size $n \cdot m$, and we will call it the route matrix, in which each element $a_{i,j}$ is equal to the number of segments that are part of any route, so the possible values can be $0$, $1$, $2$, $3$, or $4$. The route matrix in figure $2$ corresponds to the route map in figure $1$.

A map-matrix of dimensions $3n \cdot 3m$ is another method of displaying the route map, in which any node with coordinates $(i,j)$ will be replaced with a node-matrix of dimensions $3 \cdot 3$. Any node-matrix element can have 16 distinct values depending on the existing connections to the North, South, East, or West:

~[trasee.png|align=center]

# Task

Given the route matrix and all the starting and ending points of the routes, compute the corresponding map-matrix.

# Input data

The input file `trasee.in` contains on the first line the numbers $n \ m \ k$ separated by spaces, where $n$ and $m$ have the meanings from the statement, and $k$ is the number of routes on the map. The next $n$ lines contain $m$ numbers each, separated by spaces, representing the route matrix. The following $k$ lines contain four natural numbers $x \ y \ u \ v$ each, separated by a space, representing the starting and ending coordinates of the $k$ routes on the map, $(x,y)$ and $(u,v)$ respectively.

# Output data

The output file `trasee.out` will contain $3 \cdot n$ lines with $3 \cdot m$ digits $0$ or $1$ **not separated by spaces**, representing the map-matrix corresponding to the route map.

# Constraints and clarifications

* $3 \leq m,n \leq 500$
* $1 \leq k \leq 350 \ 000$
* any correct solution is accepted
* each route has **at least one** segment, each segment belongs to **only one** route
* for $25\%$ of the tests $m,n < 10$
* for another $25\%$ of the tests $m,n < 40$

# Example

`trasee.in`
```
4 3 4
0 0 1
0 2 4
1 4 3
1 4 2
1 2 1 2
3 3 3 1
2 2 4 1
4 1 2 2
```

`trasee.out`
```
000000000
000011110
000010010
000010010
011111110
010010000
010010000
011111110
010010000
010010000
011110000
000000000
```

## Explanation

$n=4$, $m=3$, $k=4$

The route matrix of dimensions $4 \cdot 3$ is the one in figure $2$. We have $4$ routes highlighted in figure $1$ between the points with coordinates 

$(1,2)$ and $(1,2)$, $(3,3)$ and $(3,1)$, $(2,2)$ and $(4,1)$, and $(4,1)$ and $(2,2)$ respectively.

The map-matrix in the output file is the one in figure $3$.