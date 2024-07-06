In Constanța county, there are at most $2\ 500$ tourist attractions spread over a grid-like area, consisting of squares with a side length of $1$ kilometer. The attractions are located at some intersection points of the grid.

Two attractions are considered *neighbors* if they are situated on one of the North, South, East, West directions at a distance of $1$ kilometer from each other.

Direct roads have been constructed between certain pairs of neighboring attractions to ensure travel between any two attractions.

Regarding each attraction, we have the following information:
- The associated number, which is unique and has a value between $1$ and the total number of attractions;
- The neighboring attractions with which it is connected by direct roads (at most four attractions).

For each two communicating attractions, the cost of paving the direct road between them is known.

# Task
Write a program that solves the following tasks:
1. A map of the county needs to be created, showing all the attractions. The map will be represented as a matrix with a maximum size of $51 \times 51$. Each element of the matrix encodes, through a sequence of four binary digits, the existence of direct roads that border a square of the grid. If there is a direct road on the north side of this square, then the most significant bit will be $1$. Otherwise, it will be $0$. The other three bits correspond, in order, to the South, East, West directions. For example, if there are roads for a square on the North, South, and West sides, the four bits will be: $1$, $1$, $0$, $1$. The map must have a minimal surface area but include all attractions. 
2. It is desired to pave some of the existing roads so that one can travel, using only paved roads, from any attraction to any other. The total cost of paving must be minimal. Specify which roads will be paved.

# Input data
In the input file `ob.in`, the first line contains the number $C$, which represents the task to be solved.

Then, there is an unknown number of lines until the end of the file, each being of the form:
`NO nvN cdsN nvS cdsS nvE cdsE nvV cdsV`
having the following meaning:
- `NO` = attraction number;
- `nvN` = north neighbor attraction number;
- `cdsN` = cost of the road to the north;
- `nvS` = south neighbor attraction number;
- `cdsS` = cost of the road to the south;
- `nvE` = east neighbor attraction number;
- `cdsE` = cost of the road to the east;
- `nvV` = west neighbor attraction number;
- `cdsV` = cost of the road to the west.

If an attraction does not have a neighbor in a certain direction, the neighbor number for that direction will be replaced with $0,$ and the cost of the direct road between the two with $0$.

**The values on a single line are separated by one or more spaces.**

# Output data
The output data is written in the file `ob.out`.

If $C=1$, print a map of the attractions using numbers between $0$ and $15$. Each number represents the decimal encoding of the four binary digits.

If $C=2$, print on the first line the required optimal cost and on subsequent lines the attractions between which the road will be paved.

# Constraints and clarifications
- The number of attractions is at most $2\ 500$.
- The map fits into a $51$ by $51$ matrix.
- The lengths of the direct roads are at most $100$.
- Direct roads between attractions are bidirectional.
- Input data is guaranteed to be mutually consistent.
- The first 10 tests are worth 50 points and have $C = 1$; the next 10 tests are worth 50 points and have $C = 2$.

# Example 1
`ob.in`
```
1
1 0 0 0 0 2 3 0 0
3 6 3 0 0 0 0 2 1
6 0 0 3 3 0 0 5 2
2 5 2 0 0 3 1 1 3
4 0 0 0 0 5 3 0 0
5 0 0 2 2 6 2 4 3
```
`ob.out`
```
2 7 5
2 11 9
```

# Example 2
`ob.in`
```
2
1 0 0 0 0 2 3 0 0
3 6 3 0 0 0 0 2 1
6 0 0 3 3 0 0 5 2
2 5 2 0 0 3 1 1 3
4 0 0 0 0 5 3 0 0
5 0 0 2 2 6 2 4 3
```
`ob.out`
```
11
1 2
2 3
6 5
2 5
5 4
```

## Explanation
Both examples correspond to the map below:
~[ex.png|width=25em]