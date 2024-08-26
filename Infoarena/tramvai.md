## Task

In a city, there are $N$ tram lines, each represented by a straight line. The stations where trams stop, allowing passengers to get on and off, are built only at the intersections of any two tram lines. A traveler is at the station at the intersection of lines $LS1$ and $LS2$ and wants to reach the station at the intersection of lines $LF1$ and $LF2$, solely by tram and covering the shortest possible distance. Determine the minimum length of a tram route between the two stations.

## Input data

The first line of the input file `tramvai.in` contains the integer $N$, representing the number of tram lines in the city. The next $N$ lines each contain 4 integers: $x1$ $y1$ $x2$ $y2$. $(x1,y1)$ and $(x2,y2)$ represent the coordinates of two distinct points in the plane, which uniquely determine the straight line corresponding to a tram line. The lines are numbered from $1$ to $N$ in the order they appear in the input file. The $N+2$-th line contains four more integers, separated by spaces: $LS1$ $LS2$ $LF1$ $LF2$.

## Output data

In the output file `tramvai.out` you will print the minimum length of a route between the two stations, traveling only along tram lines. This number will be displayed with at least 3 decimal places. An error of $0.001$ is acceptable.

## Constraints

$3 \leq N \leq 1000$

The coordinates of the points defining the tram lines are integers in the range $[0,1000]$.

$1 \leq LS1, LS2, LF1, LF2 \leq 1000$

Lines $LS1$ and $LS2$ will not be parallel or identical.

Lines $LF1$ and $LF2$ will not be parallel or identical.

On each line, trams travel in both directions.

## Example

`tramvai.in`

```
3
0 0 0 1000
0 0 1000 0
0 1 1000 1
1 2 1 3
```

`tramvai.out`

```
1.000
```