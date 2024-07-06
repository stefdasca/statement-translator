On a square board of size $n \cdot n$, a sequence of right-angled isosceles triangles is drawn.

~[Poza1.png|align=right]

Each triangle has its vertices numbered $1$, $2$, and $3$ ($2$ corresponds to the right angle, and the order $1, 2, 3$ of the vertices is counterclockwise - see the figure).

The triangles have their legs parallel to the edges of the board. The first triangle, with a leg length of $Lg$, has its vertex $1$ at row $L$ and column $C$ and is oriented as shown in the figure.
The game consists of attaching a new triangle to one of the vertices $2$ or $3$ of the current triangle. If it is attached to corner $2$, the new triangle is placed with vertex $1$ in the extension of side $[1,2]$ of the current triangle. If it is attached to corner $3$, it is placed with vertex $1$ in the extension of side $[2,3]$.

Initially, the new triangle is oriented like the previous one. It can be placed on the board if the edges are not exceeded and it does not overlap with another triangle. Otherwise, a single rotation of ${90\degree}$ to the left is performed, obtaining a new orientation of the triangle. If even in this case the new triangle cannot be placed, the game stops.

The area occupied by the first triangle is filled with the letter ‘a’; the area of the second with the letter ‘b’, and so on. When the lowercase letters of the English alphabet are exhausted, it starts again from 'a'.

# Task

Given the size of the board, the position of the first triangle (row, column), the leg length, and a sequence of triangles to be attached, it is required to generate the final matrix.

The game ends if a triangle can no longer be attached or all the triangles described in the sequence have been placed.

# Input data

In the input file `joc.in`, the first line contains $n$ (the size of the board). The second line contains $L$ (the row), $C$ (the column), and $Lg$ (the leg length) of the first triangle, separated by a space. The next lines, until the end of the file, contain two natural numbers separated by a space, representing the corner of the current triangle to which the next triangle will be attached and the leg length of the next triangle.

# Output data

In the output file `joc.out`, print the resulting matrix. The cells of the board that are not filled with letters of the alphabet will be filled with `.`.

# Constraints and clarifications

* $1 \leq n \leq 100$
* $1 \leq C, L \leq n$
* $2 \leq Lg \leq n$
* Each line in the input file and output file ends with an end-of-line marker

# Example

`joc.in`
```
20
16 8 4
3 5
2 3
3 4
2 3
3 5
3 3
2 2
3 4
2 3
3 3
3 2
3 3
3 3
2 4
```

`joc.out`
```
....................
....................
..........fffffeee..
..........ffff..ee..
..........fff....e..
..........ff..dddd..
..........f....ddd..
......hhggg...b.dd..
......h.gg...bb..d..
jjjiiii.g...bbb..c..
jj.iii.....bbbb.cc..
j..ii.....bbbbbccc..
k..i......a.........
kk.......aa.........
kkkl....aaa.........
...llm.aaaa.........
.....mm.............
.....mmmn...........
........nn..........
........nnn.........
```

# Explanation

Triangle ‘a’ is placed in row $16$ column $8$ and has a leg length of $4$.

Triangle ‘b’ is attached to corner $3$ and has a leg length of $5$.

Triangle ‘c’ is attached to corner $2$ and has a leg length of $3$. Triangles 'a', 'b', and 'c' keep the same arrangement.

Triangle ‘d’ cannot be attached in the same arrangement to corner $3$ because it has a leg length of $4$ and exceeds the board. We rotate the triangle ${90^{ \large \circ }}$ to the left and obtain a new arrangement.

Triangle ‘e’ is attached to corner $2$ and has a leg length of $3$ in the current arrangement.

Triangle ‘f’ cannot be attached in the same arrangement to ‘e’ at corner $3$ because it has a leg length of $5$ and exceeds the board. We rotate the triangle ${90^{ \large \circ }}$ to the left and get a new arrangement.

Triangle 'f' is attached to corner $3$, has a length of $5$, and a new arrangement.

The algorithm continues until the 14th triangle, 'n'. The 15th triangle can no longer be placed.