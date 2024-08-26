## Paralelogram2

Lunasorab started drawing on paper. Unfortunately, he got stuck on a problem and needs your help. He gives you a quadrilateral (not necessarily convex) and asks you to choose a point strictly on each of its sides such that the four points you choose form a parallelogram with non-zero area, and each side of the quadrilateral contains exactly one point chosen by you.

## Input data

The input file paralelogram2.in will contain on the first line $T$, the number of test cases. Each test contains $8$ integers, $X_1$ $Y_1$ $X_2$ $Y_2$ $X_3$ $Y_3$ $X_4$ $Y_4$, representing, in order, the vertices of a quadrilateral [$(X_1, Y_1)$ $(X_2, Y_2)$ $(X_3, Y_3)$ $(X_4, Y_4)$].

## Output data

The output file paralelogram2.out will contain $T$ lines, with the $i$-th line containing $8$ real numbers $PX_1$ $PY_1$ $PX_2$ $PY_2$ $PX_3$ $PY_3$ $PX_4$ $PY_4$, representing the vertices of the found parallelogram. The point $(PX_1, PY_1)$ must strictly belong to the side $(X_1, Y_1) - (X_2, Y_2)$, the point $(PX_2, PY_2)$ must strictly belong to the side $(X_2, Y_2) - (X_3, Y_3)$, and so on.

## Constraints and clarifications

$1 \leq T \leq 100$

$0 \leq X_i \leq 1000000$ for $1 \leq i \leq 4$

$0 \leq Y_i \leq 1000000$ for $1 \leq i \leq 4$

It is guaranteed that the quadrilaterals in the input file will not contain 3 collinear vertices

Any valid answer is accepted

Your answer for a test case will be considered correct if and only if the four points form, in order, the vertices of a parallelogram with non-zero area and each side of the quadrilateral contains exactly one point

Your answer will be checked with a precision of $0.0001$ both for the area of the parallelogram and for verifying that the lengths of opposite sides are equal

## Example

`paralelogram2.in` 

`1 0 0 10 0 10 10 0 10`

`paralelogram2.out` 

`9 0 10 1 1 10 0 9`

## Explanation

The initial quadrilateral is a square with vertices at $(0, 0)$, $(10, 0)$, $(10, 10)$, $(0, 10)$. The found parallelogram has vertices at $(9,0)$, $(10, 1)$, $(1, 10)$, $(0, 9)$.