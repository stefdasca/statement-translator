# Task

The stadium where Taylor Swift performs during the $\\text{Eras Tour} \\textregistered$ can be represented using a matrix with $N$ rows and $M$ columns, numbered starting from $1$. In each cell $(i, j)$, on row $i$ and column $j$ ($1 \\leq i \\leq N$ and $1 \\leq j \\leq M$), there is a chair where *friendship bracelets* can be placed. Before the concert, on each of the $N \\times M$ chairs, there is no bracelet.

During the concert, Steven makes, in order, $U$ modifications, which can be of two types:
* type $\\left(L, a, v\\right)$ — meaning that on each of the $M$ chairs on row $a$, $v$ new bracelets are placed ($1 \\leq a \\leq N$);
* type $\\left(C, a, v\\right)$ — meaning that on each of the $N$ chairs on column $a$, $v$ new bracelets are placed ($1 \\leq a \\leq M$).

After all the modifications have been made, Caroline asks Steven, in order, $Q$ questions. For each question, a natural number $K$ and the descriptions of $K$ submatrices are given. Steven needs to determine how many bracelets are, in total, on the chairs that are in at least one of the considered $K$ submatrices.

In the question, each submatrix $i$ ($1 \\leq i \\leq K$) is described by a pair of two corners: the top-left corner $(x_{i, 1}, y_{i, 1})$ and the bottom-right corner $(x_{i, 2}, y_{i, 2})$, in this order ($1 \\leq x_{i, 1} \\leq x_{i, 2} \\leq N$ and $1 \\leq y_{i, 1} \\leq y_{i, 2} \\leq M$). Thus, a chair in a cell $(t, s)$ is in a submatrix $i$ if $x_{i, 1} \\leq t \\leq x_{i, 2}$ and $y_{i, 1} \\leq s \\leq y_{i, 2}$.

# Task

Help Steven correctly answer all the $Q$ questions asked by Caroline!

# Input data

The first line of the input file `eras.in` contains the natural numbers $N$, $M$ and $U$, in this order. Each of the next $U$ lines contains, in order, a character (which can be either `L` or `C`), followed by two natural numbers, representing the $U$ modifications, in the order they are made. On the next line contains the natural number $Q$. Each of the next $Q$ lines contains a natural number $K$, followed by $4 \\cdot K$ natural numbers, representing, in order, the pairs of two corners of the $K$ submatrices described in the question, namely: $x_{1, 1}$, $y_{1, 1}$, $x_{1, 2}$, $y_{1, 2}$, $\\dots$, $x_{k, 1}$, $y_{k, 1}$, $x_{k, 2}$, and $y_{k, 2}$. The $Q$ lines represent, in order, the descriptions of the $Q$ questions. Numbers and letters (`L` or `C`) on the same line of the input file are separated by a space.

# Output data

The output file `eras.out` contains $Q$ lines, with the correct answer to the $i$-th question asked by Caroline to Steven on the $i$-th line.

# Constraints and clarifications

* $1 \\leq N, M \\leq 1 \\ 000 \\ 000 \\ 000$
* $1 \\leq U \\leq 500 \\ 000$ and $1 \\leq v \\leq 1 \\ 000$ for each of the $U$ modifications
* $1 \\leq Q \\leq 1 \\ 000$ and $1 \\leq K \\leq 100$ for each of the $Q$ questions
* Any number of bracelets can be placed on each chair.
* It is recommended to use the `long long` data type.

|#| Points |        Constraints                                         | 
|-|---------|-----------------------------------------------------------|
|1|   15    | $N, M, U \\leq 2 \\ 000$, $Q \\leq 10$, $K = 1$ |
|2|    8    | $U \\leq 100 \\ 000, Q \\leq 10$, $K = 1$                  |
|3|   11    | $U \\leq 100 \\ 000, Q \\leq 10$, $K \\leq 2$               |
|4|   19    | $U \\leq 100 \\ 000, Q \\leq 10$  \t\t\t\t\t\t\t|
|5|   10    | $K \\leq 10$                   \t\t\t\t\t\t    |
|6|   14    | $K \\leq 25$                    \t\t\t\t\t        |
|7|   23    | No additional constraints                              |

# Example 1

`eras.in`
```
6 6 3
L 1 4
C 3 5
L 5 2
2
2 1 2 4 3 1 2 2 4
2 5 1 6 6 1 6 1 6
```

`eras.out`
```
32
26
```

## Explanation

The matrix representing the stadium has $N = 6$ rows and $M = 6$ columns. Steven makes $U = 3$ modifications, as follows: in the first modification, he adds $v = 4$ bracelets on each of the six chairs on the first row, in the second modification, he adds $v = 5$ bracelets on each of the six chairs on the third column, and in the third modification, he adds $v = 2$ bracelets on each of the six chairs on the fifth row.

Caroline asks Steven, in order, $Q = 2$ questions:
* In the first question, the descriptions of $K = 2$ submatrices are considered: $x_{1, 1} = 1$, $y_{1, 1,} = 2$, $x_{1, 2} = 4$, $y_{1, 2} = 3$ (for the first submatrix: $i = 1$) and $x_{2, 1} = 1$, $y_{2, 1} = 2$, $x_{2, 2} = 2$, $y_{2, 2} = 4$ (for the second submatrix: $i = 2$);
* In the second question, the descriptions of $K = 2$ submatrices are also considered.

# Example 2

`eras.in`
```
5 4 4
L 2 50
C 2 4
L 3 23
C 2 3
3
1 1 1 5 4
3 1 2 1 2 2 2 5 4 1 3 5 3
1 1 3 1 4
```

`eras.out`
```
327
254
0
```

## Explanation

The matrix has $N = 5$ rows and $M = 4$ columns. Steven makes $U = 4$ modifications, and Caroline asks $Q = 3$ questions.