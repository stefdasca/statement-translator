## Task

Johnie has drawn $N$ points on a sheet of paper and placed them in a Cartesian coordinate system. He now wonders how many squares exist that have vertices at the points he drew. Given the number of points and their coordinates, determine the number of squares that can be formed using the given points as vertices.

## Input data

The first line of the file `patrate3.in` contains $N$, the number of points. On the next $N$ lines, there is a pair $x \ y$ representing the coordinates (abscissa and ordinate) of one of the $N$ given points.

## Output data

The file `patrate3.out` contains the required number on the first line.

## Constraints and clarifications

$1 \leq N \leq 1000$ 

The coordinates of the points are real numbers with exactly 4 decimal places in the interval $[-10000, 10000]$

The given points are distinct

The squares formed do not necessarily have sides parallel to the axes

## Example

`patrate3.in`
```
10
18.3350 44.1050
91.3200 13.3600
49.1500 50.6900
35.9300 34.8700
42.0900 17.6800
9.1000 26.5100
88.9000 53.1100
51.5700 10.9400
26.6950 17.2750
74.9300 28.6800
```

`patrate3.out`
```
2
```