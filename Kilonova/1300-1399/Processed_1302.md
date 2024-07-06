```markdown
The Galaxy Map is represented as a matrix with $N$ rows (numbered from $1$ to $N$) and $M$ columns (numbered from $1$ to $M$). Any element of the matrix represents a square-shaped area with side length of $1$ light year (called a quadrant) and can be identified by its coordinates (the row number and the column number it is located at).

The spaceship Enterprise is located in a quadrant with known coordinates and needs to reach its destination (another quadrant, different from the starting one, with also known coordinates).

The spaceship can move from one quadrant to one of its neighboring ones horizontally or vertically in one unit of time (specifically, from the quadrant at coordinates $(L,C)$, the spaceship can move to one of the quadrants at coordinates $(L-1,C), (L+1,C), (L,C-1), (L,C+1)$, without leaving the map).

Additionally, in some areas (quadrants) there are stargates. A stargate allows the spaceship to move in one unit of time to any other area where another stargate is located. If the spaceship arrives at an area with a stargate, it can move to another area with a stargate or continue its journey to one of the neighboring areas.

# Task

Determine the minimum time in which the spaceship can reach from the initial area to the final area, as well as the number of minimum duration paths. 

# Input data

The input file `poarta.in` contains on the first line the natural numbers $N, M, K$, representing in order, the number of rows, the number of columns, and the number of stargates on the map. The second line contains 4 natural numbers $L_1, C_1, L_2, C_2$, representing the coordinates of the starting area, and the coordinates of the destination area, respectively. On the following $K$ lines are written the coordinates of the areas where stargates are located, one stargate per line. The numbers on the same line are separated by a space.

# Output data

The output file `poarta.out` will contain two lines. The first line will contain the natural number $D$, representing the minimum time in which the spaceship reaches from the initial area to the destination. The second line will contain the natural number $T$, representing the number of minimum duration paths. Since the number $T$ can be very large, you need to print $T$ modulo $997$.

# Constraints and clarifications

* $1 \leq N, M \leq 100$
* $0 \leq K \leq 1\ 000$
* For $20\%$ of the tests $1 \leq N, M \leq 10, 0 \leq K \leq 10$
* $30\%$ of the score is awarded for correctly determining the minimum time. The full score is awarded for correctly determining both the minimum time and the number of minimum duration paths.

# Example

`poarta.in`
```
6 7 4
2 5 6 2
1 1
5 1
1 6
4 5
```

`poarta.out`
```
5
6
```

## Explanation

The Universe Map has $6$ rows and $7$ columns. It contains $4$ stargates ($\textcircled{1} \ \textcircled{2} \ \textcircled{3} \ \textcircled{4}$). The spaceship Enterprise $\u25A0$ is initially located at the area with coordinates $(2,5)$ and has as its destination $\u25A1$ the area with coordinates $(6,2)$.

~[img.png|width=20em]

The minimum duration of the journey from $\u25A0$ to $\u25A1$ is $5$, one possible path of duration $5$ being: $(2,5)\u2192(2,6) \u2192(1,6) \u2192(5,1) \u2192(5,2) \u2192(6,2)$.

There are $6$ paths of minimum length $5$.
```
