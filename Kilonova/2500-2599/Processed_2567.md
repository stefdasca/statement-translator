```markdown
Given $N$ points in a plane, $(x_i, y_i)$ with integer, non-negative coordinates and $q$ queries of the form $l_i \\ r_i$, with $l_i \\leq r_i$.

The angle between two lines is defined as the measure in degrees of the acute or right angle formed between the two lines. If the lines are parallel or coincide, the angle measure is $0$ degrees.

~[img.png]

- In figures (a)-(d) of the given image, some possible relative positions of the points $p_1$, $p_2$, and the line Ox are illustrated. The dashed horizontal lines in the figures are considered to be parallel to the Ox axis. The angle formed by the line $p_1p_2$ and the Ox line is considered to be the angle $\\alpha$ in the figure. In case (d), the angle has a zero measure, with the line $p_1p_2$ being horizontal.

# Task
For any two points among the given ones, which have the $y$ ordinate in the interval $[l_i, r_i]$, calculate the angle formed by the line connecting them and the Ox axis. Determine the minimum among these angles. If there are not at least two points in the given interval, the answer to the query is $-1$.

For the $q$ given queries, determine the required answer.

# Input data
The input file `puncte.in` contains on the first line the number of points $N$ and the number of queries $q$.

Each line $i$ of the next $N$ lines contains the coordinates of point $i$: $(x_i, y_i)$. It is guaranteed that there are no coinciding points.

Each line $i$ of the next $q$ lines contains the numbers $l_i$ and $r_i$, with the meaning from the statement.

# Output data
The output file `puncte.out` will contain $q$ lines, each line $i$ containing the answer for the $i$-th query.

Print the answers with at least 3 correct decimals (the difference between the committee's answer and the displayed answer must be $\\le 10^{-3}$).

# Constraints and clarifications

- $1 \\leq N \\leq 3 \\cdot 10^5$
- $1 \\leq x_i, y_i \\leq 3 \\cdot 10^5$
- $1 \\leq q \\leq 10^6$

| #  | Points | Constraints                           |
|----|--------|---------------------------------------|
| 1  | 12     | $N \\leq 100$, $q \\leq 100$         |
| 2  | 24     | $N \\leq 5\\ 000$, $q \\leq 5\\ 000$ |
| 3  | 37     | $N \\leq 2 \\cdot 10^5$, $q \\leq 2 \\cdot 10^5$ |
| 4  | 27     | Without additional constraints        |

# Example
`puncte.in`
```
7 4
3 6
2 7
5 8
1 1
5 20
17 30
18 25
1 5
8 8
7 20
20 30
```
`puncte.out`
```
-1
-1
18.434949
21.037511
```
```