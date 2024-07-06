```markdown
The fertile gardens of Bărăgan suffer immense losses annually due to drought.

Water seekers have found $n$ wells from which they want to supply $n$ gardens. Let $G_i$, $F_i$, $i=1 \ldots n$ be points in the plane representing the supply points of the gardens and respectively the points where the wells are located. For each point, the integer coordinates $(x,y)$ in the plane are given. To economize materials, the connection between a garden and a well is made through a straight pipeline. Each well supplies a single garden. The County Council of Galați will pay for the investment under the condition that the total length of the pipelines is minimal. Each unit of pipeline costs $100$ new lei (RON).

# Task

Determine $m$, the minimal total cost of the pipelines that connect each garden to exactly one well.

# Input data

The input file `seceta.in` contains:

The first line contains the natural number $n$, representing the number of gardens and wells.

The next $n$ lines contain pairs of integers $G_x \ G_y$, separated by a space, representing the coordinates of the supply points of the gardens.

The next $n$ lines contain pairs of integers $F_x \ F_y$, separated by a space, representing the coordinates of the wells' points.

# Output data

The output file `seceta.out` contains: $m$ a natural number representing the integer part of the minimal total cost of the pipelines.

# Constraints and clarifications

* $1 < n < 13$
* $0 \leq G_x, G_y, F_x, F_y \leq 200$
* No three points are collinear, whether they are gardens or wells
* Any line in the input and output files ends with an end-of-line marker

# Example

`seceta.in`
```
3
1 4
3 3
4 7
2 3
2 5
3 1
```

`seceta.out`
```
624
```

# Explanation

The minimum cost is $[6.24264 \cdot 100]=624$ by linking the pairs:

Gardens: $(1 \ 4) \ (3 \ 3) \ (4 \ 7)$

Wells: $(2 \ 3) \ (3 \ 1) \ (2 \ 5)$
```