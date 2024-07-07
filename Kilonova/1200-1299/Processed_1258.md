Sure, here is the translated text:

````markdown
On a square-shaped piece of land, there are areas of dry land and lakes. The map of the terrain is stored in a two-dimensional array $n \cdot n$ with values $1$ (water) or $0$ (dry land). Rows are numbered from $1$ to $n$ from top to bottom, and columns from $1$ to $n$ from left to right.

Each lake is surrounded by an area of dry land. The only exception is the lakes located at the edge of the terrain, which are surrounded by dry land only within the terrain and not outside it.

# Task

The goal is to traverse the land on dry land, from position $(1, 1)$ to position $(n, n)$, on a path of minimum length, moving step by step.

In one step, you can move from one square to an adjacent one to the north, east, south, or west. Write a program that:

a) Determines the number of lakes that are square-shaped and at the same time "full of $1$s"
b) In case all lakes are square-shaped and at the same time "full of $1$s", find a path with the above properties.

# Input data

The input file `lacuri.in` contains on the first line the number $n$, and on the following $n$ lines the map of the terrain (each line has $n$ values $0$ or $1$, separated by a space).

# Output data

The output file `lacuri.out` will contain:

* on the first line: the number of lakes that are square-shaped and at the same time "full of $1$s"
* in case all lakes are square-shaped and at the same time "full of $1$s", the following lines describe the chosen minimum length path. Each line in the file contains a pair of coordinates of successive positions through which the path passes (row and column, separated by a space), starting from $(1,1)$ and ending at $(n,n)$

# Constraints and clarifications

* $2 \leq n \leq 100$
* Positions $(1,1)$ and $(n,n)$ are surely free (with value $0$)
* If there are multiple solutions, any of them can be displayed
* There can be at most $100$ lakes and at least one; if a lake is square-shaped, then $1 \leq \text{side} \leq n-1$. Regardless of their shape, lakes are surely "isolated", meaning they do not "touch" any other lake. For example, if a lake contains position $(3,3)$, then another lake cannot contain any of the adjacent positions to $(3,3)$, meaning: $(2,3), (2,4), (3,4), (4,4), (4,3), (4,2), (3,2)$ and $(2,2)$.

# Example

`lacuri.in`
```
6
0 0 0 0 0 0
0 1 0 1 1 1
0 0 0 1 1 1
0 0 0 1 1 1
1 1 0 0 0 0
1 1 0 0 1 0
```

`lacuri.out`
```
4
1 1
1 2
1 3
2 3
3 3
4 3
5 3
5 4
5 5
5 6
6 6
```

# Explanation

a) The first line contains $4$ (there are $4$ square-shaped lakes and "full of $1$s")
b) Since all $4$ lakes are square-shaped and "full of $1$s", the chosen path is also written: from $(1,1), (1,2), (1,3), (2,3), (3,3), ... , (6,6)$.

Observations

1) If position $(3,5)$ had a $0$, then the lake with a side of $3$ would no longer be "full of $1$s" and then the first line would only contain the value $3$ (only $3$ square-shaped lakes would be "full of $1$s")
2) In the initial example, if position $(6,1)$ had a value of $0$, then not all lakes would be square (the bottom-left one would not be square) and only a $3$ would be displayed in the output file
3) In the initial example, if position $(5,2)$ had a value of $0$, then only a $3$ would be displayed, because the bottom-left lake would not be a square-shaped lake and "full of $1$s"
