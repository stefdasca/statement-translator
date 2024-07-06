```markdown
Gigel qualified for $\\text{ONI} \\ 2007$. Unfortunately, or fortunately, he encounters a problem similar to the one from $\\text{OJI}$, $\\text{Excel}$.
We remind that a spreadsheet in $\\text{Excel}$ is presented as a lined surface with horizontal and vertical lines. By their intersection, rectangles (called cells) are obtained, each cell having a name formed by one or more letters and a number, representing the column and row it is located on. For example, the top left cell is $\\text{A}1$, followed by, in the row, $\\text{B}$, $\\text{C}1$, $\\dots$, $\\text{Z}1$, $\\text{AA}1$, $\\text{AB}1$, $\\dots$, $\\text{BA}1$, $\\dots$
~[excel.png|align=center]

# Task

Given several cells in the form $\\text{L}x\\text{C}y$, as well as the values in these cells, display the names of the cells using the standard encoding explained above.
An $\\text{Excel}$ sheet is defined as being delimited by row $1$, column $1$, row $n$, column $m$ and this sheet is filled with the values found in the previously described cells. Indices $n$ and $m$ represent the index of the largest row and column, respectively, in which there is a non-zero value. In this sheet, the sum of the values is realized in the first column. The task is to display the results obtained in this column starting from cell $\\text{A}1$ up to cell $\\text{A}n$.

# Input data

The input file `excel.in` contains several lines, each being in the form:
$\\text{L}x\\text{C}y \\ \\text{val}$ where $\\text{L}x\\text{C}y$ represents a cell given by row $x$ and column $y$, and $\\text{val}$ is the numeric value contained in this cell.

# Output data

The output file `excel.out` will contain one line corresponding to each line in the input file. Each line will contain the name of the corresponding cell from the input file in the format described in the task $(\\text{ColumnRow})$. In addition, the output file will contain one more line that will describe column $A$, obtained as a result of summing operations. In this column being multiple values, many of which are zero, the values are to be displayed as: $valA_k$ if in cell $A_k$ there is a numeric value different from $0$, or $nr \\ 0$, where $nr$ represents how many $0$ values are consecutive between two cells $A_i \\ A_j$, where $i \\lt j, A_i \\neq 0, A_j \\neq 0$ and $A_k = 0$, with $i \\lt k \\lt j$.

# Constraints and clarifications

* $1 \\leq \\text{row index} (x) \\leq 30\\ 000\\ 000$
* $1 \\leq \\text{column index} (y) \\leq 30\\ 000\\ 000$
* The spreadsheet, before reading the input file, is considered to be "filled" with the value zero.
* $-32\\ 000 \\leq \\text{val} \\leq 32\\ 000$
* The input file contains at most $300$ lines
* Between $\\text{L}x\\text{C}y$ and $\\text{val}$ there is a single space
* The input file will contain, after the last line, the character `\\n` (end of line)
* $30\\%$ of the points are awarded for correctly displaying the names of the cells described in the input file.

# Example

`excel.in`
```
L1C1 23
L3C1 100
L1C3 -100
L29999999C26 50
L52C52 25
L53C17576 24
L53C17602 100
```

`excel.out`
```
A1
A3
C1
Z29999999
AZ52
YYZ53
YZZ53
-77 1 0 100 48 0 25 124 29999945 0 50
```

## Explanation

$\\text{A}1: 23 - 100 = -77$
$\\text{A}2: 0 \\rightarrow 1 \\ 0$
$\\text{A}3: 100$
$\\text{A}4 \\ \\text{–} \\ \\text{A}51: 0 \\rightarrow 48 \\ 0$
$\\text{A}52: 25$
$\\text{A}53: 24 + 100 = 124$
$\\text{A}54 \\ \\text{–} \\ \\text{A}29999998: 0 \\rightarrow 29999945 \\ 0$
$\\text{A}29999999: 50$
```
