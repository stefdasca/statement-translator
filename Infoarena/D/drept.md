## Task

Given $N$ points in the plane, find the minimum area of a rectangle with sides parallel to the coordinate axes that contains at least $K$ of the given points either inside or on its edges.

## Input data

The first line of the input file contains the numbers $N$ and $K$, and the following $N$ lines contain the coordinates of the points. 

## Output data

The output file must contain the required minimum area.

## Constraints and clarifications

$1 \leq K \leq N \leq 1\ 000$

all coordinates are natural numbers less than $30\ 000$
 
## Example

`drept.in`

```
13 7
5 5
7 8
6 8
5 8
4 6
6 3
4 2
8 0
9 2
3 4
7 8
5 4
5 3
```

`drept.out`

```
10
```

## Explanation

The desired rectangle has its bottom-left corner at the coordinates $(5, 3)$ and its top-right corner at the coordinates $(7, 8)$.