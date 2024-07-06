~[tzigla1.png|align=right]
Gigel has just built a house he is very proud of. However, there is still one detail to take care of: the roof. Specifically, it is about a rectangular surface of dimensions $X$ and $Y$, non-zero natural numbers, where $X$ is the width of the rectangle and $Y$ is its height. The surface needs to be covered with square pieces of tile, all having the same side $L$ (a non-zero natural number). The tile must cover the entire area of the roof without exceeding it. The tile pieces that neighbor horizontally cannot overlap; however, those that neighbor vertically must overlap on a rectangular surface, with the horizontal side (the width) equal to the tile size $L$ and the vertical side (the height) equal to $K$ (a non-zero natural number). Having computer science skills, Gigel observes that for known values $X$, $Y$, and $K$, there could be zero, one, or more values of $L$ so that the surface can be covered under the given conditions. Gigel pays based on the total area of tiles purchased. Therefore, he would like to choose tile with side $L$ so that the total cost is minimized.

# Task

Write a program that calculates the side $L$ of the tile used. If there is no solution, the value $0$ will be displayed.

# Input data

The input file `tzigla.in` contains $3$ values, each on a separate line, in the following order:
* $X = \text{the width of the area to be covered}$
* $Y = \text{the height of the area to be covered}$
* $K = \text{the height of the intersection area between two tiles}$

# Output data

The output file `tzigla.out` will contain a single line that will display the value
* $L = \text{the dimension of a tile used for the roof or} \ 0, \ \text{if there is no suitable value for} \ L.$

# Constraints and clarifications

* $1 \leq X \leq 1 \ 000 \ 000$
* $1 \leq Y \leq 1 \ 000 \ 000$
* $1 \leq K \leq X$ and $1 \leq K \leq Y$
* for a correct value of $L$, but not financially optimal, 50\% of the points are awarded.

# Example 1

`tzigla.in`
```
14
9
3
```

`tzigla.out`
```
0
```

## Explanation

For the input data, there is no solution, so $0$ is displayed.

# Example 2

`tzigla.in`
```
10
8
2
```

`tzigla.out`
```
5
```

## Explanation

~[tzigla2.png|align=center]