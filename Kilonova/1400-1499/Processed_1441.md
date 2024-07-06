The problem statement provided in Romanian has been translated into English while preserving the mathematical values, variable names, general syntax, structure, and format.

---

Consider $N$ points with integer coordinates in the Cartesian coordinate system.

# Task

Write a program that determines the number of right triangles with their vertices placed at $3$ of the given points and with the legs parallel to the coordinate axes.

# Input data

The input file `tdrept.in` contains:

- The first line contains the natural number $N$, which represents the number of points.
- The next $N$ lines contain two natural numbers $x$ and $y$, separated by a space, representing the Cartesian coordinates of the $N$ points (abscissa and ordinate).

# Output data

The output file `tdrept.out` should contain a single line that will print a natural number representing the number of right triangles that meet the given conditions. Because the number of solutions can be very large, the result will be printed modulo $666 \ 013$ (i.e., the remainder of the result divided by $666 \ 013$).

# Constraints and clarifications

* $3 \leq N \leq 100 \ 000$
* $0 \leq x, y \leq 100 \ 000$
* The $N$ points in the input file are pairwise distinct.

# Example

`tdrept.in`
```
8
1 1
1 4
10 8
4 1
9 1
5 5
7 4
7 5
```

`tdrept.out`
```
5
```

## Explanation

~[image1.png|align=left]

The right triangles formed are:

```
(1,1) (1,4) (4,1)
(1,1) (9,1) (1,4) 
(5,5) (7,4) (7,5)
(1,4) (7,4) (7,5)
(1,1) (1,4) (7,4)
```

---

The original formatting, mathematical expressions, and custom image syntax have been preserved, and potential grammar and syntax errors have been corrected according to the rules of English language.