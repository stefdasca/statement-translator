# Rectangles5

A matrix with $N$ rows and $M$ columns filled with $0$s and $1$s is given. The task is to find how many maximal rectangles exist. A maximal rectangle is a submatrix of the given matrix which is filled with $0$s and has the property that it cannot be extended anymore. A submatrix can be extended if at least one of its sides is neighbored only by cells containing $0$.

## Input data

The input file `dreptunghiuri5.in` will contain on the first line 2 natural numbers $N$ and $M$. The next $N$ lines will contain $M$ numbers each that describe the matrix.

## Output data

The output file `dreptunghiuri5.out` will contain a single number which represents the number of maximal rectangles in the given matrix.

## Constraints

$1 \leq N \leq 1000$  
$1 \leq M \leq 1000$  

## Example

`dreptunghiuri5.in`  
```
3 4  
0 1 0 0  
1 0 0 0  
0 0 1 0  
```

`dreptunghiuri5.out`  
```
6  
```