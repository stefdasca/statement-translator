## Kgon

Given $N$ points on a circle, you are required to count how many subsets of $K$ points of the set form a regular polygon.

## Input data

The input file `kgon.in` contains on the first line two natural numbers $N$ and $K$ and a real number $R$. The next $N$ lines will contain a real number $D_i$ each, representing the distance on the circle of radius $R$ from the point with coordinates $(0, R)$ to point $i$. 

## Output data

The output file `kgon.out` must contain the number of regular polygons with $K$ points.

## Constraints

$3 \leq K$  
$K \leq N$  
$N \leq 100\,000 $  
$1 \leq R$  
$R \leq 1\,000\,000 $  
It is recommended to use a precision error of $10^{-5}$  
Distances are given by going only clockwise from $(0, R)$

## Example

`kgon.in`  
```
5 3 10.000000  
0.000000  
12.978671  
20.943951  
38.111412  
41.887902  
```  

`kgon.out`  
```
1
```  

## Explanation

Points $1$, $3$, and $5$ form an equilateral triangle.