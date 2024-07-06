```
The year is $2154$, somewhere on the lush planet _Pandora_. Here, the RDA (_Resources Development Administration_) settlers want to establish a star base to exploit the natural reserves of _unobtainium_, a rare and precious ore abundant in the floating mountains (_Hallelujah Mountains_), mountains that float slowly carried by magnetic currents similar to icebergs in the sea, on the liquid gas surface of the planet.

For prospecting and exploiting the ore deposits, it is necessary to map the planet's surface and create a digitized map represented as a two-dimensional array. Thus, the region of geological interest is divided into $N \cdot N$ identical territorial squares (zones), each zone being identified by the triplet $(x, y, c)$, where $(x, y)$ represents the coordinates of the territorial zone ($x$ - the row, $y$ - the column), and $c$ the altitude (height). Between the occupied mountainous zones, there are vast areas of liquid gas, zones that have altitude $0$.

~[pandora.png|align=right]

For harvesting and transporting unobtainium to the star base, the RDA settlers use _spice-harvesters_, special ships with vertical landing capability.

Landing on floating mountains is a real challenge for RDA pilots. To be able to land, pilots must identify a flat sector (landing platform), a platform that respects the design of the landing gear of the ships (see the adjacent figure). The platform has the shape of a square with side $k$ that is made up of $k \cdot k$ territorial zones, so that $k \cdot k - 4$ zones have the same altitude, and the four corners of the square have an altitude strictly lower than the rest of the square zones.

# Task

Knowing the description of $M$ territorial zones that make up the floating mountains, determine the coordinates of the top-left corner of the landing platforms for the floating mountains that allow landing.

# Input data

The input file `pandora.in` contains on the first line three natural numbers $N$, $k$, and $M$, separated by a space, with the meaning from the statement. The next $M$ lines contain the description of the $M$ zones that make up the floating mountains, zones given in the form of a triplet of non-zero natural numbers $x$, $y$, $c$, the numbers being separated by a space.

# Output data

In the output file `pandora.out`, there will be written, one pair per line, the coordinates $x$, $y$ separated by a space, which represent the top-left corner of the landing platforms for each floating mountain that allows landing. If there are no landing platforms, $0$ will be displayed.

# Constraints and clarifications

* $2 \leq N \leq 1\ 000$
* $2 \leq M \leq 200\ 000$
* $3 \leq k < 400$
* $1 \leq x, y \leq N$
* $0 \leq c \leq 1\ 000$
* By floating mountain, we understand the entirety of the zones with non-zero altitude that are surrounded by liquid gas and are neighbors in one of the four directions: north, east, south, west. The mountainous zone is compact, meaning it does not contain zones with $c = 0$ inside. The mountains are separated by gas zones. The digital map is considered to be bordered by atmospheric gas.
* The landing platforms have non-zero altitudes.
* If a mountain has multiple landing platforms, the one with the smallest $x$ coordinate will be determined, and for equal $x$ coordinates, the one with the smallest $y$ coordinate.
* For $10\%$ of the tests $k < 10$. For another $20\%$ of the tests $N \leq 500$

# Example

`pandora.in`
```
9 3 43
1 2 1
1 3 2
1 4 1
2 1 4
2 2 2
2 3 2
2 4 2
3 1 3
3 2 1
3 3 2
3 4 1
1 6 2
1 7 3
1 8 1
2 6 3
2 7 3
2 8 3
2 9 1
3 6 1
3 7 3
3 8 2
5 2 1
5 3 4
5 4 3
6 2 4
6 3 4
6 4 4
6 5 4
7 2 2
7 3 4
7 4 3
7 5 3
8 2 2
8 3 2
6 7 5
6 8 2
6 9 5
7 7 2
7 8 2
7 9 2
8 7 1
8 8 2
8 9 1
```

`pandora.out`
```
1 2
5 2
1 6
```

## Explanation

~[pandora2.png]

Note, the platform in the bottom-right is not correct because there are corner values (values of $5$) that are greater than the values in the platform.
```
