```markdown
A monotonic matrix is a matrix where each row is ordered increasingly from left to right and each column is ordered increasingly from top to bottom. A submatrix is a rectangular region in a matrix that consists of consecutive rows and columns. The task is to determine a maximal monotonic submatrix (with the maximum number of elements) in a given matrix. If there are multiple submatrices with the maximum number of elements, the submatrix with the smallest possible top-left corner will be displayed.

# Input data

The first line of the input file `mmm.in` contains two integers, $n$ and $m$, representing the dimensions of the matrix.

Each of the following $n$ lines contains $m$ values, representing the values of the matrix. 

# Output data

The first line of the output file `mmm.out` will contain two integers, $k$ and $p$ - representing the number of rows and columns of the maximal monotonic submatrix. If there are multiple options, the one with the minimum number of rows will be displayed.

The second line of the output file `mmm.out` will contain two integers, $x$ and $y$ - the row and column of the top-left corner of the maximal monotonic submatrix. If there are multiple solutions, the leftmost one will be displayed. If there are multiple solutions with the top-left corner on the same row, the one from the smallest column will be displayed.

# Constraints and clarifications

* $1 \leq n, m \leq 100$;
* The elements of the matrix are integers between $0$ and $99$.
* The tests and constraints have been revised for the standards of the year $2023$, and the display format has also been modified compared to the original statement.

# Example 1

`mmm.in`
```
4 5
2 4 4 8 8
1 4 5 10 9
7 9 8 13 17
10 11 14 15 16
```

`mmm.out`
```
4 2
1 3
```

# Example 2

`mmm.in`
```
5 6
2 0 5 4 8 7
1 2 4 6 8 14
0 4 7 8 10 12
4 8 8 10 13 15
6 6 10 12 11 16
```

`mmm.out`
```
2 6
3 1
```
```