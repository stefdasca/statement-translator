
No one knows why, but you suddenly decided to start a career in construction. The walls you build are made of cubic bricks with side length $1$, placed in multiple layers.

To design such a wall, you have drawn a grid consisting of $M \cdot N$ squares with side length $1$, organized in $M$ rows and $N$ columns. The rows of the grid are numbered from $1$ to $M$ starting from bottom to top, and the columns are numbered from $1$ to $N$ from left to right.

Each cell of the grid has an associated cost, which needs to be paid if we place a brick in that cell. The cost of building a wall is equal to the sum of the costs of the cells where the bricks are placed.

Your walls must meet the following conditions:

1. Each brick layer consists of a single sequence of bricks, with any two consecutive bricks being adjacent (more precisely, the bricks in a layer are placed in cells of the grid located on the same line, in consecutive columns);
2. At least one brick from each layer $i$ must be placed on another brick from the layer below ($i-1$); the lowest layer must be placed on the ground (the ground being below line $1$ of the grid);
3. The total number of bricks used in the construction of the wall must not exceed a natural number $X$.

~[zidar.png]

# Task

Being a builder eager to prove yourself and knowing that you have an amount of $T$ euros, calculate the maximum number of bricks you can use in constructing a wall that costs at most $T$ euros.

# Input data

The input file `zidar.in` contains on the first line four natural numbers $M$, $N$, $X$, $T$ separated by a space with the significance given in the statement. Each of the next $M$ lines contains $N$ natural numbers between $1$ and $100$ representing the cost of placing a brick for each of the cells of the grid (more precisely, the element $j$ of the $(i+1)$-th line of the input file represents the cost of placing a brick in the cell at row $i$ and column $j$ of the grid).

# Output data

The output file `zidar.out` will contain a single line that will contain a single natural number representing the maximum number of bricks your wall can contain, respecting the imposed conditions.

# Constraints and clarifications

* $1 \leq M \leq 50$;
* $1 \leq N \leq 20$;
* $1 \leq X \leq 60$;
* $1 \leq T \leq 10\ 000$;
* For $30\%$ of the test cases $T \leq 60$. For $60\%$ of the test cases $N \leq 10$.

# Example

`zidar.in`
```
4 5 20 8
2 2 3 2 1
4 7 1 2 3
2 1 1 1 1
1 2 5 7 3
```

`zidar.out`
```
6
```

## Explanation

To construct the wall marked in the figure you need exactly $8$ euros. It is not possible to build walls with more bricks using this amount of money. 

~[zidar2.png]
