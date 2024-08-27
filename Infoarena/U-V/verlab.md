# Verlab

In this problem, we want to check if a grid is a maze or not. A maze is a grid with a series of additional properties: adjacent cells can have at most one separating wall, defined for only one of the cells, each cell on the edge is separated from the outside by a wall, and between any two cells in the grid, there is exactly one simple path composed of steps on the horizontal and vertical directions between adjacent and non-separated cells. Each cell is described by a 4-bit natural number, where true bits describe, in order, the existence of a wall in the directions up, right, down, left. For example, the number $5 = 0 \times 2^3 + 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0$ describes a cell with walls only on the right and left.

## Input data

The first number in the input file `verlab.in` is the number of tests $T$. Then for each test, the number of rows $R$ and the number of columns $C$ are given; these are followed by $R \times C$ numbers between $0$ and $15$, representing the cells in rows and columns. The numbers are given: from top to bottom and, for a fixed row, from left to right. The numbers are preceded, separated, and followed by any number of whitespace characters.

## Output data

In the output file `verlab.out`, there will be $T$ numbers, one single number for each test, in the order of the tests: $1$ for a grid that is a maze, or $0$ for a grid that is not a maze. The number is followed by an end-of-line character.

## Constraints

$1 \leq R$  
$C \leq 100$  
$T \leq 100$

## Example

`verlab.in`  
`2 2 2 13 12 3 6 1 1 14 1 0`  
`verlab.out`  
`1 0`

## Explanation

In the first test, the grid has $4$ cells, distributed over $2$ rows and $2$ columns. The top-left cell with the value $13$ has three walls: up, right, and left. The top-right cell with the value $12$ has two walls: up and right. The bottom-right cell with the value $6$ has two walls: right and down. The bottom-left cell with the value $3$ has two walls: down and left. Note how the right wall of the top-left cell separates it from the top-right cell. The grid respects the properties of a maze. In the second test, the only cell in the grid lacks one of the walls with the exterior, which makes the grid not be a maze.