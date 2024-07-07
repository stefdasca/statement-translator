
We consider a matrix with $L$ rows (numbered from top to bottom from $1$ to $L$) and $C$ columns (numbered from left to right from $1$ to $C$) which only stores values $0$ and $1$. Furthermore, the values equal to $1$ are grouped into multiple solid rectangles, which **do not** touch each other neither on rows, columns, nor diagonals. In the example from _fig. 1_, the matrix is correct because the $4$ rectangles of $1$ do not touch each other. However, in _fig. 2_, there are $2$ rectangles of $1$ that are adjacent on the column and two that are adjacent on the diagonal, so the matrix is incorrect.

~[55300bc86fef24cde07277ad815ac767.png]

In this matrix, movements can only be made in the **West** and **North** directions to elements equal to $0$, so from position $(i,j)$ you can only reach positions $(i,j-1)$ and $(i-1,j)$, marked with $0$. In this way, starting from a certain position, through successive movements, a certain number of matrix elements equal to $0$ can be accessed. For example, in _fig. 1_, from the position $(2,4)$ five components equal to $0$ can be accessed, and from the position $(5,4)$ fourteen components equal to $0$ can be accessed.

You need to answer $Q$ questions, each question being of the form: _â€œHow many elements equal to zero in the matrix can be accessed from position $(i,j)$?â€_

# Task

Write a program to determine, for each question, how many elements equal to $0$ in the matrix can be accessed from the specified position in the question.

# Input data

The first line of the file `acces.in` contains two natural numbers $L$ and $C$ separated by a space, representing the number of rows and the number of columns of the matrix, respectively. On the next $L$ lines, there are $C$ binary digits, separated by a space, representing the elements of the matrix. The next line contains a natural number $Q$, representing the number of questions. On the next $Q$ lines there are two natural numbers $i$ and $j$, separated by a space, representing the position corresponding to a question.

# Output data

The file `acces.out` contains $Q$ lines. On line $p \\ (1 \\leq p \\leq Q)$ there is a natural number $k_p$ representing the answer to the $p$-th question.

# Constraints and clarifications

* $4 \\leq L, C \\leq 1\ 000$
* $3 \\leq Q \\leq 500\ 000$
* For any question $i \\ j$ it is guaranteed that the corresponding value in the matrix is $0$.
* For all tests, the rectangles formed by values of $1$ do not touch each other.

# Example

`acces.in`
```
5 7
0 0 0 0 1 1 1
0 1 1 0 1 1 1
0 1 1 0 0 0 0
0 1 1 0 1 0 0
0 0 0 0 1 0 1
4
2 4
5 4
4 7
3 1
```

`acces.out`
```
5
14
11
3
```

## Explanation

For the first question, the $5$ components equal to $0$ that can be accessed are those in positions $(1,1), (1, 2), (1,3), (1,4), (2,4)$.
