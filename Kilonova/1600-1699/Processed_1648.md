**Gigel drew on a graph paper a polygon whose sides are arranged along the grid lines of the paper. None of the sides of the polygon are on the edge of the paper. Gigel noted in each cell of the graph paper how many of its 4 sides are on the contour of the polygon.**

# Task

Knowing the values written in the cells of the graph paper, reconstitute the polygon.

# Input data

The input file `desen.in` contains on the first line two natural numbers $N$ and $M$, separated by a space, representing the number of rows and respectively the number of columns of the grid on the graph paper. Each of the following $N$ lines contains $M$ numbers from the set $\\{0, 1, 2, 3, 4\\}$, separated by a space, representing the values written in the cells of the graph paper.

# Output data

The output file `desen.out` will contain the reconstituted drawing. The file will contain $N$ lines, each line containing exactly $2 \\cdot M - 1$ characters which can be:

* `.` (dot, ASCII code 46)
* `|` (vertical bar, ASCII code 124)
* `_` (underscore, ASCII code 95).

The first line of the output file illustrates the aspect of the first row of the graph paper (more precisely, the bottom sides of the cells in the first row), the second line of the file illustrates the aspect of the second row of the paper (the bottom sides as well as any vertical sides), etc. Let $c_1$, $c_2$, $\\dots$, $c_{2 \\cdot M - 1}$ be the characters of a line of the output file. Always $c_1 = \text{‘.’}$. Character $c_i$ (i odd, $i > 2$) is an underscore if the bottom side of cell $\\frac{i+1}{2}$ on the paper belongs to the polygon and `.` otherwise. Character $c_i$ (i even) is a vertical bar if the right side of cell $\\frac{i}{2}$ on the paper belongs to the polygon, and `.` otherwise.

# Constraints and Clarifications

* $3 \\leq N, M \\leq 1 \ 000$;
* It is guaranteed that there is a solution for the given test data.

# Example

`desen.in`
```
4 4
0 0 1 0
0 2 3 1
1 3 2 1
0 1 1 0
```

`desen.out`
```
...._..
.._|.|.
.|_._|.
.......
```

## Explanation

~[desen.png|width=15em]

