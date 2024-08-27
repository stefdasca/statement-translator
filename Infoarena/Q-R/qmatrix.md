##  Qmatrix

A matrix $A$ with $N$ rows and $N$ columns is given. The rows and columns are numbered from $1$ to $N$. The matrix $A$ stores only digits. The elements of the matrix are generated as follows: you are given the values $X$ and $Y$, then a sequence $v$ is constructed where: $v[1] = X, v[2] = Y, v[k] = A[i][j] = (v[k-2] * i + v[k-1] * j + 1) % 10$, $1 \leq i, j \leq N$, $k = N*(i-1) + j + 2$. You need to answer $Q$ queries of the form:
• $L k p$ – on which row is the $k$-th digit equal to $p$ (where $p$ is a digit) if we traverse the matrix row by row
• $C k p$ – on which column is the $k$-th number $p$ (where $p$ is a digit) if we traverse the matrix column by column 

##  Input data

The input file `qmatrix.in` contains on the first line the numbers $N$, $X$, $Y$, $Q$. The next $Q$ lines contain three values $ch$ $k$ $p$, where $ch$ can be one of the characters $L$ or $C$. 

##  Output data

The output file `qmatrix.out` will contain exactly $Q$ lines. Each line contains a single natural number which represents the answer to one query. 

##  Constraints and clarifications

$2 \leq N \leq 4000$ 

$1 \leq Q \leq 100\ 000$ 

$1 \leq X,Y \leq 10\ 000$ 

For all queries, $0 \leq p \leq 9$ and $1 \leq k \leq 1\ 000\ 000\ 000$ 

If there are fewer than $k$ values equal to $p$ in the matrix, then you will print the value $0$. 

##  Example

`qmatrix.in`
```
6 121 97 3 
C 3 9 
L 5 8 
C 200 9 
```

`qmatrix.out`
```
3 
6 
0 
```

##  Explanation

The generated matrix is 
$ \begin{array}{cccccc}
9 & 6 & 8 & 9 & 4 & 4 \\
3 & 5 & 2 & 9 & 0 & 9 \\
0 & 8 & 5 & 5 & 1 & 2 \\
7 & 3 & 8 & 5 & 8 & 9 \\
0 & 6 & 9 & 7 & 1 & 2 \\
9 & 1 & 8 & 9 & 4 & 9 \\
\end{array}$

First query: the third digit 9 is on column $3$ 

Second query: the fifth digit 8 is on row $6$ 

Third query: there are fewer than $200$ values of 9 in the matrix, so you print $0$.