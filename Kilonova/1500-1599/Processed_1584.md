Sure, here is the translated and processed text:

```
The mayor of the city has just approved a project for constructing a swimming pool on the outskirts of the locality. The area where the swimming pool is to be placed can be identified with the 2D plan (infinite). It contains $N$ trees, located at integer coordinates, with a width of $1$ meter. **There are no two trees at the same $x$ or $y$ coordinate.** Specifically, $x_i \neq x_j$ and $y_i \neq y_j$ for any $i \neq j$.

~[primar.jpg]

The swimming pool can only be placed in locations of the form of a rectangle with sides parallel to the axes, which, for sustainability reasons, must not contain any tree within its interior.

Moreover, because the budget for this project is very generous, the mayor is interested only in those **maximal** areas (which cannot be extended). In other words, a region $S$ is not valid if there is another rectangular region $S' \neq S$, with sides parallel to the axes, that does not contain any tree, and $S \subset S'$.

For example, for the case illustrated in the adjacent figure (first in the examples section), there are two valid possibilities for placing the swimming pool: the red one (with an area of $2 \times 6 = 12$) and the blue one (with an area of $4 \times 5 = 20$).

What is the sum of the areas of all possible valid regions?

**The result will be displayed modulo $10^9 + 7$.**

# Task

File `primar.in` contains on the first line $N$, the number of trees. The next $N$ lines will contain two integers $x_i$, $y_i$ ($1 \leq i \leq N$) separated by a space, representing the coordinates of the trees.

# Input data

The input file `primar.in` will contain on the first line $N$, the number of trees. The following $N$ lines will contain two integers $x_i$, $y_i$ ($1 \leq i \leq N$) separated by a space, representing the coordinates of the trees.

# Output data

The output file `primar.out` will contain a single natural number, representing the sum of the areas of all valid regions, modulo $10^9 + 7$.

# Constraints and clarifications

* For all subtasks, $x_i \neq x_j$ and $y_i \neq y_j$ for any $i \neq j$.

|#|Score|Constraints|
|-|-|--------|
|1|12|$x_i$ , $y_i \leq 10$ and $N \leq 4$|
|2|10|$x_i$ , $y_i \leq 20$ and $N \leq 20$|
|3|12|$x_i$ , $y_i \leq 120$ and $N \leq 120$|
|4|32|$x_i$ , $y_i \leq 500$ and $N \leq 500$|
|5|18|$x_i$ , $y_i \leq 10^6$ and $N \leq 1 \ 500$|
|6|16|$x_i$ , $y_i \leq 10^6$ and $N \leq 5 \ 000$|

# Example 1

`primar.in`
```
5
1 4
4 3
2 2
6 6
3 9
```

`primar.out`
```
32
```

# Example 2

`primar.in`
```
2
1 1
2 3
```

`primar.out`
```
0
```

# Example 3

`primar.in`
```
7
1 1
2 5
4 2
3 7
8 3
9 6
10 4
```

`primar.out`
```
52
```
```