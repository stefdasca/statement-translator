# Circles

Two circles are given. They can intersect at $0$, $1$, $2$ points or an infinite number of points (if they are identical).

## Task

Find the distance between the two intersection points if they intersect at exactly $2$ points, or handle the other cases accordingly (see 

## Output data

). 

## Input data

The first line of the input file `cercuri.in` contains $T$, the number of tests. Each of the following $T$ lines contains one test: a test consists of $6$ integers: $x_1$, $y_1$, $R_1$, $x_2$, $y_2$, $R_2$. 
$(x_1, y_1)$ are the coordinates of the center of the first circle, and $R_1$ is the radius of the first circle. $(x_2, y_2)$ are the coordinates of the center of the second circle, and $R_2$ is the radius of the second circle. 

## Output data

For each test, print a line containing: 
$-1$, if the two circles are identical 
$-2$, if the two circles do not intersect at any point
$-3$, if the two circles intersect at exactly one point 
the distance between the two intersection points, if the two circles intersect at exactly $2$ points 

## Constraints and clarifications

$0 \leq x_1, y_1, R_1, x_2, y_2, R_2 \leq 1\ 000$ 
The result will be displayed with a precision of $3$ decimal points 

## Example

`cercuri.in` 
```
5 
5 5 5 6 6 6 
5 5 5 6 6 6 
0 0 10 5 5 10 
0 0 10 0 0 10 
1 1000 1000 1
```
`cercuri.out`
```
7.714 
7.714 
18.708 
-1 
-2
```