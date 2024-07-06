# Statement

On a math sheet, there are $5000 \times 5000$ squares with a side length equal to $1$ cm. The squares are obviously organized in $5000$ rows (numbered from top to bottom from $1$ to $5000$) and $5000$ columns (numbered from left to right from $1$ to $5000$). The position of each square on the sheet is characterized by the row number and the column number where the square is located. On the sheet, $n$ squares are blacked out. We need to draw on the math sheet a set of squares that meet the following conditions:
* the area of the intersection between any two squares in this set is equal to $0$;
* any of the squares in this set are composed only of whole squares;
* any black square belongs to exactly one of the squares in the set;
* for any of the squares in this set, if we denote the area of the square by $S$, then the area occupied by the black squares inside that square belongs to the interval $[S/k, 4S/k)$, where $k$ is a given non-zero natural number.

# Task

Write a program that determines a set of squares that meet the above conditions.

# Input data

The input file `patrate.in` contains on the first line two non-zero natural numbers separated by a space $n$ and $k$, with the meaning given in the statement. Each of the following $n$ lines contain two non-zero natural numbers separated by a space, representing the position of a blacked-out square.

# Output data

In the output file `patrate.out`, the first line will contain a non-zero natural number $np$, representing the number of squares in the set. Each of the following $np$ lines will contain three non-zero natural numbers separated by a space; the first two values will represent the row and column of the square located in the upper-left corner of the respective square, and the third value will represent the side length of the respective square.

# Constraints and clarifications

* $1 \leq n \leq 100\ 000$;
* $5 \leq k \leq 10$;
* The coordinates of the black squares (row, column) are natural numbers from the interval $[1, 1000]$.

# Example

`patrate.in`
```
19 5
1 1
1 2
2 1
2 2
3 1
3 3
4 3
5 5
5 6
5 7
6 6
6 7
10 7
10 8
7 9
8 10
8 9
9 9
10 9
```

`patrate.out`
```
2
1 1 4
5 5 6
```

## Explanation

There are multiple possible solutions. Another solution could be:
$4$
$1 \ 1 \ 4$
$5 \ 5 \ 4$
$7 \ 9 \ 4$
$10 \ 7 \ 2$