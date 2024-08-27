## Task

You are in the corner $(1,1)$ (top-left) of a grid of $N \times M$ points. A squirrel jumps from point to point. Being a squirrel passionate about informatics, it jumps in such a way that it forms $F$ fractals of... trees, of course! The $F$ fractals look like those in the images: The images show fractals of sizes 1, 2, 4, and 8. The squirrel follows these rules:
- The squirrel starts from a given point
- Then it jumps north $P$ points, where $P$ is a given power of two
- Then it jumps along two diagonals of length $P/2$
- Then it forms four fractals of size $P/2$
- It continues until it forms fractals of size 1

The squirrel keeps jumping until it finishes a fractal, then starts with the next fractal. In how many points can you see the squirrel?

## Input data

The input file `squirrel.in` contains on the first line 3 natural numbers $N$, $M$, and $F$. The following $F$ lines describe the $F$ fractals. Each line contains 3 integers: the coordinates of the starting point for the current fractal, followed by the size of the fractal.

## Output data

The output file `squirrel.out` will contain the number of points where the squirrel can be seen.

## Constraints and clarifications
- You can see the squirrel if there is no other point (not necessarily where the squirrel jumped) between you and the squirrel.
- The squirrel stops forming the current fractal when it finishes all jumps, then starts the next fractal.
- The squirrel will never jump to your position $(1, 1)$.
- The squirrel will never jump out of the grid.
- If the squirrel jumps multiple times to the same visible point, then the point will be counted multiple times in the result.

## Constraints

$2 \leq N$, 

$M \leq 50000$

$1 \leq F \leq 1000$

$1 \leq \text{fractal size} \leq 1024$ and it is a power of two.

The total number of jumps is at most $300$ million.

For $15p$, the total number of jumps is at most $40$ million.

For another $10p$, the total number of jumps is at most $65$ million.

For another $25p$, the total number of jumps is at most $125$ million.

The memory limit is reduced compared to the contest!

## Example

`squirrel.in` 
```
14 20 3
11 10 4
7 6 2
8 7 2
```

`squirrel.out`
```
35
```

## Explanation

$14 \,\,20 \,\,3 \,\,11 \,\,10 \,\,4 \,\,7 \,\,6 \,\,2 \,\,8 \,\,7 \,\,2 \,\,35$ 
- The grid has $14$ rows and $20$ columns.
- The squirrel makes $3$ fractals: black, green, and red.
- Triangles mark the starting points of the fractals.
- Circles mark the points that are visible from $(1, 1)$.
- Bold circles mark the points where the squirrel jumps multiple times.
- The total number of visible points where the squirrel jumps is $35$.