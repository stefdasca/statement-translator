In a volcanic rectangular area of whole dimensions $N \cdot M$, divided into square cells with side length $1$, there exist $P$ geysers.

Geysers are intermittent volcanic springs that emit hot water and/or steam jets into the atmosphere at regular intervals due to the rapid heating of water in underground cavities.

~[Poza1.png|align=right|width=30em]

The eruption of a geyser produces a hot water splash in a circular area with its center located at the point $(x,y)$ on row $x$ and column $y$, and radius $r$, the affected area being considered the zone bounded by the square in which the circle is inscribed.

In the adjacent figure, we have $2$ geysers with coordinates $(3,3)$ and $(5,8)$, the first geyser with a radius of $1$, and the second geyser with a radius of $2$.

For each geyser, the interval of time $t$ consumed between eruptions, as well as the duration $d$ of an eruption, are known, values expressed in seconds.

A researcher's mission is to find a route that starts from a given point of the terrain located on the west side $(v,1)$ and crosses the area without leaving it and without passing through the same position twice until another point $(e,M)$ located on the east side.

The researcher can move in any of the **north**, **east**, **south** directions, and the time consumed for traversing a cell unaffected at a given moment is one second. Traversing an area in which **at least** one geyser is active **during its eruption period** poses significant risks for the researcher.

# Task

Determine the minimum time required to traverse from west to east of the volcanic area by the researcher without major risks.

# Input data

The file `gheizere.in` contains:

* the first line contains three natural values $N, M$ and $P$, where $N$ represents the number of rows and $M$ the number of columns of the volcanic area, and $P$ the number of geysers;
* the second line contains two natural values $v$ and $e$, where $v$ represents the starting row from the west, and $e$ the ending row on the east;
* the next $P$ lines each contain a set of five values $x, y, r, t, d$ which represent in order, for each geyser the coordinates of the center $(x,y)$, $r$ the radius of the eruption circle, $t$ the time between eruptions, and $d$ the duration of an eruption.

# Output data

The file `gheizere.out` will contain a single natural value $T$ which represents the minimum time required for the researcher to traverse the volcanic area from west to east without major risks.

# Constraints and clarifications

* $2 \leq N, M \leq 250$
* $1 \leq e, v \leq N$
* $1 \leq x \leq N$
* $1 \leq y \leq M$
* $1 \leq P \leq 1\ 000$
* $1 \leq r \leq 5$
* $1 \leq d \leq 5$
* $2 \leq t < 10$
* Two geysers cannot have the same coordinates for the center of the circle
* Initially, all geysers are inactive
* The researcher traverses the route without stopping
* There is always a solution for the input data
* The maximum duration of a route traversed by the researcher is $\leq 1\ 000$ seconds

# Example

`gheizere.in`
```
9 10 5
1 9
2 6 1 2 2
3 3 1 3 3
6 8 2 6 1
8 2 1 4 2
9 5 1 4 1
```

`gheizere.out`
```
18
```

# Explanation

One of the possible routes that starts from $(1,1)$ and reaches $(9,10)$ in minimum time is marked, second by second, in the following figure.

The areas influenced by the geysers are marked with gray squares, and the center of each geyser is highlighted (**bold**).

~[Poza2.png|align=left|width=20em]