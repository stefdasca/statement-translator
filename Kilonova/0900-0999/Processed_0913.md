We have a matrix of dimensions $N \cdot M$, with elements $0$ and $1$. We call a segment a sequence of at least two $1$s next to each other, all on the same row or all on the same column of the matrix.

# Task

Determine the number of pairs of segments:

1. located on distinct rows of the matrix;
2. located on distinct columns of the matrix;

# Input data

The file `paralele.in` contains on the first line, separated by a space, three natural values in order: $T, N$, and $M$. If $T$ is $1$, only requirement $1$ needs to be solved, and if $T$ is $2$, only requirement $2$ needs to be solved.
Starting from the second line, the elements of the matrix are found, one row of the matrix per line in the file. Elements on the same line are separated by a space.

# Output data

The file `paralele.out` contains on the first line a natural number representing the requested value.

# Constraints and clarifications

* $1 \leq T \leq 2$;

|#|Score|Constraints|
|-|-|--------|
|1|30|$T = 1, N = 2, 2 \leq M \leq 500$ and all elements $1$ on any of the lines, if they exist, form a compact sequence.|
|2|30|$T = 2, 2 \leq N \leq 500, 2 \leq M \leq 500$ and on any column, there are at most two adjacent values of 1.|
|3|9|$T = 1, 2 \leq N \leq 500, 2 \leq M \leq 500$|
|4|9|$T = 2, 2 \leq N \leq 500, 2 \leq M \leq 500$|
|5|12|$T = 1, 35\ 000 \leq N \leq 40\ 000, 8 \leq M \leq 10$|
|6|10|points from the office|

# Example

`paralele.in`
```
1 5 6
0 1 1 1 0 0
1 0 0 0 0 0
0 0 0 1 0 0
1 1 0 1 1 0
0 1 1 0 0 0
```

`paralele.out`
```
11
```

## Explanation

The first value in the input file being $1$, we are interested in segments formed on rows. On the first row, there is a sequence of $1$ values consisting of three elements. It produces three segments: one with the first two values of $1$, one with the last two values of $1$, and one with all three values of $1$. No segment is found on the second row, as there are not at least two adjacent $1$s. No segment is found on the third row, there are two segments on the fourth row, and there is one segment on the fifth row. 

The requested number is obtained as follows: each of the three segments on the first row is parallel with each of the segments on the fourth and fifth rows, and the segments on the fourth row are parallel with the segment on the last row. For the presented example, if we had $T = 2$, the calculated result would have to be $1$ (the segment on the second column is parallel with the segment on the fourth column).