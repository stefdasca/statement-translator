Corina bought a piece of patterned cloth from the store, shaped as a rectangle, to cut out a tablecloth for the kitchen table. Being passionate about chess, Corina chose a material consisting of $n \times m$ squares of the same size colored in white or black. The squares are adjacent and are arranged in rows and columns parallel to the sides of the rectangular cloth that was purchased. Two squares are called neighbors if they share a side.

The cloth does not necessarily follow the structure of a chessboard, meaning the neighboring squares in the same row or column are not necessarily alternately colored.

Corina therefore proposes to cut out a rectangle with the maximum number of squares, parallel to the sides of the purchased rectangular cloth, that respects the alternating colors of a chessboard.

# Task
Determine the maximum number of whole squares of a rectangle with sides parallel to those of the purchased material, which can be cut out such that there are no two neighboring squares having the same color.

# Input data
The file `fadema.in` contains on the first line two natural numbers $n$ and $m$ representing the number of rows and the number of columns of the purchased cloth material, respectively.
Each of the following $n$ lines contains $m$ digits `0` or `1` separated by a space, representing the colors of the squares on the material. The digit `0` encodes the color white, and the digit `1` encodes the color black.

# Output data
The file `fadema.out` will contain on the first line a single natural number $A$, representing the maximum number of squares of a rectangle that can be cut out such that it respects the task from the statement. If there are no rectangles with at least two squares having alternating colors, the value $1$ will be printed.

# Constraints and clarifications
- $2 \leq N \leq 1\ 000$
- $2 \leq M \leq 1\ 000$
- For correctly solving the task while respecting the problem constraints, 90 points are awarded.
- For correct results respecting the problem constraints and $n, m \leq 100$, 20 points are awarded.
- For correct results respecting the problem constraints and $n, m \leq 200$, 40 points are awarded.
- For correct results respecting the problem constraints and $n, m \leq 400$, 65 points are awarded.
- Automatically 10 points are awarded.

# Example 1
`fadema.in`
```
3 4
0 0 1 0
1 1 0 0
1 0 1 0
```
`fadema.out`
```
6
```
## Explanation
The rectangle delimited by rows $1$ and $3$, and columns $2$ and $3$ has $6$ squares.

# Example 2
`fadema.in`
```
4 5
0 1 1 0 1
1 0 1 0 1
0 0 1 1 0
1 1 0 1 1
```
`fadema.out`
```
5
```
## Explanation
The rectangle delimited by row $2$, and columns $1$ and $5$ has $5$ squares.