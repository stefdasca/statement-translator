# Mihai's Journey in Image Processing

Mihai is exploring image processing techniques and begins to discover ways to detect object contours in the analyzed photos. Thus, he discovered the concept of applying a kernel to an image.

## Intro to kernels

A kernel is an odd-order square matrix that can be applied over a general matrix through convolution. Convolution is a mathematical operation that involves, in this case, centering the kernel on each pixel of the image (row by row) and calculating a sum over the central pixel and the surrounding pixels, which will replace the pixel in the final image.

For example, let's assume we have the kernel $K$ and the matrix $A$:

$$ K = \begin{bmatrix} 0 & -1 & 0 \\ -1 & 5 & -1 \\ 0 & -1 & 0 \end{bmatrix} $$

$$ A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix} $$

The elements of matrix $A$, after applying the kernel, will have the values:

$$ A = \begin{bmatrix} 0 & 5 \\ 10 & 15 \end{bmatrix} $$

As a general formula, we can consider that applying a kernel produces pixels according to the following formula (where the pixels on the right-hand side used in the calculations are exclusively pixels from the old matrix, or $0$ for those positions where the kernel is applied on a marginal/edge pixel and partially exits the matrix):

$$ A_{\text{new}}[i][j] = \sum_{d_i = -1}^{1} \sum_{d_j = -1}^{1} A[i + d_i][j + d_j] \cdot K[1 + d_i][1 + d_j] $$

For the given matrix $A$, the results are:

* $A_{\text{new}}(0, 0) = 5 \cdot A(0, 0) - A(1, 0) - A(0, 1) - A(-1, 0) - A(0, -1) = 5 \cdot 1 - 3 - 2 - 0 - 0 = 0$
* $A_{\text{new}}(1, 0) = 5 \cdot A(1, 0) - A(2, 0) - A(1, 1) - A(0, 0) - A(1, -1) = 5 \cdot 3 - 0 - 4 - 1 = 10$
* $A_{\text{new}}(0, 1) = 5 \cdot A(0, 1) - A(1, 1) - A(0, 2) - A(-1, 1) - A(0, 0) = 5 \cdot 2 - 4 - 0 - 0 - 1 = 5$
* $A_{\text{new}}(1, 1) = 5 \cdot A(1, 1) - A(2, 1) - A(1, 2) - A(0, 1) - A(1, 0) = 5 \cdot 4 - 0 - 0 - 2 - 3 = 15$

# Task

Mihai decided to create a program to help him understand the application of a specific kernel on any given matrix, but he has a problem. More precisely, he does not obtain the expected results. Help him! The program written by Mihai can be found [here](kernel.cpp) or on the right side of the page under _“Attachments”_.

# Input data

The first line contains the number of rows and columns of the matrix, as well as a maximum value ($maxval$) that no element of the result matrix can exceed.
The following lines contain the matrix.

# Output data

Print the received input data (number of rows/columns and the maximum value), as well as the new values of the elements in the matrix.

# Constraints and clarifications

* The elements in the result must fit within the interval $[0, maxval]$. If exceeded, the value is brought to the nearest end.
* The number of rows or columns of the matrix will not exceed $100$.

# Example 1

`stdin`
```
2 2 100
1 2
3 4
```

`stdout`
```
2 2 100
0 5
10 15
```

# Example 2

`stdin`
```
2 2 10
8 6
-5 1
```

`stdout`
```
2 2 10
10 10
0 4
```

## Explanation

If it weren't limited, the resulting matrix would look like this:

$$ \begin{bmatrix} 39 & 21 \\ -34 & 4 \end{bmatrix} $$