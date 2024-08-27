## Task

Miruna has $N$ points on a plane. Find two lines that satisfy the following conditions:
   - They are parallel.
   - Each line passes through at least one of the $N$ points.
   - There are no points between the lines.
   - The distance between them is maximal.

## Input data

The input file `culoar.in` will contain the natural number $N$ on the first line. Each of the next $N$ lines will contain two integers, representing the coordinates of the points.

## Output data

In the output file `culoar.out` you will print a single real number representing the distance between the two lines found.

## Constraints and clarifications
- $2 \leq N \leq 1000$
- There will not be 3 collinear points.
- The coordinates of the points will be in the range $[1, 10000]$.
- The result will be printed with 6 exact decimal places.

## Example

`culoar.in` 
```
2 
1 1 
4 1 
```

`culoar.out` 
```
3.000000 
```

`culoar.in` 
```
4 
1 1 
10 6 
19 3 
5 5 
```

`culoar.out` 
```
9.486833 
```