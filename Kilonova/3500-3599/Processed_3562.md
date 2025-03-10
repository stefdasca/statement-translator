# Townsville City Needs a New Surveillance System!

The mayor wants to reduce costs and presents you with the city's plan, seeking your help.

Townsville can be represented by a Cartesian coordinate system in the plane, where the $OX$ axis represents the ground level. It consists of $n$ blocks, placed on the $OX$ axis at positions with consecutive natural abscissas, from $1$ to $n$. For each block $i$, its height $h_i$ is known. In other words, block $i$ ($1 \leq i \leq n$) is the segment that connects the coordinate point $(i, 0)$, the base of the block, with the point $(i, h_i)$, the top of the block.

The mayor wants to place a surveillance camera at a position with **natural coordinates** in the plane, with an abscissa between $1$ and $n$ ($1 \leq x \leq n$), from which both the first and last blocks can be observed by the camera. The camera has a view of a block if the segment connecting the camera with the top of the block does not intersect other blocks (this segment can intersect other block tops without the view being obstructed). Also, the camera cannot be placed inside a block, but it can be placed anywhere outside or even on top of one of the blocks.

Determine the point with the minimum ordinate (minimum coordinate $y$) where the camera can be placed. If there are multiple points with the minimum ordinate that satisfy the task, among these, display the one with the minimum abscissa (coordinate $x$).

# Input data

The file `vedere.in` contains on the first line a number $n$ representing the number of blocks. The second line contains $n$ natural values representing the heights of the blocks in the order of numbering from $1$ to $n$.

# Output data

The file `vedere.out` contains the coordinates $x$ and $y$ of the sought point (**natural numbers** separated by space).

# Constraints and clarifications

* $2 \leq n \leq 100 \ 000$;
* $1 \leq h_i \leq 1 \ 000 \ 000 \ 000$, for any $1 \leq i \leq n$;
* It is guaranteed that the sought $y$ is at most $1 \ 000 \ 000 \ 000$.
* For tests worth $18$ points: $n$, the heights of the blocks, and the sought $y \leq 5 \ 000$;
* For other tests worth $13$ points: $n \leq 5 \ 000$ and the sought point is on top of a block;
* For other tests worth $24$ points: the sought point is on top of a block;
* For other tests worth $18$ points: $n \leq 5 \ 000$.

# Example 1

`vedere.in`
```
14
2 1 2 3 4 1 6 4 6 7 7 1 4 4
```

`vedere.out`
```
10 8
```

## Explanation

In the first example, placing the camera at coordinates $(10, 8)$ allows both the first and last blocks to be visible. Note that the segments connecting the camera to blocks $1$ and $n$ also intersect the tops of blocks $7$ and $11$, respectively. These intersections are allowed and do not obstruct the view.

~[vedere.png|align=center]

# Example 2

`vedere.in`
```
2
10 20
```

`vedere.out`
```
1 10
```

## Explanation

In the second example, placing the camera at the top of block $1$ achieves the point with the minimum ordinate from which both blocks are visible.