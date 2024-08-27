## Task

Bored to tears during his geometry class, Bogdanel started drawing circles. He now wants to select any number of circles - be they $C1$, $C2$ $\dots$ $Ck$ - such that $C_{i+1}$ is contained in $C_i$, for $1 \leq i \leq k-1$. Moreover, because not all circles turned out perfectly, he associated a degree of beauty $F[i]$ with each circle. Being curious by nature, Bogdănel wants to select the circles such that the sum of their degrees of beauty is maximized.

## Input data

The input file `cercuri4.in` contains on the first line an integer $N$, representing the number of circles drawn. Following that are $N$ lines containing 4 integers - $X[i]$, $Y[i]$, $R[i]$, $F[i]$, representing the coordinates of the center, the radius of the circle, and the degree of beauty, respectively.

## Output data

The output file `cercuri4.out` will contain a single integer, representing the sum of the degrees of beauty of the selected circles.

## Constraints and clarifications

$N \leq 3000$

$X[i], Y[i], R[i] \leq 100\ 000\ 000$

$F[i] \leq 50\ 000$

## Example

`cercuri4.in`
```
4
1 1 4 1
1 1 1 2
1 2 1 4
10 12 14 2
```

`cercuri4.out`
```
5
```