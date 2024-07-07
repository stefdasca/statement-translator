
A fence is made up of several rectangular panels. Each panel is, in turn, constructed from $N \times M$ bricks. One of the panels poses a problem because it is damaged. The panel is represented on paper using a matrix with $N$ rows and $M$ columns, numbered from $1$ to $N$, and from $1$ to $M$ respectively. The matrix contains only $0$ and $1$ values and follows these rules:
* An element equal to $1$ indicates the presence of a brick in that position, while an element equal to $0$ indicates its absence
* Row $1$ and row $N$ contain only $1$ values because the top and bottom edges of the panel are intact
* From any element equal to $1$ located within the matrix, one can reach row $1$, row $N$, or both by moving only up or only down, traversing only values equal to $1$
* There is at least one stable column (composed entirely of elements equal to $1$).

It is desired to modify the panel, and for this, you can delete up to $K$ adjacent columns from the matrix. After deletion, the remaining columns are brought together, and the top part of the panel is vertically shifted downwards until a stable column is formed.

# Task

Determine the minimum height $\\text{Hmin}$ the panel can have by deleting at most $K$ adjacent columns. Identify the minimum number of adjacent columns that need to be deleted to achieve the height $\\text{Hmin}$.

# Input data

The input file `placa.in` contains on the first line $3$ natural numbers $N$, $M$, $K$ separated by a space, having the meaning mentioned in the problem statement. On each of the next $M$ lines of the file, there are pairs of natural numbers $N_1, N_2$ separated by a space. Thus, on the $(i + 1)$th line of the input file, the number $N_1$ represents the number of elements equal to $1$ located on column $i$, starting with row $1$ and moving "down" until encountering a value equal to $0$, or until reaching row $N$; the number $N_2$ represents the number of elements equal to $1$ located on column $i$, starting with row $N$ and moving "up" until encountering a value equal to $0`, or until reaching row $1$.

# Output data

The output file `placa.out` will contain on the first line the required minimum height $\\text{Hmin}$, and on the second line the minimum number of columns that need to be removed to achieve the height $\\text{Hmin}$.

# Constraints and clarifications

* $1 \\leq N \\leq 100\ 000$
* $1 \\leq M \\leq 100\ 000$
* $1 \\leq K \\lt M$
* It is guaranteed that on the lines containing information about the $M$ columns of the matrix, there is at least one line where the value $N$ appears twice, otherwise the sum of the two values is strictly less than $N$
* All values in the file are strictly positive
* $30\\%$ of the points are granted if only the first value is correct and $70\\%$ of the points are granted if only the second value is correct

# Example

`placa.in`
```
5 6 3
1 1
2 1
1 2
5 5
1 3
1 1
```

`placa.out`
```
3
2
```

## Explanation

The initial matrix:
$1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1$
$0 \\ 1 \\ 0 \\ 1 \\ 0 \\ 0$
$0 \\ 0 \\ 0 \\ 1 \\ 1 \\ 0$
$0 \\ 0 \\ 1 \\ 1 \\ 1 \\ 0$
$1 \\ 1 \\ 1 \\ 1 \\ 1 \\ 1$

The minimum height is $3$ and can be obtained by eliminating, for example, columns $3, 4, 5$ resulting in the matrix:
$1 \\ 1 \\ 1$
$0 \\ 1 \\ 0$
$1 \\ 1 \\ 1$

Another way to achieve the same height but by removing the minimum number of columns ($4$ and $5$) leads to:
$1 \\ 1 \\ 1 \\ 1$
$0 \\ 1 \\ 1 \\ 0$
$1 \\ 1 \\ 1 \\ 1$
```

Please verify the English grammar and syntax for coherence.
