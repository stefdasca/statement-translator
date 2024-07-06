```markdown
The planar surface of a *pseudo-billiard* table is made up of $n \times n$ square cells with a side length equal to $1$ (one unit), assembled together, arranged in $n$ rows numbered from $1$ to $n$ and $n$ columns, numbered from $1$ to $n$. On the table, $K$ balls are placed, each ball located in the center of a specific cell of the table. A player wants to place a square frame on the surface of the table having the length of the diagonal equal to $D$ units.

He has to answer $m$ questions of the form $x y$. Each question means: how many balls are found **inside** or **on the sides of the frame**?

The frame is placed such that each corner is positioned **in the center** of a cell, the opposite corners are found on the same column, respectively in the same row, and the "top" corner is placed **in the center** of the cell found at row $x$ and column $y$.

# Task
Knowing the side length $n$ of the table, the number of $m$ questions, the number of $K$ balls placed on the table, their positions and the length $D$ of the diagonal of the square frame, it is required to:
1. Determine the number of cells which will be found **entirely** inside the frame, if it is placed on the table surface as described above.
2. Provide one answer for each of the $m$ questions.

# Input data
The input file `pseudobil.in` contains on the first line a natural number $p$. For all input tests, the number $p$ can only have the value $1$ or $2$.

The second line contains the natural numbers $n$, $K$, and $D$ separated by a space.

On each of the following $K$ lines, there are two numbers $a$ and $b$ ($a, b \leq n$) representing the row and column of the cell in the center of which a ball will be placed.

On line $K + 3$ there is a natural number $m$.

The following $m$ lines contain two natural numbers $x$ and $y$, representing the row and column of the cell in the center of which the "top" corner of the frame will be placed.

# Output data
If the value of $p$ is $1$, **only point 1** from the task will be solved. In this case, the output file `pseudobil.out` will contain a single natural number $n_1$, representing the number of cells that will be found **entirely** within the frame.

If the value of $p$ is $2$, **only point 2** from the task will be solved. In this case, the output file `pseudobil.out` will contain $m$ lines. On each line $i$ will be written a natural number $n_2$, representing the answer to question $i$.

# Constraints and clarifications
- $3 \leq n \leq 1\ 500$
- $1 \leq K \leq 55\ 000$
- $2 \leq D \leq n – 1$ and $D$ is an even number
- $1 \leq m \leq 100\ 000$
- The positions of the frame are distinct.
- Values for $x$ and $y$ are guaranteed so that the frame is placed within the surface of the pseudo-billiard table.
- For correctly solving the first point, 20 points are awarded, and for the second point, 80 points are awarded.
- For the first $35\%$ of the tests which verify point 2, the relations $m \leq 1\ 000$ and $n \leq 500$ are respected.
- For the first $75\%$ of the tests which verify point 2, the relations $m \leq 10\ 000$ and $n \leq 1\ 000$ are respected.

# Example 1
`pseudobil.in`
```
1
5 2 4
3 4
5 2
1
1 3
```
`pseudobil.out`
```
5
```
## Explanation
$p = 1$, $n = 5$, $K = 2$, $D = (3 + 2 \cdot 0.5) = 4$
**Attention! For this test only point 1 from the task is solved.**
\
The number of cells located entirely inside the frame is $n_1 = 5$.
~[0.jpg|width=20em]

It is observed that in this case it is sufficient to read the data from the first two lines.

# Example 2
`pseudobil.in`
```
2
6 5 4
2 3
1 1
5 6
4 4
3 5
2
1 3
2 4
```
`pseudobil.out`
```
3
2
```
## Explanation
$p = 2$, $n = 6$, $K = 5$, $D = 4$.
**Attention! For this test only point 2 from the task is solved.**
\
The first question is $1\ 3$. There are two balls on the sides of the frame and one inside, so $n_2 = 3$.
~[1.jpg|width=20em]

The second question is $2\ 4$. One ball is on one of the sides of the frame and one inside, so $n_2 = 2$.
~[2.jpg|width=20em]
```