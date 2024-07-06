Based on an image taken from a satellite, a map of a small locality is created. The locality occupies a rectangular area, with its sides oriented in the North-South and East-West directions. By studying the image obtained from the satellite, the cartographers found that all $k$ buildings have the shape of distinct rectangles. The image can be represented as an array with $n \cdot m$ cells arranged in $n$ lines numbered from $1$ to $n$ and $m$ columns numbered from $1$ to $m$.

We define a **road** as a rectangular section of the array that traverses the **entire locality** in the East-West direction and has a maximum number of lines or a rectangular section that traverses the **entire locality** in the North-South direction and has a maximum number of columns. Roads, obviously, should not pass through buildings.

Cartographers are interested in representing only the buildings on this map to scale, not the roads. Therefore, to create the map, the widths of the roads have been reduced to a single cell.

The array representing the image of the locality is encoded as follows: $1$ for a cell occupied by a building and $0$ for an unoccupied cell.

# Task

Given $n$, $m$, and $k$, as well as the array encoding the image, determine:

1. The number $S$ of cells occupied by the **square** building with the maximum side and the number of buildings $C$ chosen from the remaining $k-1$ buildings that **fit** inside the square building with the maximum side, without overlapping its marginal cells.
2. The array representing the map derived from processing the initial image.

# Input data

The input file `harta.in` contains on the first line a natural number $p$. For all input tests, the number $p$ can only have the value $1$ or the value $2$.

The second line contains the natural numbers $n$, $m$, and $k$ separated by spaces.

On each of the next $k$ lines, there are four natural numbers $i_1$, $j_1$, $i_2$, $j_2$, separated by spaces, where the first two numbers represent the coordinates of the North-West extreme cell, and the last two, the coordinates of the South-East extreme cell for each of the $k$ buildings.

# Output data

* If the value of $p$ is $1$ then **only task 1 will be solved**. In this case, the output file `harta.out` will contain the two numbers $S$ and $C$ having the meaning described in task 1, separated by a single space.
* If the value of $p$ is $2$, then **only task 2 will be solved**. In this case, the output file `harta.out` will contain the array representing the map obtained based on the satellite image. The file will have $n_1$ lines. Each line will contain $m_1$ values $0$ or $1$ separated by a single space. Cells located at the edges of buildings will have the value $1$. Cells inside buildings, as well as those outside, will have the value $0$.

# Constraints and clarifications

* $3 \leq n, m \leq 1\ 500$
* $1 \leq i_1 \leq i_2 \leq n$
* $1 \leq j_1 \leq j_2 \leq m$
* $1 \leq k \leq 1\ 000$
* The maximum side of any rectangle is a natural number between $1$ and $50$.
* It is guaranteed that there are solutions for both tasks for all test cases.
* Correctly solving the first task awards $20$ points, while the second task awards $80$ points.

# Example 1

`harta.in`
```
1
7 7 4
1 1 4 4
6 2 6 4
3 6 3 6
6 6 7 7
```

`harta.out`
```
16 2
```

## Explanation

**Attention! Only task 1 is solved for this test.**

The building with coordinates $(1 \ 1 \ 4 \ 4)$ is the largest square and occupies $S = 4 \cdot 4 = 16$ cells. The buildings with coordinates $(3 \ 6 \ 3 \ 6)$ and $(6 \ 6 \ 7 \ 7)$ **fit** inside the building $(1 \ 1 \ 4 \ 4)$ without overlapping its marginal cells. Thus, $C = 2$.
~[Poza1.png|width=20em]

# Example 2

`harta.in`
```
2
10 11 4
1 2 4 4
8 9 8 9
7 3 9 5
2 9 3 9
```

`harta.out`
```
0 1 1 1 0 0 0 0 0 0 0
0 1 0 1 0 0 1 1 1 0 0
0 1 0 1 0 0 1 0 1 0 0
0 1 1 1 0 0 1 0 1 1 0
0 0 0 0 0 0 1 0 0 0 0
0 0 1 1 1 0 1 1 1 0 0
0 0 1 0 1 0 0 0 1 0 0
0 0 1 1 1 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0 0
```

## Explanation

**Attention! Only task 2 is solved for this test.**

In the image, there are $5$ roads determined by the rectangles: $(1 \ 1 \ 10 \ 1)$, $(1 \ 6 \ 10 \ 8)$, $(1 \ 10 \ 10 \ 11)$, $(5 \ 1 \ 6 \ 11)$ and $(10 \ 1 \ 10 \ 11)$.
~[Poza2.png|width=23em]

On the map, the $5$ roads will have the coordinates: $(1 \ 1 \ 9 \ 1)$, $(1 \ 6 \ 9 \ 6)$, $(1 \ 8 \ 9 \ 8)$, $(5 \ 1 \ 5 \ 8)$ and $(9 \ 1 \ 9 \ 8)$.
~[Poza3.png|width=23em]