## Task

Write a program that reads the natural number $n$ and the coordinates of the $n$ points $A_1$, $A_2$, $\dots$, $A_n$, and determines:
1. the coordinates of the bottom-left and top-right vertices of the minimum area rectangle, with sides parallel to the coordinate axes and containing within or on its edges all the $n$ points;
2. the maximum number of perfect segments that can connect point $A_1$ with points $A_2$, $A_3$, $\dots$, $A_n$. 

## Input data

The input file `perfect2.in` contains:
- The first line contains a natural number $p$; 
  for all input tests, the number $p$ can only be either $1$ or $2$;
- The second line contains a natural value $n$ representing the number of points chosen from set $A$;
- Each of the following $n$ lines contains two non-zero natural numbers, separated by a single space, representing the coordinates $(x_1, y_1)$ of point $A_1$, $\dots$, the coordinates $(x_n, y_n)$ of point $A_n$. 

## Output data

If the value of $p$ is $1$, then only task $1$ will be solved. In this case, the output file `perfect2.out` will contain on the first line four natural numbers separated by spaces, representing the abscissa and ordinate of the bottom-left vertex, and top-right (in this order) of the minimum area rectangle, with sides parallel to the coordinate axes and containing within or on its edges all the $n$ points representing the answer to task $1$.

If the value of $p$ is $2$, then only task $2$ will be solved. In this case, the output file `perfect2.out` will contain on the first line a natural number representing the maximum number of perfect segments that can connect point $A_1$ with points $A_2$, $A_3$, $\dots$, $A_n$ representing the answer to task $2$. 

## Constraints and clarifications

$n$ is a non-zero natural number,
$3 \leq n \leq 200\ 000$

$x_1$, $x_2$, $\dots$, $x_n$, $y_1$, $y_2$, $\dots$, $y_n$ are non-zero natural numbers 
$1 \leq x_1$, $x_2$, $\dots$, $x_n \leq 4\ 500$;

$1 \leq y_1$, $y_2$, $\dots$, $y_n \leq 4\ 500$;

at least three points out of the chosen $n$ are not collinear;

the $n$ points in the plane are distinct two by two;

for the correct solution of the first task, $20$ points are awarded, and for the second task, $80$ points are awarded.

## Example

`perfect2.in`

`perfect2.out`

$1$
$7$
$8$ $3$
$3$ $1$
$1$ $4$
$5$ $4$
$7$ $2$
$6$ $5$
$4$ $2$

$1$ $1$ $8$ $5$

`2`
$11$
$5$ $3$
$1$ $5$
$1$ $4$
$3$ $4$
$5$ $4$
$6$ $5$
$4$ $2$
$3$ $1$
$7$ $2$
$8$ $3$
$1$ $1$

$6$

## Explanation

Attention! For the first example, only task $1$ is resolved! $7$ points are chosen:
$A_1 (8,3)$, $A_2 (3,1)$, $A_3 (1,4)$, $A_4 (5,4)$, $A_5 (7,2)$, $A_6 (6,5)$, $A_7 (4,2)$. The minimum area rectangle, with sides parallel to the coordinate axes and containing within or on its edges all the $n$ points has the bottom-left vertex at coordinates $(1,1)$ and the top-right vertex at coordinates $(8,5)$.

Attention! For the second example, only task $2$ is resolved! $11$ points are chosen:
$A_1 (5,3)$,
$A_2 (1,5)$,
$A_3 (1,4)$,
$A_4 (3,4)$,
$A_5 (5,4)$,
$A_6 (6,5)$,
$A_7 (4,2)$,
$A_8 (3,1)$,
$A_9 (7,2)$,
$A_{10} (8,3)$,
$A_{11} (1,1)$.

There are at most $6$ perfect segments that can connect point $A_1$ with points $A_2$, $A_3$, $\dots$, $A_{11}$. These are: $A_1 A_3$, $A_1 A_4$, $A_1 A_5$, $A_1 A_6$, $A_1 A_7$, $A_1 A_9$.

Segment $A_1 A_{11}$ is not perfect because it contains the point with coordinates $(3,2)$. Segment $A_1 A_{10}$ is not perfect because it contains the points with coordinates $(6,3)$ and $(7,3)$. Segment $A_1 A_2$ is not perfect because it contains point $A_4$. Segment $A_1 A_8$ is not perfect because it contains point $A_7$.