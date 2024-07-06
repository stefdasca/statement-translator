~[patratele.jpg|align=right|width=25em]

Gigel has in front of him a math sheet with a drawing obtained by drawing several horizontal and vertical lines of length $1$ along the model of the math sheet.

Gigel learned from his older colleagues a game that is played by two players: they delimit a rectangular area on the math sheet, then, in turn, draw a line on one side of a small square. The one who manages to form the most small squares wins. Gigel's eyes are trained to see a math problem immediately, even if he is playing.

Looking at the drawing on the sheet, he wonders: "How many squares have been formed from the drawn lines?"

In the adjacent drawing, the sheet consists of $3$ rows and $5$ columns, as well as the lines drawn up to a certain point. Three squares of side $1$, two squares of side $2$, and one square of side $3$ can be distinguished.

In our problem, we will encode each square of side $1$ on the sheet with a natural number between $0$ and $15$ obtained by summing the coding of each side as follows:

* $1$ – if the top side is drawn
* $2$ – if the right side is drawn
* $4$ – if the bottom side is drawn
* $8$ – if the left side is drawn

Then the sum of the side codings is made to find the coding of each square. In this way, the drawing can be encoded through a two-dimensional array of size $3 \times 5$ with the following values:

```
9 7 15 13 7
14 15 11 15 11
1 3 12 7 14
```

# Task

Given the dimensions $n$ and $m$ of the math sheet, as well as the two-dimensional array of size $n \times m$ containing the coding of the sheet, determine:

* the total number of squares present on the math sheet in the drawing according to the coding
* the distribution of the number of squares in strictly increasing order of side lengths
* where an additional line can be drawn so that the total number of squares increases and becomes maximized

# Input data

The input file `patratele.in` contains on the first line three natural numbers $n\\ m\\ t$, separated by a space, indicating the dimensions of the math sheet $n \times m$, respectively the task to be solved ($1, 2$ or $3$). Each of the following $n$ lines contains $m$ natural numbers, each representing the coding of the math sheet.

# Output data

The output file `patratele.out` will contain the following, depending on the required task:

* If $t = 1$, the first line will contain the total number of determined squares;
* If $t = 2$, each line will display two non-zero natural numbers $a$ and $b$, separated by a space, indicating the side length of the squares ($a$), respectively the number of squares with the side of the respective length ($b$), in strictly increasing order of $a$ values;
* If $t = 3$, the first line will contain the maximum number of squares, and the second line will contain two natural values $lin, col$ and a word $poz$ separated by a space, where $lin, col$ represent the coordinates of the square of side $1$ where the additional line is drawn, and $poz \in \{$`TOP`$, `RIGHT`$, `BOTTOM`$, `LEFT`$, `NO`$\}$ (it will display `NO` if no line can be drawn — in this case, the three numerical values displayed will also be $0$).

# Constraints and clarifications

* The numbering of the rows and columns of the math sheet starts from $1$.
* If for task $t=3$ multiple positions for drawing the line are obtained, the solution with the minimum row index will be displayed, and in case of equality after rows, the solution with the minimum column index will be displayed. In case there are multiple possibilities to draw a line in the same square, the positions will be taken in the order `TOP`, `RIGHT`, `BOTTOM`, `LEFT`.
* $1 \leq n, m \leq 60$
* For $30$ points, $t = 1$.
* For $30$ points, $t = 2$.
* For $10$ points, $t = 3$ and $1 \leq n, m \leq 20$.
* For $30$ points, $t = 3$.

# Example 1

`patratele.in`
```
3 5 1
9 7 15 13 7
14 15 11 15 11
1 3 12 7 14
```

`patratele.out`
```
6
```

## Explanation

Task $1$ is solved. A total of $6$ squares have been found.

# Example 2

`patratele.in`
```
3 5 2
9 7 15 13 7
14 15 11 15 11
1 3 12 7 14
```

`patratele.out`
```
1 3
2 2
3 1
```

## Explanation

Task $2$ is solved.

$3$ squares of side $1$

$2$ squares of side $2$

$1$ square of side $3$

# Example 3

`patratele.in`
```
3 5 3
9 7 15 13 7
14 15 11 15 11
1 3 12 7 14
```

`patratele.out`
```
9
2 5 BOTTOM
```

## Explanation

Task $3$ is solved. If an additional line is drawn at the square in row $2$ column $5$ bottom, $3$ more squares are obtained.

# Example 4

`patratele.in`
```
3 3 3
9 1 3
8 0 2
12 0 0
```

`patratele.out`
```
0
0 0 NO
```

## Explanation

Task $3$ is solved. No new square can be added by drawing a single line.