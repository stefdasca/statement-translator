On a chessboard with $n$ rows and $n$ columns, there are breadcrumbs and an ant. For each square, including the one where the ant is located, on row $i$ and column $j$, the amount of breadcrumbs is equal to the remainder of the division of $i + j$ by $6$. Thus, for $n = 4$, the chessboard contains the following amounts of breadcrumbs:

|2|3|4|5|
-|-|-|-
|**3**|**4**|**5**|**0**|
|**4**|**5**|**0**|**1**|
|**5**|**0**|**1**|**2**|

The ant (denoted with `F` in the figure below) can move from the square where it is located to any of the eight neighboring squares, numbered as follows:

|8|1|2|
-|-|-
|**7**|**F**|**3**|
|**6**|**5**|**4**|

The ant moves, starting from the square located in the top-left corner, to one of the neighboring squares, and so on. On its way, the ant feeds on all the breadcrumbs in the squares it passes through (after it leaves the square, the amount of breadcrumbs becomes $0$). The path of the ant is given by a sequence of $k$ natural numbers (ranging between $1$ and $8$) which specify, at each step, the next square in the path.

# Task

Write a program that, for a given path, determines the total amount of breadcrumbs eaten by the ant, as well as the number of squares it passed through the most times.

# Input data

The input file `furnica.in` contains on the first line the numbers $n$ and $k$, separated by a space, and on the next line $k$ natural numbers ($1, 2, 3, 4, 5, 6, 7$ or $8$) separated by a space, representing the next square in the path for a current square.

# Output data

The output file `furnica.out` will contain, on the first line, the total amount of breadcrumbs and the number of squares from the task separated by a space.

# Constraints and clarifications

* $1 < n < 101$;
* $0 < k < 201$;
* The ant's path does not go outside the board.

# Example

`furnica.in`
```
4 10
3 6 5 3 2 6 3 6 2 3
```

`furnica.out`
```
23 2
```

## Explanation

The ant's path passes through the following squares (row, column): $(1,1) \rightarrow (1,2) \rightarrow (2,1) \rightarrow (3,1) \rightarrow (3,2) \rightarrow (2,3) \rightarrow (3,2) \rightarrow (3,3) \rightarrow (4,2) \rightarrow (3,3) \rightarrow (3,4)$.

On the path, the following amount of breadcrumbs is eaten: $2+3+3+4+5+5+0+0+0+0+1=23$

The squares with coordinates $(3,2)$ and $(3,3)$ are passed through the most times (twice).