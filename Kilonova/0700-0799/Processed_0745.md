
A rectangular matrix with $m$ rows and $n$ columns, containing natural values, is considered. We traverse the matrix starting from the top-left corner to the bottom-right corner. A traversal consists of several moves. With each move, a jump is executed horizontally and a step vertically. A jump means that we can move from one cell to any other cell on the same row, while a step means that we can move from one cell to the cell immediately below it. The exception is the last move (when we are on the last row), where we will only make a jump to reach the bottom-right corner, but we will not make the corresponding step. Thus, the traversal will consist of visiting $2 \cdot m$ cells.

# Task

Write a program to determine the minimum sum that can be obtained for such a traversal.

# Input data

The input file `lacusta.in` contains on the first line two natural numbers separated by a space $m \\ n$, representing the number of rows and the number of columns of the matrix, respectively. On the next $m$ lines, the matrix is described, each containing $n$ numbers separated by a space.

# Output data

The output file `lacusta.out` will contain a single line where the minimum sum found will be printed.

# Constraints and clarifications

* $1 \leq m, n \leq 100$
* The values of the matrix elements are integers in the range $[1, 255]$

# Example

`lacusta.in`
```
4 5
3 4 5 7 9
6 6 3 4 4
6 3 3 9 6
6 5 3 8 2
```

`lacusta.out`
```
28
```

## Explanation

The path is: 
$(1,1)\rightarrow(1,3)\rightarrow$
$(2,3)\rightarrow(2,2)\rightarrow$
$(3,2)\rightarrow(3,3)\rightarrow$
$(4,3)\rightarrow(4,5)$
