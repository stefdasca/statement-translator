In a developing country, in a certain city, the parking lot that the city hall wants to build has a rectangular shape and can be encoded using a matrix with $L$ rows (numbered from $1$ to $L$) and $C$ columns (numbered from $1$ to $C$). Practically, paving it entirely would require $L \cdot C$ square meters of tiles. The company that produces the tiles and is favored by the mayor builds tiles with a width of one meter and a length that can be more than one meter (but an integer value). The company assembles the tiles into packages, and all packages have exactly the same content (tiles in a package may have different lengths). Since public spending is at its peak, the mayor decides to buy one package of tiles for each column of the parking lot and cannot use tiles from any other package for that column. It is also known that each column has exactly one tree planted, which cannot be cut down. We assume a tree occupies exactly the area corresponding to a $1 \cdot 1$ tile.

# Task

After a councilor points out that it might be possible that the structure of the purchased package does not allow the paving of any column, and the mayor disagrees with this hypothesis, he decides to hire you as a programmer to tell him the number of distinct ways to pave the parking lot. When counting the variants, it should be noted that all tiles in a package are of different colors. We consider two paving methods distinct if there is at least one column where the same spot is covered by tiles of different colors.

# Input data

The file `parcare.in` contains numbers on the first line: $N$ (number of tiles in a package), $L$ (number of rows of the parking lot), $C$ (number of columns of the parking lot). The second line contains $N$ non-zero natural values representing the lengths of the tiles (they have a width of $1$). _There can be tiles of the same size, but they differ in color_. The third line contains $C$ numbers, the $i$-th representing the row where the tree is located on column $i$. Numbers on each line are separated by a space.

# Output data

The file `parcare.out` contains the number of paving methods, modulo $666 \ 013$

# Constraints and clarifications

* $1 \leq N \leq 20$
* $2 \leq L \leq 20$
* $1 \leq C \leq 100 \ 000$
* The lengths of the tiles are non-zero natural numbers less than $L$
* The values on the last line of the input file are between $1$ and $L$, inclusive

# Example

`parcare.in`
```
5 7 2
1 2 3 4 5
4 2
```

`parcare.out`
```
12
```
