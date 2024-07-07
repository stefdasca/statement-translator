
# Task
~[Picture 1.png|align=right|width=50%]

Gigi is a passionate constructor and today he is analyzing a very important detail in any construction: stairs. A staircase can be represented as a set of tiles in an array. A staircase of level $n$ has $n$ columns: the first column has a height of $1$, the second has a height of $2$, $\\dots$, the last has a height of $n$.
A staircase of level $n$ is beautiful if it can be covered with $n$ squares of any size, disjoint. (In the image, the staircase is of level $7$. There are $4$ green squares of size $1 \\times 1$, each using one tile, $2$ yellow squares of size $2 \\times 2$, each using $4$ tiles, and one red square of size $4 \\times 4$ using $16$ tiles). Gigi receives queries defined by a number $K$ and needs to answer with a number that represents the count of beautiful staircases of different levels he can build using at most $K$ tiles.

Given $Q$ the number of queries and the number of tiles for each query, determine their answers.

# Input data

The first line of the input file `scari.in` contains a number $Q$ representing the number of queries. The following $Q$ lines contain a single integer, $k$, which represents the number of tiles that can be used.

# Output data

The output file `scari.out` will contain $Q$ lines, each containing a single number that represents the maximum number of beautiful staircases that can be built using at most $k$ tiles.

# Constraints and clarifications

* $Q \\leq 1 \\ 000$;
* $K \\leq 1 \\ 000 \\ 000 \\ 000 \\ 000 \\ 000 \\ 000$; 
* For $20\\%$ of the tests $Q \\leq 20$ and $K \\leq 100$.

# Example

`scari.in`
```
4
1
8
6
100
```

`scari.out`
```
1
2
1
3
```

## Explanation

For $1$: with a single tile, we can build only one staircase of level $1$.
For $8$: with $8$ tiles we can build only $2$ beautiful staircases: one of level $1$ (costs $1$) and another one of level $3$ (which costs $6$). In total, we spend $7$ (the last remaining tile cannot be used to create an interesting staircase of different levels than $1$ and $3$). Very important: the staircase of level $2$ is not beautiful (it cannot be colored in $2$ squares).
