Georgel and Ionel have invented a game. Georgel writes in each cell on a math sheet, which takes the form of a two-dimensional grid with $n$ rows and $m$ columns, values of $0$ or $1$. Ionel determines $3$ distinct shapes that Georgel must identify on the math sheet in the given position or rotated as in Figure 1, 2, or 3. The three proposed shapes are:
~[joc1.png|align=center]
For a game, Georgel must identify them on the sheet in the form of cells filled with $1$.

# Task

Write a program to identify the number of occurrences for all specified shapes.

# Input data

The input file `joc.in` contains values of $n$ and $m$ separated by a space on the first line, followed by $n$ lines containing the values from the cells on the sheet (not separated by spaces).

# Output data

The output file `joc.out` will contain on the first line the total number of identified shapes, of any of the three types.

# Constraints and clarifications

* $0 \lt m, n \lt 100$
* A cell can be part of one or more shapes.

# Example

`joc.in`
```
5 5
00100
00110
01111
00100
00100
```

`joc.out`
```
7
```

## Explanation

There are $2$ shapes of the first type, $3$ shapes of the second type, and $2$ of the third type, as shown in the drawing.
~[joc2.png|align=center]