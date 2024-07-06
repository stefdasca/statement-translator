```markdown
# Task

A lark and a nightingale live in a character matrix of dimensions $N \\cdot N$, the characters being `A`, `B`, and `.`. `A` is a position that the lark can claim, `B` is a position that the nightingale can claim, and `.` is a position that neither bird can claim.

The lark (`A`) wants to claim a piece of land in the shape of a single square. She wants to maximize the area of this square, and the total number of positions in the square is the final score. Below, on the right, is the maximum size square (with a score of $9$) that she can claim (represented by `X`).

```
.BB..A .BB..A
.B...A .B...A
BBBAAA BBBXXX
BBBAAA BBBXXX
..BAAA ..BXXX
...... ...... 
```

The nightingale (`B`) wants to claim a piece of land in the shape of a single square, rotated by $45$ degrees. (You can also think of this shape as a rhombus). She wants to maximize the area of this square, and the total number of positions in the square is her final score. Below, on the right, is the maximum size rhombus (with a score of $5$) that she can claim (represented by `X`).

```
.BB..A .BB..A
.B...A .X...A
BBBAAA XXXAAA
BBBAAA BXBAAA
..BAAA ..BAAA
...... ......  
```

The following are some examples of squares (for the lark) and rotated squares/rhombuses (for the nightingale):

```
..... ..... XXXXX
..... ..XX. XXXXX
..X.. ..XX. XXXXX
..... ..... XXXXX
..... ..... XXXXX

..... ..... ..X..
..... ..X.. .XXX.
..X.. .XXX. XXXXX
..... ..X.. .XXX.
..... ..... ..X..
```

Help them both accomplish their goal quickly!

# Input data

The first line contains $N$, the dimension of the matrix.

In the next $N$ lines, there are $N$ characters each, `A`, `B`, or `.`, representing the positions that can be taken by the lark, the positions that can be taken by the nightingale, and the positions that cannot be taken by either bird.

# Output data

The first line will contain two values: the largest area that the lark can claim and the largest area that the nightingale can claim.

# Constraints and clarifications

* $N \\leq 1 \\ 000$;

|#|Score|Constraints|
|-|-|---------|
|0|0|Example|
|1|30|$N \\le 100$ and the matrix contains only `A` and `.`|
|2|10|$N \\le 100$|
|3|30|The matrix contains only `A` and `.`|
|4|30|No additional constraints|

# Example

`stdin`
```
6
.BB..A
.B...A
BBBAAA
BBBAAA
..BAAA
......
```

`stdout`
```
9 5
```

## Explanation

The explanation for this example is found in the statement.
```