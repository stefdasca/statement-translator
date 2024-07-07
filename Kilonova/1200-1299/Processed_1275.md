In the city of Ababuribu, there exists a special rectangular road section. The road consists of $m$ rows and $n$ square tiles of the same size. However, the tiles are colored in $n$ different colors, coded by integers ranging from $1$ to $n$. It is known that for each color there are exactly $m$ tiles colored in that color. The coordinates of the tiles will be given by the row and column in which the tile is located, with row numbering starting from the top down beginning with $1$ and column numbering done from left to right starting with $1$. The mayor of the city wants to build a pedestrian crossing on this section of the road. A crossing will consist of $m$ tiles all having the same color and located vertically one below the other, from the first to the last row. Thus the tiles that will form the crossing will have coordinates of the form $(1,c), (2,c), (3,c), \dots, (m,c)$, where $c$ is the column on which the crossing is built. To construct the crossing, the mayor allows the builders to choose the color (from the $n$ available) that the pedestrian crossing will have as well as the column on which the crossing will be built. Additionally, the builders are allowed to swap the tiles on the road, but the total effort must be as low as possible. The effort of swapping two tiles with coordinates $(x,y)$ and respectively $(x1,y1)$ is equal to $|x-x1|+|y-y1|$, where $|a|$ denotes the absolute value of $a$. For example, for the road in the adjacent figure, the most efficient solution is to build a crossing of color $1$ on column $6$.

~[image.png|align=left]

The effort of constructing this crossing is $5$. The following swaps will be made: the tile $(1,6)$ with the tile $(1,7)$, the tile $(2,5)$ with the tile $(3,6)$, and the tile $(3,7)$ with the tile $(4,6)$. If there are multiple solutions involving the same minimum effort, the mayor prefers the color with the smallest code, and if for that color multiple crossings can be built with the same minimum effort, he will prefer the leftmost crossing.

# Task

Given the dimensions $m$ and $n$ of the road and the colors of the $m \times n$ tiles, determine the necessary effort to build the pedestrian crossing, the color that this crossing will have, and the column on which the crossing will be built.

# Input data

The input file `trecere.in` contains on the first line two natural numbers $m$ and $n$ separated by a space, representing the number of rows respectively the number of columns of the road. The next $m$ lines of the file will contain $n$ natural numbers ranging from $1$ to $n$ (inclusive) separated by a space, representing the colors of the tiles on the road.

# Output data

The output file `trecere.out` will contain on its first line three integers $a, b$ and $c$, separated by a space, having the following meaning: $a$ the effort put in to build the pedestrian crossing, $b$ the color of the pedestrian crossing, and $c$ the column on which the crossing is built.

# Constraints and clarifications

* $1 \leq m, n \leq 120$
* For the correct value of the effort put in, $30\%$ of the score is awarded

# Example

`trecere.in`
```
4 7
4 3 3 6 3 2 1
6 3 4 6 1 1 5
5 6 2 4 5 4 1
7 2 5 2 7 7 7
```

`trecere.out`
```
5 1 6
