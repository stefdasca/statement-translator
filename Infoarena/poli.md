## Task

A polyomino is a connected geometric figure made of squares with an area of $1$, having vertices at integer coordinate points. Clearly, the squares have their edges parallel to the coordinate axes. Two squares are called adjacent if they share a common side. A figure is connected if from any square of the figure you can reach any other square by passing through a succession of squares where any two consecutive squares are adjacent. Two polyominoes are considered identical if one can be obtained from the other by a translation. A horizontal edge of a polyomino is made up of a sequence of squares of area $1$ of the polyomino, such that any two consecutive squares share a common vertical edge. A polyomino is horizontally-convex if any horizontal line (a line parallel to the $Ox$ axis) intersects only one horizontal edge of the polyomino or none. For example, the polyomino in Figure 1 is horizontally convex, but the polyomino in Figure 2 is not horizontally convex. Write a program that determines the number of horizontally convex polyominoes with area $n$.

## Input data

The input file `poli.in` contains a single line, which contains a positive natural number $n$.

## Output data

The output file `poli.out` contains a single line, which will contain the number of horizontally convex polyominoes with area $n$.

## Constraints

$0 < n \leq 1000$

## Example

`poli.in`
`3`

`poli.out`
`6`

`poli.in`
`9`

`poli.out`
`6466