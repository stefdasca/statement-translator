In a square matrix with all elements equal to $0$ or $1$, we define a complete segment as a line segment with endpoints on the matrix's contour.

- A complete segment of rank $1$ consists of a row of the matrix with all elements equal to $1$.
- A complete segment of rank $2$ consists of a column of the matrix with all elements equal to $1$.
- A complete segment of rank $3$ consists of a semi-diagonal of the matrix, parallel to the main diagonal (including it) and with all elements equal to $1$.
- A complete segment of rank $4$ consists of a semi-diagonal of the matrix, parallel to the secondary diagonal (including it) and with all elements equal to $1$.

Two or more adjacent segments of the same type form a band of the same rank as these segments.

# Task

Given a binary matrix $n$, determine the matrix's maximum band. If there are multiple such bands, the one with the highest rank ($4$ > $3$ > $2$ > $1$) will be displayed, and among these, the one with the maximum sum of the elements' indices.

# Input data

The input file `banda.in` contains on the first line the value $n$ representing the number of rows; each of the following $n$ lines contains the elements of one row, separated by spaces.

# Output data

The output file `banda.out` will contain in the first line the rank of the band, the second line contains the number of complete segments forming the band, and the third line contains the number of elements in the band.

# Constraints and clarifications

* $0 < n \leq 1\ 000$;
* The existence of a band in each test is guaranteed.

# Example

`banda.in`
```
10
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
0 0 1 1 1 1 1 1 1 0
0 0 0 0 1 1 1 1 1 0
0 0 0 1 1 1 1 1 0 0
0 0 1 1 1 1 1 1 1 0
1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1
0 1 1 0 1 1 1 1 1 1
1 1 1 0 1 0 1 0 0 1
```

`banda.out`
```
3
3
24
```

## Explanation

~[banda.png]

The matrix contains:
- rank $1$: $2$ bands with $2$ lines and $20$ values of $1$;
- rank $3$: $2$ bands with $3$ lines and $24$ values of $1$, respectively $2$ lines and $3$ values of $1$;
- rank $4$: one band with $2$ lines and $19$ values of $1$, respectively one with $2$ lines and $3$ values of $1$.

The maximum band has rank $3$, contains $3$ lines, and has $24$ values of $1$.