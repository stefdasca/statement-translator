Expand

K0kalaru47 has a polygon. A convex polygon with $N$ vertices is given. You can move a vertex $A$ of the polygon to another point $B$ in the plane, only if the Euclidean distance from $A$ to $B$ is at most $R$.

## Task

Move the vertices of the polygon so that the area of the resulting polygon is as large as possible.
Scoring You have access to the tests here and to the commission's polygons here. Let $A$ be the maximum area of the polygon obtained by the commission, $A$ be the area of the polygon obtained by the contestant on the same test, and $A$ be the area of the polygon from the input on that test. Let .

The number of points you receive on a test is equal to:
- $P$ scoring
  - $P$ < 30 $\to$ 0 points
  - $30 \leq P$ < 50 $\to$ 1 point
  - $50 \leq P$ < 60 $\to$ 2 points
  - $60 \leq P$ < 70 $\to$ 3 points
  - $70 \leq P$ < 80 $\to$ 4 points
  - $80 \leq P$ < 90 $\to$ 5 points
  - $90 \leq P$ < 95 $\to$ 6 points
  - $95 \leq P$ < 98 $\to$ 7 points
  - $98 \leq P$ < 99 $\to$ 8 points
  - $99 \leq P$ < 100 $\to$ 9 points
  - $100 \leq P$ $\to$ 10 points

## Input data

The input file `expand.in` contains on the first line a number $T$, representing the test number. The second line contains two natural numbers $N$ and $R$. The next $N$ lines contain two real numbers, separated by a space, representing the coordinates $x$ and $y$ of the vertices of the first polygon. The vertices of the polygon are given in either clockwise or counterclockwise order.

## Output data

The output file `expand.out` will contain on $N$ lines the coordinates that make up the polygon, i.e., on line $i$ will contain the coordinates to which you moved point $i$.

## Constraints and clarifications

$2 \leq N \leq 50$
It is guaranteed that if we can move a vertex $A$ of the polygon to a point $B$ in the plane, then there is no other vertex of the polygon that can be moved to $B$.
In tests $1$ and $2$, the input polygons are regular.

## Example

`expand.in`
```
0
4 1
0 0
4 0
4 4
0 4
```

`expand.out`
```
-0.707107 -0.707107
4.70711 -0.707107
4.70711 4.70711
-0.707107 4.70711
```

## Explanation

We move vertex $A$ to $A'$, vertex $B$ to $B'$, vertex $C$ to $C'$, and vertex $D$ to $D'$.