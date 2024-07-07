A lake has a cubic shape with side length $M$ (a natural number). It is divided into $M^3$ elementary positions. A position (a cell) is identified by the coordinates $n$, $l$, $c$, as in a three-dimensional space, where:

* $n$ represents the level ($1$ being the one right near the water surface, $M$ being the one at the bottom of the lake), 
* $l$ represents the line (line $1$ is the one closest to the viewer),
* $c$ represents the column (column $1$ is the one on the viewer's left).

~[lac.png]

**Example for $m = 4$**

_Examples of elementary moves_:

- from position ($4$, $2$, $2$) it is possible to move to one of the positions: ($3$, $1$, $1$), ($3$, $1$, $2$), ($3$, $1$, $3$), ($3$, $2$, $1$), ($3$, $2$, $2$), ($3$, $2$, $3$), ($3$, $3$, $1$), ($3$, $3$, $2$), ($3$, $3$, $3$);
- from position ($2$, $1$, $1$) it is possible to move to one of the positions: ($1$, $1$, $1$), ($1$, $1$, $2$), ($1$, $2$, $1$), ($1$, $2$, $2$).

There is a special cell at the water surface, considered at level $0$ and specifically the one where a diver starting from the bottom of the lake must eventually arrive.

In the lake, there are elementary positions considered as workstations that need to send certain messages to the surface. These stations can be in any number and can be placed anywhere in the cube (including at the diver’s starting position).

The diver can move from its position only to a position on the immediate upper level (from level $i$ to level $i-1$, for $1 \leq i \leq m$) and which differs in line and column by at most $1$ compared to the previous position. Thus, from one position it is possible to move (see figure) to a maximum of $9$ positions on the immediate upper level.

The diver is at the bottom of the lake at coordinates $m$, $l_1$, $c_1$. He must reach the surface of the lake (that is, _above_ the first level of the cube), in a position with coordinates $0$, $l_2$, $c_2$, that is, just above the position $1$, $l_2$, $c_2$ in the cube.

# Task

You must determine which path the diver should take to bring to the destination as many messages as possible, respecting the restrictions from the statement.

# Input data

The input file `scafandrul.in` contains:

* the first line contains five numbers $m \ l_1 \ c_1 \ l_2 \ c_2$ separated by a space, representing $m$ the size of the cube, $l_1$, $c_1$ the line and column of the starting position, and $l_2$, $c_2$ the line and column of the arrival position;
* the second line contains the number $y$ of stations in the lake;
* the next $y$ lines contain sets of four numbers $n \ l \ c \ p$. The first three numbers $n \ l \ c$ represent the coordinates of a station, and the last number $p$ represents the number of messages to be sent from that station;

# Output data

The output will be written in the file `scafandrul.out` in the following format:

* the first line will contain the maximum number of messages brought to the surface.
* the next $m+1$ lines will contain sets of four numbers $n \ l \ c \ p$, the first three numbers representing the coordinates of the visited stations (in the traversal order), and the last number representing the number of messages collected from that station.

The first line of the $m+1$ represents the starting point, and the last line represents the arrival point (level $0$).

# Constraints and clarifications

* $2 \leq M \leq 20$
* $0 \leq P \leq 100$
* Exiting the lake is only allowed through the arrival point.
* There is no station at the arrival point.
* If for a certain position all possible moves are to cells without stations, then a line with the coordinates of the chosen cell and the value $0$ for the number of messages (as for a station with $0$ messages) will be written in the output file.

# Example

`scafandrul.in`
```
3 2 2 2 2
6
1 3 1 10
2 1 3 9
2 2 1 6
2 3 2 7
2 3 3 8
3 2 2 5
```

`scafandrul.out`
```
22
3 2 2 5
2 3 2 7
1 3 1 10
0 2 2 0
