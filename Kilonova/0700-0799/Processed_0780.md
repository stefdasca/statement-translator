# Task

In the final stage of the **_Little Artists' Team Contest_**, two teams $A$ and $B$ tied for first place with the same score. The Evaluation Committee, to separate them, introduced a new tiebreak event that targets both the talent and cleverness of the children.

Thus, team $A$ must create a black-and-white collage using a white rectangular board and $n$ black rectangles. The members of this team will have to stick all the rectangles onto the board, with their sides parallel to the sides of the board. There may also be rectangles stuck inside another rectangle, or rectangles that intersect, or rectangles with sides on the edges of the board, as well as areas of the board not covered by rectangles.

After placing all the rectangles, team $A$ must inform team $B$ of the number $n$ of black rectangles received, the length $m$ of the horizontal side of the board, the length $p$ of the vertical side of the board, and the coordinates of the bottom-left and top-right corners of each rectangle on the board (coordinates referring to the Cartesian reference $xOy$ with the origin $O$ in the bottom-left corner of the board and the coordinate axis $Ox$, respectively $Oy$, on the right edge of the horizontal side, respectively the vertical side of the board).

To win the contest, team $B$ must guess the number of maximal contiguous white regions contained in the collage created by team $A$. A white region is considered contiguous if any two points $P, Q$ in that region can be connected by a straight or broken line that does not intersect the interior of any black rectangle. A maximal contiguous white region is considered maximal if there is no other larger contiguous white region that includes that region.

# Task

Write a program that reads the number $n$ of black rectangles received by team $A$, the lengths $m$ and $p$ of the sides of the board, the coordinates of the bottom-left and top-right corners of each black rectangle received, and determines the number of maximal contiguous white regions present in the collage created by team $A$.

# Input data

The input file `colaj.in` contains:
- The first line contains a natural value $n$, representing the number of black rectangles given to team $A$.
- The second line contains $2$ natural numbers, separated by a space, representing the lengths of the sides of the board.
- The next $n$ lines each contain four natural numbers, separated by a space, representing the coordinates $(a_1, b_1)$ and $(c_1, d_1)$ of the bottom-left and top-right corners of the first rectangle,..., the coordinates $(a_n, b_n)$ and $(c_n, d_n)$ of the bottom-left and top-right corners of the $n$-th rectangle.

# Output data

The output file `colaj.out` will contain a single line that will print a single natural number representing the number of maximal contiguous white regions contained in the collage.

# Constraints and clarifications

* $1 \leq n \leq 100$
* $a_1 < c_1 \leq m, \ a_2 < c_2 \leq m, ..., \ a_n < c_n \leq m$
* $b_1 < d_1 \leq p, \ b_2 < d_2 \leq p, ..., \ b_n < d_n \leq p$
* All the coordinates of the vertices of the rectangles and the lengths of the sides of the board are natural numbers, $0 < m, p < 8 \ 000$
* If $(x, y)$ and $(z, t)$ are the coordinates of vertices of two distinct rectangles, then: $x≠z$ and $y≠t$.
* In $40\%$ of the tests: $n < 30, m \leq 180, p \leq 180$
* In $40\%$ of the tests: $70 \leq n \leq 100, 180 < p < 1 \ 000, 180 < m < 1 \ 000$
* In $20\%$ of the tests: $50 < n < 80, 7 \ 000 < m < 8 \ 000, 7 \ 000 < p < 8 \ 000$

# Example

`colaj.in`
```
7
17 16
1 1 10 5
2 6 8 8
0 9 17 15
3 2 4 11
5 3 6 12
7 4 12 13
14 10 16 14
```

`colaj.out`
```
6
```

## Explanation

$n=7, m=17, p=16.$
There are $7$ black rectangles.
The collage created by team $A$ is the one in the adjacent drawing. There are $6$ maximal contiguous white regions (the ones numbered in the adjacent figure).

~[8478697f35a31fcf85f5fa15f11235c8.png]