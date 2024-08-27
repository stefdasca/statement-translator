# Rectangles

Clod was bored one day in math class and while the teacher was explaining Pick’s theorem on the board, Clod was thinking of a more interesting problem: for a grid of lattice points with dimensions $N*M$ (lattice points are points with integer coordinates), what is the number of rectangles with vertices at lattice points? Clod is curious if there is a formula for this problem and would like to know the solution for different grid sizes, to try to guess such a formula.

## Task

Help Clod find the answer!

## Input data

In the input file `dreptunghiuri.in`, the first line will contain two integers $m$ and $n$ separated by a space.

## Output data

The output file `dreptunghiuri.out` will contain on the first line a single integer representing the number of rectangles requested in the problem.

## Constraints

$0 < m, n \leq 400$

For tests worth a total of 60 points,

$0 < m, n \leq 90$

## Example

`dreptunghiuri.in`
```
3 3
```

`dreptunghiuri.out`
```
10
```

## Explanation

In the 10 figures, all rectangles that can be formed with corners at integer coordinate points for a grid of dimensions $3 \times 3$ are drawn.