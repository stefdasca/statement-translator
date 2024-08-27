## Geometry

The set $A$ contains $N$ points $A_i$ in a plane with known integer coordinates $(A_i.x, A_i.y)$. For a query defined by a point $Q = (Q.x, Q.y)$, you are asked to find the area of the convex hull of the points: $\{Q\} ∪ \{A_i | A_i.x < Q.x$ and $A_i ∈ A\}$. Determine the answer for a series of $M$ queries of this type relative to the initial set $A$. The convex hull of a set of points is the convex polygon of minimal area that contains all the points inside or on its edges.

## Input data

The first line of the file `geometrie.in` contains the non-zero natural numbers $N$ and $M$. The following $N$ lines contain two numbers $A_i.x$ $A_i.y$ separated by space. The next $M$ lines contain two numbers $Q.x$ $Q.y$ separated by space. In the input file, both the points $A_i$ and points $Q$ are in increasing order of their $x$ values.

## Output data

The file `geometrie.out` must contain $M$ lines with the answers to the queries in order. Print the answer with one decimal precision.

## Constraints and clarifications

• $N, M \leq 10^5$

• $0 \leq A_i.x, A_i.y, Q.x$, and $Q.y \leq 10^9$

• The points in the set $A$ have distinct $A_i.x$ values.

• The convex hull of a set with at most two points has an area equal to zero.

• For 20 points worth of tests, $N \leq 3$

• For 40 points worth of tests, $N \times M \leq 10^3$

• For 60 points worth of tests, $N \times M \leq 10^6$

## Example

`geometrie.in` `geometrie.out`
3 3
1 3
4 5
5 1
3 3
6 8
8 4
`0.0`
`15.0`
`14.5`

`geometrie.in` `geometrie.out`
9 2
1 3
3 5
4 1
6 4
8 6
9 1
10 3
11 5
13 2
4 3
10 4
`3.0`
`32.0`

## Explanation for the second example:

Given the input file, for the first query $(4, 3)$, the points within its $x$ coordinate (greater than or less than $4$) define the convex hull area, which results in $3.0$. For the second query $(10, 4)$, the points within its $x$ coordinate define a larger convex hull area, which results in $32.0$.