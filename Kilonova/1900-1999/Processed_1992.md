
# Task

We consider a rectangular matrix $A$ with $m$ rows and $n$ columns with values $0$ or $1$, the rows and columns being numbered from $1$ to $m$, respectively from $1$ to $n$. We call a rectangle with corners $(x_1, y_1)$, $(x_2, y_2)$ where $x_1 < x_2$ and $y_1 < y_2$ the set of elements $A_{ij}$ with $x_1 \leq i \leq x_2$ and $y_1 \leq j \leq y_2$. We call the perimeter of the rectangle with corners $(x_1, y_1)$, $(x_2, y_2)$ the set of elements $A_{ij}$ for which $x_1 = i$ and $y_1 \leq j \leq y_2$ or $x_2 = i$ and $y_1 \leq j \leq y_2$ or $x_1 \leq i \leq x_2$ and $y_1 = j$ or $x_1 \leq i \leq x_2$ and $y_2 = j$.

Determine the maximum difference between the number of elements equal to $1$ and the number of elements equal to $0$ on the perimeter of the same rectangle, as well as the number of rectangles for which this difference is obtained.

# Input data

The first line of the input file `peri.in` contains the numbers $m$ and $n$, separated by a single space. The following $m$ rows contain the matrix $A$, with the numbers on the same line separated by a space.

# Output data

The output file `peri.out` will contain a single line that contains two integers separated by a space. The first number is the maximum difference between the number of elements $1$ and the number of elements $0$ on the perimeter of a rectangle. The second integer is the number of rectangles for which the difference between the number of elements $1$ and the number of elements $0$ on the perimeter is maximum.

# Constraints and clarifications

* $1 \leq n, m \leq 250$;
* By difference, it is not meant an absolute value difference!

# Example

`peri.in`
```
4 5
1 0 0 1 0
0 1 1 0 0
0 1 0 1 0
1 1 1 0 1
```

`peri.out`
```
4 2
```
