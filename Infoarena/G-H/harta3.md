## Task

Assign different coordinates to the $N$ points such that the $M$ relations are respected, while the distance between $A$ and $B$ is minimized.

## Input data

The input file `harta3.in` contains on the first line the numbers $N$ and $M$, as specified in the statement. The second line contains the points $A$ and $B$. The following $M$ lines contain 3 numbers each: $X$, $Y$, and $D$.

## Output data

The output file `harta3.out` contains on the first line $N$ numbers representing the coordinates on the $OX$ axis of the $N$ points.

## Constraints and clarifications

$2 \leq N \leq 10\,000$  
$0 \leq M \leq 10\,000$  
For each $X, Y, D$, $1 \leq D \leq 100$.  
Attention! It is guaranteed that the minimum distance between $A$ and $B \leq 2\,400$.  
The points' coordinates must belong to the interval $[-1\,000\,000, 1\,000\,000]$.  
If there are multiple solutions, any of them can be displayed.  
It is guaranteed that there is a solution!

## Example

`harta3.in`  
```
5 3  
1 3  
1 2 3  
2 4 1  
1 5 6  
```

`harta3.out`  
```
0 3 1 4 6  
```