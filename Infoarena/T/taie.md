# Cut

Given $N$ segments in the plane through their endpoints coordinates, $(X1[i], Y1[i])$ and $(X2[i], Y2[i])$, find a line that intersects all the segments or state if none exists.

## Input data

The input file `taie.in` will contain on the first line the number of segments, $N$, and on the next $N$ lines, 4 numbers representing the coordinates of the endpoints of each segment.

## Output data

The output file `taie.out` will print, on the first line, the coordinates of 2 points that determine a line which intersects all the $N$ segments. If no such line exists, it will print $-1$.

## Constraints

$1 \leq N \leq 1000$   
$ -10000 \leq X1[i], Y1[i], X2[i], Y2[i] \leq 10000$  
It is guaranteed that any two given segments do not intersect.  
The error should be less than $10^{-5}$.

## Example

`taie.in`  
```
5
9.000000 4.500000 3.500000 -1.000000
-2.000000 -2.000000 8.000000 -2.000000
-0.500000 2.500000 6.000000 3.500000
7.000000 5.000000 -1.000000 4.500000
9.000000 -2.000000 -1.000000 -5.000000
```

`taie.out`  
```
4.500000 3.000000 6.000000 -2.000000
```