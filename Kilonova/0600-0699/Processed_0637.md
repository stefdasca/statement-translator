```markdown
Given an array $A$, whose elements are defined by the relation $A_i$ = $i^K \cdot 2^i$ for any $1 \leq i$, where $K$ is a given natural number. The elements of this array are placed in a matrix $M$, consisting of $L$ rows and $C$ columns, as follows: $M_{11} = A_1$, $M_{21} = A_2$, $M_{12} = A_3$, $M_{31} = A_4$, $M_{22} = A_5$, $M_{13} = A_6$, $M_{41} = A_7$, $M_{32} = A_8$ ..., that is, traversing the matrix on diagonals from bottom-left to top-right.

For example, for $K=0$, $L=3$ and $C=4$, the array $A$ is composed of elements $2, 4, 8, 16, 32, 64...$, and the matrix $M$ will be filled as:

~[ashima_matrice.png|align=center|width=50%]

# Task
Ashima asks you to respond to $Q$ queries of the form:
* $l_1 \\ l_2 \\ c_1 \\ c_2$ : what is the sum of the elements $M_{ij}$ in matrix $M$ such that $l_1 \leq i \leq l_2$ and $c_1 \leq j \leq c_2$?

# Input data
The first line of the input file contains the numbers $K$, $L$, $C$ and $Q$, and the following $Q$ lines contain four numbers each $l_1 \\ l_2 \\ c_1 \\ c_2$.

# Output data 
The output file will contain $Q$ lines. On line $i$ the result of the $i$-th query will be printed, modulo $1\ 000\ 000\ 007$.

# Constraints and clarifications
* $0 \leq K \leq 3$
* $1 \leq L,C \leq 100\ 000$
* $1 \leq Q \leq 200$
* $1 \leq l_1 \leq l_2 \leq L$
* $1 \leq c_1 \leq c_2 \leq C$
* $0 \leq l_2 - l_1, c_2 - c_1 \leq 1\ 000$

|#|Score|Constraints|
|-|-|--------|
|1|16|$1 \leq L,C \leq 100$|
|2|21|$1 \leq L,C \leq 1\ 000$|
|3|27|$K=0$|
|4|15|$K=1$|
|5|12|$K=2$|
|6|9|$K=3$|

# Example 1
`ashima.in`
```
0 3 4 3
1 1 2 4
1 2 1 3
1 3 2 3
```
`ashima.out`
```
584
366
1512
```

## Explanation
For this example, the matrix $M$ is filled as given in the stated example.
- For the first query, the sum of elements between the rows $1$ and $1$ and columns $2$ and $4$ needs to be calculated. The sum of these elements is $8 + 64 + 512 = 584$.
- For the second query, the sum of elements between the rows $1$ and $2$ and columns $1$ and $3$ needs to be calculated. The sum of these elements is $2 + 8 + 64 + 4 + 32 + 256 = 366$.
- For the third query, the sum of elements between the rows $1$ and $3$ and columns $2$ and $3$ needs to be calculated. The sum of these elements is $8 + 64 + 32 + 256 + 128 + 1024 = 1512$.

# Example 2
`ashima.in`
```
1 2 5 2
1 1 2 4
1 2 1 3
```
`ashima.out`
```
1080
642
```

## Explanation

For this example we have $K = 1$, so the array $A$ has elements $1 \cdot 2^1$, $2 \cdot 2^2$, $3 \cdot 2^3$, ..., $10 \cdot 2^{10}$, and the matrix $M$, with $2$ rows and $5$ columns is filled as follows:

~[incaomatrice.png|width=50%]

- For the first query, the sum of elements between the rows $1$ and $1$ and columns $2$ and $4$ needs to be calculated. The sum of these elements is $24 + 160 + 896 = 1080$.
- For the second query, the sum of elements between the rows $1$ and $2$ and columns $1$ and $3$ needs to be calculated. The sum of these elements is $2 + 24 + 160 + 8 + 64 + 384 = 642$.

\
If you managed to answer the queries, the array $\textbf{A shi}$ and the matrix $\textbf{Ma}$ thank you for your help!
```
