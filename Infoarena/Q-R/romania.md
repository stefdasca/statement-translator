Romania

Let $P$ be a regular convex polygon with $N$ vertices numbered in counterclockwise order. At a certain point, you have drawn $K$ oriented diagonals of this polygon, with the property that no two of them intersect except, possibly, at their endpoints. From now on, we will call $x$ the "source" of the diagonal $x \rightarrow y$. You only noted the source of each diagonal on a sheet of paper, and now you wonder if you can recover the diagonals with just this information.

## Input data

The input file `romania.in` will contain on its first line the numbers $N$ and $K$ as described. The second line contains $K$ numbers, representing the list of vertices that are sources of the diagonals.

## Output data

The output file `romania.out` will contain $K$ lines, each containing a pair $x \ y$ indicating the diagonal oriented from vertex $x$ to vertex $y$. If there is no solution, the file will contain only the value $-1$.

## Constraints and clarifications

$3 \leq N \leq 100\ 000$

For tests worth 40 points $N \leq 1\ 500$

$1 \leq K \leq N - 3$

The vertices in the input file are natural numbers from the interval $[1, N]$.

Recall that a diagonal of the polygon is any segment that connects two non-consecutive vertices of this polygon.

Any correct solution is accepted.

If you are wondering why this problem is called Romania: we do not know either.

## Example

`romania.in`

```
5 2
1 4
```

`romania.out`

```
1 3
4 1
```