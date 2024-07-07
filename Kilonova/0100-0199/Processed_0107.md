
A matrix with $N$ rows and $2$ columns of integers is given. The rows are numbered from $1$ to $N$, and the columns from $1$ and $2$.

There are $4$ operations that can be performed on the matrix: $S_3, J_3, S_4, J_4$.

In a $J_k$ operation, $k$ (distinct) rows of the matrix are selected and permuted circularly downwards, and in an $S_k$ operation, $k$ (distinct) rows are selected and permuted circularly upwards ($k=3,4$).

$$
\begin{vmatrix}
\cdots & \cdots \\
x_1 & x_2 \\
\cdots & \cdots \\
y_1 & y_2 \\
\cdots & \cdots \\
z_1 & z_2 \\
\cdots & \cdots \\
\end{vmatrix}
\rightarrow
\begin{vmatrix}
\cdots & \cdots \\
z_1 & z_2 \\
\cdots & \cdots \\
x_1 & x_2 \\
\cdots & \cdots \\
y_1 & y_2 \\
\cdots & \cdots \\
\end{vmatrix}
\\
$$

$$
\text{Operation } J_3
$$

$$
\begin{vmatrix}
\cdots & \cdots \\
x_1 & x_2 \\
\cdots & \cdots \\
y_1 & y_2 \\
\cdots & \cdots \\
z_1 & z_2 \\
\cdots & \cdots \\
\end{vmatrix}
\rightarrow
\begin{vmatrix}
\cdots & \cdots \\
y_1 & y_2 \\
\cdots & \cdots \\
z_1 & z_2 \\
\cdots & \cdots \\
x_1 & x_2 \\
\cdots & \cdots \\
\end{vmatrix}
\\
$$

$$
\text{Operation } S_3
$$

The operations $S_4$ and $J_4$ are similar, only that instead of $3$ rows, $4$ are chosen.

# Task
Write a program that, by performing at most $2N$ operations of type $S_3, J_3, S_4, J_4$ on the given matrix, transforms it so that none of its columns contain a strictly increasing subsequence of length greater than $\\lceil \\sqrt{N} \\rceil$ (i.e., the smallest integer greater than or equal to $\\sqrt{N}$).

# Input data
The input file `matrice.in` contains on the first line the natural number $N$. Each of the following $N$ lines contains $2$ integers separated by a space, representing the matrix elements.

# Output data
The output file `matrice.out` will contain one operation per line. An operation is identified by its type (it can be `J3`, `S3`, `J4` or `S4`) and $3$ numbers (for `J3` and `S3`) or $4$ numbers (for `J4` and `S4`) in strictly increasing order, representing the rows on which the operation is executed. The type of the operation and the other numbers must be separated by exactly one space.
**Attention!** The type of the operation consists of two characters written without a space between them.

# Constraints and clarifications
* $6 \leq N \leq 30\ 000$;
* A strictly increasing subsequence of a sequence $a_1, a_2, ..., a_N$ is a sequence $a_{i_1}, a_{i_2}, ..., a_{i_k}$, where $1 \leq i_1 < i_2 < ... < i_k \leq N$ and $a_{i_1} < a_{i_2} < ... < a_{i_k}$;
* The elements of the matrix are integers greater than or equal to $0$ and less than or equal to $65\ 000$.

# Example

`matrice.in`
```
6
1 2
3 1
4 4
6 3
5 5
2 6
```

`matrice.out`
```
S4 1 3 4 5
J3 4 5 6
```

Explanation
---

After performing the operations, the matrix will be
```
4 4
3 1
6 3
2 6
5 5
1 2
```
The length of the longest strictly increasing subsequence on the first column is $2$, and on the second it is $3$ ($2$ and $3$ are less than or equal to $\\lceil \\sqrt{N} \\rceil = \\lceil \\sqrt{6} \\rceil = 3$).
