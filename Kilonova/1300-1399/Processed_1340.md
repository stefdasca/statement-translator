From a math sheet containing $D \times D$ squares arranged in $D$ rows and $D$ columns, a figure was cut out. The cut-out figure is compact (has no holes) and consists of $N$ squares from the sheet.

# Task

Write a program that determines the perimeter of the cut-out figure.

# Input data

The input file `figura.in` contains the following:

- The first line contains the natural number $D$.
- The second line contains the natural number $N$.
- The following $N$ lines contain the coordinates of the cut-out squares (the row and column where the square is located, separated by a space), one square per line.

# Output data

The output file `figura.out` will contain a single line with a single natural number representing the perimeter of the cut-out figure.

# Constraints and clarifications

* $1 \leq D \leq 20$
* $1 \leq N \leq D \cdot D$
* Rows are numbered from top to bottom from $1$ to $D$; columns are numbered from left to right from $1$ to $D$.
* The side length of a square is $1 \text{cm}$.

# Example

`figura.in`
```
6
3
1 1
1 2
2 1
```

`figura.out`
```
8
```

## Explanation

The math sheet has $36$ squares arranged in $6$ rows and $6$ columns. The cut-out figure is marked in black.  
~[figura.png|align=center]

