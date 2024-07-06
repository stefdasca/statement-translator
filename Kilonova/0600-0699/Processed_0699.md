```markdown
The universe map is considered to be a matrix with $250$ rows and $250$ columns. In each cell, there is a so-called stargate, and in certain cells, there are stargate crews. In one move, a crew can move from their current location to any other location that has a second stargate, in our case to any other position in the matrix. No more than one crew can be in a cell at the same time. At any point, only one crew can move from one stargate to another.

# Task

Given a number $p$ of crews, with the initial and final positions specified for each crew, determine the minimum number of moves required for all crews to get from their initial positions to their final positions.

# Input data
The input file `poarta.in` has the following format:
- The first line contains the natural number $p$ representing the number of crews.
- The next $p$ lines contain 4 natural numbers each, the first two representing the coordinates of the initial position of a crew (row and column), the next two representing the coordinates of the final position of the same crew (row and column).

# Output data
The first line of the output file `poarta.out` contains a single number representing the minimum number of moves required.

# Constraints and clarifications
- $1 < p < 5\ 000$
- The coordinates of the initial and final positions of the crews are natural numbers within the range $[1, 250]$.
- **Pay attention to cases where the initial position is the same as the final position!**
- The initial positions of the $p$ crews are distinct from each other.
- The final positions of the $p$ crews are distinct from each other.

# Example
`poarta.in`
```
3
1 2 3 4
6 5 3 9
3 4 1 2
```
`poarta.out`
```
4
```

## Explanation
~[0.gif|width=50em]
```