```markdown
Let $N$ and $K$ be two natural numbers.
* All points in the plane with **integer coordinates** $(x,y)$ such that $0 \leq x \leq N, 0 \leq y \leq N$ are connected by horizontal and vertical lines of length $1$.
* Then $K$ lines of length $1$ from the above lines **are removed**.

We define a **path** as a continuous sequence of horizontal or vertical lines of length $1$, between the origin of the coordinate system and the point with coordinates $(N, N)$, with total length $2 \cdot N$.

# Task

Determine the total number of **distinct paths**. 

For example, if $N = 3$ and $K = 4$ lines from all drawn lines are removed (the dashed lines), then according to the figures below, the total number of distinct paths will be $6$.

~[image.png|align=left]

# Input data

The input file `npath.in` contains on the first line the numbers $N$ and $K$, separated by a space, as described above, and on each of the next $K$ lines there will be a triplet of numbers $x, y, d$ with the following meaning:

* $x, y$ represent the coordinates of the point where a line starts to be removed.
* $d = 1$ if the line will be removed horizontally to the right.
* $d = 2$ if the line will be removed vertically upwards.

# Output data

The output file `npath.out` will contain on the first line the remainder of the division of the total number of distinct paths by $3000017$.

# Constraints and clarifications

* $1 \leq N \leq 5 \ 000$
* $0 \leq K \leq 100$
* Two paths are distinct if the sequence of horizontal and vertical lines differs by at least one position
* For tests worth $52$ points $0 \leq K \leq 15$

# Example

`npath.in`
```
3 4
1 0 2
2 1 2
2 2 1
1 2 2
```

`npath.out`
```
6
```

## Explanation

$N = 3$ and $K = 4$. From the initial grid, $4$ lines are removed, namely:

* The vertical line between the points with coordinates $(1,0)$ and $(1,1)$
* The vertical line between the points with coordinates $(2,1)$ and $(2,2)$
* The horizontal line between the points with coordinates $(2,2)$ and $(3,2)$
* The vertical line between the points with coordinates $(1,2)$ and $(1,3)$

In total, there are $6$ different ways to reach the point with coordinates $(3,3)$ from the origin without crossing removed lines (according to the figures above). The remainder of $6$ divided by $3000017$ is $6$.
```

I have double-checked the statement and made necessary grammar and syntax corrections to ensure it follows the rules of the English language correctly.