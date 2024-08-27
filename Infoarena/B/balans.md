# Balans

Bronzarel has been discharged from the hospital and is now healthy. Immediately after his discharge, he met with his good friend Zaharel and they started solving problems! One of the problems they tried to solve proved too difficult for them, so they will need your help. Let $A$ be a matrix of natural numbers with $N$ rows and $M$ columns. We define a matrix $B$ of size $P*Q$ as a submatrix of matrix $A$ if there exist numbers $(x,y)$ such that $B_{i,j} = A_{i+x,j+y}$ for $1 \leq i \leq P$ and $1 \leq j \leq Q$. Additionally, we define the balance of a matrix as the ratio between the sum of all elements in the matrix and their count. The problem that Zaharel and Bronzarel have been struggling with requires determining a submatrix of maximum balance in matrix $A$ that has at least $R$ rows and $C$ columns. Since things are never "simple," matrix $A$ is not just any matrix, but a very special one, namely its rows and columns can be circularly permuted.

##  Task

Determine the submatrix of maximum balance from a given matrix, taking into account that its rows and columns can be circularly permuted beforehand to obtain a more favorable result.

##  Input Data

The first line of the `balans.in` file will contain the numbers $N,M,R,C$ representing the dimensions of matrix $A$ and the lower bounds of the required submatrix dimensions. The next $N$ lines will contain $M$ natural numbers each.

##  Output Data

The `balans.out` file will contain a single line with a value representing the maximum possible balance of a submatrix. The result will be displayed with 3 exact decimal places.

##  Constraints and Clarifications

$1 \leq N, M \leq 150$

$0 \leq R \leq N$

$0 \leq C \leq M$

$0 \leq A_{i,j} \leq 100\,000$

##  Example

`balans.in`

```
3 4 2 1
15 5 15 8
1 2 1 3
4 8 8 4
```

`balans.out`

```
11.500
```

##  Explanation

The rows are circularly permuted once, yielding the matrix:

```
1 2 1 3
4 8 8 4
15 5 15 8
```

The maximum balance submatrix is highlighted.