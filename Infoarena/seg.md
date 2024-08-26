# Segments

You are given $N$ segments. Find the minimum length of a closed broken line that contains the given segments on its sides. The broken line must be drawable starting from any point on it, traversing each side only once, and returning to the starting point (the line can self-intersect).

## Input data

The first line contains the number $T$ of tests, followed by $T$ tests. The first line of a test will contain the number $N$, and the next $N$ lines will contain the coordinates of the segment endpoints.

## Output data

For each test, print the length of the lines that need to be drawn, displayed with $6$ decimal places rounded.

## Constraints

$1 \leq N \leq 17$

The coordinates of the points are in the range $[ -2000 , 2000 ]$

The input file will contain a maximum of $500$ tests

Among which at most $4$ will have $N > 10$

For each test, the answer will be considered correct only if the absolute difference between the official answer and the contestant's answer is less than or equal to $10^{-6}$.

## Example

`seg.in` `seg.out` 
```
2 
2 
1 1 1 2 
1 1 2 2 
3 
-931.693980 781.297764 -767.512077 1305.542158 
933.100984 -166.303237 1225.734021 -125.170151 
320.771418 -163.911119 -148.087080 -332.428961 
1.000000 4427.669962 
```

## Explanation

In test 1,
connecting $1 2$ with $2 2$ results in a length of $1$