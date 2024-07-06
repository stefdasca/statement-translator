Let's consider a chessboard of size $n$ ($n$ is **even**), where its rows and columns are numbered from $1$ to $n$. On this board, each square contains a natural number such that the sum of the numbers on the white squares equals the sum of the numbers on the black squares. 

The neighboring squares of the square with coordinates $(i, j)$, $1 \leq i \leq n$, $1 \leq j \leq n$ are all the squares from the given list: $(i-1, j)$, $(i, j-1)$, $(i+1, j)$, $(i, j+1)$, whose coordinates belong to the interval $[1,n]$.

We define two operations:

1. `1 i j k p x` – add the same natural number $x$ to the values of two **neighboring** squares located at the positions $(i,j)$ and $(k,p)$.
2. `2 i j k p` – subtract from the values of two **neighboring** squares located at the positions $(i,j)$ and $(k,p)$ the minimum value retained at the two positions.

# Task

Using as few operations of type $1$ or $2$ as possible, transform the chessboard into one with only zero values.

# Input data

The input file `sah.in` contains on the first line the natural number $n$, and on the following $n$ lines, each containing $n$ natural numbers representing one line of the matrix.

# Output data

The output file `sah.out` will contain multiple lines. On each line, an operation is defined, so it will contain either six numbers if the operation is of type $1$, or five numbers if the operation is of type $2$.

# Constraints and clarifications
* $2 \leq n \leq 100$ and $n$ is even;
* $0 \leq a_{ij} \leq 500$, for $1 \leq i, j \leq n$;
* $1 \leq i, j,k,p \leq n$ and $0 \leq |x| < 1\ 000\ 000\ 000$;
* $0 \leq a_{ij} \leq 10^{9}$ at any moment of time;
* Values written on the same line in the input file and in the output file are separated by a space.
* If in a test the number of operations you obtain is less than $n^2$ and the operations lead to the zero matrix, then you will receive full marks for that test.
* The specified constraints are for each test, the score being the sum of the points obtained for each test.
* Values written on the same line in the input file and in the output file are separated by a space.
* Any correct solution is accepted.
* You will receive the maximum score (100% of the test value) if the number of operations you obtain is less than $n^2$;
* You will receive partial marks (50% of the test value) if the number of operations you obtain is between $[n^2, 2 * n^2]$;
* You will not receive any marks (0% of the test value) if the number of operations you obtain is greater than $2 * n^2$ or if there are incorrect operations;

# Example

`sah.in`
```
2
7 5
3 1
```

`sah.out`
```
1 2 1 2 2 4
2 1 1 2 1
2 1 2 2 2
```

## Explanation

After the first operation, the matrix becomes:
```
7 5
7 5
```

After the second operation, the matrix becomes:
```
0 5
0 5
```

After the third operation, the matrix becomes:
```
0 0
0 0
```
