## Task

Given $N$ points in the $XOY$ plane with integer coordinates. A point is called external if both of the following conditions are met simultaneously:
1. It can be moved as much as possible to the left or right without touching another point.
2. It can be moved as much as possible up or down without touching another point.
A point is called internal if it cannot be moved as much as possible either to the left/right or up/down without touching another point. Write a program that finds the number of external points and the number of internal points from the initial configuration, and then executes two types of operations: "add point" and "remove point." After each operation, the new number of external points and the new number of internal points are required again.

## Input data

The input file points2.in contains:
1. The first line contains the number $N$ of initial points.
2. Each of the following $N$ lines contains two positive integers, separated by a space, representing the coordinates of each point.
3. On the line $N + 2$, there is a natural number $Q$, representing the number of operations to be performed.
4. The following $Q$ lines contain 3 positive integers: the first number can be $1$ - if adding a point or $2$ - if removing a point. The next two numbers constitute the coordinates of the point to be added/removed.

## Output data

The output file points2.out will contain $Q + 1$ lines. The first line will contain the initial number of external and internal points. On the line $i + 1$ will contain the number of external and internal points after operation $i$.

## Constraints

$0 < N \leq 100000$

$0 < Q \leq 100000$

$0 < \text{coordinates of each point} \leq 100000$

It is guaranteed that for each type $2$ operation, the point to be deleted is in the plane.

It is guaranteed that at any moment there will not be $2$ or more points with the same coordinates simultaneously in the plane.

For $40\%$ of tests, $Q \leq 2000$ and there are no more than $2000$ points simultaneously in the plane.

## Example

`points2.in`

```
10
1 4
2 1
1 2
3 4
4 2
2 2
1 1
3 1
3 2
4 3
6
1 5 1
6 1 7
2 2 1
1 2 3
```

`points2.out`

```
7 2
7 2
8 1
8 1
7 2
8 1
```

## Explanation

The initial set of points is given in the figure above. The internal point is marked with □, the external points are marked with ▪, and the rest of the points are marked with ο