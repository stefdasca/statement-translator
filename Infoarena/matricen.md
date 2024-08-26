# Matricen

This year, Santa Claus gave you an unusual gift, namely a binary matrix $A$ with $N$ rows and $N$ columns. However, interesting matrices are those matrices in which each row has only equal elements. Dan Claus, Santa Claus's brother, asks for your help with a problem to put in a good word for you with Santa. Dan provides you with $Q$ submatrices of the initial matrix and asks you to find, for each submatrix, the minimum number of operations needed to make the resulting submatrix interesting. In one operation, you can swap any two elements in the submatrix. Dan provides you with the top-left corner of the submatrix as well as its bottom-right corner. If $(L1, C1)$ is the top-left corner and $(L2, C2)$ is the bottom-right corner, then the submatrix is formed by the elements $A_{i,j}$, where $L1 \leq i \leq L2$ and $C1 \leq j \leq C2$.

## Input data

The input file `matricen.in` contains on the first line two natural numbers $N$ and $Q$, separated by a single space, with the meaning explained above. Then follow $N$ lines with $N$ elements each, either $0$ or $1$, representing the matrix $A$. The elements of a line are separated by a single space. Then follow $Q$ lines representing Dan Claus's questions. Each such line contains four natural numbers $L1$, $C1$, $L2$, and $C2$, separated by a single space. The first two numbers represent the row and column corresponding to the top-left corner of the submatrix, and the last two the row and column of the bottom-right corner.

## Output data

In the output file `matricen.out`, you will print $Q$ lines, each line $i$ containing the minimum number of swaps required for the $i$-th submatrix from the input file. If there is no solution, print $-1$.

## Constraints and clarifications

$1 \leq N \leq 300$

$1 \leq Q \leq 50\ 000$

For 50$\%$ of the tests $Q \leq 1000$

## Example

```
matricen.in
3 3
0 0 0
0 1 0
1 1 0
2 1 3 3
1 2 2 3
1 1 1 3

matricen.out
1
-1
0 
```

## Explanations

For the first submatrix, you can swap the element at position $(2, 2)$ with the one at position $(3, 3)$.

For the second submatrix, there is no solution, hence we print $-1$.

The third submatrix already contains a row in which all elements are equal, so no operations are needed.