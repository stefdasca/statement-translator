# Arbsat2

Given $N$ points in the plane with positive integer coordinates, it is required to add up to $M$ points to the set of $N$ points so that the following property is satisfied: any rectangle with an area greater than $0$, determined by two of the $N + M$ points (both the initial and the added ones), contains at least one other point inside or on the edges.

## Input data

The input file `arbsat2.in` will contain on the first line the numbers $N$ and $M$. The next $N$ lines will contain pairs in the form $x, y$, indicating that there is a point at coordinate $(x, y)$ in the plane. The pairs $N$ and $M$ used in the official tests are found in the following table. Test $0$ is the example and will not be scored.

Test 
`0 1 2 3 4 5 6 7 8 9 10`

$N$
`2 57 486 977 4972 14971 29999 49974 49982 49992 49984`

$M$
`4 390 4500 10000 61869 228412 450013 796101 801999 791348 790324`

## Output data

The output file `arbsat2.out` will contain on the first line the number $X$ of added points, and on the following lines the $X$ points.

## Constraints and clarifications

The coordinates of the points will be within the range $[1, 100\ 000\ 000]$.

There will not be multiple points at the same coordinate pair in the input file.

The points in the output file must be distinct, both among themselves and from those in the input file.

## Example

`arbsat2.in`
```
2 4
8 7
7 9
```

`arbsat2.out`
```
1
7 7
```