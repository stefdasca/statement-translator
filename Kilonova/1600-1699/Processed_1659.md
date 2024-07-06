```markdown
A chessboard with $n$ lines and $n$ columns is considered, and $n = 4 \cdot k + 1$. The lines of this board are numbered from top to bottom starting with line $1$, and the columns are numbered from left to right starting with $1$. In each field of this board, a natural number from the set $\{1, 2, \dots, n^2\}$ is written according to the following rules:

* Start from the top-left corner of the board, and advance using the knight's move.
* Move horizontally to the right and continue along the border formed by the first two lines, the first two columns, the last two lines, and the last two columns, **clockwise**;
* Perform several tours of the board until the entire border is filled without jumping twice in the same square, without jumping outside this border, and without leaving any field vacant;
* From the final position reached, it should be possible to jump to the top-left corner of the remaining uncovered square;
* Continue moving inside the remaining uncovered square, using rules a), b), c), d) until the interior square of side $1$ is reached, which will contain the value $n^2$.

Recall that a knight's move consists of a move of two squares horizontally followed by a move of one square vertically or a move of two squares vertically followed by a move of one square horizontally. The knight in the following figure can reach any of the 8 shaded positions with a single jump:

~[horse1.png|align=right]

For example, for $n = 5$, after one tour of the board, the following partial coverage is obtained:

~[horse2.png]

And after the second tour, the partial coverage is as follows:

~[horse3.png]

For $n = 9$, the coverage is as follows:

~[horse4.png]

# Task

Given the value of $n$ representing the size of the board and a number $p$, determine the row and column of the square in the board where number $p$ is written, according to the rules above.

# Input data

The file `horse.in` contains two numbers:

$n$ - the number of lines and columns of the board on the first line
$p$ - the number in a square of the board on the second line

# Output data

The file `horse.out` will contain two numbers: the row and the column of the square where number $p$ is written, separated by a space.

# Constraints and clarifications

* $4 < n < 46\ 340$
* $n = 4 \cdot k + 1$
* $1 \leq p \leq n^2$
* For $50\%$ of the tests $n \leq 1\ 000$

# Example 1

`horse.in`
```
5
24
```

`horse.out`
```
2 1
```

## Explanation

On a $5 \cdot 5$ board, the number $24$ will reach row $2$ and column $1$.

# Example 2

`horse.in`
```
9
36
```

`horse.out`
```
8 9
```

## Explanation

On a $9 \cdot 9$ board, the number $36$ will reach row $8$ and column $9$.

# Example 3

`horse.in`
```
41
1000
```

`horse.out`
```
14 7
```

## Explanation

On a $41 \cdot 41$ board, the number $1 \ 000$ will reach row $14$ and column $7$.
```