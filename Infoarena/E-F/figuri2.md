## Task

Gigel just learned in geometry class the definition of a square: a parallelogram with all sides and angles equal. In the problem given to Gigel, it is considered that any square has its sides parallel to the coordinate axes (with the sides of the square described in the input file). Additionally, he also learned the definition of a rhombus: a parallelogram with all sides equal. In the problem he has to solve, it is considered that a rhombus is actually a square, but rotated by $45^\circ$. Gigel is given (in addition to the definitions of the $2$ geometric figures described above) a binary square matrix (i.e., consisting of the elements $0$ and $1$), and he is asked to find the maximum side length of a square made entirely of $1$s contained within the matrix, the number of squares of maximum side length contained in the matrix, the maximum side length of a rhombus made entirely of $1$s contained within the matrix, and the number of rhombuses of maximum side length. Write a program that solves Gigel's problem.

## Input data

The input file figuri2.in contains on the first line an integer $N$, representing the number of rows and columns of the binary matrix. The next $N$ lines each contain $N$ integer values from the set $\{0, 1\}$, not separated by spaces.

## Output data

The output file figuri2.out should print $2$ values on the first line: $LP$ and $NP$, separated by a single space, representing the maximum side length of a square made only of $1$s and included in the matrix described in the input file and the number of squares of maximum side length included in the matrix. The second line of the file should print another $2$ values: $LR$ and $NR$, also separated by a single space, representing the maximum side length of a rhombus made only of $1$s and included in the matrix described in the input file and the number of rhombuses of maximum side length included in the matrix.

## Constraints and clarifications

$3 \leq N \leq 255$

A square with the top-left corner at coordinates $(i, j)$ and side length $L$ has the property that all unit squares in the matrix with coordinates of the form $(i + p, j + q)$, with $0 \leq p, q < L$, have the value $1$.

A rhombus with center $(i, j)$ and side length $L$ has the property that all unit squares in the matrix with coordinates of the form $(i + p, j + q)$, with $|p| + |q| < L$, have the value $1$.

## Example

`figuri2.in`

```
6
001101
111111
111111
011111
001110
111100
```

`figuri2.out`

```
3 4
3 3
```

## Explanation

The squares with side length $3$ have top-left corners at coordinates (row, column): $(2, 2)$; $(2, 3)$; $(2, 4)$; $(3, 3)$.

The rhombuses with side length $3$ have centers at coordinates (row, column): $(3, 3)$; $(3, 4)$; $(4, 4)$.