## Rectangles3

Suppose we have a grid with $N$ rows and $M$ columns forming $N \times M$ cells, each initially holding the value $0$. We perform $K$ operations of the type: add$(i_1, j_1, i_2, j_2, v)$ which has the following effect: the values in the cells of the rectangle with the lower-left corner at position $(i_1, j_1)$ and the upper-right corner at position $(i_2, j_2)$ increase by the value $v$.

## Task

Calculate the maximum value that appears in the cells after performing the $K$ operations and determine the number of cells in which it appears.

## Input data

The input file `rectangles3.in` contains the natural numbers $N$, $M$, and $K$ separated by a space on the first line. Each of the following $K$ lines contains the arguments of an operation separated by a space: $i_1 \; j_1 \; i_2 \; j_2 \; v$.

## Output data

The output file `rectangles3.out` will contain two numbers separated by a space on the first line: the maximum value in the cells and the number of cells in which it appears.

## Constraints and clarifications

$1 \leq N, M \leq 1\,000\,000\,000$

$1 \leq K \leq 1\,000$

$|v| \leq 1\,000\,000$, where $|v|$ is the absolute value of $v$

For 20% of the tests $N, M, K \leq 100$

For another 30% of the tests $N, M \leq 2\,000$

## Example

`rectangles3.in`
```
5 5 3
1 1 2 2 1
4 2 5 5 3
2 2 4 4 2
```

`rectangles3.out`
```
5 3
```

## Explanation

Cells $(4, 2)$, $(4, 3)$, and $(4, 4)$ all contain the value $5$. The rest of the cells contain strictly smaller values.