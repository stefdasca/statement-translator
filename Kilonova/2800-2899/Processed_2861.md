In a city, there is a rectangular garden made up of $n \times m$ squares, arranged in the form of a matrix with $n$ rows and $m$ columns. In each square, a single plant of a certain species can be cultivated. The species are identified by distinct numbers between $1$ and $s$. Due to meteorological phenomena, some squares no longer have flowers.

The soil in each square has a certain moisture coefficient. For cultivation, each species of flowers needs a minimum soil moisture value. Specifically, if the soil moisture in a square is less than the specific moisture of the plant, it cannot be cultivated in that square. The garden owner wants to redecorate it by keeping the already existing plants but also cultivating new plants in the squares from which the flowers have disappeared, so as to obtain an area as large as possible covered with plants of the same species.

A zone is defined as a group of squares, so that any two squares in the zone are either adjacent (i.e., they share a common side) or can be reached from one to the other by moving only from a square to one adjacent to it. The area of ​​a zone is equal to the number of squares that make up the zone.

# Task

Determine the area value of the maximum area zone cultivated with plants of the same species, obtained after redecorating the garden.

# Input data

The input file `gradina.in` contains on the first line three non-zero natural numbers separated by a space: $n$, $m$ and $s$ where $n$ and $m$ represent the number of rows and the number of columns of the matrix representing the garden, respectively, and $s$ is the number of plant species that can be cultivated in the garden.

In the next $n$ lines, there are $m$ natural numbers ranging between $0$ and $s$, representing the matrix $T$, which encodes the garden as follows: the $j$th element on the $i+1$th line of the file ($T_{i, j}$) is equal to $0$ if the corresponding square does not contain flowers or, otherwise, is equal to the species number of the flower.

On the $n+2$ line, there are $s$ natural numbers, separated by a space, representing in order the minimum moisture coefficients required for the $s$ species of flowers.

In the next $n$ lines, there are $m$ natural numbers separated by a space; the $j$th number on the $(n+2+i)$th line of the file represents the soil moisture coefficient of the square located on the $i$th row and $j$th column of the garden.

# Output data

The output file `gradina.out` will contain a single line which will contain a natural number, representing the area value of the maximum area zone cultivated with plants of the same species, after redecorating the garden.

# Constraints and clarifications

* $4 \leq n, m \leq 50$
* $2 \leq s \leq 100$
* The soil moisture coefficients of the species and soil are non-zero natural numbers less than $1\ 000$.

# Example

`gradina.in`
```
6 6 5
2 0 0 1 4 4
0 0 1 1 0 0
0 0 0 0 3 0
0 1 5 5 0 0
1 2 2 0 5 4
5 2 0 0 3 0
10 6 4 9 8
10 20 3 10 5 10
2 12 20 8 7 9
14 5 9 8 10 2
2 16 15 14 7 2
12 14 12 15 14 12
11 14 11 9 11 12
```

`gradina.out`
```
10
```

## Explanation

The value displayed in the output file is the area for the maximum area zone occupied by species $3$ and formed by $10$ squares occupying the positions: $(1,2)$, $(2,2)$, $(2,5)$, $(2,6)$, $(3,1)$, $(3,2)$, $(3,3)$, $(3,4)$, $(3,5)$, $(4,5)$.