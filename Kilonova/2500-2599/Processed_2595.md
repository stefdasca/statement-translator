```markdown
Costin has a square matrix $A$ with $N$ rows (numbered from top to bottom from $1$ to $N$) and $N$ columns (numbered from left to right from $1$ to $N$). Initially, all elements of the matrix are equal to $0$. A sequence of $M$ operations will be performed on the matrix $A$, of the following types:
* $1 \\ i_1 \\ j_1 \\ i_2 \\ j_2 \\ X$ - add the value $X$ to all elements in the submatrix with the top-left corner at $(i_1, j_1)$ and bottom-right corner at $(i_2, j_2)$. In other words, all elements $A_{i,j}$ with $i_1 \leq i \leq i_2$ and $j_1 \leq j \leq j_2$ are incremented by $X$.
* $2 \\ K$ - the matrix will be rotated $K$ times by 90 degrees to the left (see fig. 1, for $K = 1$).
* $3$ - horizontal flip (the first row becomes the last row, the second becomes the penultimate, and so on, see fig. 2)
* $4$ - vertical flip (the first column will become the last column, the second will become the penultimate, and so on - see fig. 3)

~[img1.jpg]

# Task

Write a program that, given $N$, and a sequence of $M$ operations, displays the resulting matrix after performing the operations in order.

# Input data

The input file `matrix.in` contains on the first line the number $N$, the second line contains the number $M$, and on the following $M$ lines, the $M$ operations in sequence, in the form described in the statement, one operation per line.

# Output data

The output file `matrix.out` will contain $N$ lines, each containing $N$ numbers separated by spaces, describing the resulting matrix after performing the operations.

# Constraints and clarifications

* $1 \leq N \leq 1\ 500$
* $1 \leq M \leq 100\ 000$
* $1 \leq X, K \leq 1\ 000\ 000\ 000$
* All numbers in the input file are natural.

|#|Score|Constraints|
|-|-|-|
|1|10|$1 \leq N, M \leq 200$, there are only operations of type 1|
|2|25|$1 \leq N, M \leq 200$.|
|3|17|there are only operations of type 1; without additional constraints|
|4|24|there are only operations of type 1, 3, and 4; without additional constraints|
|5|24|without additional constraints|

# Example

`matrix.in`
```
3 5
1 2 2 3 3 2
2 2
1 1 2 3 3 1
3
4
```

`matrix.out`
```
1 1 0
1 3 2
1 3 2
```
```