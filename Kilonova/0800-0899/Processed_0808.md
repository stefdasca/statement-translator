~[numerus.png|align=right]

In a fun math class, Mr. Numerus proposes that his students fill in a grid with natural numbers, consisting of $6$ columns labeled $A$, $B$, $C$, $D$, $E$, and $F$, and an infinite number of rows. The grid will be filled with natural numbers, starting with the number $1$. In odd rows, the filling is done from left to right, and in even rows from right to left. The last number in a row will be identical to the penultimate number (in the direction of filling) in the same row.

The adjacent figure shows the first $7$ rows of the grid filled in.

Since on a board or a sheet of paper the number of rows is limited, so the grid can be effectively filled for a small number of rows, Mr. Numerus wants his students to determine, with the help of a computer, the image of a certain row of the grid and the position or positions where a given natural number can be found.

# Task

Deduce the rule according to which line $k$ of the grid is filled and write a program that reads the natural numbers $k$ and $n$ and determines:

a) the natural numbers on line $k$, viewed from left to right;
b) the row in the grid where the natural number $n$ is located;
c) the column or columns in the grid where the natural number $n$ is located.

# Input data

The input file `numerus.in` contains a single line containing two natural numbers $k$ and $n$, separated by a space.

# Output data

The output file `numerus.out` will contain $3$ lines:

* The first line will contain the numbers on line $k$ of the grid;
* The second line will contain a natural number representing the row in which the natural number $n$ is found in the grid;
* The third line will contain the letter or letters that represent the column or columns where the natural number $n$ is found in the grid; in the situation where two letters need to be displayed, they will be separated by a space.
* Solving requirement a) awards 40% of the points, requirement b) 30% of the points, and requirement c) 30% of the points.

# Constraints and clarifications

* $5 \leq k < 2 \cdot 10^8$;
* $1 \leq n < 10^9$;

# Example

`numerus.in`
```
10 40
```

`numerus.out`
```
50 50 49 48 47 46
8
A B
```

## Explanation

~[numerus1.png]