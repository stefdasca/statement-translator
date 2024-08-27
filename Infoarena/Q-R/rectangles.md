# Rectangles

Bored during math class, Laura drew $N$ rectangles with sides parallel to the coordinate axes on a page of her math notebook. Since the class hasn't ended yet, she now wonders how many squares exist in the drawing she just finished.

## Task

## Input data

The input file `rectangles.in` contains on the first line an integer $N$. The following $N$ lines contain 4 integers $x_1$, $y_1$, $x_2$, $y_2$, where $(x_1, y_1)$ and $(x_2, y_2)$ represent the opposite corners of a rectangle.

## Output data

The output file `rectangles.out` contains the number of squares present in the drawing.

## Constraints and clarifications

$1 \leq N \leq 1\,000$

The coordinates of the points in the input file range between $0$ and $10^9$.

For $60\%$ of the tests, the coordinates of the points in the input file will range between $0$ and $2\,000$.

## Example

`rectangles.in`

`
3
0 0 3 3 
0 1 3 2 
1 0 2 3 
`

`rectangles.out`

`
14
`

## Explanation

In the drawing, there are $9$ squares of side $1$, $4$ squares of side $2$, and one square of side $3$.