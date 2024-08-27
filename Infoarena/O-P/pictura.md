# Painting

Mitrutz has recently started painting matrices. Because he wants to see how skilled you are at painting, he provides you with a matrix of $N*M$ cells painted by him. Each cell has a color between $0$ and $K$. If a cell is colored $0$, it means it has not been painted yet.

We call a ‘zone’ of color $x$, a maximal subset of cells in the matrix with the property that all have color $x$ and there exists a path between any two (passing through adjacent cells of the same color). It is known that all zones follow a line (with a thickness of $1$) which can change direction and self-intersect but cannot double back (the thickness is 1 everywhere). For more clarity, see the explanations below:

Valid zone of color $x$ (2 self-intersections, 9 direction changes)
```
0 0 0 0 x x x x
0 0 0 x 0 x 0 0
x x 0 x x x x 0
x 0 0 x 0 x 0 x
0 x 0 0 x 0 x x
x 0 0 x 0 0 0 0
0 x 0 0 x x x x
x x x x 0 0 0 0
```

Incorrect zone of color $x$ (does not appear in tests)
```
0 0 0 0 x 0 0 0
0 0 0 0 x x 0 0
0 0 0 0 0 0 x 0
0 0 0 x 0 0 0 0
0 x x x 0 0 0 0
0 0 0 x 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```

## Task

Determine $K$, the number of colors used, and for each color $i$, determine the number $Z_i$ of zones where it appears, $D_i$ how many times it changes direction (the sum of direction changes for each zone where the color appears), and $I_i$ how many times it self-intersects (the sum of the number of intersections for each zone).

## Input Data

The input file `pictura.in` contains numbers $N$ and $M$ on the first line. The next $N$ lines contain $M$ integers each describing Mitrutz's matrix.

## Output Data

The output file `pictura.out` contains on the first line the number $K$ of colors used. The next $K$ lines each contain 3 numbers. Line $i+1$ contains numbers $Z_i$, $D_i$, and $I_i$ separated by spaces.

## Constraints

1 $\leq N, M \leq 1000$

## Example

`pictura.in`
```
6 6
3 3 0 1 0 1
0 3 0 1 0 0
1 1 1 1 1 1
0 0 0 1 0 1
2 2 0 1 1 1
0 2 2 0 0 0
```
`pictura.out`
```
3
2 3 1
1 2 0
1 1 0
```

## Explanation

There are $3$ colors in the given matrix: $1$, $2$, and $3$. Color $1$ appears in two zones, in one of which it self-intersects once and changes direction three times, and in the other not at all. Color $2$ appears in a single zone and changes direction twice. Color $3$ also appears only in one zone. Its direction changes once.