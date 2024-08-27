# Pietre2

In ancient Egypt, pyramids were built on square-shaped lands. These lands were divided into square zones with a side length of $1$. On these squares, a number of stone cubes were placed. When placing a new cube, the Egyptians started somewhere from the edge of the land and advanced such that at each step they passed on a square where the number of stone cubes was exactly $1$ more than the number of cubes in the place where they were located. They could not step from one square to another that was diagonally adjacent. The stone was placed on the square from which they could no longer advance.

## Task

Determine the longest path the Egyptians will travel to transport a stone to its place.

## Input data

The input file `pietre2.in` contains on the first line the length $n$ of the side of the square on which the stones are transported. Each of the following $n$ lines contains $n$ natural numbers, separated by spaces, representing the number of stone cubes on the corresponding squares.

## Output data

The output file `pietre2.out` should contain on the first line a natural number, representing the length of the longest path (the number of steps needed to advance from an arbitrary position through adjacent squares). On the second line, the output file should contain the starting position, indicating the row index and the column index, separated by a space. If there is no position from which it is possible to advance upward, the first line of the file will contain the number $0$, and the second line will contain two numbers equal to $0$.

## Constraints and clarifications

$1 \leq n \leq 100$

$0 \leq \text{number of cubes on a square} \leq 10\,000$

If there are multiple solutions, print only one.

## Example

`pietre2.in`
```
6
1 2 2 2 2 2
4 3 4 2 2 1
1 1 5 6 1 8
1 1 9 6 7 1
3 4 4 5 1 1
2 1 1 1 1 5
```

`pietre2.out`
```
5
1 1
```

## Explanation

Starting from the top-left corner, you can take at most $5$ steps ($1 \to 2$, $2 \to 3$, $3 \to 4$, $4 \to 5$, $5 \to 6$). From any other position, the paths would be shorter.