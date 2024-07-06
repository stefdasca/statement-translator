# Task

RAU-Gigel has discovered a new passion: graffiti. He feels a growing need to express his artistic spirit, to practice, to explore, and to try new techniques... and for this, he needs space.

Taking a tour through the neighborhood, RAU-Gigel discovers an abandoned depot surrounded by a fence made of concrete slabs of different widths and heights, arranged in a continuous line. "A pristine canvas," he thinks. And he begins to measure the concrete slabs, one by one, with the thought that once he gets home, he will sketch his next artistic creation.

He wants to choose a few adjacent concrete slabs and create his artwork on the maximal rectangular area delineated by these slabs. What is the maximum drawing area? Help RAU-Gigel to make several simulations.

~[graffiti.png]

In the adjacent image, the fence made of concrete slabs, numbered from $1$ to $5$, sizes (width X height): `4 X 8`, `5 X 4`, `7 X 2`, `3 X 3`, `8 X 10` units of size. By repeated queries of the form $(x, y)$, RAU-Gigel wants to find out how large the rectangular drawing area can be that will cover the adjacent concrete slabs: $x, x+1, ..., y$.

For example, for the query $(2, 4)$, the drawing will have a width of $5 + 7 + 3 = 15$, and a height of $min(4, 2, 3) = 2$, so the drawing area will be $30$. The same unit of size will be used everywhere.

# Input data

The input file `graffiti.in` contains the following data: The first line contains the natural number $N$ representing the number of concrete slabs, indexed from $1$ to $N$, then $N$ lines contain pairs in the form of `L H`, separated by a space, representing the width and height of each concrete slab. Then follows a line with the natural number $Q$ representing the number of queries, followed by $Q$ lines containing the queries: pairs in the form of `x y`, with $x \leq y$, separated by a space.

# Output data

The output file `graffiti.out` will contain the answers to the queries, in the order they are requested, one per line.

# Constraints and clarifications

* $1 \leq N, Q, L, H \leq 100\ 000$, $1 \leq x \leq y \leq N$;
* For tests worth $40$ points: $N, Q \leq 1\ 000$;
* For other tests worth $30$ points: $N \leq 1\ 000$.

# Example

`graffiti.in`
```
5
4 8
5 4
7 2
3 3
8 10
2
2 4
4 5
```

`graffiti.out`
```
30
33
```

## Explanation

We have $5$ concrete slabs with dimensions `4 X 8`, `5 X 4`, `7 X 2`, `3 X 3`, `8 X 10` and $2$ queries. 

For the query $(2, 4)$, the drawing area will have a width of $5 + 7 + 3 = 15$ and a height of $min(4, 2, 3) = 2$, so the area is $30$.

For the query $(4, 5)$, the drawing area will have a width of $3 + 8 = 11$, and its height will be $3$, so the area is $33$.