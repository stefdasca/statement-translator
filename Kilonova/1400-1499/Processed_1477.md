```markdown
A matrix with $L$ rows and $C$ columns is considered, which only stores values from the set $\{0, 1, 2\}$. A non-empty submatrix (formed from at least one row and at least one column) of this matrix is called homogeneous if the number of $0$ values is equal to the number of $1$ values and equal to the number of $2$ values. For example, in the matrix

$$
\begin{array} {|r|r|r|r|r|r|r|r|r|}
\hline
0 &1 &2 &0 \\
\hline
1 &2 &0 &1 \\
\hline
\end{array}
$$

there are six homogeneous submatrices, which are:

$$
\begin{aligned}
\text{1)} \begin{array} {|r|r|r|r|r|r|}
\hline
0 &1 &2 \\
\hline
1 &2 &0 \\
\hline
\end{array} &
& \text{2)} \begin{array} {|r|r|r|r|r|r|}
\hline
1 &2 &0 \\
\hline
2 &0 &1 \\
\hline
\end{array} &
& \text{3)} \begin{array} {|r|r|r|}
\hline
0 &1 &2 \\
\hline
\end{array}
\end{aligned}
$$

$$
\begin{aligned}
& \text{4)} \begin{array} {|r|r|r|}
\hline
1 &2 &0 \\
\hline
\end{array} &
& \text{5)} \begin{array} {|r|r|r|}
\hline
1 &2 &0 \\
\hline
\end{array} &
& \text{6)} \begin{array} {|r|r|r|}
\hline
2 &0 &1 \\
\hline
\end{array}
\end{aligned}
$$

The third and fourth submatrices are formed from the first row of the initial matrix, and the fifth and sixth submatrices are formed from the second row.

# Task

Determine how many non-empty homogeneous submatrices exist.

# Input data

The file `omogene.in` contains on the first line the natural numbers $L$ and $C$. The following $L$ lines contain $C$ natural numbers separated by spaces representing each row of the matrix.

# Output data

The file `omogene.out` will contain on the first line a single natural number representing the number of non-empty homogeneous submatrices.

# Constraints and clarifications

* $2 \leq L \leq C \leq 5\ 000$
* $4 \leq L \cdot C \leq 65\ 536$
* Note, a submatrix is formed from a continuous sequence of rows and columns, so for example, if rows $1, 2$ and $5$ are chosen from a matrix, they do not form a submatrix
* The number of homogeneous submatrices will be less than $2 \cdot 10^9$
* The entire matrix can be a homogeneous submatrix

# Example 1

`omogene.in`
```
2 4
0 1 2 0
1 2 0 1
```

`omogene.out`
```
6
```

# Explanation

The six submatrices were mentioned in the statement.

# Example 2

`omogene.in`
```
3 3
0 1 2
0 2 2
0 1 1
```

`omogene.out`
```
3
```
```