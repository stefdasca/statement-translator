```
The Vizima Fortress in the kingdom of Temeria can be represented by a matrix with $N$ rows and $M$ columns, numbered starting from $1$. Vizima is a flourishing fortress due to the large number of merchants and craftsmen present. For this reason, each cell is assigned a profit corresponding to that area. King Foltest wants to rebuild the fortress walls, but as the war with the Nilfgaard Empire looms and the kingdom's resources are limited, he must choose a defendable portion, represented as a submatrix. A submatrix is identified by a **configuration** of four numbers $(i_1, j_1, i_2, j_2)$ ($1 \leq i_1 \leq i_2 \leq N$, $1 \leq j_1 \leq j_2 \leq M$) in this order, and consists of the elements located on the consecutive rows $i_1, i_1+1, \ldots, i_2$ and the consecutive columns $j_1, j_1+1, \ldots, j_2$ of the matrix through which the fortress is represented. The **sides** of the submatrix are equal to the number of rows and columns from which it took elements, and the **profit** of the submatrix is the sum of the values in its cells.

# Task
Write a program that, knowing the fortress matrix and a value $K$, determines:
1) the maximum profit of a submatrix with sides equal to $K$, as well as the configuration that identifies it.
2) the maximum profit of a submatrix with sides at most equal to $K$, as well as the configuration that identifies it.

# Input data
The input file `cetate.in` contains on the first line a value $c$ equal to $1$ or $2$, representing the task to be solved. The next line contains in order $N$, $M$ and $K$, with the meaning from the statement, and on the following $N$ lines are $M$ numbers each, representing the values in the given matrix. The numbers on the same line of the file are separated by a space.

# Output data
The output file `cetate.out` will contain on the first line the maximum profit requested, according to the task, and on the second line will contain 4 natural numbers, representing the configuration that identifies the obtained submatrix. If there are multiple submatrices according to the task, the one for which the configuration consisting of the 4 numbers above is lexicographically smallest will be considered.

# Constraints and clarifications
- $1 \leq N,M \leq 400$
- $1 \leq K \leq \min(N,M)$
- The values given for the fortress matrix are in the range $[-10^9, 10^9]$.
- For tests worth 20 points, $c=1$, and for the rest of the tests, worth 70 points, $c=2$. For tests worth 8 points, $c=1$ and $1 \leq N,M \leq 70$. For tests worth 25 points, $c=2$ and $1 \leq N,M \leq 70$.
- The configuration $(x_1, x_2, x_3, x_4)$ is lexicographically smaller than the configuration $(y_1, y_2, y_3, y_4)$ if there is a $p$ such that $x_p < y_p$ and $x_1 = y_1$, $x_2 = y_2$, $\ldots$, $x_{p-1} = y_{p-1}$.

# Example 1
`cetate.in`
```
1
3 4 3
-1 -1 -1 -1
-1 2 -1 -1
-1 -1 -1 -1
```
`cetate.out`
```
-6
1 1 3 3
```

## Explanation
In this example, the task 1 is solved. The submatrix with the configuration $(i_1=1, j_1=1, i_2=3, j_2=3)$, consisting of the elements on rows 1, 2, and 3 and columns 1, 2, and 3, was determined. Another submatrix with a profit of $-6$ is the one given by the configuration $(1,2,3,4)$, which is however lexicographically larger than the one shown, so it is not an accepted solution.

# Example 2

`cetate.in`
```
2
3 4 3
-1 -1 -1 -1
-1 2 1 -1
-1 -1 -1 -1
```
`cetate.out`
```
3
2 2 2 3
```

## Explanation

In this example, task 2 is solved. All submatrices with sides $1$, $2$ or $3$ were considered, and the found submatrix, with sides $1$ and $2$, is the only maximum profit submatrix that meets the conditions imposed by the task.
```