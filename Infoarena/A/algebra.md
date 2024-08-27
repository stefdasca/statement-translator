## Task

A square matrix $A$ with real elements from the interval $[0,1]$ is given, having $N$ rows and $N$ columns. The sum of the elements of each row and each column is equal to $1$. $A$ can be written as a linear combination of permutation matrices, i.e., $A = x_1 *P_1 + \dots + x_K *P_K$, where $P_1, P_2, \dots, P_K$ are permutation matrices (not necessarily distinct) with $N$ rows and $N$ columns, and $x_1, \dots, x_K$ are real numbers from the interval $[0,1]$ with the property that $x_1 + \dots + x_K = 1$. A permutation matrix with $N$ rows and $N$ columns contains exactly $N$ elements of $1$, one on each row and each column, and the rest of the elements are equal to $0$. The representation of matrix $A$ in the specified form is not necessarily unique. Given a matrix $A$ with the properties mentioned in the statement, determine the value $K$, the real numbers $x_1, \dots, x_K$, and the corresponding permutation matrices $P_1, \dots, P_K$.

## Input data

The first line of the input file `algebra.in` will contain the integer number $N$. The next $N$ lines will contain $N$ real numbers each, representing the elements of the matrix $A$ in order, from row 1 to row $N$ and from column 1 to column $N$. The elements of $A$ are given with a maximum of 9 decimal places.

## Output data

The first line of the output file `algebra.out` will contain the integer number $K$. The next $2*K$ lines will contain the numbers $x_1, \dots, x_K$, and the permutation matrices $P_1, \dots, P_K$, as follows: on line $2*i-1$ of the $2*K$ lines, you will print the real number $x_i$ with at least 9 decimal places. On line $2*i$, you will describe the matrix $P_i$ as a sequence of $N$ integers, separated by at least one space: $C_1 C_2 \dots C_N$. The value $C_j$ in this sequence will represent the column where the element equal to $1$ is located on row $j$ of matrix $P_i$.

## Constraints and clarifications

$1 \leq N \leq 30$

The result of multiplying a real number $x$ by a matrix $P$ with $N$ rows and $N$ columns is a matrix $Q$ with $N$ rows and $N$ columns, having elements $Q_{i,j} = x*P_{i,j}$.

The result of adding two matrices $P$ and $Q$ with $N$ rows and $N$ columns is a matrix $R$ with $N$ rows and $N$ columns, having elements $R_{i,j} = P_{i,j} + Q_{i,j}$.

There is no upper limit on the value of $K$. However, it can be demonstrated that, for any matrix $A$ having the specified properties, there exist values $x_i$ and permutation matrices $P_i$ such that $K \leq N*(N-1)+1$.

The solution provided by your program will be considered correct if, after performing the sum $x_1 *P_1 + x_2 *P_2 + \dots + x_K *P_K$, each element in the resulting matrix differs from the corresponding element in matrix $A$ by at most $10^{-9}$ in absolute value, the sum $x_1 + x_2 + \dots + x_K$ lies in the interval $[1.0 - 10^{-9}, 1.0 + 10^{-9}]$, and each value $x_i$ is in the interval $[0,1]$.

## Example

`algebra.in`

```
3
0.4 0.5 0.1
0.3 0.3 0.4
0.3 0.2 0.5
```

`algebra.out`

```
5
0.300000000000
1 2 3
0.200000000000
2 1 3
0.300000000000
2 3 1
0.100000000000
1 3 2
0.100000000000
3 1 2
```