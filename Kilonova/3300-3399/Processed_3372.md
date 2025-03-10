
# Task

After getting frustrated that you need $O(N^3)$ operations to multiply 2 matrices, you thought of the following matrix multiplication algorithm:
<br>
Two matrices of size $N$ x $N$ are multiplied by rotating the second matrix by 90 degrees clockwise. Then, element by element, the result in the cell $(i,j)$ is equal to the product of the elements from the two matrices at positions $(i,j)$ plus their sum.
Formally, if we have $A \cdot B = M$ and $C$ is the matrix $B$ rotated 90 degrees to the right, then $M_{i,j} = A_{i,j} \cdot C_{i,j} + A_{i,j} + C_{i,j}$.
<br>
Given a matrix $M$, how many pairs of matrices $(A, B)$, with natural elements, exist such that $A \cdot B = M$?
The answer is very large, so the result will be displayed as the remainder when divided by $998244353$.

# Input data

The first line contains $N$, followed by the matrix $M$.

# Output data

Print the number of matrix pairs requested modulo $998244353$.

# Constraints and clarifications

* $1 \leq N \leq 1000$
* $0 \leq M_{i,j} \leq 10^6$

# Example 1

`stdin`
```
2
0 0
0 1
```

`stdout`
```
2
```

## Explanation

One pair is:

A=$\begin{pmatrix}
   0 & 0 \\
   0 & 0
\end{pmatrix}$

and 

B=$\begin{pmatrix}
   0 & 1 \\
   0 & 0
\end{pmatrix}$

Matrix $B$ is rotated and composed with $A$ as described resulting exactly in the matrix from the input.

The other pair is:

A=$\begin{pmatrix}
   0 & 0 \\
   0 & 1
\end{pmatrix}$

and 

B=$\begin{pmatrix}
   0 & 0 \\
   0 & 0
\end{pmatrix}$


# Example 2

`stdin`
```
4
8 12 54 1
43 34 1 32
0 0 123 34
101 64 72 10
```

`stdout`
```
28311552
```
