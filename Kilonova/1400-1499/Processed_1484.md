~[birouri.png|align=right]
Arhi has proposed to extend the office building he initially designed on a single level numbered with $1$, divided into $n \cdot n$ square zones with side length $1$, each corresponding to an office, by constructing multiple levels. In the corners of all the offices, resistance beams are built. To ensure the integrity of the entire building, Arhi will design new levels, numbered $2$, $3$, ... as long as they contain at least one office and the following four rules are respected:

$R1$: each new level will be designed in the form of a rectangle or square of maximum area for odd-numbered levels, and in the form of a square of maximum area for even-numbered levels;

$R2$: each corner of the walls of a new level must be placed on a resistance beam between two or more offices from the previous level;

$R3$: any two corners of the walls of a new level will be placed on different walls (a wall cannot be completely superimposed on another wall) and at least two opposite corners of a new level will be located on opposite walls of the previous level;

$R4$: any portion of the wall on level $k \ (k \gt 1)$, built above an office on level $k - 1$, will overlap exactly one of the sides of the office, or it will traverse it diagonally.

The offices on level $k \ (k \gt 1)$ will be built exactly above those on the previous level, thus levels $2$, $4$ etc. will have triangular spaces next to the walls that will not belong to any office.
The numbers inscribed on the offices in the above image indicate the level corresponding to the offices visible from above the building.

# Task

Given the length $n$ of the side of the first level of the building, determine:
1. the maximum number of levels the building can have
2. the total number of offices in the building with the maximum number of levels

# Input data

The input file `birouri.in` contains on the first line one of the values $1$ or $2$, representing task $1$, if it is required to determine the maximum number of levels the building can have, or task $2$, if it is required to determine the total number of offices in the building with the maximum number of levels.
The second line contains a natural number $n$ (representing the length of each wall of the first level of the building).

# Output data

The output file `birouri.out` contains on the first line a natural number representing the maximum number of levels the building can have, if the task was $1$, or a natural number representing the total number of offices in the building with the maximum number of levels, if the task was $2$.

# Constraints and clarifications

* $3 \leq n \leq 32\ 768$
* For the correct solving of task $1$, $30\%$ of the score is awarded, and for the correct solving of task $2$, $70\%$ of the score is awarded.

# Example 1

`birouri.in`
```
1
10
```

`birouri.out`
```
5
```

## Explanation

The example corresponds to the image above. The building with a base level with side length $10$ will have $5$ levels.
Level $6$ is no longer built, as it would not contain an office.

# Example 2

`birouri.in`
```
2
10
```

`birouri.out`
```
172
```

## Explanation

* on the first level $100$ offices;
* on the second level $40$ offices;
* on the third level $24$ offices;
* on the fourth level $4$ offices;
* on the fifth level $4$ offices.

$100 + 40 + 24 + 4 + 4 = 172$