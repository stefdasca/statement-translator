The Rectangle $ABCD$ has sides of length $w$ and $h$, which are even natural numbers.

~[Poza2.png|align=right]

This rectangle is drawn on a graph paper and is divided into $w \cdot h$ squares of side $1$. The vertices $A$, $B$, $C$, and $D$ are placed at the corners of these squares of side $1$. We select a point $P$ inside the rectangle $ABCD$, located at a corner of a square of side $1$ and connect it with the four corners of the rectangle with straight line segments. Some segments intersect squares of side $1$ in exactly two distinct points, while others in just one point.

We call a square $2$-intersected if it is intersected by a segment in exactly $2$ distinct points. In the rectangle in the adjacent figure, the segment $PA$ passes through $3$ $2$-intersected squares, the segment $PB$ passes through $9$ $2$-intersected squares, the segment $PC$ passes through $13$ $2$-intersected squares, and the segment $PD$ through $7$.

# Task

Given two natural numbers $w$ and $h$ representing the lengths of the sides of the rectangle $ABCD$, a natural number $n$, and $n$ natural numbers $x_1, x_2, \ldots, x_n$. The point $P$ is placed, in turn, at all interior points of the rectangle $ABCD$ which are corners of squares of side $1$. For each value $x_i$ ( $1 \leq i \leq n$ ), determine the number of distinct segments that pass through exactly $x_i$ $2$-intersected squares.

# Input data

The input file `intersectii.in` contains on the first line three natural numbers $w$, $h$ (representing the dimensions of the rectangle) and $n$. The following $n$ lines contain one natural number $x_i$ with the above-mentioned significance.

# Output data

The output file `intersectii.out` will contain $n$ lines. Each line $i$ will contain the number of segments that pass through exactly $x_i$ $2$-intersected squares after placing point $P$ at each corner of a square of side $1$ inside the rectangle $ABCD$.

# Constraints and clarifications

* $2 \leq w, h \leq 2 \ 000$ even natural numbers
* $2 \leq n \leq 100 \ 000$
* The point $P$ is chosen only inside the rectangle
* For $40$% of tests $2 \leq w, n, h \leq 500$

# Example

`intersectii.in`
```
4 6 2
3
5
```

`intersectii.out`
```
12
4
```

# Explanation

There can be $12$ segments that pass through exactly $3$ $2$-intersected squares and $4$ segments that pass through exactly $5$ $2$-intersected squares.