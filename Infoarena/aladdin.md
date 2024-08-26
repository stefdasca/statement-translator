## Task

Help Aladdin create a carpet that meets the conditions set by Princess Jasmine!

## Input data

The input file `aladdin.in` will contain two integers $N$ and $M$ on the first line.  
The following $N - 1$ lines will contain $M - 1$ integers each, separated by spaces, such that the $j$-th integer on line $i + 1$ of the file represents the number of squares of the square that occupies the squares with coordinates $(i, j)$, $(i + 1, j)$, $(i, j+1)$, and $(i + 1, j + 1)$ that need to be colored black.

## Output data

If no carpet can be constructed that meets Jasmine's requirements, the output file `aladdin.out` will contain the number $-1$ on the first line.  
If there are solutions, any of them can be displayed.  
The output file will contain $N$ lines and $M$ elements on each line separated by a space; $0$ will represent a square colored in white and $1$ a square colored in black.

## Constraints and clarifications

$1 \leq N$  
$1 \leq M \leq 1000$

## Example

`aladdin.in`
```
4 4
3 2 3
2 3 3
1 2 1
1 1 1
```

`aladdin.out`
```
0 1 1 0
1 1 0 1
1 0 1 1
0 0 0 0
```