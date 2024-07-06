Oli has a set square in the shape of a right-angled triangle, with legs of lengths $L1$ and $L2$ units, and a math notebook with $M$ rows and $N$ columns of squares with side length of one unit.
~[echer1.png|align=right]
Oli positioned the set square in the top-left corner of the paper, as shown in the image on the right, and wants to move it so that it touches the bottom-right corner of the paper with any corner of the set square, using only moves of the following form:
~[echer2.png|align=center]

# Task

Write a program that reads the lengths of the set square legs, the number of rows, and the number of columns of the paper and determines:

1. the minimum number of moves $K$ needed to move the set square from the top-left corner of the math notebook to the point where the set square touches the bottom-right corner of the paper
2. the $K$ moves made to move the set square from the top-left corner of the paper until one corner of the set square touches the bottom-right corner of the paper; if there are multiple solutions, the smallest lexicographic solution should be displayed. A sequence of moves $X = (X_1, X_2, ..., X_K)$ is lexicographically smaller than another sequence of moves $Y = (Y_1, Y_2, ..., Y_K)$ if $\\exists P (1 \\leq P \\leq K)$ such that $X_I = Y_I, \\forall I \\in \\{1, 2, ..., P - 1\\}$ and $X_P < Y_P$. For example, the sequence of moves $1, 2, 3, 1$ is lexicographically smaller than the sequence of moves $1, 2, 4, 1$.

# Input data

The input file `echer.in` contains on the first line one of the values $1$ or $2$, representing task $1$ if it is required to determine the minimum number of moves to move the set square from the top-left corner of the math notebook to the point where it touches the bottom-right corner of the paper, or task $2$, if it is required to determine the moves made to move the set square from the top-left corner of the paper until one corner of the set square touches the bottom-right corner of the paper.
The second line of the file contains four natural numbers, separated by a space, representing the values $L1, L2, M$ and $N$, in this order.

# Output data

The output file `echer.out` will contain on the first line a natural number $K$ representing the minimum number of moves if the task was $1$, or $K$ natural numbers separated by a space representing the moves made to move the set square from the top-left corner of the math notebook until one corner of the set square touches the bottom-right corner of the paper, if the task was $2$.

# Constraints and clarifications

* $1 \\leq L1, L2 \\leq 1 \ 000$.
* $1 \\leq M, N \\leq 1 \ 000 \ 000$.
* It is guaranteed that there is a solution for any set of input data.
* Correctly solving task $1$ will earn $30\%$ of the points.
* Correctly solving task $2$ will earn $70\%$ of the points.

# Example 1

`echer.in`
```
1
2 3 8 9
```

`echer.out`
```
8
```

## Explanation

8 moves are needed, as shown in the image below.
~[echer3.png|align=center]

# Example 2

`echer.in`
```
2
2 3 8 9
```

`echer.out`
```
1 2 3 1 2 3 1 4
```

## Explanation

The moves are illustrated in the image above.