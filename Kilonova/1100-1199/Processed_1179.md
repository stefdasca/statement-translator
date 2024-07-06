Here is the translated text:

---

A monotone matrix is a matrix where, if read by rows from left to right or by columns from top to bottom, the traversed values are increasing. A submatrix is a rectangular region from a matrix with the property that it is formed from consecutive rows and columns. The task is to determine a maximal monotone submatrix from a given matrix. If there are multiple such submatrices, you will write as a result only one of those with the minimum number of rows.

# Input data

The first line of the input file `mmm.in` contains two integers, $n$ and $m$, representing the dimensions of the matrix. 

Each of the following $n$ lines contain $m$ values, representing the values of the matrix.

# Output data

The first line of the output file `mmm.out` will contain two integers $k$ and $p$ representing the number of rows and columns of the maximal monotone matrix.

The next $k$ lines will contain $p$ values, representing the values from the found maximal monotone matrix.

# Constraints and clarifications

* $1 \leq n, m \leq 100$
* The elements of the matrix are integers ranging between $0$ and $99$.
* If there are multiple such submatrices, any of those with the minimal number of rows will be displayed.

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
4 8
5 10
8 13
14 15
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
0 4 7 8 10 12
4 8 8 10 13 15
```

---